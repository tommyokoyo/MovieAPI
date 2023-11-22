from storage.users import User
from utils.database_connection import Base, session, engine

Base.metadata.create_all(engine)

# demo users
user_1 = User('Thomas', 'Okoyo', 'okoyotommy@gmail.com', 'password')
user_2 = User('Sera', 'Ndabari', 'ndabarisera@gmail.com', 'password')
user_3 = User('Robert', 'Okoyo', 'okoyorobert@gmail.com', 'password')
user_4 = User('Maryanne', 'Atieno', 'atieno@gmail.com', 'password')
user_5 = User('Jesse', 'Juma', 'jessejuma@gmail.com', 'password')

session.add(user_1)
session.add(user_2)
session.add(user_3)
session.add(user_4)
session.add(user_5)

session.commit()
session.close()
