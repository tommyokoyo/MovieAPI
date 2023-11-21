from models import User

users = User.all()
for user in users:
    print(user)
