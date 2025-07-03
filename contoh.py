from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Halo dunia, ini aplikasi Python di web!"

if __name__ == '__main__':
    app.run()
