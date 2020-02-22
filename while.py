icq = {"привет": "привет",
 "Как дела?": "Намана",
 "че делаешь?": "ничего"}

def ask_user(icq):
    while True:
        user_question = input(">>>")
        if user_question in icq:
            print(icq[user_question])

ask_user(icq)    