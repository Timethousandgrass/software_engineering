import psycopg2
import time
import datetime


class SQL():
    O_ONO = 1
    
    def __init__(self):
        self.PostgreSQLConnection  =  psycopg2.connect(database="bike1", user="postgres",password="252012", host="localhost", port="5432")
        self.pgsql_cursor = self.PostgreSQLConnection.cursor()
        
        
    def get_password(self, u_uno):
        """输入用户号得到用户密码"""
        u_uno = str(u_uno)
        try:
            self.pgsql_cursor.execute("select u_password from u_user where u_uno = '{}';".format(u_uno))
            return self.pgsql_cursor.fetchall()[0][0]
        except:
            self.pgsql_cursor.execute("abort")
            return ''
        
        
    def sign_up(self, u_uno, u_uname, u_password, u_phone_num):
        """
        输入用户号、用户名、密码、联系方式来注册新账户,
        注册时同时插入卖家买家表
        """
        u_uno = str(u_uno)
        u_uname = str(u_uname)
        u_password = str(u_password)
        u_phone_num = str(u_phone_num)
        try:
            self.pgsql_cursor.execute("insert into u_user values('{}', '{}', '{}', '{}');".
                                      format(u_uno, u_uname, u_password, u_phone_num))
            self.PostgreSQLConnection.commit()
        except:
            self.pgsql_cursor.execute("abort")
            return ''
            
    def init_s_seller(self, s_sno):
        """输入用户号,第一次卖出时要创建卖家信息"""
        s_sno = str(s_sno)
        try:
            self.pgsql_cursor.execute("""
            insert into s_seller(s_sno, s_unpayed_amount, s_payed_amount) values('{s_sno}', 0, 0);
                                      """.format(s_sno = s_sno))
            self.PostgreSQLConnection.commit()
        except :
            self.pgsql_cursor.execute("abort")
            return '' 
    
    
    def get_s_pay_RQ_code_url(self, s_sno):
        """输入用户号,获得卖家留下的付款码"""
        s_sno = str(s_sno)
        try:
            self.pgsql_cursor.execute("select s_pay_RQ_code_url from s_seller where s_sno = '{}';".format(s_sno))
            return self.pgsql_cursor.fetchall()[0][0]
        except:
            self.pgsql_cursor.execute("abort")
            return ''
        
        
    def set_s_pay_RQ_code_url(self, s_sno, s_pay_RQ_code_url):
        """输入用户号和付款码地址,设置卖家付款码"""
        s_sno = str(s_sno)
        s_pay_RQ_code_url = str(s_pay_RQ_code_url)
        try:
            self.pgsql_cursor.execute("update s_seller set s_pay_RQ_code_url='{}' where s_sno='{}';".
                                 format(s_pay_RQ_code_url, s_sno))
            self.PostgreSQLConnection.commit()
        except:
            self.pgsql_cursor.execute("abort")
            return ''
         
    
    def init_o_order(self, o_sno, o_price):
        """输入卖家号和卖出价格,创建卖家提交的交易单"""
        o_sno = str(o_sno)
        o_price = str(o_price)
        o_up_date = time.strftime("%Y-%m-%d %H:%M:%S")
        try:
            self.pgsql_cursor.execute("""
            insert into o_order(o_ono, o_sno, o_if_sold, o_wear_rate, o_up_date, o_price, o_if_confirmed) 
            values('{o_ono}', '{o_sno}', false, 1, '{o_up_date}', '{o_price}', false);
            """.format(o_ono = str(SQL.O_ONO), o_sno = o_sno, o_up_date = o_up_date, o_price = o_price))
            self.PostgreSQLConnection.commit()
            SQL.O_ONO += 1
            return SQL.O_ONO-1
        except :
            self.pgsql_cursor.execute("abort")
            return ''
    
    
    def upload_pic(self, p_ono, p_url):
        """输入订单号,上传照片地址,可多次上传"""
        p_ono = str(p_ono)
        p_url = str(p_url)
        try:
            self.pgsql_cursor.execute("""
            insert into p_pic values('{p_ono}', '{p_url}');
            """.format(p_ono = p_ono, p_url = p_url))
            self.PostgreSQLConnection.commit()
        except :
            self.pgsql_cursor.execute("abort")
            return ''
    
    
    def add_bike_tag(self, bt_ono, bt_tag):
        """输入订单号,上传自行车描述标签,可多次上传"""
        bt_ono = str(bt_ono)
        bt_tag = str(bt_tag)
        try:
            self.pgsql_cursor.execute("""
            insert into bt_bike_tag values('{bt_ono}', '{bt_tag}');
            """.format(bt_ono = bt_ono, bt_tag = bt_tag))
            self.PostgreSQLConnection.commit()
        except :
            self.pgsql_cursor.execute("abort")
            return ''
    
    def set_price(self, o_ono, o_price):
        """输入订单号和价格,设定价格"""
        o_ono = str(o_ono)
        o_price = str(o_price)
        try:
            self.pgsql_cursor.execute("""
            update o_order set o_price = {o_price} where o_ono = '{o_ono}';
            """.format(o_ono = o_ono, o_price = o_price))
            self.PostgreSQLConnection.commit()
        except :
            self.pgsql_cursor.execute("abort")
            return ''
    
    def set_seller_unpayed_amount(self, o_ono):
        """输入订单号, 修改s_seller表的卖家收款数, 
        既然卖家将车辆托管到平台, 平台就应该欠卖家一个自行车的钱数"""
        o_ono = str(o_ono)
        try:
            self.pgsql_cursor.execute("""
            select o_sno,o_price from o_order where o_ono = '{o_ono}'
            """.format(o_ono = o_ono))
            o_sno,o_price = self.pgsql_cursor.fetchall()[0]
        except :
            self.pgsql_cursor.execute("abort")
            return '' 
        
        try:
            self.pgsql_cursor.execute("""
            select s_unpayed_amount from s_seller where s_sno = '{o_sno}'
            """.format(o_sno = o_sno))
            s_unpayed_amount_before = self.pgsql_cursor.fetchall()[0][0]
            if s_unpayed_amount_before == None:
                s_unpayed_amount_before = 0
        except KeyError:
            self.pgsql_cursor.execute("abort")
            return '' 
        
        try:
            self.pgsql_cursor.execute("""
            update s_seller set s_unpayed_amount = {s_unpayed_amount_before}+{o_price} where s_sno = '{o_sno}';
                                      """.format(s_unpayed_amount_before = s_unpayed_amount_before,
                                                 o_price = o_price, 
                                                 o_ono = o_ono, 
                                                 o_sno = o_sno))
            self.PostgreSQLConnection.commit()
        except :
            self.pgsql_cursor.execute("abort")
            return ''
    
    def set_lock_code(self, o_ono, o_code):
        """输入订单号和车锁密码,设定密码"""
        o_ono = str(o_ono)
        o_code = str(o_code)
        try:
            self.pgsql_cursor.execute("""
            update o_order set o_code = '{o_code}' where o_ono = '{o_ono}';
            """.format(o_ono = o_ono, o_code = o_code))
            self.PostgreSQLConnection.commit()
        except :
            self.pgsql_cursor.execute("abort")
            return ''
    
    
    def delete_o_order(self, o_ono):
        """输入订单号,删除订单"""
        o_ono = str(o_ono)
        try:
            self.pgsql_cursor.execute("""
            delete from o_order where o_ono = '{o_ono}';
            """.format(o_ono = o_ono))
            self.PostgreSQLConnection.commit()
        except :
            self.pgsql_cursor.execute("abort")
            return ''
        
    #以下为买家部分
    def init_b_buyer(self, b_bno):
        """输入用户号,初始化买家信息"""
        b_bno = str(b_bno)
        try:
            self.pgsql_cursor.execute("""
            insert into b_buyer values('{b_bno}', 0);
                                      """.format(b_bno = b_bno))
            self.PostgreSQLConnection.commit()
        except KeyError:
            self.pgsql_cursor.execute("abort")
            return '' 
    
    
    def set_buyer_o_order(self, o_ono, o_bno):
        """输入订单号,买家号,将订单中设为买家购买"""
        o_ono = str(o_ono)
        o_bno = str(o_bno)
        try:
            self.pgsql_cursor.execute("""
            update o_order set o_bno = '{o_bno}' where o_ono = '{o_ono}';
                                      """.format(o_ono = o_ono, o_bno = o_bno))
            self.PostgreSQLConnection.commit()
        except :
            self.pgsql_cursor.execute("abort")
            return '' 
    
    
    def get_price(self, o_ono):
        o_ono = str(o_ono)
        try:
            self.pgsql_cursor.execute("""
            select o_price from o_order where o_ono = '{o_ono}';
                                      """.format(o_ono = o_ono))
            return self.pgsql_cursor.fetchall()[0][0]
        except :
            self.pgsql_cursor.execute("abort")
            return ''
    
    
    def set_buyer_payed_amount(self, o_ono):
        """输入订单号和付款金额, 修改o_order和b_buyer表的买家付款数,和买家总付款数.
        在买家付款到二维码后,修改订单的买家已付金额，修改b_buyer的买家全部已付金额"""
        o_ono = str(o_ono)
        try:
            self.pgsql_cursor.execute("""
            select o_bno, o_price from o_order where o_ono = '{o_ono}'
            """.format(o_ono = o_ono))
            o_bno, o_price = self.pgsql_cursor.fetchall()[0]
        except :
            self.pgsql_cursor.execute("abort")
            return '' 
        
        try:
            self.pgsql_cursor.execute("""
            select b_payed_amount from b_buyer where b_bno = '{o_bno}'
            """.format(o_bno = o_bno))
            b_payed_amount = self.pgsql_cursor.fetchall()[0][0]
            if b_payed_amount == None:
                b_payed_amount = 0
        except :
            self.pgsql_cursor.execute("abort")
            return '' 
        
        try:
            self.pgsql_cursor.execute("""
            begin transaction;
            update o_order set o_buyer_paid = {o_price} where o_ono = '{o_ono}';
            update o_order set o_if_sold = true where o_ono = '{o_ono}';
            update o_order set o_sold_date = '{o_sold_date}' where o_ono = '{o_ono}';
            update b_buyer set b_payed_amount = {b_payed_amount}+{o_price} where b_bno = '{o_bno}';
            
            commit;
            
                                      """.format(o_price = o_price,
                                                 b_payed_amount = b_payed_amount, 
                                                 o_ono = o_ono, 
                                                 o_bno = o_bno,
                                                 o_sold_date=time.strftime('%Y-%m-%d %H:%M:%S')))
            self.PostgreSQLConnection.commit()
        except :
            self.pgsql_cursor.execute("abort")
            return ''

        
    def set_seller_payed_amount(self, o_ono):
        """输入订单号, 修改o_order和s_seller表的卖家收款数
        在买家确认订单后,付钱给卖家,修改卖家的未付款金额和已付款金额,
        同时将订单修改为卖出状态,记录卖出日期"""
        o_ono = str(o_ono)
        try:
            self.pgsql_cursor.execute("""
            select o_sno,o_buyer_paid from o_order where o_ono = '{o_ono}'
            """.format(o_ono = o_ono))
            o_sno,payed_amount_now = self.pgsql_cursor.fetchall()[0]
        except :
            self.pgsql_cursor.execute("abort")
            return '' 
        
        try:
            self.pgsql_cursor.execute("""
            select s_payed_amount, s_unpayed_amount from s_seller where s_sno = '{o_sno}'
            """.format(o_sno = o_sno))
            payed_amount_before , unpayed_amount_before = self.pgsql_cursor.fetchall()[0]
            if payed_amount_before == None:
                payed_amount_before = 0
        except :
            self.pgsql_cursor.execute("abort")
            return '' 
        
        try:
            self.pgsql_cursor.execute("""
            begin transaction;
            update o_order set o_seller_paid = {payed_amount_now} where o_ono = '{o_ono}';
            update o_order set o_if_confirmed = true where o_ono = '{o_ono}';
            update o_order set o_confirmed_date = '{o_confirmed_date}' where o_ono = '{o_ono}';
            update s_seller set s_payed_amount = {payed_amount_before}+{payed_amount_now} where s_sno = '{o_sno}';
            update s_seller set s_unpayed_amount = {unpayed_amount_before}-{payed_amount_now} where s_sno = '{o_sno}';
            commit;
            
                                      """.format(payed_amount_before = payed_amount_before,
                                                 unpayed_amount_before = unpayed_amount_before,
                                                 payed_amount_now = payed_amount_now, 
                                                 o_ono = o_ono, 
                                                 o_sno = o_sno,
                                                 o_confirmed_date=time.strftime('%Y-%m-%d %H:%M:%S')))
            self.PostgreSQLConnection.commit()
        except :
            self.pgsql_cursor.execute("abort")
            return ''
        
        
    def get_pic(self, p_ono):
        """获得输入订单号的全部照片"""
        p_ono = str(p_ono)
        try:
            self.pgsql_cursor.execute("""
            select p_url from p_pic where p_ono = '{p_ono}';
                                      """.format(p_ono = p_ono))
            urls = self.pgsql_cursor.fetchall()
            return [urls[i][0] for i in range(len(urls))]
        except:
            self.pgsql_cursor.execute("abort")
            return ''
        
        
    def get_bike_tag(self, bt_ono):
        """获得输入订单号的全部tag"""
        bt_ono = str(bt_ono)
        try:
            self.pgsql_cursor.execute("""
            select bt_tag from bt_bike_tag where bt_ono = '{bt_ono}';
                                      """.format(bt_ono = bt_ono))
            urls = self.pgsql_cursor.fetchall()
            return [urls[i][0] for i in range(len(urls))]
        except:
            self.pgsql_cursor.execute("abort")
            return ''
    
    
    def get_seller_phone_num(self, o_ono):
        """输入订单号,得到买家电话号码"""
        o_ono = str(o_ono)
        try:
            self.pgsql_cursor.execute("""
            select u_user.u_phone_num from o_order, u_user where o_order.o_sno = u_user.u_uno;
                                      """.format(o_ono = o_ono))
            return self.pgsql_cursor.fetchall()[0][0]
        except :
            self.pgsql_cursor.execute("abort")
            return ''
    
    
    def get_buyer_phone_num(self, o_ono):
        """输入订单号,得到卖家电话号码"""
        o_ono = str(o_ono)
        try:
            self.pgsql_cursor.execute("""
            select u_user.u_phone_num from o_order, u_user where o_order.o_bno = u_user.u_uno;
                                      """.format(o_ono = o_ono))
            return self.pgsql_cursor.fetchall()[0][0]
        except :
            self.pgsql_cursor.execute("abort")
            return ''

        
    def get_buyer_num(self, o_ono):
        """输入订单号,得到卖家号码"""
        o_ono = str(o_ono)
        try:
            self.pgsql_cursor.execute("""
            select o_bno from o_order where o_ono = '{o_ono}';
                                      """.format(o_ono = o_ono))
            return self.pgsql_cursor.fetchall()[0][0]
        except :
            self.pgsql_cursor.execute("abort")
            return ''
    
    
    def get_seller_num(self, o_ono):
        """输入订单号,得到卖家号码"""
        o_ono = str(o_ono)
        try:
            self.pgsql_cursor.execute("""
            select o_sno from o_order where o_ono = '{o_ono}';
                                      """.format(o_ono = o_ono))
            return self.pgsql_cursor.fetchall()[0][0]
        except :
            self.pgsql_cursor.execute("abort")
            return ''
    
    
    def get_lock_code(self, o_ono):
        """输入订单号,得到密码锁密码"""
        o_ono = str(o_ono)
        try:
            self.pgsql_cursor.execute("""
            select o_code from o_order where o_ono = '{o_ono}';
                                      """.format(o_ono = o_ono))
            return self.pgsql_cursor.fetchall()[0][0]
        except :
            self.pgsql_cursor.execute("abort")
            return ''
    
    
    def set_sold(self, o_ono):
        """设定订单号对应车辆已出售,并记录售出日期"""
        o_ono = str(o_ono)
        try:
            self.pgsql_cursor.execute("""
            update o_order set o_if_sold = true where o_ono = '{o_ono}';
            update o_order set o_sold_date = '{o_sold_date}' where o_ono = '{o_ono}';
            """.format(o_ono = o_ono, o_sold_date=time.strftime('%Y-%m-%d %H:%M:%S')))
            self.PostgreSQLConnection.commit()
        except :
            self.pgsql_cursor.execute("abort")
            return ''
    
    
    def set_put_on(self, o_ono):
        """设定订单号对应车辆重新上架,且清除买家相关信息"""
        o_ono = str(o_ono)
        
        o_bno = self.get_buyer_num(o_ono)
        o_price =  self.get_price(o_ono)
        try:
            self.pgsql_cursor.execute("""
            select b_payed_amount from b_buyer where b_bno = '{o_bno}';
                                      """.format(o_bno = o_bno))
            b_payed_amount_before = self.pgsql_cursor.fetchall()[0][0]
        except:
            self.pgsql_cursor.execute("abort")
            return ''
            
        
        try:
            self.pgsql_cursor.execute("""
            begin transaction;
            update b_buyer set b_payed_amount = {b_payed_amount_before} - {o_price};
            update o_order set o_if_sold = false where o_ono = '{o_ono}';
            update o_order set o_if_confirmed = false where o_ono = '{o_ono}';
            update o_order set o_bno = null where o_ono = '{o_ono}';
            update o_order set o_sold_date = null where o_ono = '{o_ono}';
            update o_order set o_buyer_paid = 0 where o_ono = '{o_ono}';
            update o_order set o_seller_paid = 0 where o_ono = '{o_ono}';
            commit;
            """.format(o_ono = o_ono, b_payed_amount_before = b_payed_amount_before, o_price = o_price))
            self.PostgreSQLConnection.commit()
        except:
            self.pgsql_cursor.execute("abort")
            return ''
    
    def clear_all(self):
        """一键删库"""
        try:
            self.pgsql_cursor.execute("""
            begin transaction;
            delete from bt_bike_tag;
            delete from p_pic;
            delete from o_order;
            delete from s_seller;
            delete from b_buyer;
            delete from a_admin;
            delete from u_user;
            commit;
            """)
            self.PostgreSQLConnection.commit()
            SQL.O_ONO = 1
        except KeyError:
            self.pgsql_cursor.execute("abort")
            return ''
    
    def clear_admin(self):
        try:
            self.pgsql_cursor.execute("""
            delete from a_admin;
            commit;
            """)
            self.PostgreSQLConnection.commit()
            SQL.O_ONO = 1
        except KeyError:
            self.pgsql_cursor.execute("abort")
            return ''
    
    #审核
    def get_order_by_date(self, o_up_date=time.strftime('%Y-%m-%d %H:%M:%S')):
        """提交按日期返回订单"""
        try:
            self.pgsql_cursor.execute("""
            select o_ono, o_sno, o_up_date, o_price from o_order where o_up_date = '{o_up_date}';
            """.format(o_up_date = o_up_date))
            orders = self.pgsql_cursor.fetchall()
        except:
            self.pgsql_cursor.execute("abort")
            return ''
        return [(orders[i], self.get_pic(orders[i][0]), self.get_bike_tag(orders[i][0])) for i in range(len(orders))]
    
    
    def get_order_new(self):
        """返回未被审核过的订单,及其相关信息"""
        try:
            self.pgsql_cursor.execute("""
            select o_ono, o_sno, o_up_date, o_price from o_order where o_if_approved is null;
            """)
            orders = self.pgsql_cursor.fetchall()
        except:
            self.pgsql_cursor.execute("abort")
            return ''
        return [(orders[i], self.get_pic(orders[i][0]), self.get_bike_tag(orders[i][0])) for i in range(len(orders))]
    
    
    def get_order_unsold(self):
        """返回未卖出且审核通过的订单,及其相关信息"""
        try:
            self.pgsql_cursor.execute("""
            select o_ono, o_sno, o_up_date, o_price from o_order where o_if_sold = false and 
            o_if_approved = true;
            """)
            orders = self.pgsql_cursor.fetchall()
        except:
            self.pgsql_cursor.execute("abort")
            return ''
        return [(orders[i], self.get_pic(orders[i][0]), self.get_bike_tag(orders[i][0])) for i in range(len(orders))]
    
    
    def set_if_approved(self, o_ono, if_approved):
        """输入订单号和是否通过审核"""
        o_ono = str(o_ono)
        if if_approved:
            if_approved = 'true'
        else:
            if_approved = 'false'
            
        try:
            self.pgsql_cursor.execute("""
            update o_order set o_if_approved = '{if_approved}' where o_ono = '{o_ono}';
            """.format(o_ono = o_ono, if_approved = if_approved))
            self.PostgreSQLConnection.commit()
        except :
            self.pgsql_cursor.execute("abort")
            return ''
    
    
    def get_if_approved(self, o_ono):
        try:
            self.pgsql_cursor.execute("""
            select o_if_approved from o_order where o_ono = '{o_ono}';
            """.format(o_ono = o_ono))
            return self.pgsql_cursor.fetchall()[0][0]
        except :
            self.pgsql_cursor.execute("abort")
            return ''
    
    
    def init_admin_seller(self, s_sno, RQ_code_url):
        """创建超级卖家,充当平台收款方,买家付款到这个超级卖家的付款码中"""
        s_sno = str(s_sno)
        RQ_code_url = str(RQ_code_url)
        try:
            self.pgsql_cursor.execute("""
            insert into s_seller(s_sno, s_unpayed_amount, s_payed_amount, s_pay_RQ_code_url) values('{s_sno}', 0, 0, '{RQ_code_url}');
                                      """.format(s_sno = s_sno, RQ_code_url = RQ_code_url))
            self.PostgreSQLConnection.commit()
        except :
            self.pgsql_cursor.execute("abort")
            return ''
    
    
    def init_admin(self, u_uno, u_uname, u_password, u_phone_num, a_salary):
        """初始化管理员，插入一个管理员的信息，可插入多个"""
        u_uno = str(u_uno)
        u_uname = str(u_uname)
        u_password = str(u_password)
        u_phone_num = str(u_phone_num)
        a_salary = float(a_salary)
        
        self.sign_up(u_uno, u_uname, u_password, u_phone_num)
        try:
            self.pgsql_cursor.execute("""
            insert into a_admin(a_ano, a_salary) values('{a_ano}', {a_salary});
                                      """.format(a_ano = u_uno, a_salary = a_salary))
            self.PostgreSQLConnection.commit()
        except :
            self.pgsql_cursor.execute("abort")
            return ''
    
    
    def get_if_admin(self, u_uno):
        """获得用户号u_uno是否为管理员，是的话返回True"""
        u_uno = str(u_uno)
        try:
            self.pgsql_cursor.execute("""
            select a_ano from a_admin;
            """)
            admin_list = self.pgsql_cursor.fetchall()
            
            return u_uno in [each[0] for each in admin_list]
        except :
            self.pgsql_cursor.execute("abort")
            return ''
    

    def get_order_unsold_by_tag(self, bt_tag):
        """根据输入tag输出所有未卖出订单中符合tag条件的订单信息"""
        bt_tag = str(bt_tag)
        try:
            self.pgsql_cursor.execute("""
            select bt_ono from bt_bike_tag where bt_tag = '{bt_tag}';
            """.format(bt_tag = bt_tag))
            order_list = self.pgsql_cursor.fetchall()
            order_list = [each[0] for each in order_list]
        except :
            self.pgsql_cursor.execute("abort")
            return ''
        order_detail = list()
        for each_order in order_list:
            try:
                self.pgsql_cursor.execute("""
                select o_ono, o_sno, o_up_date, o_price from o_order where o_if_sold = false and o_ono =  '{o_ono}';
                """.format(o_ono = each_order))
                order_detail.append(self.pgsql_cursor.fetchall()[0])
            except:
                self.pgsql_cursor.execute("abort")
                return ''
        #return order_detail
        return [(order_detail[i], self.get_pic(order_detail[i][0]), self.get_bike_tag(order_detail[i][0])) for i in range(len(order_detail))]
        

    def get_order_unsold_by_sno(self, o_sno):
        """根据输入tag输出所有未卖出订单中符合tag条件的订单信息"""
        o_sno = str(o_sno)
        try:
            self.pgsql_cursor.execute("""
            select o_ono, o_sno, o_up_date, o_price from o_order where o_sno =  '{o_sno}';
            """.format(o_sno = o_sno))
            order_detail = self.pgsql_cursor.fetchall()
        except:
            self.pgsql_cursor.execute("abort")
            return ''
        # return order_detail
        return [(order_detail[i], self.get_pic(order_detail[i][0]), self.get_bike_tag(order_detail[i][0])) for i in range(len(order_detail))]
    
    
    def get_order_by_bno(self, o_bno):
        """根据输入tag输出所有未卖出订单中符合tag条件的订单信息
        订单号、卖家号、买家号、上架日期、出售日期、价格、卖家所得、买家付款额、订单是否已确认、订单确认日期"""
        o_bno = str(o_bno)
        try:
            self.pgsql_cursor.execute("""
            select o_ono, o_sno, o_bno, o_up_date, o_sold_date, o_price, o_seller_paid, o_buyer_paid, o_if_confirmed, o_confirmed_date
            from o_order where o_bno =  '{o_bno}';
            """.format(o_bno = o_bno))
            order_detail = self.pgsql_cursor.fetchall()
        except:
            self.pgsql_cursor.execute("abort")
            return ''
        #return order_detail
        return [order_detail[0], self.get_pic(order_detail[0][0]), self.get_bike_tag(order_detail[0][0])]
