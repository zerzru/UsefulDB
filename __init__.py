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

#import packages for framework
import os
import time
import json
import datetime
import platform
import requests
import bs4
import pymysql.cursors  

__author__ = 'Elisey Sharov'

try:
    #system for checking the availability of user settings
    try:
        with open('config.json', mode='r') as f:
            data = json.load(f)
            use_lib = data['use_lib']
            version = data['version']
            lang = data['lang']
    except Exception as er:
        print(er)
        answer = input('By using this framework, you accept the license agreement. Do you confirm?(Yes/No): ')
        #If the input length is more than two characters(this excludes checking
        #for errors, such as eys instead of yes), then save, otherwise do nothing
        if len(answer) > 2:
            dict = {}
            with open('config.json', mode='w') as f:
                dict['use_lib'] = True
                dict['version'] = 'Beta'
                dict['lang'] = input('Select the language to use (English/Russian): ')
                json.dump(dict, f)
            print('Applying settings...')
            time.sleep(2)
            with open('config.json', mode='r') as fh:
                data = json.load(fh)
                use_lib = data['use_lib']
                version = data['version']
                lang = data['lang']
        else:
            print("You don't can use this framework")
            time.sleep(5)
            quit()
    #end of system

    if use_lib:
        #system for check of avialable for new versions
        try:
            s = requests.get('http://scgofficial.esy.es/version.html')
            b = bs4.BeautifulSoup(s.text, "html.parser")
            p1 = b.select('.version .fw')
            result_ver = p1[0].getText()
            if version == result_ver:
                internet_connection = True
            else:
                if version == 'Beta':
                    internet_connection = True
                elif version == '1.0.0' or '1.0.1' or '1.0.2' or '1.0.3':
                    internet_connection = True
                else:
                    internet_connection = True
        except:
            internet_connection = False
        #end of system

        #create something
        class create:
            def __init__(self, i):
                self.Item = i
            #create user
            class user:
                def __init__(self, n):
                    self.Name = n

                def params(user, password, database=None, root=False):
                    if root:
                        try:
                            with open('config.json', mode='r') as f:
                                data = json.load(f)
                            print('You already have a super-user')
                        except Exception as er:
                            with open('config.json', mode='w') as f:
                                dict = {}
                                if database == None:
                                    dict['user'] = user
                                    dict['password'] = password
                                    dict['root'] = root
                                else:
                                    print("Super-user don't have databases")
                            raise er
                    else:
                        try:
                            with open('hosted_info.json', mode='r') as f:
                                data = json.load(f)
                                host = data['host']
                                db_user = data['user']
                                passw = data['pass']
                                db = data['database']
                                answer = input('Would you like to change table? (y/n): ')
                                if answer == 'y':
                                    table = input('New table: ')
                                else:
                                    table = data['table']
                                    #connect to SQL-database
                                connection = pymysql.connect(host='{}'.format(host),
                                                             user='{}'.format(db_user),
                                                             password='{}'.format(passw),
                                                             db='{}'.format(db),
                                                             charset='utf8mb4',
                                                             cursorclass=pymysql.cursors.DictCursor)
                                try:
                                    with connection.cursor() as cursor:
                                        sql = "INSERT INTO `{}` (`email`, `password`) VALUES (%s, %s);".format(table)
                                        cursor.execute(sql, ('{}'.format(user), '{}'.format(password)))
                                    connection.commit()
                                except Exception as er:
                                    print('Something is wrong: ', er)
                                finally:
                                    connection.close()
                        except Exception as er:
                            host = input('Enter the host: ')
                            db_user = input('Enter the database user: ')
                            passw = input('Enter the database password: ')
                            db = input('Enter the database: ')
                            with open('hosted_info.json', mode='w') as f:
                                dict = {}
                                dict['host'] = host
                                dict['user'] = db_user
                                dict['pass'] = passw
                                dict['database'] = db
                                dict['table'] = input('Enter the database table: ')
                                json.dump(dict, f)
                                #connect to SQL-database
                                connection = pymysql.connect(host='{}'.format(host),
                                                             user='{}'.format(db_user),
                                                             password='{}'.format(passw),
                                                             db='{}'.format(db),
                                                             charset='utf8mb4',
                                                             cursorclass=pymysql.cursors.DictCursor)
                                try:
                                    with connection.cursor() as cursor:
                                        sql = "INSERT INTO `{}` (`email`, `password`) VALUES (%s, %s);".format(table)
                                        cursor.execute(sql, ('{}'.format(user), '{}'.format(password)))
                                    connection.commit()
                                except Exception as er:
                                    print('Something is wrong: ', er)
                                    raise er
                                finally:
                                    connection.close()
            #create database
            class database:
                def __init__(self, n, c):
                    self.Name = n
                    self.Columns = c

                def params(name):
                    try:
                        with open('hosted_info.json', mode='r') as f:
                            data = json.load(f)
                            host = data['host']
                            db_user = data['user']
                            passw = data['pass']
                            db = data['database']
                            #connect to SQL-database
                            connection = pymysql.connect(host='{}'.format(host),
                                                         user='{}'.format(db_user),
                                                         password='{}'.format(passw),
                                                         db='{}'.format(db),
                                                         charset='utf8mb4',
                                                         cursorclass=pymysql.cursors.DictCursor)
                            try:
                                with connection.cursor() as cursor:
                                    sql = "CREATE DATABASE `%s`;"
                                    cursor.execute(sql, ('{}'.format(name)))
                                connection.commit() #saving changes
                            except Exception as er:
                                print('Something is wrong: ', er)
                            finally:
                                connection.close()
                                
                    except Exception as er:
                        host = input('Enter the host: ')
                        db_user = input('Enter the database user: ')
                        passw = input('Enter the database password: ')
                        db = input('Enter the database: ')
                        with open('hosted_info.json', mode='w') as f:
                            dict = {}
                            dict['host'] = host
                            dict['user'] = db_user
                            dict['pass'] = passw
                            dict['database'] = db
                            json.dump(dict, f)
                            #connect to SQL-database
                            connection = pymysql.connect(host='{}'.format(host),
                                                         user='{}'.format(db_user),
                                                         password='{}'.format(passw),
                                                         db='{}'.format(db),
                                                         charset='utf8mb4',
                                                         cursorclass=pymysql.cursors.DictCursor)
                        try:
                            with connection.cursor() as cursor:
                                sql = "CREATE DATABASE `%s`;"
                                cursor.execute(sql, ('{}'.format(name)))
                            connection.commit() #saving changes
                        except Exception as er:
                            print('Something is wrong: ', er)
                        finally:
                            connection.close()

            #create table, is not avialable
            class table:
                def __init__(self, n, db):
                    self.Name = n
                    self.DataBase = db

                def params(name, columns):
                    columns = int(columns)
                    def send_data():
                        try:
                            start_num = 0
                            while start_num < columns:
                                title_c = input('Name of column: ')
                                type_c = input('Type (int, id, text, date, varchar): ')
                                try:
                                    length_c = int(input('Length: '))
                                except:
                                    print('Length must to be int!')
                                    pass
                                primary = bool(input('Is this column primary?(True/False): '))
                                start_num += 1
                                with open('hosted_info.json', mode='r') as f:
                                    data = json.load(f)
                                    host = data['host']
                                    db_user = data['user']
                                    passw = data['pass']
                                    db = data['database']
                                    connection = pymysql.connect(host='{}'.format(host),
                                                                 user='{}'.format(db_user),
                                                                 password='{}'.format(passw),
                                                                 db='{}'.format(db),
                                                                 charset='utf8mb4',
                                                                 cursorclass=pymysql.cursors.DictCursor)
                                try:
                                    with connection.cursor() as cursor:
                                        if primary:
                                            sql = 'CREATE TABLE `%s`(`%s` %s(%s) NOT NULL);'
                                            cursor.execute(sql, ('{}'.format(name),
                                                                ('{}'.format(title_c),
                                                                ('{}'.format(type_c),
                                                                ('{}'.format(length_c))))))
                                            connection.commit()
                                        else:
                                            sql = 'CREATE TABLE `%s`(`%s` %s(%s));'
                                            cursor.execute(sql, ('{}'.format(name),
                                                                ('{}'.format(title_c),
                                                                ('{}'.format(type_c),
                                                                ('{}'.format(length_c))))))
                                            connection.commit()
                                except Exception as er:
                                    print('Something is wrong:', er)
                                finally:
                                    connection.close()
                        except Exception as er:
                            print('Something is wrong:', er)
                    try:
                        if columns == 0:
                            print("Count of columns don't can be zero!")
                        else:
                            send_data()
                    except Exception as er:
                        print('Something is wrong:', er)
        #write info in log.txt
        with open('log.txt', mode='a') as f:
            info = platform.machine()
            now = datetime.datetime.now()
            pyversion = platform.python_version()
            os = platform.system()
            f.write('[{}]: UsefulDB {}, machine: {}, Python {}, OS: {}; Config: [lang={}, use={}]; Internet-connection: {};\n'.format(
                     now, version, info, pyversion, os, lang, use_lib, internet_connection))
    else:
        time.sleep(2)
        print(searching)
        time.sleep(4)
        print(tracking)
        time.sleep(10)
        #write info in log.txt
        with open('log.txt', mode='a') as f:
            info = platform.machine()
            now = datetime.datetime.now()
            pyversion = platform.python_version()
            os = platform.system()
            f.write('[{}]: UsefulDB {}, machine: {}, Python {}, OS: {}; Config: [lang={}, use={}]; Internet-connection: {}; Error: {}\n'.format(
                     now, version, info, pyversion, os, lang, use_lib, internet_connection, ))
except Exception as error:
    #write info in log.txt
    with open('log.txt', mode='a') as f:
        info = platform.machine()
        now = datetime.datetime.now()
        pyversion = platform.python_version()
        os = platform.system()
        f.write('[{}]: UsefulDB {}, machine: {}, Python {}, OS: {}; Config: [lang={}, use={}]; Internet-connection: {}; Error: {}\n'.format(
                 now,  version, info, pyversion, os, lang, use_lib, internet_connection, error))