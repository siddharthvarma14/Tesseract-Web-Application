import os
from flask import Flask,request,render_template,send_from_directory


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index',methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT,'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)
    
    for file in request.files.getlist('file'):
        print(file)
        filename = file.filename
        destination = "/".join([target,filename])
        print(destination)
        file.save(destination)
    
    return render_template('complete.html', image_name=filename)

@app.route('/index/<filename>')
def send_image(filename):
    return send_from_directory("images",filename)



if __name__ == "__main__":
    app.run()

