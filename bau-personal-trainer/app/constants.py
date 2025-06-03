class ErrorMessages:
    EMAIL_EXISTS = "A user with this email already exists"
    INVALID_AGE = "Age must be between 13 and 120 years"
    INVALID_WEIGHT = "Weight must be between 0 and 500 kg"
    INVALID_HEIGHT = "Height must be between 0 and 300 cm"
    INVALID_GOAL = "Goal must be one of: 'lose', 'maintain', 'gain'"
    DATABASE_ERROR = "Database error occurred: {}"
    UNEXPECTED_ERROR = "An unexpected error occurred: {}"

class ValidationRules:
    MIN_AGE = 13
    MAX_AGE = 120
    MIN_WEIGHT = 0
    MAX_WEIGHT = 500
    MIN_HEIGHT = 0
    MAX_HEIGHT = 300
    VALID_GOALS = ["lose", "maintain", "gain"] 