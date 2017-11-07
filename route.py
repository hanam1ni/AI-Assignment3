#!flask/bin/python

import sys
from nQueen import *
from flask import Flask, render_template, request, redirect, Response
import random, json

app = Flask(__name__)

@app.route('/')
def output():
	return 'This is Default Route'

@app.route('/queen', methods = ['POST'])
def solver():
	# Get JSON
	data = request.get_json()
	nQueen = int(data['nQueen'])
	initTemp = int(data['initTemp'])
	coolRate = float(data['coolRate'])
	QUEEN = simulatedAnnealing(coolRate, initTemp, nQueen)
	return json.dumps(QUEEN)

if __name__ == '__main__':
	# run!
	app.run()