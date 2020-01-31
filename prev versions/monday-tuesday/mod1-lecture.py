
from flask import Flask

APP = Flask( __name__)

@APP.route( '/')

def main():

	return "<h1>Hello, bitches!</h1>"

#	print( "<h1>Hello, bitches!</h1>")
#	return 0


if __name__ == '__main__':
	APP.run( debug= True, port= 8080)
#	main()