from flask import Flask, render_template, jsonify, request
from dcgenerator1 import dcgenerator1
from dcgenerator2 import dcgenerator2
from dcgenerator3 import dcgenerator3
from dcmotor1 import dcmotor1
from dcmotor2 import dcmotor2
from dcmotor3 import dcmotor3
import random


app = Flask(__name__)

dcmotor_functions = [dcmotor1, dcmotor2, dcmotor3]
dcgenerator_functions = [dcgenerator1, dcgenerator2, dcgenerator3]

@app.route('/')
def home():
	return render_template ('base.html')


@app.route('/_get_qs', methods=['POST'])
def get_qs():

	try:

		q_type = request.form['type']
		q_difficulty = request.form['difficulty']

		if q_type == 'dcmotor':
			question_html, solution_html = random.choice(dcmotor_functions)(q_difficulty)

		if q_type == 'dcgenerator':
			question_html, solution_html = random.choice(dcgenerator_functions)(q_difficulty)

		

		return jsonify({
			'status': True,
			'question': question_html,
			'solution': solution_html})

	except Exception as e:
		print "Error: ", e
		return jsonify({'status': False})





	return render_template ('base.html')



if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)

