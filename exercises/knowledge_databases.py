from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random
engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()






def add_article(name,topic,rating):
	new_article = Knowledge( 
		article_name = name, 
		article_topic = topic, 
		article_rating = int(rating))

	print(repr(new_article))
	session.add(new_article)
	session.commit()


# name=input("enter a name \n")
# topic=input("enter a topic \n")
# rate=input("enter a rate: \n")
# add_article(name,topic,rate)

def query_all_articles():
   student = session.query(Knowledge).all()
   return student
# print(query_all_articles())

def query_article_by_topic(topic):
   student = session.query(Knowledge).filter_by(article_topic = topic).all()
   return student
# print(query_article_by_topic("birds"))

def delete_article_by_topic(topic):
   session.query(Knowledge).filter_by(article_topic = topic).delete()
   session.commit()
# delete_article_by_topic("birds")

def delete_all_articles():
	session.query(Knowledge).delete()
	session.commit()
# delete_all_articles()
print(query_all_articles())

def edit_article_rating(name,rate):
	# editting using filters


