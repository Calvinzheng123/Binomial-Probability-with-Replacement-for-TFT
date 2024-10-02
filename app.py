from flask import Flask, render_template, request, redirect, url_for, flash
import logging
from tft_calculator import tft_probability_to_3_star, champion_costs

app = Flask(__name__)
app.secret_key = "your_secret_key"  

logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    return render_template('index.html', champion_costs=champion_costs)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        level = int(request.form['level'])
        unit_cost = int(request.form['unit_cost'])
        remaining_copies = int(request.form['remaining_copies'])
        total_rolls = int(request.form['total_rolls'])
        copies_needed = int(request.form['copies_needed'])
        units_bought = int(request.form['units_bought'])
        
        if not (1 <= level <= 11 and 1 <= unit_cost <= 5):
            flash("Invalid input for level or unit cost.")
            return redirect(url_for('index'))
        
        probability = tft_probability_to_3_star(
            level, unit_cost, remaining_copies, total_rolls, 
            copies_needed, units_bought, champion_costs
        )
        return render_template('result.html', probability=probability)

    except ValueError as e:
        logging.error(f"Input error: {e}")
        flash("Please enter valid numbers.")
        return redirect(url_for('index'))
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        flash("An unexpected error occurred. Please try again.")
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
