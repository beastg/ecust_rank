from bs4 import BeautifulSoup
import requests
def get_soup(username):
    url = "https://cn.vjudge.net/user/" + username
    try:
        html = requests.get(url)
    except:
        print(url)
        return False	
    print(html)
    txt = html.text
    soup = BeautifulSoup(txt, 'lxml')
    return soup
# def username_exist(username):
#     soup = get_soup(username)
#     t = soup.find_all('h1')
#     if len(t) > 0 or t[0].text == '卧槽 ??':
#         return False
#     return True
def new_user(user):
    import db
    user = dict(user)
    db.new_user(user)
    return True
def query(username):
    soup = get_soup(username)
    if not soup:
        return False
    t = soup.find_all('a')
    ans = list()
    for e in t:
        c = e.attrs
        try:
            ans.append((e['title'], e.text))
        except:
            pass
    return ans
if __name__ == '__main__':
    query('yyecust')
