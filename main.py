from flask import Flask
from flask import render_template
from flask import request
import crawler
import db
app = Flask(__name__)

@app.route("/")
def index():
    users = db.get_all_users()
    users = list(map(list, users))
    for user in users:
        uid = user[0]
        user.append(db.get_record(uid))
    return render_template('index.html', users = users)

@app.route("/wyfsb", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if crawler.new_user(request.form):
            return render_template('info.html', info='注册成功')
        else:
            return render_template('info.html', info='有问题')
    return render_template('register.html')

@app.route("/yzylj", methods=['GET', 'POST'])
def update():
    db.update_all()
if __name__ == '__main__':
    update()
    app.run(host='0.0.0.0', port=80)
