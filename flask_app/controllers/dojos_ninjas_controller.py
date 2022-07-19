from flask import redirect, render_template,request
from flask_app import app
from flask_app.models.dojo_model import Dojos
from flask_app.models.ninja_model import Ninjas

#always use the decarator
@app.route("/")
def show_all():
    dojos = Dojos.get_all()
    return render_template("show_all.html",dojos = dojos)

#adds dojo and validates that somethin is inputed
@app.route("/add/dojo",methods = ["post"])
def create_dojo():
    if not Dojos.validatin_dojos(request.form):
        return redirect("/")
    Dojos.add_one(request.form)
    return redirect("/")


'''
******************************
******************************
________ninjas routes________
******************************
******************************
'''

# show the ninjas that are in the selectet dojo
@app.route("/show_one/<int:num>")
def show_one_dojo_with_ninjas(num):
    data = {"id":num
    }
    one_dojo = Dojos.get_ninjas_in_dojo(data)
    return render_template("one_dojo.html",one_dojo = one_dojo)



@app.route("/add/ninja")
def new_ninja():
    all_dojos = Dojos.get_all()
    return render_template("add_ninja.html",all_dojos = all_dojos)

#add ninjas and validates that something is inputed
@app.route("/add/ninja", methods = ["post"])
def add_ninja():
    if not Ninjas.flassh_message(request.form):
        return redirect("/add/ninja")
    data = {
        "f_name":request.form["f_name"],
        "l_name": request.form["l_name"],
        "age":request.form["age"],
        "dojos_id": request.form["dojos_id"]
    }
    Ninjas.add_ninja(data)
    print(data)
    return redirect(f"/show_one/{data['dojos_id']}")