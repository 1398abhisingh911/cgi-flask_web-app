from flask import Flask
from flask import render_template
from flask import request


app=Flask("MyWebMenu")

@app.route("/")
def main():
    data=render_template("main.html")
    return data

@app.route("/docker")
def docker():
    data=render_template("docker.html")
    return data


@app.route("/aws")
def aws():
    data=render_template("aws.html")
    return data


@app.route("/hadoop")
def hadoop():
    data=render_template("hadoop.html")
    return data

@app.route("/ansible")
def ansible():
    data=render_template("ansible.html")
    return data

@app.route("/linux")
def linux():
    data=render_template("linux.html")
    return data

if __name__ == '__main__':
        app.run(debug= True)