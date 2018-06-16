import UsefulDB

class StartTest:
    def CreateUser(root=False):
        if root:
            create.user.params(user='Admin', password='12345', root=True)
            a = input('$ ')
            eval(a)
        else:
            create.user.params(user='No-Admin', password='12345')
            a = input('$ ')
            eval(a)

    def CreateDatabase(columns):
        create.database.params(name='Test', columns=columns)
        a = input('$ ')
        eval(a)

    def DeleteUser():
        delete.user.params(user='Admin', password='12345', static=True, confirm=True)
        a = input('$ ')
        eval(a)

    def DeleteRootedUser():
        delete.user.params(user='Admin', password='12345', root=True, confirm=True)
        a = input('$ ')
        eval(a)

    def DeleteDatabase():
        delete.database.params(name='Test', confirm=True)
        a = input('$ ')
        eval(a)

    def SearchFile(filename):
        import os
        os.startfile(filename)
        a = input('$ ')
        eval(a)

    def AddColumn():
        edit.database.add.column('Test', 'email')
        a = input('$ ')
        eval(a)

    def RemoveColumn():
        edit.database.remove.column('Test', 'email')
        a = input('$ ')
        eval(a)

a = input('$ ')
eval(a)