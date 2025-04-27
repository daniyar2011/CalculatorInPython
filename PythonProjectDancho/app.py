from idlelib.history import History

from  flask import Flask, render_template, request, redirect,url_for
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


history = []





@app.route("/calculator", methods=['GET','POST'])
def calculator():
    expression = ""
    result = ""
    if request.method == 'POST':
        expression = request.form.get("expression","")
        button = request.form.get("button","")

        if button == "AC":
            expression=""
        elif button == "=":
            try:

                result = str(eval(expression))
                history.append(f"{expression} = {result}")
                expression = result
            except:
                result = "Ошибка"
                history.append(f"{expression} = Ошибка!")
                expression = ""
        else:
            expression = expression + button
            result = expression
    return render_template("calcucator.html",result=result,expression=expression, history=history)

if __name__ == "__main__":
    app.run(debug=True)






