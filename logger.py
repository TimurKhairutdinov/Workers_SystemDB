import datetime
import users as us
def loging(text):

    now = datetime.datetime.now()
    with open('log.txt', 'a', encoding='utf-16') as log:
        log.writelines(f'\n{now} : {text}')


def view_log():
    print(('Для доступа к log, необходимо иметь права администратора!\n'
           'Введите логин: \n'))
    login = str(input('>> '))
    loging(f'Ввод пользователем login: {login}')
    find_user_status = False
    for i in us.user.keys():
        if login == i:
            find_user_status = True
            loging(f'Пользователь: {login} найден.')

    if find_user_status != False:
        print('Введите пароль: \n')
        password_from_user = str(input('>> '))
        loging(f'Ввод пользователем password: {password_from_user}')
        password = us.user.get(login)
        if password_from_user == password:
            loging(f'login: {login} password: {password_from_user} Complete!')
            print(('Доступ открыт.\n'
                   '________________\n'))
            with open('log.txt', 'r',encoding='utf-16') as log:
                r = log.readlines()
                for line in r:
                    print(line)
            loging(f'Пользователь {login} получил доступ к log')
        else:
            loging(f'Пользователь {login} не получил доступ к log, неверный password:{password_from_user}')
            print('Доступ закрыт!')
    else:
        print('Пользователь не найден.')
        loging(f'Пользователь: {login} не найден.')
