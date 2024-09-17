# flask_template

`flask --app run.py shell`

```python
from webapp import db
from webapp.blue.app00.models import User
db.create_all()
admin_user = User(email='admin@example.com', is_admin=True)
admin_user.set_password('admin_password')
db.session.add(admin_user)
db.session.commit()
exit()
```

`flask --app run.py db init`

`flask --app run.py db migrate`

`flask --app run.py db upgrade`
