from blueprintapp.app import db
""" 
class Person(db.Model):
    __tablename__ = 'people'

    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer)
    job = db.Column(db.Text)

    def __repr__(self):
        return f'Person with name {self.name} and age {self.age}'
"""

#for to do our database. Put them in terminal.
#flask db init
#flask db migrate -m "Initial migration."
#flask db upgrade
""" 
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String)
    description = db.Column(db.String)

    def __repr__(self):
        return f'<User: {self.username}, Role: {self.role}>'

    def get_id(self):
        return self.uid

"""

class Todo(db.Model):
    __tablename__ = 'todos'

    tid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<TODO {self.title}, Done: {self.done}>"

    def get_id(self):
        return self.tid
