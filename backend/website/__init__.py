from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import path
from flask_login import LoginManager
from flask import jsonify,request,session
from flask_login import login_user, login_required, logout_user, current_user
db = SQLAlchemy()
DB_NAME = "database.db"
from flask_login import UserMixin
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey,Column, String, Integer, CHAR, Float
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy

class Product(db.Model):
        __tablename__='products'
        id = db.Column('id', db.Integer, primary_key=True,autoincrement=True)
        name = db.Column('name', db.String(150))
        price = db.Column('price', db.Float)
        image_url = db.Column('image_url', db.String(200), nullable=False)
        product_type = db.Column('product_type', db.String(20))  # type include:desktop, laptop, motherboard, case, cpu,RAM
        description = db.Column('description', db.String(200))
        use = db.Column('use', db.String(20))  # use may be:business, academic, gaming or all
        match = db.Column('match', db.String(20))  # Intel->for all products that match intel CPU, AMD->match AMD,
        # both->for both, '-' if it is a desktop or laptop,  creater_id if it is configuration

        def __init__(self, name, price, image_url, product_type, descritpion, use, match):
            #self.id = id
            self.name = name
            self.price = price
            self.image_url = image_url
            self.product_type = product_type
            self.description = descritpion
            self.use = use
            self.match = match

        def __repr__(self):
            return {'id': self.id, 'name': self.name, 'price': self.price, 'image_url': self.image_url,
                    'product_type': self.product_type, 'description': self.description, 'use': self.use, 'match': self.match}



class Employee(db.Model, UserMixin):
        __tablename__='employees'
        id = db.Column('id',db.Integer, primary_key=True,autoincrement=True)
        username = db.Column('username',db.String(50), nullable=False,unique=True)
        password = db.Column('password',db.String(50),nullable=False)
        no_warnings=db.Column('no_warnings',db.Integer, default=0)
        no_compliments=db.Column('no_compliments',db.Integer, default=0)
        wage=db.Column('wage',db.Float, default=500)
        def __init__(self, username,password, no_warnings=0,no_compliments=0,wage=500) :
            
            self.username=username
            self.password=password
            self.no_warnings=no_warnings
            self.no_compliments=no_compliments
            self.wage=wage
        def __repr__(self):
            return {'id':self.id,'username':self.username, 'password':self.password,'no_warnings':self.no_warnings,'no_compliments':self.no_compliments, 'wage':self.wage}
    
class Owner(db.Model, UserMixin):
        __tablename__='owner'
        id = db.Column('id',db.Integer, primary_key=True,autoincrement=True, unique=True)
        username = db.Column('username',db.String(50),nullable=False)
        password = db.Column('password',db.String(50),nullable=False)
        def __init__(self,  username, password):
    
            self.username=username
            self.password=password
        def __repr__(self):
            return {'id':self.id,'username':self.username, 'password':self.password}
class Customer(db.Model, UserMixin):
        __tablename__='customers'
        id = db.Column('id',db.Integer, primary_key=True,autoincrement=True)
        email=db.Column('email',db.String(70), nullable=False,unique=True)
        username = db.Column('username',db.String(50), nullable=False,unique=True)
        password = db.Column('password',db.String(50),nullable=False)
        no_warnings=db.Column('no_warnings',db.Integer, default=0)
        no_compliments=db.Column('no_compliments',db.Integer, default=0)
        balance=db.Column('balance',db.Float, default=500)
        discount=db.Column('discount',db.Integer, default=0)
        def __init__(self, username,email,password, no_warnings,no_compliments,balance, discount) :
        
            self.username=username
            self.email=email
            self.password=password
            self.no_warnings=no_warnings
            self.no_compliments=no_compliments
            self.balance=balance
            self.discount=discount
        def __repr__(self):
            return {'id':self.id,'username':self.username,'email':self.email, 'password':self.password,'no_warnings':self.no_warnings,'no_compliments':self.no_compliments, 'balance':self.balance, 'discount':self.balance}
    

class Rating(db.Model):
        __tablename__='ratings'
        id= db.Column('id',db.Integer, primary_key=True,autoincrement=True)
        value=db.Column('value',db.Integer)
        customer_id=db.Column('customer_id',db.Integer, db.ForeignKey('customers.id'))
        product_id=db.Column('product_id',db.Integer, db.ForeignKey('products.id'))

        def __init__(self,value, cunstomer_id, product_id):
            
            self.value=value
            self.customer_id=cunstomer_id
            self.product_id=product_id
        def __repr__(self):
            return{'id':self.id, 'value':self.value,'customer_id':self.customer_id, 'product_id':self.product_id}
class Comment(db.Model):
        __tablename__='coments'
        id= db.Column('id',db.Integer, primary_key=True,autoincrement=True)
        text=db.Column('text',db.String(500))
        commentator_status=db.Column('commentator_statu',db.String(15))#status is visitor/customer/employee/owner
        commentator_id=db.Column('commentator_id',db.Integer, db.ForeignKey('customers.id'))
        product_id=db.Column('product_id',db.Integer, db.ForeignKey('products.id'))

        def __init__(self, text, commentator_status,commentator_id, product_id):
        
            self.text=text
            self.commentator_status=commentator_status
            self.commentator_id=commentator_id
            self.product_id=product_id
        def __repr__(self):
            return{'id':self.id, 'text':self.text,'commentator_id':self.commentator_id, 'commentator_status':self.commentator_status,'product_id':self.product_id}


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    with app.app_context():
        databasecreation(db)
    ###-----------database is ready ------------   
    @app.route('/api/products')
    def get_products():
            products = Product.query.all()
            return jsonify({'products': [p.__repr__() for p in products]})
    @app.route('/login', methods=['GET', 'POST'])
    def Login():
        username = request.form['email']
        password = request.form['password']
        account = request.form['account']
        if account=='Owner':
          user=Owner.query.filter_by(username=username).first()
          session_key='owner_id'
        elif account=='Employee':
            user=Employee.query.filter_by(username=username).first()
            session_key='employee_id'
        elif account=='Customer':
            user=Customer.query.filter_by(username=username).first()
            session_key='customer_id'

        if user:
            if user.password== password: 
                session[session_key] = user.id
                return jsonify({'success': True}), 200
            else:
                return jsonify({'status': 'error', 'message': 'Incorrect Password '})
        else:
             return jsonify({'status': 'error', 'message': 'Email does not exist.'}),401


    
    return app
















###-------------------DATABASE-----------------------------
def databasecreation(db):
    if not path.exists('instance/' + DB_NAME):
        db.create_all()
        print('Created Database!')


        product_info=[['MSI All-in-One Computer Modern AM242P', 799.0, 'https://c1.neweggimages.com/ProductImage/83-152-952-V22.jpg', 'desktop', 'MSI All-in-One Computer Modern AM242P 11M-1070US Intel Core i3 11th Gen 1115G4 (3.00GHz) 8GB DDR4 256 GB M.2 NVMe SSD 23.8" Windows 11 Home 64-bit', 'a', '-'], ['MSI All-in-One Computer PRO ', 1349.0, 'https://c1.neweggimages.com/ProductImageCompressAll1280/83-151-271-01.jpg', 'desktop', 'MSI All-in-One Computer PRO AP272 13M-287US Intel Core i7 13th Gen 13700 (2.10GHz) 16GB DDR4 1 TB M.2 NVMe SSD SSD 27" Windows 11 Pro 64-bit', 'b', '-'], ['Lenovo ThinkCentre  M920z 23.8" ', 629.0, 'https://c1.neweggimages.com/ProductImage/BJGES23032211WAEAD0.jpg', 'desktop', 'Lenovo ThinkCentre M920z 23.8" All in One Desktop Core i7-8700 3.2 GHz 16GB 512GB SSD Win10', 'b', '-'], ['Lenovo ThinkCentre M93z ', 193.99, 'https://c1.neweggimages.com/ProductImageCompressAll1280/BBP9S2211140S6TZYB9.jpg', 'desktop', 'Lenovo ThinkCentre M93z All in One i5-4570s 2.90GHZ 8GB RAM 1TB Hard Drive WIFI Wired Mouse and Keyboard Windows 10 Pro - Grade B', 'a', '-'], ['HP ProOne 600 G1 21.5” ', 589.99, 'https://c1.neweggimages.com/ProductImageCompressAll1280/A6AB_131388159916541969tJQD9yken6.jpg', 'desktop', 'HP ProOne 600 G1 21.5” LED All-in-One Desktop Intel Quad-Core i5-4570s 2.90Ghz 8GB DDR3 RAM 500 GB Hard Drive DVDRW Webcam Windows 10 Home 64-Bit 1920 x 1080p', 'b', '-'], ['MSI All-in-One Computer PRO AP272 12M', 1059.0, 'https://c1.neweggimages.com/ProductImageCompressAll1280/A24GD2212250E5VO972.jpg', 'desktop', 'MSI All-in-One Computer PRO AP272 12M-092US Intel Core i5 12th Gen 12400 (2.50GHz) 16 GB DDR4 (2 x 8 GB) 3200 MHz 500GB M.2 NVMe SSD 27" Windows 11 Pro', 'a', '-'], ['HP All-in-One Computer', 458.99, 'https://c1.neweggimages.com/ProductImageCompressAll1280/V1DSD211020WGMMF.jpg', 'desktop', 'HP All-in-One Computer 24-dd0117c Ryzen 3 3rd Gen 3250U (2.60GHz) 8GB DDR4 512 GB PCIe SSD 23.8" Windows 10 Home 64-bit', 'b', '-'], ['Lenovo V130 All-in-One, 19.5', 419.0, 'https://c1.neweggimages.com/ProductImageCompressAll1280/B0GJD23040714MKRRE8.jpg', 'desktop', 'Lenovo V130 All-in-One, 19.5" HD+ Display, Intel Celeron J4025, 16GB DDR4 RAM, 1TB PCIe SSD, Wi-Fi, Wired Keyboard & Mouse, Windows 11 Pro, Black', 'a', '-'], ['Acer All-in-One Computer Aspire C27', 799.99, 'https://c1.neweggimages.com/ProductImageCompressAll1280/83-101-894-22.png', 'desktop', 'Acer All-in-One Computer Aspire C27-1655-URi5 Intel Core i5 11th Gen 1135G7 (2.40GHz) 8GB DDR4 512 GB PCIe SSD 27" Windows 11 Home 64-bit', 'a', '-'], ['Dell OptiPlex 7450 23.8" FHD Touchscreen ', 564.99, 'https://c1.neweggimages.com/ProductImageCompressAll1280/AF0KD2203220WMHVD36.jpg', 'desktop', 'Dell OptiPlex 7450 23.8" FHD Touchscreen 1920 x 1080 All in One Desktop Intel Quad Core i5-7500 3.80GHz 16 GB DDR4 512 GB M.2 SSD + 1TB HD WiFi, Type-C USB, Webcam, Windows 10 Pro', 'b', '-'], ['New Dell Inspiron 5400 All-in-One Business Desktop', 845.0, 'https://c1.neweggimages.com/ProductImageCompressAll1280/B4U9D22110915D5IZ81.jpg', 'desktop', 'New Dell Inspiron 5400 All-in-One Business Desktop 23.8" Full HD Touchscreen Intel Iris Xe Graphics Intel Core i5-1135G7 12GB DDR4 RAM 256GB PCIe SSD 1TB HDD Wireless Keyboard + Mouse Windows 11 Pro', 'b', '-'], ['HP 27 All-in-One Desktop PC', 1258.99, 'https://c1.neweggimages.com/ProductImageCompressAll1280/A8X5S2206100WN56B19.jpg', 'desktop', 'HP 27 All-in-One Desktop PC, AMD Ryzen 7 5700U, 12 GB RAM, 256 GB SSD & 1 TB Hard Drive, Full HD IPS Display, Windows 11 Pro, 720p Privacy Webcam, Dual Mics, Keyboard and Mouse (27-CB0052, 2022)', 'g', '-'], ['HP 22-dd0000 22-dd0210 ', 499.0, 'https://c1.neweggimages.com/ProductImageCompressAll1280/A6ZPD2203200FZ0XW38.jpg', 'desktop', 'HP 22-dd0000 22-dd0210 All-in-One Computer - AMD Athlon Silver 3050U Dual-core (2 Core) 2.30 GHz - 4 GB RAM DDR4 SDRAM - 256 GB M.2 PCI Express NVMe SSD - 21.5" Full HD 1920 x 1080 - Desktop - Sn', 'a', '-'], ['ASUS All-in-One Computer M3700WUA-DS704 Ryzen 7 5000 Series 5700U ', 1162.99, 'https://c1.neweggimages.com/ProductImageCompressAll1280/V009D2210280ELO5E75.jpg', 'desktop', 'ASUS All-in-One Computer M3700WUA-DS704 Ryzen 7 5000 Series 5700U (1.80GHz) 16GB DDR4 512 GB PCIe SSD 27" Touchscreen Windows 11 Home 64-bit', 'a', '-'], ['Dell Inspiron 5400 24" ', 875.0, 'https://c1.neweggimages.com/ProductImageCompressAll1280/AE4ND22081217UCH6F3.jpg', 'desktop', 'Dell Inspiron 5400 24" Inch Full HD TouchScreen All-In-One PC,11th Gen Intel Core i5-1135G7 Processor,16GB DDR4,256GB SSD Plus 1TB HDD, Intel Iris Xe Graphics,Wifi-AX, Bluetooth,HDMI,Windows 10 Pro', 'b', '-'], ['MSI All-in-One Computer PRO AP243TP ', 749.99, 'https://c1.neweggimages.com/ProductImageCompressAll1280/AR0TD2210271BMKNY72.jpg', 'desktop', 'HP Essential All-in-One Computer 23.8" FHD AMD Ryzen 3, 8 GB; 512 GB SSD', 'b', '-'], ['MSI All-in-One Computer PRO AP243TP ', 1349.0, 'https://c1.neweggimages.com/ProductImageCompressAll1280/V1DSD2302030VV4650F.jpg', 'desktop', 'MSI All-in-One Computer PRO AP243TP 12M-007US Intel Core i7 12th Gen 12700 (2.10GHz) 16GB DDR4 1 TB M.2 SSD 23.8" Touchscreen Windows 11 Pro 64-bit', 'b', '-'], ['ACER Aspire 27" FHD Premium AIO Computer ', 969.99, 'https://c1.neweggimages.com/ProductImageCompressAll1280/AEYJS221017t2fsF.jpg', 'desktop', 'ACER Aspire 27" FHD Premium AIO Computer | 12th Gen Intel Core i5-1235U Processor | 16GB RAM | 1TB SSD | Intel Iris Xe Graphics | Wireless Mouse & Keyboard | Windows 11 | Bundle with Mouse Pad', 'a', '-'], ['Dell Inspiron 5410 24"', 899.0, 'https://c1.neweggimages.com/ProductImageCompressAll1280/AE4ND2211100CAHGND3.jpg', 'desktop', 'Dell Inspiron 5410 24" Inch Full HD TouchScreen All-In-One PC,12th Gen Intel Core i5-1235U 10-Core Processor,16GB DDR4,256GB SSD Plus 1TB HDD, Intel Graphics,Wifi-AX, Bluetooth,HDMI,Windows 10 Pro', 'b', '-'], ['ASUS All-in-One Computer Vivo', 688.99, 'https://c1.neweggimages.com/ProductImage/A0ZXD2203211C5Z5342.jpg', 'desktop', 'ASUS All-in-One Computer Vivo AiO V241EA-DB003 Pentium Gold 7505 (2.00GHz) 8GB DDR4 512 GB PCIe SSD 23.8" Windows 10 Home 64-bit', 'a', '-'], ['ACER Aspire 27" FHD Premium AIO Computer ', 1127.03, 'https://c1.neweggimages.com/ProductImageCompressAll1280/V009D2206230EJ25K35.jpg', 'laptop', 'Lenovo Laptop ThinkBook 13x G2 IAP Intel Core i5 12th Gen 1235U (1.30GHz) 16GB Memory 512 GB PCIe SSD Intel Iris Xe Graphics 13.3" Touchscreen Windows 11 Pro 64-bit 21AT000XUS', 'b', '-'], ['ASUS Laptop ExpertBook', 816.2, 'https://c1.neweggimages.com/ProductImage/A6ZPD2204210KRS4E21.jpg', 'laptop', 'ASUS Laptop ExpertBook Intel Core i5 11th Gen 1135G7 (2.40GHz) 8GB Memory 256 GB SSD Intel Iris Xe Graphics 15.6" Windows 10 Pro 64-bit B1500CEA-XH51', 'b', '-'], ['Toshiba Dynabook Tecra ', 299.99, 'https://c1.neweggimages.com/ProductImageCompressAll1280/1B4-0019-015E2-S04.jpg', 'laptop', 'Toshiba Dynabook Tecra A40-G Intel Celeron Processor 5205U 1.90 GHz, 14.0" HD, 4 GB DDR4, 128 GB PCIe NVMe, Intel UHD Graphics, 802.11ax Wireless, Bluetooth, Windows 10 Pro Education', 'a', '-'], ['ASUS ZenBook 14 Ultra-Slim Laptop ', 1034.99, 'https://c1.neweggimages.com/ProductImageCompressAll1280/34-236-056-V01.jpg', 'laptop', 'ASUS ZenBook 14 Ultra-Slim Laptop 14" FHD Display, AMD Ryzen 7 5800H CPU, AMD Radeon Graphics, 16GB RAM, 1TB PCIe SSD, NumberPad, Windows 11 Pro, Pine Grey, UM425QA-EH74', 'b', '-'], ['ASUS VivoBook S 16X Slim Laptop', 864.99, 'https://c1.neweggimages.com/ProductImageCompressAll1280/34-236-317-01.jpg', 'laptop', 'ASUS VivoBook S 16X Slim Laptop, 16" WUXGA (1920 x 1200) 16:10 Display, Intel Core i5-12500H CPU, 8GB RAM, 512GB NVMe SSD, Windows 11 Home, Midnight Black, S5602ZA-DB51', 'b', '-'], ['Acer Laptop Aspire 5', 499.95, 'https://c1.neweggimages.com/ProductImageCompressAll1280/34-360-142-V01.jpg', 'laptop', 'Acer Laptop Aspire 5 Intel Core i5 11th Gen 1135G7 (2.40GHz) 12GB Memory 512 GB PCIe SSD Intel Iris Xe Graphics 14.0" Windows 11 Home 64-bit A514-54-5819', 'a', '-'], ['SAMSUNG Laptop Galaxy Book2', 1249.99, 'https://c1.neweggimages.com/ProductImageCompressAll1280/34-132-511-S01.jpg', 'laptop', 'SAMSUNG Laptop Galaxy Book2 Pro Intel Core i5 12th Gen 1240P (1.70GHz) 8GB Memory 512 GB SSD Intel Iris Xe Graphics 15.6" Windows 11 Home 64-bit NP950XED-KA2US', 'b', '-'], ['MSI Laptop Prestige', 957.99, 'https://c1.neweggimages.com/ProductImage/34-156-166-S30.jpg', 'laptop', 'MSI Laptop Prestige 14Evo Intel Core i5 12th Gen 1240P (1.70GHz) 16GB Memory 512 GB NVMe SSD Intel Iris Xe Graphics 14.0" Windows 11 Home 64-bit Prestige 14Evo A12M-013', 'a', '-'], ['ASUS ZenBook Duo 14 UX482 14', 1137.99, 'https://c1.neweggimages.com/ProductImage/34-236-020-01.jpg', 'laptop', 'ASUS ZenBook Duo 14 UX482 14" FHD Touch Display, Intel Evo Platform, Core i5-1155G7, 8GB RAM, 512GB PCIe SSD, ScreenPad Plus, Windows 10 Home, Wifi 6, Celestial Blue, UX482EAR-EB51T', 'b', '-'], ['ASUS ZenBook Duo 14 UX482', 1439.99, 'https://c1.neweggimages.com/ProductImage/34-736-315-S05.jpg', 'laptop', 'Microsoft Surface Laptop 4 AMD Ryzen 7 4000 Series 4980U 8 GB LPDDR4X Memory 512 GB SSD AMD Radeon Graphics 15" PixelSense Touchscreen Windows 10 Home 64-bit - Platinum - 5W6-00001', 'b', '-'], ['MSI Laptop Summit E14Evo', 1166.22, 'https://c1.neweggimages.com/ProductImage/34-156-153-V07.jpg', 'laptop', 'MSI Laptop Summit E14Evo Intel Core i5 12th Gen 1240P (1.70GHz) 16GB Memory 512 GB NVMe SSD Intel Iris Xe Graphics 14.0" Windows 11 Pro 64-bit Summit E14Evo A12M-026', 'a', '-'], ['ASUS Laptop ZenBook Pro Duo', 2939.99, 'https://c1.neweggimages.com/ProductImage/34-236-213-01.jpg', 'laptop', 'ASUS Laptop ZenBook Pro Duo Intel Core i9 12th Gen 12900H (2.50GHz) 32GB Memory 1 TB PCIe SSD NVIDIA GeForce RTX 3060 Laptop GPU 15.6" 4K / UHD Touchscreen Windows 11 Pro 64-bit UX582ZM-XS99T', 'b', '-'], ['HP Laptop ENVY', 1409.99, 'https://c1.neweggimages.com/ProductImage/V1DSD22070712MHRJ28.jpg', 'laptop', 'HP Laptop ENVY Intel Core i7 12th Gen 12700H (2.30GHz) 16GB Memory 512 GB PCIe SSD Intel Arc A370M 16.0" Touchscreen Windows 11 Home 64-bit 16-h0010nr', 'a', '-'], ['Microsoft Surface Laptop', 1399.99, 'https://c1.neweggimages.com/ProductImage/34-736-694-01.png', 'laptop', 'Microsoft Surface Laptop 5 - 13.5" Touchscreen - Intel Core i7-1255U - 16GB RAM - 512GB SSD - Windows 11 Home - Intel Evo Platform - RBG-00026 - Matte Black', 'a', '-'], ['Microsoft Surface Laptop ', 1399.99, 'https://c1.neweggimages.com/ProductImage/A24GD2210260CO40S73.jpg', 'laptop', 'Microsoft Surface Laptop 5 - 13.5" Touchscreen - Intel Core i7-1255U - 16GB RAM - 512GB SSD - Windows 11 Home - Intel Evo Platform - RBG-00062 - Sandstone', 'a', '-'], ['Lenovo Laptop Slim 7 ProX ', 1404.21, 'https://c1.neweggimages.com/ProductImage/A9UWD2209200FN8OAB8.jpg', 'laptop', 'Lenovo Laptop Slim 7 ProX 14IAH7 Intel Core i7 12th Gen 12700H (2.30GHz) 16GB Memory 512 GB PCIe SSD NVIDIA GeForce RTX 3050 Laptop GPU 14.5" Touchscreen Windows 11 Home 64-bit 82V10000US', 'B', '-'], ['Acer Swift 3 Thin & Light Laptop', 899.99, 'https://c1.neweggimages.com/ProductImage/A8TKS210327LyxnR.jpg', 'laptop', 'Acer Swift 3 Thin & Light Laptop, 14" Full HD IPS, AMD Ryzen 7 4700U Octa-Core, Radeon Graphics, 8GB RAM, 512GB NVMe-PCIe SSD, Wi-Fi 6, Backlit Keyboard, Fingerprint Reader, Windows 10 Home', 'b', '-'], ['SAMSUNG Laptop Galaxy Book2', 587.19, 'https://c1.neweggimages.com/ProductImage/34-132-362-S01.jpg', 'laptop', 'SAMSUNG Laptop Galaxy Book Ion NP930XCJ-K01CA Intel Core i5 10th Gen 10210U (1.60 GHz) 8 GB Memory 256 GB NVMe SSD Intel UHD Graphics 13.3" Windows 10 Home 64-bit', 'a', '-'], ['SAMSUNG Laptop Galaxy Book Pro ', 617.0, 'https://c1.neweggimages.com/ProductImage/A1CZD210514JNBJC.jpg', 'laptop', 'SAMSUNG Laptop Galaxy Book Pro Intel Core i5 11th Gen 1135G7 (2.40GHz) 8 GB LPDDR4X Memory 512 GB SSD Intel Iris Xe Graphics 15.6" Windows 10 Home NP950XDB-KA2US', 'b', '-'], ['SAMSUNG Laptop Galaxy Book Pro', 1099.0, 'https://www.newegg.com/mystic-silver-samsung-galaxy-book-pro-np950xdb-ka2us-mainstream/p/N82E16834132410?Item=9SIAKS8JJ74494', 'laptop', 'SAMSUNG Laptop Galaxy Book Pro Intel Core i5 11th Gen 1135G7 (2.40GHz) 8 GB LPDDR4X Memory 512 GB SSD Intel Iris Xe Graphics 15.6" Windows 10 Home NP950XDB-KA2US', 'b', '-'], ['HP Laptop EliteBook 1040 G9', 1099.0, 'https://c1.neweggimages.com/ProductImage/A6ZPD2206240SHCP196.jpg', 'laptop', 'HP Laptop EliteBook 1040 G9 Intel Core i5 12th Gen 1235U (1.30GHz) 16GB Memory 256 GB PCIe SSD Intel Iris Xe Graphics 14.0" Windows 11 Pro 64-bit 6E5C4UT#ABA', 'a', '-'], ['ASUS Z790-E ', 499.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0653703_443614.jpg', 'motherboard', 'ASUS Z790-E ROG Strix Gaming WiFi Intel LGA 1700 ATX Motherboard', 'g', 'Intel'], ['MSI X570S MAG TOMAHAWK MAX', 229.0, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0640444_310110.jpg', 'motherboard', 'X570S MAG TOMAHAWK MAX WiFi AMD AM4 ATX Motherboard', 'a', 'Intel'], ['Z790I MPG Edge', 359.0, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0664308_549741.jpg', 'motherboard', 'Z790I MPG Edge WiFi Intel LGA 1700 Mini-ITX Motherboard', 'b', 'Intel '], ['ASUS Z790 ROG', 629.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0653702_443572.jpg ', 'motherboard', 'ASUS Z790 ROG Maximus Hero Intel LGA 1700 ATX Motherboard', 'g', 'Intel'], ['ASRock X670E Pro RS', 249.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0652773_438705.jpg', 'motherboard', 'X670E Pro RS AMD AM5 ATX Motherboard', 'b', 'AMD'], ['Gigabyte B650I Aorus', 269.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0664322_549766.jpg ', 'motherboard', 'Gigabyte B650I Aorus Ultra AMD AM5 Mini-ITX Motherboard', 'b', 'AMD'], ['ASRock B650M PG Riptide ', 159.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0660141_513226.jpg', 'motherboard', 'ASRock B650M PG Riptide AMD AM5 microATX Motherboard', 'a', 'AMD'], ['Gigabyte Z790 AORUS ELITE AX', 259.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0659678_516385.jpg', 'motherboard', 'Gigabyte Z790 AORUS ELITE AX Intel LGA 1700 ATX Motherboard', 'b', 'Intel'], ['Corsair Vengeance RGB', 334.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0665485_566133.jpg', 'RAM', 'Vengeance RGB 96GB (2 x 48GB) DDR5-5600 PC5-44800 CL40 Dual Channel Desktop Memory Kit CMH96GX5M2B5600C40 - Black', 'g', 'AMD'], ['Corsair Dominator Platinum RGB', 169.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0653876_443093.jpg', 'RAM', 'Corsair Dominator Platinum RGB 32GB (2 x 16GB) DDR5-6000 PC5-48000 CL36 Dual Channel Desktop Memory Kit CMT32GX5M2D6000 - Black', 'a', 'Intel'], ['TeamGroup T-Force Delta RGB ', 259.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0662950_538652.jpg', 'RAM', 'TeamGroup T-Force Delta RGB 64GB (2 x 32GB) DDR5-6000 PC5-48000 CL38 Dual Channel Desktop Memory Kit FF4D564G6000HC3 - White', 'b', 'Intel '], ['TeamGroup Vulcan 64GB', 234.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0662952_538694.jpg', 'RAM', 'TeamGroup Vulcan 64GB (2 x 32GB) DDR5-6000 PC5-48000 CL38 Dual Channel Desktop Memory Kit FLBD564G6000HC3 - Black', 'b', 'AMD'], ['G.Skill Ripjaws S5', 199.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0649240_400457.jpg', 'RAM', 'G.Skill Ripjaws S5 64GB (2 x 32GB) DDR5-5200 PC5-41600 CL36 Dual Channel Desktop Memory Kit F5-5200J3636D32GX2-RS5K - Black', 'a', 'AMD'], ['TeamGroup T-FORCE Vulcan Alpha 32GB', 92.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0653833_443259.jpg', 'RAM', 'TeamGroup T-FORCE Vulcan Alpha 32GB (2 x 16GB) DDR5-5600 PC5-44800 CL40 Dual Channel Desktop Memory Kit FLABD532G5600HC - Black', 'a', 'AMD'], ['Crucial 32GB ', 109.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0661340_524926.jpg', 'RAM', 'Crucial 32GB (2 x 16GB) DDR5-5600 PC5-44800 CL46 Dual Channel Desktop Memory Kit CT2K16G56C46U5 - Black', 'a', 'AMD'], ['64GB (2 x 32GB) ', 174.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0643707_343442.jpg', 'RAM', '64GB (2 x 32GB) DDR5-4800 PC5-38400 CL40 Dual Channel Desktop Memory Kit CT2K32G48C40U5 - Black', 'a', 'Intel'], ['Vengeance RGB 96GB ', 334.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0665485_566133.jpg', 'RAM', 'Vengeance RGB 96GB (2 x 48GB) DDR5-5600 PC5-44800 CL40 Dual Channel Desktop Memory Kit CMH96GX5M2B5600C40 - Black', 'g', 'Intel'], ['Flare X5 Series 32GB ', 119.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0653727_440792.jpg', 'RAM', 'Flare X5 Series 32GB (2 x 16GB) DDR5-6000 PC5-48000 CL36 Dual Channel Desktop Memory Kit F5-6000J3636F16GX2-FX5 - Black', 'b', 'AMD'], ['Dominator Platinum RGB 32GB', 159.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0653876_443093.jpg', 'RAM', 'Dominator Platinum RGB 32GB (2 x 16GB) DDR5-6000 PC5-48000 CL36 Dual Channel Desktop Memory Kit CMT32GX5M2D6000 - Black', 'a', 'AMD'], ['T-Force Delta Alpha RGB 32GB', 159.99, ' https://m.media-amazon.com/images/I/81JEfdUVCTL._AC_SL1500_.jpg ', 'RAM', 'T-Force Delta Alpha RGB 32GB (2 x 16GB) DDR5-5600 PC5-44800 CL40 Dual Channel Desktop Memory Kit FF8D532G5600HC4 - White', 'b', 'Intel'], ['Trident Z5 Neo RGB Series 32GB ', 149.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0653732_440784.jpg ', ' RAM', 'Trident Z5 Neo RGB Series 32GB (2 x 16GB) DDR5-6000 PC5-48000 CL36 Dual Channel Desktop Memory Kit F5-6000J3636F16GX2-TZ5NR - Black', 'b', 'Intel'], ['Trident Z5 RGB 32GB', 159.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0646756_375238.jpg', 'RAM', 'Trident Z5 RGB 32GB (2 x 16GB) DDR5-6400 PC5-51200 CL32 Dual Channel Desktop Memory Kit F5-6400J3239G16GX2-TZ5RK - Black', 'b', 'Intel'], ['Vengeance RGB 64GB', 299.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0660400_516708.jpg ', 'RAM', 'Vengeance RGB 64GB (2 x 32GB) DDR5-5600 PC5-44800 CL40 Dual Channel Desktop Memory Kit CMH64GX5M2B5600 - Black', 'g', 'Intel'], ['H5 Flow Tempered Glass ATX Mid', 94.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0652315_433417.jpg ', 'case', 'H5 Flow Tempered Glass ATX Mid-Tower Computer Case - Black', 'all', 'both'], ['X1 Tempered Glass ATX Mid-', 44.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0643497_340034.jpg ', 'case', 'X1 Tempered Glass ATX Mid-Tower Computer Case - Black', 'all', 'both'], ['O11 Dynamic EVO Tempered Glass ATX Mid', 169.99, ' https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0645430_360057.jpg ', 'case', 'O11 Dynamic EVO Tempered Glass ATX Mid-Tower Computer Case - White', 'all', 'both'], ['Lancool 205 Mesh Type C Tempered Glass ATX Mid', 89.99, ' https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0650078_409540.jpg ', 'case', 'Lancool 205 Mesh Type C Tempered Glass ATX Mid-Tower Computer Case - Black', 'all', 'both'], ['O11 Dynamic EVO Tempered Glass ATX Mid', 159099.0, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0645428_360032.jpg ', 'case', 'O11 Dynamic EVO Tempered Glass ATX Mid-Tower Computer Case - Black', 'all', 'both'], ['Lancool 216 RGB Tempered Glass ATX Mid', 109.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0660145_512251.jpg', 'case', 'Lancool 216 RGB Tempered Glass ATX Mid-Tower Computer Case - Black', 'all', 'both'], ['LANCOOL III RGB Tempered Glass ATX Mid', 169.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0649250_399089.jpg', 'case', 'LANCOOL III RGB Tempered Glass ATX Mid-Tower Computer Case - Black', 'all', 'both'], ['Lancool II MESH Type C RGB', 109.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0642886_329698.jpg', 'case', 'Lancool II MESH Type C RGB Tempered Glass ATX Mid-Tower Computer Case - Black', 'all', 'both'], ['Ryzen 9 7900X Raphael AM5 ', 549.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0652682_436535.jpg', 'CPU', 'Ryzen 9 7900X Raphael AM5 4.7GHz 12-Core Boxed Processor - Heatsink Not Included', 'b', 'AMD'], ['Ryzen 9 5900X Vermeer', 549.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0630283_195099.jpg', 'CPU', 'Ryzen 9 5900X Vermeer 3.7GHz 12-Core AM4 Boxed Processor - Heatsink Not Included', 'b', 'AMD'], ['Ryzen 5 3600 Matisse ', 149.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0653895_442897.jpg', 'CPU', 'Ryzen 5 3600 Matisse 3.6GHz 6-Core AM4 Boxed Processor - Wraith Stealth Cooler Included', 'a', 'AMD'], ['Ryzen 7 7700X Raphael AM5', 399.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0652683_436501.jpg', 'CPU', 'Ryzen 7 7700X Raphael AM5 4.5GHz 8-Core Boxed Processor - Heatsink Not Included', 'b', 'AMD'], ['Ryzen 5 5600G Cezanne', 259.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0639744_301259.jpg', 'CPU', 'Ryzen 5 5600G Cezanne 3.9GHz 6-Core AM4 Boxed Processor - Wraith Stealth Cooler Included', 'a', 'AMD'], ['Ryzen 5 5600X Vermeer', 299.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0630285_195073.jpg', 'CPU', 'Ryzen 5 5600X Vermeer 3.7GHz 6-Core AM4 Boxed Processor - Wraith Stealth Cooler Included', 'b', 'AMD'], ['Core i7-13700K Raptor Lake', 519.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0652626_436196.jpg', 'CPU', 'Core i7-13700K Raptor Lake 3.4GHz Sixteen-Core LGA 1700 Boxed Processor - Heatsink Not Include', 'b', 'Intel'], ['Core i9-12900K Alder Lake', 649.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0641915_326694.jpg', 'CPU', 'Core i9-12900K Alder Lake 3.2GHz Sixteen-Core LGA 1700 Boxed Processor - Heatsink Not Included', 'g', 'Intel'], ['Core i9-13900K Raptor Lake', 729.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0652624_436188.jpg', 'CPU', 'Core i9-13900K Raptor Lake 3.0GHz Twenty Four-Core LGA 1700 Boxed Processor - Heatsink Not Included', 'g', 'Intel'], ['Core i5-13600K Raptor Lake', 379.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0652628_436212.jpg', 'CPU', 'Core i5-13600K Raptor Lake 3.5GHz Fourteen-Core LGA 1700 Boxed Processor - Heatsink Not Included', 'b', 'Intel'], ['Core i3-13100 Raptor Lake', 149.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0662150_533471.jpg', 'CPU', 'Core i3-13100 Raptor Lake 3.4GHz Quad-Core LGA 1700 Boxed Processor - Heat Sink Included', 'a', 'Intel'], ['Core i5-12400 Alder Lake', 219.99, 'https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/0645582_362020.jpg', 'CPU', 'Core i5-12400 Alder Lake 2.5GHz Six-Core LGA 1700 Boxed Processor - Intel Stock Cooler Included', 'a', 'Intel']]
        for info in product_info:
            product=Product(name=info[0],price=info[1],image_url=info[2],product_type=info[3],  descritpion=info[4], use=info[5],match=info[6])
            db.session.add(product)

        owner=Owner(username='owner123', password='csc322')
        db.session.add(owner)
        employee1=Employee(username='employee1', password='pass1')
        db.session.add(employee1)
        employee2=Employee(username='employee2', password='pass2')
        db.session.add(employee2)
        employee3=Employee(username='employee3', password='pass3')
        db.session.add(employee3)



        db.session.commit()


