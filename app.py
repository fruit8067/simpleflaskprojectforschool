from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import re

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbjung

"""
todo
1. 8조까지 만들기
2. bank account system 만들기
3. 온라인 배포하기
"""

"""
bank account sysmtem dev roadmap

1. make login system (if user doenst in db then make db else > load money in db
2. if total funded money > bank account -> you overed your bank account else > success!
"""


def check_balance(user):
    studentAccount_receive = user

    if db.bankAccount.find_one({"name": studentAccount_receive}):
        temp = db.bankAccount.find_one({"name": studentAccount_receive})
        return temp.get("money")
    else:
        db.bankAccount.insert_one({"name": studentAccount_receive, "money": 100000})
        return 100000


@app.route('/index')
def home():
    return render_template('index.html', user='')


@app.route('/page')
def page():
    return render_template('page.html')


@app.route('/page/<User>/<Group>')
def page_user(User, Group):
    Group = Group + "Group"
    temp = list(db.description.find({"Group": Group}))
    User = list(db.bankAccount.find({"name": User}))
    return render_template('page.html', Title=temp[0]['Title'], Long_explain=temp[0]['Long_explain'],
                           money=format(User[0]["money"],','))


@app.route('/sign_in')
def sign_in():
    return render_template('sign_in.html')


@app.route('/<user1>')
def logedin(user1):
    if (db.bankAccount.find_one({"name": user1})):
        return render_template('index.html', user=f'{user1}')
    else:
        db.bankAccount.insert_one({"name": user1, "money": 100000})
        return render_template('index.html', user=f'{user1}')


@app.route('/result')
def result():
    return render_template('result.html')


# API 역할을 하는 부분
@app.route('/review', methods=['POST'])
def write_review():
    Group = request.form['Group']
    Account = request.form['Account']
    Account = re.sub(r'[^0-9]', '', Account)
    Input = request.form['input']
    Input = int(Input)
    student = request.form['student']
    print(Group, student)
    if Input > int(Account):
        return jsonify({'msg': f'저장 실패! 잔여 금액을 초과하셨습니다. 잔여 금액 : {Account}'})
    else:
        temp = list(db.crowdfunding.find({"name": Group}))
        temp = temp[0]['FundedMoney']
        db.crowdfunding.update_one({"name": Group}, {"$set": {"FundedMoney": temp + Input}})
        temp = list(db.bankAccount.find({"name": student}))
        temp = temp[0]['money']
        db.bankAccount.update_one({"name": student}, {"$set": {"money": temp - Input}})
        return jsonify({'msg': '저장완료'})


@app.route('/review', methods=['GET'])
def read_reviews():
    client_reviews = list(db.description.find({}, {'_id': False}))
    print(client_reviews)
    Funded_money = list(db.crowdfunding.find({}, {'_id': False}))
    print(Funded_money)
    return jsonify({'all_reviews': client_reviews, 'funded_money': Funded_money})


@app.route('/bank', methods=['POST'])
def bank():
    studentAccount_receive = request.form['user_give']

    if db.bankAccount.find_one({"name": studentAccount_receive}):
        temp = db.bankAccount.find_one({"name": studentAccount_receive})
        return jsonify({'msg': temp.get("money")})
    else:
        db.bankAccount.insert_one({"name": studentAccount_receive, "money": 100000})
        return jsonify({'msg': 100000})


@app.route('/bank2', methods=['POST'])
def get_account():
    user = request.form['user']
    temp = db.bankAccount.find({"name": user})
    return jsonify({'msg': temp[0]['money']})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
