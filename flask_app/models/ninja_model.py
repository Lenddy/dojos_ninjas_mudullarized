from flask_app.config.connectTomysql import connectToMySQL
from flask_app import db
from flask import flash

class Ninjas:
    def __init__(self,data):
        self.id = data["id"]
        self.f_name = data["f_name"]
        self.l_name = data["l_name"]
        self.age = data["age"]
        self .dojos_id = data["dojos_id"]


#for adding a ninja
    @classmethod
    def add_ninja(cls,data):
        query  ="insert into ninjas (f_name,l_name,age,dojos_id) values (%(f_name)s,%(l_name)s,%(age)s,%(dojos_id)s);"
        result = connectToMySQL(db).query_db(query,data)
        print(result)
        return result


# validates user input and flashes them if is wrong
    @staticmethod
    def flassh_message(ninjas):
        is_valid = True
        if len(ninjas["f_name"]) < 3 :
            flash("First name must be at least 3 characters","first_name_error")
            is_valid = False
        if len(ninjas["l_name"])< 3:
            flash("Last name must be at least 3 characters","last_name_error")
            is_valid = False
        if len(ninjas["age"]) < 1 :
            flash("you must have at least 1 number","age_error")
            is_valid
        return is_valid
