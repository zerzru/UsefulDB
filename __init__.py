'''
This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

__author__ = 'Elisey Sharov' #name of UsefulDB author

#importing packages for framework
import os
import json
import time
import datetime
import platform
import requests
import bs4
import pymysql.cursors

#it's for checking new versions
with open('config.json', mode='r') as f:
    data = json.load(f)
    VERSION = data['version']

#function for fast saving config, optimize lines of code
def confirm_rules():
    with open('config.json', mode='w') as f:
        dict = {}
        dict['version'] = VERSION
        dict['whatisit'] = True
        dict['host'] = input('Insert your host: ')
        dict['user'] = input('Insert host user: ')
        dict['password'] = input('Insert host password: ')
        json.dump(dict, f)

try: #try to check new version and condition of internet-connection
    s = requests.get('http://scgofficial.esy.es/version.html')
    b = bs4.BeautifulSoup(s.text, "html.parser")
    p1 = b.select('.version .fw')
    result_ver = p1[0].getText()
    if VERSION == result_ver:
        NET = True
    else:
        if VERSION == 'Beta': #you wanna to crach your PC?
            NET = True
            print('You have a Beta-version of UsefulDB. This version may contain more bugs and errors, than simple version')
        elif VERSION == '1.0.0' or '1.0.1' or '1.0.2' or '1.0.3': #if you use this versions - you're a bad man
            NET = True
            print('You have old version of UsefulDB. Please, update the framework for get new features and bug fixes!')
        else: #another versions is not can be
            NET = True
            print("Are you change the 'config.json' file?")
except: #if you haven't internet-connection or sever have problems
    NET = False
    print("System can't check avialable of new versions. Check the internet-connection and try again")

#checking code for errors for log.txt
try:
    try: #checking info in config.json(first launch or second+)
        with open('config.json', mode='r') as f:
            data = json.load(f)
            VERSION = data['version']
            USE = data['whatisit']
            host = data['host']
            db_user = data['user']
            db_pass = data['password']
    except Exception as error:
        answer = input('By using this framework, you accept the rules of GNU 3.0 License. Are you confirm? (Y/N): ')
        if answer == 'Y': #if input = Y, calling function
            confirm_rules()
            USE = True
        elif answer == 'y': #also if input = y
            confirm_rules()
            USE = True
        else: #you must to accept the license rules
            print("You don't can use this framework")
            time.sleep(8)
            quit()
        raise error

    if USE:
        #don't touch this!
        with open('log.txt', mode='a') as f:
            info = platform.machine()
            now = datetime.datetime.now()
            pyversion = platform.python_version()
            os = platform.system()
            f.write('[{}]: '.format(now)
                    + 'UsefilDB {}; '.format(VERSION)
                    + 'Python {}; '.format(pyversion)
                    + 'Machine {}; '.format(info)
                    + 'OS {}; '.format(os)
                    + 'Config [use = {}]; '.format(USE)
                    + 'Internet-connection: {};\n'.format(NET)
                   )

        if NET:
            class create: #create something
                def __init__(self, i):
                    self.Item = i

                def info():
                    print('Wanna to create something? Call this class!')

                class user: #create super-user
                    def __init__(self, n, p):
                        self.Name = n
                        self.Pass = p

                    def info():
                        print('Wanna get the acces to command panel? Create a super-user!')

                    def params(name, password, confirm=False):
                        if confirm:
                            try:
                                with open('root.json', mode='r') as f:
                                    data = json.load(f)
                                    user = data['user']
                                    password = data['pass']
                                    print('You already have super-user')
                            except Exception as error:
                                with open('root.json', mode='w') as f:
                                    dict = {}
                                    dict['user'] = name
                                    dict['pass'] = password
                                    print('Super-user {} is created. Now you can use command panel'.format(name))
                                raise error
                        else:
                            pass

                class table: #create table in database
                    def __init__(self, n):
                        self.Name = n

                    def info():
                        print('Wanna create table? Call create.table.params(name, columns)!')

                    def params(name, columns):
                        columns = int(columns) #if you write like '3'(must be 3), system converting str to int
                        with open('config.json', mode='r') as f:
                            data = json.load(f)
                            host = data['host']
                            db_user = data['user']
                            db_pass = data['password']
                        try: #are you have correct info of database name?
                            with open('host.json', mode='r') as f:
                                data = json.load(f)
                                db = data['database']
                        except Exception as error: #if not
                            answer = input('Insert the database name: ')
                            with open('host.json', mode='w') as f:
                                dict = {}
                                dict['database'] = answer
                                json.dump(dict, f)
                            raise error
                        #connecting to database
                        connection = pymysql.connect(host=host,
                                                    user=db_user,
                                                    password=db_pass,
                                                    db=db,
                                                    charset='utf8mb4',
                                                    cursorclass=pymysql.cursors.DictCursor
                                                    )
                        number = 0
                        start_num = 0
                        while number < columns: #calculator for checking creating columns: it's first? second? another?
                            columnName = input('Name of column: ') #column name
                            columnLength = int(input('Length: ')) #column length
                            columnType = input('Type (int, varchar or another): ') #column type
                            columnCondition = bool(input('Is this column primary? (True/False): ')) #is this primary?
                            if start_num <= 0:
                                MAINCOLUMN = columnName
                            else:
                                columnCondition = False
                            try:
                                now = datetime.datetime.now()
                                if columnCondition:
                                    start_num += 1
                                    with connection.cursor() as cursor:
                                        sql = 'CREATE TABLE `%s`(`{}` {}({}) NOT NULL);'.format(columnName,
                                                                                                columnType,
                                                                                                columnLength
                                                                                                )
                                        with open('connection_log.txt', mode='a') as f:
                                            f.write('[{}]: columnID: {}; columnName: {}; columnType: {}; '.format(now, number,
                                                                                                                  columnName,
                                                                                                                  columnType
                                                                                                                  )
                                                    + 'columnLength: {}, columnCondition: {}; SQL: {}\n'.format(columnLength,
                                                                                                                columnCondition,
                                                                                                                sql))
                                        cursor.execute(sql, ('{}'.format(name)))
                                        connection.commit() #saving changes
                                        with connection.cursor() as cursor:
                                            sql = "SELECT * FROM `%s`"
                                            cursor.execute(sql, ('{}'.format(name)))
                                            result = cursor.fetchone()
                                            print(result)
                                else:
                                    print(columnCondition)
                                    time.sleep(5)
                                    with connection.cursor() as cursor:
                                        sql = "ALTER TABLE `%s` ADD `{}` {}({}) NOT NULL AFTER `{}`;".format(columnName,
                                                                                                             columnType,
                                                                                                             columnLength,
                                                                                                             MAINCOLUMN
                                                                                                             )
                                        with open('connection_log.txt', mode='a') as f:
                                            f.write('[{}]: columnID: {}; columnName: {}; columnType: {}; '.format(now, number,
                                                                                                                  columnName,
                                                                                                                  columnType
                                                                                                                  )
                                                    + 'columnLength: {}, columnCondition: {}; SQL: {}\n'.format(columnLength,
                                                                                                                columnCondition,
                                                                                                                sql))
                                        cursor.execute(sql, ('{}'.format(name)))
                                        connection.commit() #saving changes
                                        with connection.cursor() as cursor:
                                            sql = "SELECT * FROM `%s`"
                                            cursor.execute(sql, ('{}'.format(name)))
                                            result = cursor.fetchone()
                                            print(result)
                            except Exception as er:
                                print('Something wrong: ', er)
                                now = datetime.datetime.now()
                                with open('connection_log.txt', mode='a') as f:
                                    f.write('[{}]: columnID: {}; columnName: {}; columnType: {}; '.format(now, number,
                                                                                                    columnName,
                                                                                                    columnType)
                                            + 'columnLength: {}, columnCondition: {}; SQL: {} Error: {};\n'.format(columnLength,
                                                                                                                   columnCondition,
                                                                                                                   sql, er))
                            finally:
                                number += 1
                            if number > columns:
                                connection.close()
                                break


        else: #framework needed in stability of internet-connection and server work
            time.sleep(8)
            pass
    else: #if you trying to launch framework, but you don't accept the licence rules, framework just close himself
        pass

#and this!
except Exception as error:
    with open('log.txt', mode='a') as f:
        info = platform.machine()
        now = datetime.datetime.now()
        pyversion = platform.python_version()
        os = platform.system()
        f.write('[{}]: '.format(now)
                + 'UsefilDB {}; '.format(VERSION)
                + 'Python {}; '.format(pyversion)
                + 'Machine {}; '.format(info)
                + 'OS {}; '.format(os)
                + 'Config [use = {}]; '.format(USE)
                + 'Internet-connection: {}; '.format(NET)
                + 'Error: {};\n'.format(error)
               )