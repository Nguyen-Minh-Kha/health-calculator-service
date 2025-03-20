from flask import Flask, request, jsonify, render_template
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/bmi', methods=['POST'])
def bmi():
    data = request.get_json()
    
    if not data or 'height' not in data or 'weight' not in data:
        return jsonify({"error": "Missing required parameters"}), 400
    
    try:
        height = float(data['height'])
        weight = float(data['weight'])
        
        if height <= 0 or weight <= 0:
            return jsonify({"error": "Height and weight must be positive values"}), 400
            
        bmi_value = calculate_bmi(height, weight)
        
        # Determine BMI category
        category = "Unknown"
        if bmi_value < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi_value < 25:
            category = "Normal weight"
        elif 25 <= bmi_value < 30:
            category = "Overweight"
        else:
            category = "Obese"
            
        return jsonify({
            "bmi": round(bmi_value, 2),
            "category": category
        })
    except ValueError:
        return jsonify({"error": "Invalid parameters"}), 400

@app.route('/bmr', methods=['POST'])
def bmr():
    data = request.get_json()
    
    required_params = ['height', 'weight', 'age', 'gender']
    if not data or not all(param in data for param in required_params):
        return jsonify({"error": "Missing required parameters"}), 400
    
    try:
        height = float(data['height'])
        weight = float(data['weight'])
        age = float(data['age'])
        gender = data['gender'].lower()
        
        if height <= 0 or weight <= 0 or age <= 0:
            return jsonify({"error": "Invalid parameters"}), 400
            
        if gender not in ['male', 'female']:
            return jsonify({"error": "Gender must be 'male' or 'female'"}), 400
            
        bmr_value = calculate_bmr(height, weight, age, gender)
        
        return jsonify({
            "bmr": round(bmr_value, 2),
            "daily_calories": {
                "sedentary": round(bmr_value * 1.2, 0),
                "light_exercise": round(bmr_value * 1.375, 0),
                "moderate_exercise": round(bmr_value * 1.55, 0),
                "active": round(bmr_value * 1.725, 0),
                "very_active": round(bmr_value * 1.9, 0)
            }
        })
    except ValueError:
        return jsonify({"error": "Invalid parameters"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)