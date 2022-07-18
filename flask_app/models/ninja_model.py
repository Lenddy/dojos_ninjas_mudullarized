from flask_app.config.connectTomysql import connectToMySQL
from flask_app import db




class Ninjas:
    def __init__(self,data):
        self.id = data["id"]
        self.f_name = data["f_name"]
        self.l_name = data["l_name"]
        self.age = data["age"]
        self .dojos_id = data["dojos_id"]



    @classmethod
    def add_ninja(cls,data):
        query  ="insert into ninjas (f_name,l_name,age,dojos_id) values (%(f_name)s,%(l_name)s,%(age)s,%(dojos_id)s);"
        result = connectToMySQL(db).query_db(query,data)
        print(result)
        return result



