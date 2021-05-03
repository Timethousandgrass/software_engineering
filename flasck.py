from flask import Flask, request, render_template, send_file
import os
import json
import SQL_file

app = Flask(__name__)

# 需要初始化管理员

'''@app.route('/get_file/data/<name>', methods=['GET'])  # <file_name>
def get_local_resource(name):  # file_name
    # print(request.args.get('name'))
    basedir = os.path.abspath(os.path.dirname(__file__))
    print(basedir)
    print(name)
    # basedir一般是在配置文件中
    file_path = os.path.join(basedir, 'data', name)
    print(file_path)
    return send_file(file_path)'''


@app.route('/update/', methods=['POST'])
def update():
    """上架车辆信息"""
    """存图片的过程不确定"""
    global db
    account = request.form.get('account')
    name = request.form.get('name')
    age = request.form.get('age')
    price = request.form.get('money')
    filenum = request.form.get('filenum')
    img0 = request.files.get('file0')
    print(account)
    print(name)
    print(age)
    print(price)
    print(filenum)
    if db.init_s_seller(account) == '': return 'account_False'
    if db.set_s_pay_RQ_code_url(account, '') == '': return 'pay_RQ_code_url_False'
    ono = db.init_o_order(account, price)
    filenum = int(filenum)  # filenum就是前端传来的图片个数
    files = []
    paths = []
    for i in range(filenum):
        par = 'file' + str(i)  # 得到对应的图片的参数名
        files.append(request.files.get(par))  # 根据参数名获得对应的图片文件
    for file in files:
        file.save('data/')  # 把图片文件存在本地的filepath路径下
        # 注意这个filename应该每张图片对应一个自己的不同的文件名，根据后端需要而自行设定
    for path in paths:
        # path是图片在本地的地址
        db.upload_pic(ono, path)
    img0.save('data/img0.jpg')
    # db.insert(idd, name, age, 'data/%s.jpg' % idd)
    # idd += 1
    return 'update_OK'


"""@app.route('/agree/', methods=['POST'])
def agree():
    # num是车辆的编号
    global db
    o_ono = request.form.get('num')
    # 下面对卖家提交的待审核车辆进行同意操作
    if db.set_if_approved(o_ono, 1) == '':
        return 'agree_False'
    else:
        return o_ono"""

"""@app.route('/del/', methods=['POST'])
def dele():
    # num是车辆的编号
    global db
    o_ono = request.form.get('num')
    # 下面对卖家提交的待审核车辆进行删除操作
    if db.delete_o_order(o_ono) == '':
        return 'dele_False'
    else:
        return o_ono"""


@app.route('/search/', methods=['POST'])
def search():
    """对于能否运行有极大疑惑"""
    # 实现根据key值来查询对应的车辆信息，key值就是买家的搜索类别
    # 这个函数被复用了，key值也可以是买家的账号，根据账号返回买家已经被后台确定的车辆信息
    # 又被复用了，key值也可以是'admin0'，表示这是管理员要看卖家提交的车辆信息
    # key值也可以是'admin1'，表示这是管理员要根据买家付款备注中的的账号以及车辆编号来
    global db
    dicts = []
    key = request.form.get('key')
    # 车辆类型有两种 山地车、普通车
    if str.isdecimal(key):
        # 返回买家的已经被后台确认收到款的车辆信息
        """因为这个函数不同，所以返回格式需要改动"""
        result = db.get_order_by_bno(key)
        for i in result:
            dicts.append({'no': i[0][0], 'name': i[2][0], 'age': i[2][1], 'money': i[0][5], 'pics': i[1]})
    elif key == 'admin0':
        # 返回卖家提交的待审核的车辆信息
        result = db.get_order_new()
    elif key == '山地车' or '普通车':
        # 返回满足条件（（属性name）==key）的车辆信息
        result = db.get_order_unsold_by_tag(key)
    else:
        # 返回10条未卖出的车辆信息，最好设一个计数器，每次返回下一个10条信息
        result = db.get_order_unsold()
    for i in result:
        dicts.append({'no': i[0][0], 'name': i[2][0], 'age': i[2][1], 'money': i[0][3], 'pics': i[1]})
    # dist1是符合key类别的车辆的信息
    # dist1 = {车辆的编号(也就是订单的编号)，车辆的类别(name)属性，车辆的年龄(age)属性，车辆的价格，图片总数量，图片0链接，图片1链接，...}
    # return [dist1, dist2, ...]
    # dist1 = {'no': '1', 'name': '山地车', 'age': '3', 'money': 100,
    #          'pics': ['http://localhost:5555/get_file/data/1.jpg', 'http://localhost:5555/get_file/data/10.jpg']}
    # dist2 = {'no': '2', 'name': '山地车', 'age': '3', 'money': 100,
    #          'pics': ['http://localhost:5555/get_file/data/1.jpg', 'http://localhost:5555/get_file/data/10.jpg']}
    return json.dumps(dicts)


"""@app.route('/signup/', methods=['POST'])
def signup():
    global db
    account = request.form.get('account')
    name = request.form.get('name')
    password = request.form.get('password')
    phone = request.form.get('phone')
    if account == '' or name == '' or password == '' or phone == '':
        return '不能为空'
    if db.sign_up(account, name, password, phone) == '':
        return 'sign_up_False'
    else:
        return 'sign_up_True'"""

'''@app.route('/login/', methods=['POST'])
def login():
    global db
    account = request.form.get('account')
    password = request.form.get('password')
    if db.get_password(account) is None:
        return 'login_error:no such user'
    if password == db.get_password(account):
        if db.get_if_admin(account):
            return {'right': '1', 'admin': '1'}
        else:
            return {'right': '1', 'admin': '0'}
    else:
        return {'right': '0', 'admin': '0'}'''

'''@app.route('/money/', methods=['GET'])
def money():
    """返回平台收款码"""
    return send_file('data/OIP.jpg')'''


@app.route('/confirm/', methods=['POST'])
def confirm():
    """过程不确定"""
    global db
    account = request.form.get('account')
    bike_num = request.form.get('bike_num')
    # eg confirm('20180001','123')
    # 证明买家（账号是20180001) 为车辆编号是123的车付了款，后台人员支付宝收到信息后，根据支付宝上备注的买家账号account与车辆编号bike_num来更新数据库的车辆表的
    db.set_buyer_o_order(bike_num, account)
    db.set_buyer_payed_amount(bike_num)
    db.set_seller_payed_amount(bike_num)
    db.set_sold(bike_num)
    return 'confirm successfully'


if __name__ == '__main__':
    basedir = os.path.abspath(os.path.dirname(__file__))
    print(basedir)
    db = SQL_file.SQL()
    app.run(host='0.0.0.0', port=5555)  # ,debug=True
