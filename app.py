from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    if request.method == "POST":
        return render_template('greet.html', name_var=request.form.get("name_var", "pendemic"))


# 원래 위 아래 라우터 두개에서 >>> 한개로  위에 한 라우터에 표현! 
"""
@app.route('/greet', methods=["POST"])
def greet():
    return render_template('greet.html', name_var=request.form.get("name_var", "pendemic"))
"""