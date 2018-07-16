# UsefulDB
<a href="https://travis-ci.org/ZerZru/UsefulDB">![Travis CI](https://api.travis-ci.org/ZerZru/UsefulDB.svg?branch=master)</a> ![Github All Releases](https://img.shields.io/github/downloads/ZerZru/UsefulDB/total.svg) ![PyPI](https://img.shields.io/pypi/v/usefuldb.svg) ![PyPI - Format](https://img.shields.io/pypi/format/UsefulDB.svg) <br> <br>
![project_logo](https://raw.githubusercontent.com/ZerZru/UsefulDB/master/images/logo-readme.jpg)

# Contents
<h2>
    <ol>
        <li><a href="#license">License</a></li>
        <li><a href="#training">Training</a></li>
        <ol>
            <li><a href="#training?about">About</a></li>
            <li><a href="#training?examples">Examples</a></li>
            <ol>
                <li><a href="#training?examples_creating">Creating</a></li>
                <li><a href="#training?examples_deleting">Deleting</a></li>
            </ol>
        </ol>
        <li><a href="#main">Main</a></li>
        <ol>
            <li><a href="#main?about">About</a></li>
            <li><a href="#main?examples">Examples</a></li>
            <ol>
                <li><a href="#main?examples_creating">Creating</a></li>
                <li><a href="#main?examples_deleting">Deleting</a></li>
            </ol>
        </ol>
        <li><a href="#installing">Installing</a></li>
        <li><a href="#bugreport">Bug report</a></li>
        <li><a href="#authors">Authors</a></li>
        <li><a href="#changelog">Change log</a></li>
        <li><a href="#contact">Contact</a></li>
    </ol>
</h2>

<a name="license"></a>
## License
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

<a name="training"></a>
# Training
<a name="training?about"></a>
## About training
Do you already have databases and their components? You want to use this framework, but are afraid to spoil something? Or just want to understand how it works? In any case, I recommend starting with this mode. It does not connect to the Internet, it only works with local files, so you can not worry about your databases. Just go to the "Education" folder, create a new file and import the __init__ file
```python
[installed/folder/Education/]
from __init__ import *
```
Now you can enter the same commands, open the folder where the framework is installed, and look at the JSON table files
<a name="training?examples"></a>
## Examples
Framework can create and delete files. So:
<a name="training?examples_creating"></a>
### Creating

This command will create super-user:
```python
create.user.params('Admin', '12345', confirm=True) #also create.user.params(name='Admin', password='12345', confirm=True)
```
This command will create database:
```python
create.database.params('Test') #also create.database.params(name='Test')
```
And this command will create table:
```python
create.table.params('Test', 3) #also create.table.params(name='Test', 3) or create.table.params(name='Test', '3')
```
<a name="training?examples_deleting"></a>
### Deleting
This command will delete user:
```python
delete.user.params('Admin', '12345', confirm=True) #also delete.user.params(name='Admin', password='12345', confirm=True)
```
This command will delete database:
```python
delete.database.params('Test', confirm=True)
```
This command will delete table:
```python
delete.table.params('Test', confirm=True)
```

<a name="main"></a>
# Main
<a name="main?about"></a>
## About main

This is the main job of the framework. Now, with the wrong treatment, you can break something. Although the framework has a protection system for incorrect data entry, this does not guarantee the protection of your developments.

<a name="main?examples"></a>
## Exmaples
<a name="main?examples_creating"></a>
### Creating
This command will create super-user:
```python
create.user.params('Admin', '12345', confirm=True) #also create.user.params(name='Admin', password='12345', confirm=True)
```
This command will create database:
```python
create.database.params('Test') #also create.database.params(name='Test')
```
And this command will create table:
```python
create.table.params('Test', 3) #also create.table.params(name='Test', 3) or create.table.params(name='Test', '3')
```
### Deleting
<a name="main?examples_deleting">
This command will delete user:
```python
delete.user.params('Admin', '12345', confirm=True) #also delete.user.params(name='Admin', password='12345', confirm=True)
```
This command will delete database:
```python
delete.database.params('Test', confirm=True)
```
This command will delete table:
```python
delete.table.params('Test', confirm=True)
```

<a name="installing"></a>
# Installing

```batch
pip install UsefulDB
```

Installation via the PIP may not work, so for now, I recommend downloading the archive of the framework and unpacking it into the folder you need

<a name="bugreport"></a>
# Bug report

If you have bugs or another issues, please, send to mail scg-publicmail@yandex.ru 2 files: <br>
-log.txt <br>
-connection_log.txt <br>

If you send all 2 files, I can more fastly fix framework problem. Thanks.

<a name="changelog"></a>
# Change log

Version 1.0.4 Beta[right now]:<br>
-Rewrited code <br>
-Rewrited GUI mode <br>
-Using PEP8 <br>
-New feature: settings <br>
-New feature: logs <br>
-New mode: trainig <br>
-Added easter eggs <br>
-Some bug fixes

Version 1.0.3: <br>
-Some bug fixes

Version 1.0.2: <br>
-Some bug fixes <br>
-New feature: system of checking internet-connection <br>
-New feature: command panel <br>
-New feature: check avialable of new versions <br> <br>

Version 1.0.1: <br>
-Some bug fixes <br> <br>

Version 1.0.0: <br>
-Base framework work

<a name="contact"></a>
# Contact

© 2018; Elisey Sharov

elisey.sharow@yandex.ru - main e-mail <br>
playofstiverz@gmail.com - second e-mail <br>
scg-publicmail@yandex.ru - e-mail for your errors and another issues
