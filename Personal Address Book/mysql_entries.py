import pymysql


class users_table:
    def __init__(self):
        self.db = pymysql.connect(host="localhost", user="root", password="vicky", db="PABapp")
        self.cursor = self.db.cursor()

    def get_uname(self, uid):
        cmd1 = "select Username from idpass where Userid='%s'" % uid
        self.cursor.execute(cmd1)
        username = self.cursor.fetchone()
        self.db.commit()
        self.db.close()
        return username[0]

    def view_table(self, uid):
        cmd2 = "select * from %s" % uid
        self.cursor.execute(cmd2)
        entries = self.cursor.fetchall()
        self.db.commit()
        self.db.close()
        return entries

    def create_entry(self, uid, a, b, c, d, e, f, g):
        cmd1 = f"""insert into {uid} (Firstname, Lastname, Birthday, Mobno, Mail_id, Address, Notes) 
        values(%s,%s,%s,%s,%s,%s,%s)"""
        cmd2 = (a, b, c, d, e, f, g)
        self.cursor.execute(cmd1, cmd2)
        self.db.commit()
        self.db.close()
        print("\n--Entry Added Successfully!--")

    def get_sno_list(self, uid):
        cmd3 = "select SNo from %s" % uid
        self.cursor.execute(cmd3)
        sno_data = self.cursor.fetchall()
        sno_list = []
        self.db.commit()
        self.db.close()
        for i in sno_data:
            sno_list.append(i[0])
        return sno_list

    def update_entry(self, uid, entry, value, sno):
        cmd4 = f"""update {uid} set %s='%s' where SNo = %s""" % (entry, value, sno)
        self.cursor.execute(cmd4)
        self.db.commit()
        self.db.close()
        print(f"\n--Entry of {value} to column({entry}) Updated Successfully--\n")

    def delete_entry(self, uid, sno):
        cmd5 = f"""delete from {uid} where SNo = %s""" % sno
        self.cursor.execute(cmd5)
        self.db.commit()
        self.db.close()
        print(f"\n--The SNo:{sno} entry has been Deleted Successfully--")

