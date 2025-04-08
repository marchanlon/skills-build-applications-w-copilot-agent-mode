from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.test_data import TEST_USERS, TEST_TEAMS, TEST_ACTIVITIES, TEST_LEADERBOARD, TEST_WORKOUTS
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = []
        for user_data in TEST_USERS:
            user = User(_id=ObjectId(), **user_data)
            user.save()
            users.append(user)

        # Create teams
        for team_data in TEST_TEAMS:
            members = [User.objects.get(username=member) for member in team_data.pop('members')]
            team = Team(_id=ObjectId(), **team_data)
            team.save()
            team.members = members  # Directly assign the members list
            team.save()  # Save the team again after assigning members

        # Create activities
        for activity_data in TEST_ACTIVITIES:
            user = User.objects.get(username=activity_data.pop('user'))
            duration_parts = list(map(int, activity_data.pop('duration').split(':')))
            duration = timedelta(hours=duration_parts[0], minutes=duration_parts[1], seconds=duration_parts[2])
            activity = Activity(_id=ObjectId(), user=user, duration=duration, **activity_data)
            activity.save()

        # Create leaderboard entries
        for leaderboard_data in TEST_LEADERBOARD:
            user = User.objects.get(username=leaderboard_data.pop('user'))
            leaderboard = Leaderboard(_id=ObjectId(), user=user, **leaderboard_data)
            leaderboard.save()

        # Create workouts
        for workout_data in TEST_WORKOUTS:
            workout = Workout(_id=ObjectId(), **workout_data)
            workout.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))