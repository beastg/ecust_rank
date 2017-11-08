import sqlite3
def get_all_users():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    res = c.execute("SELECT * FROM user")
    return list(res)
def add_record(userid, res):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    sql = "INSERT INTO crawler VALUES (NULL, {},{},{},{},{},{})".format(userid, res[0][1], res[1][1], res[2][1], res[3][1], res[4][1])
    res = c.execute(sql)
   # c.execute()
    conn.commit()
def get_record(uid):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    sql = "SELECT * FROM crawler WHERE uid = {} ORDER BY cid DESC LIMIT 1".format(uid)
    res = c.execute(sql)
    res = list(map(list, res))
    return res
def update_all():
    import crawler
    users = get_all_users()
    for user in users:
        username = user[1]
        userid = user[0]
        res = crawler.query(username)
        add_record(userid, res)
def new_user(user):
    username = user['username'][0]
    major = user['major'][0]
    realname = user['name'][0]
    year = user['year'][0]
    sql = '''INSERT INTO user VALUES (NULL, "{}", "{}", "{}", {})'''.format(username, realname, major, year)
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute(sql)
    conn.commit()
    update_all()
    return True
if __name__ == '__main__':
    update_all()