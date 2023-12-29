from flask import Flask, render_template

app = Flask('oderman', template_folder="templates", static_folder="static")

@app.route('/')
@app.route('/index')
def index_view():
    return render_template("index.html")


@app.route('/menu')
def menu():
    return render_template("menu.html")


if __name__ == "__main__":
    app.run(debug=True)