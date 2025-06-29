# BAU Personal Trainer API

A FastAPI-based backend service for a personal training application that helps users manage their fitness goals and workout plans.

## Features

- User management:
  - Registration with validation
  - Age (13-120 years)
  - Weight (0-500 kg)
  - Height (0-300 cm)
  - Fitness goals (lose/maintain/gain)
- Comprehensive workout plans:
  - Create personalized workout plans
  - Multiple pre-defined templates:
    - Beginner Strength Training
    - Intermediate Hypertrophy
    - Advanced Powerlifting
    - Cardio and Endurance
    - Flexibility and Mobility
  - Exercise categorization:
    - Muscle groups (chest, back, legs, etc.)
    - Exercise types (strength, cardio, flexibility, etc.)
    - Equipment tracking
  - Progress tracking:
    - Weight, sets, and reps logging
    - Difficulty ratings
    - Pain/discomfort monitoring
    - Historical progress view
- Data validation and constraints
- SQLite database persistence
- RESTful API endpoints
- Domain-driven design architecture

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd bau-pt
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- Windows:
```bash
.\venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the FastAPI server:
```bash
uvicorn bau-personal-trainer.app.main:app --reload
```

The server will start at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:
- Interactive API documentation: `http://localhost:8000/docs`
- Alternative API documentation: `http://localhost:8000/redoc`

### Available Endpoints

#### User Management

##### POST /users/signup
Register a new user with their fitness details.

Request body:
```json
{
    "email": "user@example.com",
    "age": 25,
    "weight": 70.5,
    "height": 175.0,
    "goal": "lose"
}
```

##### GET /users
Retrieve all registered users.

#### Workout Plans

##### GET /workout-plans/templates
Get predefined workout plan templates for different experience levels and goals:
- Beginner Strength Training
- Intermediate Hypertrophy
- Advanced Powerlifting
- Cardio and Endurance
- Flexibility and Mobility

##### POST /workout-plans
Create a new workout plan.

Request body:
```json
{
    "name": "My Workout Plan",
    "description": "Custom workout plan",
    "difficulty_level": "intermediate",
    "duration_weeks": 12,
    "workouts_per_week": 4,
    "user_id": 1,
    "target_muscle_groups": ["chest", "back", "legs"],
    "exercises": [
        {
            "name": "Barbell Bench Press",
            "sets": 3,
            "reps": 10,
            "rest_seconds": 90,
            "notes": "Keep proper form",
            "muscle_groups": ["chest", "shoulders", "triceps"],
            "categories": ["strength", "compound"],
            "equipment": "barbell",
            "weight_kg": 60
        }
    ]
}
```

##### GET /workout-plans/{user_id}
Get all workout plans for a specific user.

##### GET /workout-plans/{user_id}/{plan_id}
Get a specific workout plan by ID.

##### PUT /workout-plans/{user_id}/{plan_id}
Update an existing workout plan.

Request body:
```json
{
    "name": "Updated Plan Name",
    "difficulty_level": "advanced",
    "target_muscle_groups": ["back", "legs"],
    "exercises": [
        {
            "name": "Deadlift",
            "sets": 5,
            "reps": 5,
            "rest_seconds": 180,
            "muscle_groups": ["back", "legs", "core"],
            "categories": ["strength", "compound"],
            "equipment": "barbell",
            "weight_kg": 100
        }
    ]
}
```

##### DELETE /workout-plans/{user_id}/{plan_id}
Delete a workout plan.

#### Exercise Progress Tracking

##### POST /workout-plans/{user_id}/{plan_id}/exercises/{exercise_id}/progress
Log progress for a specific exercise.

Request body:
```json
{
    "weight_kg": 65.0,
    "completed_sets": 3,
    "completed_reps": 10,
    "difficulty_rating": 7,
    "felt_pain": false,
    "notes": "Increased weight by 5kg"
}
```

##### GET /workout-plans/{user_id}/{plan_id}/exercises/{exercise_id}/progress
Get progress history for a specific exercise.

## Project Structure

```
bau-personal-trainer/
├── app/
│   ├── api/
│   │   ├── __init__.py      # API router configuration
│   │   ├── users/           # Users domain
│   │   │   ├── __init__.py
│   │   │   ├── routes.py    # User endpoints
│   │   │   ├── services.py  # User business logic
│   │   │   ├── models.py    # User Pydantic models
│   │   │   └── entities.py  # User database models
│   │   └── workout_plans/   # Workout plans domain
│   │       ├── __init__.py
│   │       ├── routes.py    # Workout endpoints
│   │       ├── services.py  # Workout business logic
│   │       ├── models.py    # Workout Pydantic models
│   │       └── entities.py  # Workout database models
│   ├── __init__.py
│   ├── main.py             # FastAPI application setup
│   ├── database.py         # Database connection setup
│   ├── database_init.py    # Database initialization
│   ├── exceptions.py       # Custom exceptions
│   └── constants.py        # Validation rules and messages
├── requirements.txt
└── README.md
```

## Data Models

### Exercise Categories
- **Muscle Groups**: chest, back, shoulders, biceps, triceps, legs, core, full_body
- **Exercise Types**: strength, cardio, flexibility, plyometric, bodyweight, compound, isolation
- **Equipment**: none, dumbbells, barbell, kettlebell, resistance_bands, machine, cable, bodyweight

### Validation Rules

#### Users
- Age: 13-120 years
- Weight: 0-500 kg
- Height: 0-300 cm
- Goals: lose/maintain/gain

#### Workout Plans
- Difficulty: beginner/intermediate/advanced
- Duration: 1-52 weeks
- Workouts per week: 1-7
- Exercises:
  - Sets: 1-10
  - Reps: 1-100
  - Rest time: 0-300 seconds
  - Weight: 0-500 kg

#### Progress Tracking
- Weight: 0-500 kg
- Sets: 1-10
- Reps: 1-100
- Difficulty rating: 1-10 scale
- Pain tracking: boolean with optional location

## Error Handling

The API provides clear error messages for:
- Invalid data formats
- Out-of-range values
- Duplicate email addresses
- Database errors
- Resource not found
- Validation constraints

## Development

The project follows clean architecture principles with:
- Domain-driven design
- Separation of concerns
- Dependency injection
- Type hints
- Custom exception handling
- Centralized validation rules

## License

[Your chosen license]

## Contributing

[Your contribution guidelines]
