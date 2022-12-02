import pymysql

class userid:
    def __init__(self):
        self.db = pymysql.connect(host="localhost", user="root", password="vicky", db="PABapp")
        self.cursor = self.db.cursor()

    def get_userid(self):
        self.cursor.execute("select Userid from idpass")
        db_uid = self.cursor.fetchall()
        db_uid_list = []
        for i in db_uid:
            db_uid_list.append(i[0].lower())
        self.db.commit()
        self.db.close()
        return db_uid_list

    def get_password(self, uid):
        cmd1 = "select Userpass from idpass where Userid='%s'" % uid
        self.cursor.execute(cmd1)
        upass = self.cursor.fetchone()
        self.db.commit()
        self.db.close()
        return upass[0]

    def get_mob(self, uid):
        cmd2 = "select Usermob from idpass where Userid='%s'" % uid
        self.cursor.execute(cmd2)
        umob = self.cursor.fetchone()
        self.db.commit()
        self.db.close()
        return umob[0]

class create_new_user(userid):
    def __init__(self, uname, uid, upass, umob):
        super().__init__()
        self.uname = uname
        self.uid = uid
        self.upass = upass
        self.umob = umob

    def create_user(self):
        cmd1 = """insert into idpass (Username, Userid, Userpass, Usermob) values(%s,%s,%s,%s)"""
        cmd2 = (self.uname, self.uid, self.upass, self.umob)
        self.cursor.execute(cmd1, cmd2)
        cmd3 = """create table %s(SNo smallint primary key auto_increment,
                Firstname varchar(30) not null,
                Lastname varchar(30), 
                Birthday varchar(20),
                Mobno varchar(20), 
                Mail_id varchar(40), 
                Address varchar(200),
                Notes varchar(200))""" % self.uid
        self.cursor.execute(cmd3)
        print("\nSignUp Process Success!\n")
        print(f"Hello {self.uname}, welcome to my App!")
        self.db.commit()
        self.db.close()

def get_idlist():
    idlist = userid().get_userid()
    return idlist

def check_umob(uid, mob):
    db_mob = userid().get_mob(uid)

    if mob == db_mob:
        return userid().get_password(uid)
    else:
        return False

