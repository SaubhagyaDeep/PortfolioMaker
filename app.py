from flask import Flask,render_template, request,session
import uuid
import os 

app=Flask(__name__)
app.secret_key= "I AM BATMAN"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/design')
def design():
    return render_template('design.html')

@app.route('/form/<string:design>', methods=["GET","POST"])
def form(design):
    session['design_sess']=design
    return render_template('form.html')

@app.route('/upload', methods=["GET","POST"])
def upload():
    desging_upload = session.get("design_sess")
    if desging_upload == "design1":
        design_name = "Design1.html"
    elif desging_upload == "design2":
        design_name = "Design2.html"
    elif desging_upload == "design3":
        design_name = "Design3.html"
    elif desging_upload == "design4":
        design_name = "Design4.html"
    else:
        design_name="Design2.html"

    if request.method=='POST':
        name=request.form.get('firstname')
        lastname=request.form.get('lastname')
        school=request.form.get('school')
        college=request.form.get('college')
        phone=request.form.get('phone')
        email=request.form.get('email')

        skill1=request.form.get('skill1')
        skill2=request.form.get('skill2')
        skill3=request.form.get('skill3')
        skill4=request.form.get('skill4')
        about=request.form.get('about')
        git=request.form.get('github')
        linkedin=request.form.get('linkedin')

        key=uuid.uuid1()
        #single image uploading method
        img=request.files['dp']
        img.save(f"venv/static/images/{img.filename}")
        img_new_name= f"{key}{img.filename}"
        os.rename(f"venv/static/images/{img.filename}",f"venv/static/images/{img_new_name}")
    return render_template(design_name,img=img_new_name,dname = name,dlname = lastname,dsch = school, dcol = college,dph = phone,demail = email,ds1 = skill1,ds2 = skill2,ds3 =skill3,ds4 = skill4,dabout = about,dgit=git,dlinkedin=linkedin)

 
app.run(debug=True)

#line 53 in design1 me venv/static/images/{{img}} krna tha but aese hi chl rha 