import requests
import misc
import json


token = misc.token

# https://api.telegram.org/bot1550057543:AAGsIiMfET1vqwX74kFdpaIVI79MwMnAF0w/sendmessage?chat_id=472745426&text=hello%20world
URL = 'https://api.telegram.org/bot' + token + '/'


def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


def get_message():
    data = get_updates()

    chat_id = data['result'][-1]['message']['chat']['id']
    message_text = data['result'][-1]['message']['text']

    message = {'chat_id': chat_id, 'text': message_text}
    return message


def main():
    d = get_message()
    # print(type(d))
    # with open('updates.json', 'w') as f:
    #     json.dump(d, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()
