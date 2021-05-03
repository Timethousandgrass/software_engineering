CREATE TABLE u_user(
u_uno varchar(8) Primary Key,	--用户代码, 学号
u_uname varchar(8) not null,	--用户名
u_password varchar(20) not null,	--用户密码
u_phone_num varchar(20)
);

CREATE TABLE a_admin(
a_ano varchar(8) Primary Key,	--管理员
a_salary real,					--管理员薪水
FOREIGN KEY(a_ano) REFERENCES u_user(u_uno)
);

CREATE TABLE s_seller(
s_sno varchar(8) Primary Key,	--卖家号码
s_unpayed_amount real,			--平台欠下卖家的金额
s_payed_amount real,			--平台已支付卖家调度金额
s_pay_RQ_code_url varchar(128), --平台支付给卖家所用的支付码
FOREIGN KEY(s_sno) REFERENCES u_user(u_uno)
);

CREATE TABLE b_buyer(
b_bno varchar(8) Primary Key,	--买家号码
b_payed_amount real,			--买家已支付金额
FOREIGN KEY(b_bno) REFERENCES u_user(u_uno)
);

CREATE TABLE o_order(
o_ono varchar(10) Primary Key,	--订单号
o_sno varchar(8) not null,		--卖家号码
o_bno varchar(8),		--买家号码
o_if_sold BOOLEAN,				--是否已出售
o_wear_rate real not null,		--二手车的评估磨损度,自行车的售价为 o_wear_rate*o_price
o_code varchar(10),				--自行车密码锁密码
o_up_date timestamp without time zone not null,		--上架时间
o_sold_date timestamp without time zone,				--出售时间
o_price real not null,			--卖家购入自行车时的价格
o_buyer_paid real,				--买家已付金额
o_seller_paid real,				--已付卖家金额
o_if_approved BOOLEAN,			--是否审核通过
o_if_confirmed BOOLEAN,
o_confirmed_date timestamp without time zone,				--出售时间
FOREIGN KEY(o_sno) REFERENCES s_seller(s_sno),
FOREIGN KEY(o_bno) REFERENCES b_buyer(b_bno)
);

CREATE TABLE p_pic(
p_ono varchar(10),				--照片依赖的订单号,某个订单下,自行车的预览照片
p_url varchar(128),				--照片外链
PRIMARY KEY(p_ono, p_url),
FOREIGN KEY(p_ono) REFERENCES o_order(o_ono)
);

CREATE TABLE bt_bike_tag(
bt_ono varchar(10),				--订单自行车的各个tags
bt_tag varchar(64),			--具体类型,
PRIMARY KEY(bt_ono, bt_tag),
FOREIGN KEY(bt_ono) REFERENCES o_order(o_ono)
);



insert into u_user values('20180001', 'AAA', '11111111');
insert into u_user values('20180002', 'BBB', '11111111');
insert into u_user values('20180003', 'CCC', '11111111');
insert into u_user values('20180004', 'DDD', '11111111');


insert into s_seller values('20180001', 0, 200.2);
insert into s_seller values('20180003', 0, 200.2);
insert into b_buyer  values('20180002', 200.2);
insert into b_buyer  values('20180004', 200.2);


insert into o_order values('001', '20180001', '20180002',
true, 0.8, '88888888', '2021-1-1', '2021-1-2', '240.24');

insert into o_order values('002', '20180003', '20180004',
true, 0.9, '66666666', '2021-4-1', '2021-4-2', '100');

insert into p_pic values('001', 'https://wx3.sinaimg.cn/large/006AfEgvgy1gpvx1uy428j31x32wqnpl.jpg');
insert into p_pic values('001', 'https://wx2.sinaimg.cn/large/006AfEgvgy1gpvx20sl8rj31xf2zxkjt.jpg');
insert into p_pic values('001', 'https://wx4.sinaimg.cn/large/006AfEgvgy1gpvx24se86j3214340b2h.jpg');
insert into p_pic values('001', 'https://wx1.sinaimg.cn/large/006AfEgvgy1gpvx28c4ymj322o340he1.jpg');
insert into p_pic values('001', 'https://wx2.sinaimg.cn/large/006AfEgvgy1gpvx2dr88tj3204340e89.jpg');
insert into p_pic values('001', 'https://wx3.sinaimg.cn/large/006AfEgvgy1gpvx2hy3thj322o3404qx.jpg');
insert into p_pic values('001', 'https://wx4.sinaimg.cn/large/006AfEgvgy1gpvx2m2is3j31x73024qv.jpg');

insert into p_pic values('002', 'https://wx2.sinaimg.cn/large/006AfEgvgy1gpx0wq6zn0j322o340x6q.jpg');
insert into p_pic values('002', 'https://wx4.sinaimg.cn/large/006AfEgvgy1gpx0wt7lnsj31yk33ce82.jpg');
insert into p_pic values('002', 'https://wx4.sinaimg.cn/large/006AfEgvgy1gpx0wxkjp7j322o340hdu.jpg');
insert into p_pic values('002', 'https://wx2.sinaimg.cn/large/006AfEgvgy1gpx0wz7tb1j31qk2nsu0x.jpg');
insert into p_pic values('002', 'https://wx1.sinaimg.cn/large/006AfEgvgy1gpx0x1mrpyj31og2ioe81.jpg');
insert into p_pic values('002', 'https://wx1.sinaimg.cn/large/006AfEgvgy1gpx0x4hfh8j320k340hdu.jpg');
insert into p_pic values('002', 'https://wx3.sinaimg.cn/large/006AfEgvgy1gpx0xb2ho2j31zk3404qr.jpg');

insert into p_pic values('002', 'https://wx4.sinaimg.cn/large/006AfEgvgy1gpx4m7k4mij31kq2bchdw.jpg');
insert into p_pic values('002', 'https://wx1.sinaimg.cn/large/006AfEgvgy1gpx4mf4w46j31jk2bcqv8.jpg');
insert into p_pic values('002', 'https://wx3.sinaimg.cn/large/006AfEgvgy1gpx4mawvr4j31jk2bce84.jpg');

select * from o_order, p_pic
where o_order.o_ono = p_pic.p_ono and o_order.o_sno = '20180001';

--begin transaction;
--DROP TABLE s_seller cascade;
--DROP TABLE b_buyer cascade;
--DROP TABLE o_order cascade;
--DROP TABLE p_pic cascade;
--commit;