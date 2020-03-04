from flask import Flask
from index import get_balance_from_account
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    login = request.args.get('login')
    passwords = request.args.get('password')
    phone = request.args.get('phone')
    if request.args.get('login'):
        return get_balance_from_account(login, passwords, phone)
    else:
        return "Request is empty"


if __name__ == "__main__":
    app.debug = "TRUE"
    app.run()
