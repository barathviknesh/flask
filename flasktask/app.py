from flask import Flask, render_template
app = Flask(
    __name__,
    template_folder="templates"
)


@app.route("/")
def hello_world():
    return "hello world !"


@app.route("/page")
def hello_webpage():
    return render_template("hello.html")


@app.route("/page/<name>")
def hello_name(name):
    return render_template("helloname.html", name=name)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
