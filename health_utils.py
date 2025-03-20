def calculate_bmi(height, weight):
    """
    Calculate Body Mass Index (BMI) given height in meters and weight in kilograms.
    
    Formula: BMI = weight (kg) / height^2 (m^2)
    """
    bmi = weight / (height ** 2)
    return bmi

def calculate_bmr(height, weight, age, gender):
    """
    Calculate Basal Metabolic Rate (BMR) using the Harris-Benedict equation.
    
    For males:
    BMR = 88.362 + (13.397 × weight in kg) + (4.799 × height in cm) - (5.677 × age in years)
    
    For females:
    BMR = 447.593 + (9.247 × weight in kg) + (3.098 × height in cm) - (4.330 × age in years)
    """
    if gender == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:  # female
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    
    return bmr