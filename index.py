import requests
from bs4 import BeautifulSoup


def get_balance_from_account(login, passwd, number):
    url = "https://passport.yandex.ru/auth?origin=money&retpath=https%3A%2F%2Fmoney.yandex.ru%2F%3Ffrom%3Dauth"


    headers = {
        "accept-language": "ru",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36 OPR/66.0.3515.115",
        "accept-encoding": "gzip, deflate, br",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    }

    yandex = requests.session()
    yandex.headers = headers
    html = yandex.get("https://passport.yandex.ru/auth/welcome").text
    soup = BeautifulSoup(html, 'html.parser')
    csrf_token = soup.find(attrs={"name": "csrf_token"}).attrs['value']
    data = {"csrf_token": csrf_token, "login": login, "passwd": passwd}

    answer = yandex.post(url, data).text

    if 0:
    # Прохождение проверки номера
        commit_url = "https://passport.yandex.ru/registration-validations/auth/challenge/commit"
        soup = BeautifulSoup(answer, 'html.parser')
        csrf_token = soup.find(attrs={"name": "csrf_token"}).attrs['value']
        data = {"csrf_token": csrf_token, "challenge": "phone", "number": number}
        answer = yandex.post(url, data).text

    soup = BeautifulSoup(answer, 'html.parser')
    balance = soup.find(
        attrs={"class": "price__whole-amount text text_size_xxxxl text_view_primary text_weight_regular"}).text
    return balance




