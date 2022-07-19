from flask_app.config.connectTomysql import connectToMySQL
from flask_app import db
from flask_app.models import ninja_model
from  flask import flash


class Dojos:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.ninjas = []

#shows all the dojos 
    @classmethod
    def get_all(cls):
        query = "select * from dojos;"
        result = connectToMySQL(db).query_db(query)
        return result

#adds on dojo
    @classmethod
    def add_one(cls,data):
        query = "insert into dojos (name)values (%(name)s);"
        result = connectToMySQL(db).query_db(query,data)
        return result

# join dojos and ninjas and  displays the ninjas that are attach to selected dojo
    @classmethod
    def get_ninjas_in_dojo(cls,data):
        query = "select * from dojos left join ninjas on ninjas.dojos_id = dojos.id where  dojos.id = %(id)s;"
        result = connectToMySQL(db).query_db(query,data)
        print(result)
        dojo = cls(result[0])
        for item in result:
            ninja_data = { 
                **item,
                "id": item["ninjas.id"]
            }
            dojo.ninjas.append(ninja_model.Ninjas(ninja_data))
        return dojo

#validates user input and flashes them if its wrong
    @staticmethod
    def validatin_dojos(dojos):
        validate = True
        if len(dojos["name"]) < 2:
            flash("name must be at least 2 characters","dojo_error")
            validate = False
        return validate