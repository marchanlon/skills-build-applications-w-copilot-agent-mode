# Test data for OctoFit Tracker
# This file contains sample data for users, teams, activities, leaderboard, and workouts.

TEST_USERS = [
    {"username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
    {"username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
    {"username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
    {"username": "crashoverride", "email": "crashoverride@mhigh.edu", "password": "crashoverridepassword"},
    {"username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
]

TEST_TEAMS = [
    {"name": "Blue Team", "members": ["thundergod", "metalgeek"]},
    {"name": "Gold Team", "members": ["zerocool", "crashoverride", "sleeptoken"]},
]

TEST_ACTIVITIES = [
    {"user": "thundergod", "activity_type": "Cycling", "duration": "1:00:00"},
    {"user": "metalgeek", "activity_type": "Crossfit", "duration": "2:00:00"},
    {"user": "zerocool", "activity_type": "Running", "duration": "1:30:00"},
    {"user": "crashoverride", "activity_type": "Strength", "duration": "0:30:00"},
    {"user": "sleeptoken", "activity_type": "Swimming", "duration": "1:15:00"},
]

TEST_LEADERBOARD = [
    {"user": "thundergod", "score": 100},
    {"user": "metalgeek", "score": 90},
    {"user": "zerocool", "score": 95},
    {"user": "crashoverride", "score": 85},
    {"user": "sleeptoken", "score": 80},
]

TEST_WORKOUTS = [
    {"name": "Cycling Training", "description": "Training for a road cycling event"},
    {"name": "Crossfit", "description": "Training for a crossfit competition"},
    {"name": "Running Training", "description": "Training for a marathon"},
    {"name": "Strength Training", "description": "Training for strength"},
    {"name": "Swimming Training", "description": "Training for a swimming competition"},
]