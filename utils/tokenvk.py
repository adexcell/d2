import webbrowser as wb
from urllib.parse import urlencode
from config import APP_ID, AUTH_URL, AUTH_DATA_APP


def get_token(app_id):  # запрашивает токен у клиента
    AUTH_DATA_APP['client_id'] = app_id
    wb.open_new_tab(AUTH_URL + urlencode(AUTH_DATA_APP))
    access_token = input(str('Please, copy and insert your vk token: \n'))
    return access_token


if __name__ == '__main__':
    get_token(APP_ID)