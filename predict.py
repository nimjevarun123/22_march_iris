from flask import Flask , request,render_template
from app.utiles import select_flower
import config

app = Flask(__name__)

@app.route("/")
def flower():
    return render_template("fool.html")   

@app.route("/predict_flower", methods = ['POST'])
def flower_type():
    data = request.form
    print (f"data = {data}")
    iris_select = select_flower(data)
    result = iris_select.predict_flower_type()
    return str(result)


if __name__ == "__main__":
    app.run(host = config.HOST ,port = config.PORT , debug = config.DEBUG )
