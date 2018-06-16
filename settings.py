import json
import time
import UsefulDB

with open('config.json', mode='r') as f:
    data = json.load(f)
    if data['lang'] == 'Russian':
        deleting_succes = 'Удаление завершено'
        a = 'Новое значение: '
        succes = 'Готово'
        search_error = 'Команды не существует'
    else:
        deleting_succes = 'Succefully deleted'
        a = 'Enter new value: '
        succes = 'Done'
        search_error = 'Command is not exists'

def DeleteSettings():
    with open('config.json', mode='r') as f:
        data = json.load(f)
        version = data['version']
        with open('config.json', mode='w') as fh:
            dict = {}
            dict['version'] = version
            json.dump(dict, fh)
            print(deleting_succes)
    a_c = input('$ UsefulDB: ')
    eval('{}'.format(a_c))

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

    else:
        print(search_error)
    a_c = input('$ UsefulDB: ')
    eval('{}'.format(a_c))

a_c = input('$ UsefulDB: ')
eval('{}'.format(a_c))