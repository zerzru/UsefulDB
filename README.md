# Contents

<h2>
	Education <br>
	<ol>
		<li><a href="#training?about">About</a></li>
		<li><a href="#training?examples">Examples</a></li>
		<ol>
			<li><a href="#training?examples_creating">Creating items</a></li>
			<li><a href="#training?examples_deleting">Deleting items</a></li>
		</ol>
	</ol>
	Main <br>
	<ol>
		<li><a href="#main?about">About</a>
		<li><a href="#main?examples">Examples</a>
		<ol>
			<li><a href="#main?examples_create_user">Creating user</a></li>
			<li><a href="#main?examples_create_database">Creating database</a></li>
			<li><a href="#main?examples_create_table">Creating table</a></li>
			<li><a href="#main?examples_deletes">Deletes</a></li>
		</ol>
		<li> <a href="#changelog">Changelog</a></li>
		<li> <a href="#contact">Contact</a></li>
	</ol>
</h2>

<a name="training?about"></a>
<h2> About training </h2>
If you already have a database and want to learn how to manage the framework, I have made a separate part of it "Training" so that you do not spoil anything. The main part of the framework and the training is very similar, but the training only works with local files to show you how the framework works. Training has being in "Education" folder.
<a name="education?examples"></a>
<h2> Education examples </h2>
<a name="education?examples_creating"></a>
<h3>Creating items</h3>

```python
create.user.params(user='Test', password='12345') #creating user
create.user.params(user='Admin', password='im_the_best_admin_with_very_hard_password') #creating a super-user for get new feature: command panel
create.database.params(name='Test', columns=3)
```

After launch this commands, in your folder(when you set settings after first framework launch) created a 2 files: user_<ID>.json and database_<NAME>.json. In root folder created 1 new file: rooted_users.json

<a name="education?examples_deleting"></a>
<h3>Deleting items</h3>

```python
delete.user.params(user='Test', password='12345', confirm=True) #deleting user
delete.database.params(name='Test', confirm=True) #deleting database
```

If you try to delete not exists file, you get the error alert.
