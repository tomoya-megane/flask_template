# flask_template

## code structure

* README.md
* .gitignore
* run.py
* instance/ #db
* migrations/
* notebook/
* webapp/
  * \_\_init\_\_.py
    * `admin.add_view(UserModelView(User, db.session))`
    * `admin.add_view(UserLoginHistoryModelView(UserLoginHistory, db.session))`
    * `load_user`
    * `before_request`
    * `home`
  * config.py
  * utils/
    * \_\_init\_\_.py
  * static/
    * bootstrap-5.3.0-examples/
    * bootstrap-5.3.3-dist/
    * DataTables/
    * fontawesome-free-6.6.0-web/
    * plotly/
  * templates/
    * base.html
    * home.html
  * blue/
    * \_\_init\_\_.py
    * app00/
      * \_\_init\_\_.py
      * views.py
        * `login`
        * `logout`
      * models.py
        * `User`
        * `UserLoginHistory`
      * forms.py
        * `LoginForm`
      * admin.py
        * `AdminModelView`
        * `UserModelView`
        * `UserLoginHistoryModelView`
      * templates/
        * login.html
    * app01/
      * \_\_init\_\_.py
      * templates/
    * app02/
      * \_\_init\_\_.py
      * templates/

## run app

`python run.py`

## add user

`flask --app run.py shell`

```python
from webapp import db
from webapp.blue.app00.models import User

db.create_all()

admin_user = User(email='admin@example.com', is_admin=True)
admin_user.set_password('admin123')

db.session.add(admin_user)
db.session.commit()

exit()
```

`flask --app run.py db init`

`flask --app run.py db migrate`

`flask --app run.py db upgrade`
