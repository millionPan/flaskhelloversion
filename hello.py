from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    return '<h1 style="color:purple;font-size:40px;">hello,World!</h1>'


if __name__=='__main__':
    app.run(debug=True)