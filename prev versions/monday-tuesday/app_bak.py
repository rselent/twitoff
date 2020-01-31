
from flask import Flask

# APP = Flask( __name__)

# @APP.route( '/')

# def main():

#	return "<h1>Hello, bitches!</h1>"

def create_app():
	app = Flask( __name__)

	@app.route( '/')
	def root():
		return "<h1>Aloha, bitches!<h1>"

	return app


#if __name__ == '__main__':
#	app.run( debug= True, port= 8080)
#	main()