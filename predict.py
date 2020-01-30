

"""
Prediction of Users based on tweet embeddings
"""
import numpy as np
# from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

from .models import User
from .twitter import BASILICA


def predict_user( user1_name, user2_name, tweet_text):
	"""
	Determine and return which user is more likely to say a given Tweet
	"""

	user1 = User.query.filter( User.name == user1_name).one()
	user2 = User.query.filter( User.name == user2_name).one()
	user1Embeddings = np.array( [tweet.embedding for tweet in user1.tweets])
	user2Embeddings = np.array( [tweet.embedding for tweet in user2.tweets])
	embeddings = np.vstack( [user1Embeddings, user2Embeddings])
	labels = np.concatenate( [np.ones( len( user1.tweets)),
							np.zeros( len( user2.tweets))])
	# log_reg = LogisticRegression().fit(embeddings, labels)
	kPred = KNeighborsClassifier( weights= 'distance', metric= 'cosine').fit( embeddings, labels)

	tweetEmbedding = BASILICA.embed_sentence( tweet_text, model= 'twitter')
	# return log_reg.predict(np.array(tweet_embedding).reshape(1, -1))
	return kPred.predict( np.array( tweetEmbedding).reshape( 1, -1))
