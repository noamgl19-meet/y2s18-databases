from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__ = "Knowledge"
	article_id = Column(Integer, primary_key = True)
	article_name = Column(String)
	article_topic = Column(String)
	article_rating = Column(Integer)
	def __repr__(self):
		if (self.article_rating >= 7):
			return ("if you wanna study "+self.article_topic +", "+self.article_name+ " is going to be perfect for you. \n infact, its rating is "+str(self.article_rating) +"/10\n"
				+"article Name: {}\n"
            	"article topic: {} \n"
                "article rating: {}").format(
    				self.article_name, self.article_topic, self.article_rating)



				
		else:
			return ("Unfortunately, this article does not have a better rating. \nMaybe, this is an article that should be replaced soon!.\n"
				+"article Name: {}\n"
            	"article topic: {} \n"
                "article rating: {}").format(
    				self.article_name, self.article_topic, self.article_rating)
				


				
	