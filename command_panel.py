from os import listdir
import os
import json
import time
import UsefulDB

access = False

with open('config.json', mode='r') as f:
    data = json.load(f)
    path = data['path']

try:
    with open('rooted_users.json', mode='r') as f:
        data = json.load(f)
        username = data['user']
        userpassword = data['password']
    u_a = input('Enter the username: ')
    u_p = input('Enter the password: ')
    if u_a != username:
        print('Wrong username')
    elif u_p != userpassword:
        print('Wrong password')
    else:
        print('Logging to the subprocces...')
        time.sleep(2)
        print('All done.')
        time.sleep(1)
        access = True
except:
    print("You don't have a super-user")

if access:
    def ChangeSettings(command):
        if command == 'agreement':
            new_agreement = input(a)
            if new_agreement == 'False':
                new_agreement = False
            else:
                new_agreement = True
            with open('config.json', mode='r') as f:
                dict = json.load(f)
                with open('config.json', mode='w') as fh:
                    dict['use_lib'] = new_agreement
                    json.dump(dict, fh)
                    print(succes)

        elif command == 'path':
            new_path = input(a)
            with open('config.json', mode='r') as f:
                dict = json.load(f)
                with open('config.json', mode='w') as fh:
                    dict['path'] = new_path
                    json.dump(dict, fh)

        elif command == 'lang':
            new_lang = input(a)
            with open('config.json', mode='r') as f:
                dict = json.load(f)
                with open('config.json', mode='w') as fh:
                    dict['lang'] = new_lang
                    json.dump(dict, fh)
        a = input('$ ')
        eval('{}'.format(a))

    class file:
        def delete(file):
            try:
                os.remove(r'{}\{}'.format(path, file))
                print('Succesfully finished')
            except:
                print('Is not exists')
            a = input('$ ')
            eval('{}'.format(a))

        def create(file):
            if file == 'config':
                with open('config.json', mode='r') as f:
                    dict = {}
                    dict['version'] = '1.0.4'
                    json.dump(dict, f)
                    print('Succesfully finished')
            elif file == 'reg_users':
                   try:
                       with open('registered_users.json', mode='r') as f:
                           data = json.load(f)
                       print('You already have a this file')
                   except:
                        with open('registered_users.json', mode='w') as f:
                            dict = {}
                            dict['count'] = 0
                            json.dump(dict, f)
                            print('Succesfully finished')
            elif file == 'settings':
                shutil.copyfile(r'reserve/test.py', r'test.py')
            else:
                print('Command is not exists')
            a = input('$ ')
            eval('{}'.format(a))

    class config:
        def delete(confirm=False):
            if confirm:
                with open('config.json', mode='r') as f:
                    data = json.load(f)
                    version = data['version']
                    with open('config.json', mode='w') as fh:
                        dict = {}
                        dict['version'] = version
                        json.dump(dict, fh)
            else:
            	print('You miss an attribute.')
            a = input('$ ')
            eval('{}'.format(a))

        def change(attribute):
            if attribute == 'path':
                ChangeSettings('path')
            elif attribute == 'lang':
                ChangeSettings('lang')
            elif attribute == 'agreement':
                ChangeSettings('agreement')
            else:
                print('Command is not exists')
            a = input('$ ')
            eval('{}'.format(a))

    class info:
        def static(item):
            if item == 'users':
                with open('registered_users.json', mode='r') as f:
                    data = json.load(f)
                    print('Count of users is {}'.format(data['count']))
            elif item == 'files':
                print('You have a {} files'.format(len(listdir(path))))
            else:
                print('Command is not exists')
            a = input('$ ')
            eval('{}'.format(a))

        def check_version():
            try:
                s = requests.get('http://scgofficial.esy.es/version.html')
                b = bs4.BeautifulSoup(s.text, "html.parser")
                p1 = b.select('.version .fw')
                result_ver = p1[0].getText()
                if version == result_ver:
                    pass
                elif version != result_ver:
                    print('New version is detected. For get new functions or fix bugs, please, update UsefulDB')
            except:
                print("System don't can check new versions. Please, check the Internet-connection and retry")

    a = input('$ ')
    eval('{}'.format(a))
else:
    print("You don't have access to this panel")
    time.sleep(10)
    quit()