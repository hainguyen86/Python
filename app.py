from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return "Amazing Spider man \n Trump is a racist \n I want to \nfly to the moon!"

