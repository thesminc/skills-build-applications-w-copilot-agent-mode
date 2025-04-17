from datetime import timedelta
from bson import ObjectId

def get_test_data():
    return {
        "users": [
            {"_id": ObjectId(), "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
            {"_id": ObjectId(), "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
            {"_id": ObjectId(), "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
            {"_id": ObjectId(), "username": "crashoverride", "email": "crashoverride@hmhigh.edu", "password": "crashoverridepassword"},
            {"_id": ObjectId(), "username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
        ],
        "teams": [
            {"_id": ObjectId(), "name": "Blue Team"},
            {"_id": ObjectId(), "name": "Gold Team"},
        ],
        "activities": [
            {"_id": ObjectId(), "user": "thundergod", "activity_type": "Cycling", "duration": timedelta(hours=1)},
            {"_id": ObjectId(), "user": "metalgeek", "activity_type": "Crossfit", "duration": timedelta(hours=2)},
            {"_id": ObjectId(), "user": "zerocool", "activity_type": "Running", "duration": timedelta(hours=1, minutes=30)},
            {"_id": ObjectId(), "user": "crashoverride", "activity_type": "Strength", "duration": timedelta(minutes=30)},
            {"_id": ObjectId(), "user": "sleeptoken", "activity_type": "Swimming", "duration": timedelta(hours=1, minutes=15)},
        ],
        "leaderboard": [
            {"_id": ObjectId(), "user": "thundergod", "score": 100},
            {"_id": ObjectId(), "user": "metalgeek", "score": 90},
            {"_id": ObjectId(), "user": "zerocool", "score": 95},
            {"_id": ObjectId(), "user": "crashoverride", "score": 85},
            {"_id": ObjectId(), "user": "sleeptoken", "score": 80},
        ],
        "workouts": [
            {"_id": ObjectId(), "name": "Cycling Training", "description": "Training for a road cycling event"},
            {"_id": ObjectId(), "name": "Crossfit", "description": "Training for a crossfit competition"},
            {"_id": ObjectId(), "name": "Running Training", "description": "Training for a marathon"},
            {"_id": ObjectId(), "name": "Strength Training", "description": "Training for strength"},
            {"_id": ObjectId(), "name": "Swimming Training", "description": "Training for a swimming competition"},
        ],
    }
