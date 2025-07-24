from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)
number_to_guess = random.randint(1, 100)
attempts = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    global attempts, number_to_guess

    data = request.get_json()
    try:
        guess = int(data.get('guess'))
    except (ValueError, TypeError):
        return jsonify({'message': 'Invalid input. Please enter a number.'}), 400

    attempts += 1

    if guess < number_to_guess:
        return jsonify({'message': 'Too low! Try again.'})
    elif guess > number_to_guess:
        return jsonify({'message': 'Too high! Try again.'})
    else:
        response = {
            'message': f'🎉 Congratulations! You guessed it in {attempts} attempts.',
            'success': True
        }
        number_to_guess = random.randint(1, 100)
        attempts = 0
        return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
