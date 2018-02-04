from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
 
session = DBSession()




# >>> myFirstRestaurant = Restaurant(name = "Pizza Palace")
# >>> session.add(myFirstRestaurant)
# >>> session.commit()
# >>> session.query(Restaurant).all()
# [<database_setup.Restaurant object at 0xb6a0bd4c>]
# >>> session.query(MenuItem).all()
# []
# >>> cheesepizza = MenuItem(name = "Vegan Pizza", description = "Chao Cheese and homemade marinara", course = "Entree", price = "11.99", restaurant = myFirstRestaurant)
# >>> session.add(cheesepizza)
# >>> session.commit()
# >>> session.query(MenuItem).all()