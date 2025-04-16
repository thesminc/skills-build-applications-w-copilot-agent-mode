from django.core.management.base import BaseCommand # type: ignore
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        user1 = User.objects.create(username='john_doe', email='john@example.com', password='password123')
        user2 = User.objects.create(username='jane_doe', email='jane@example.com', password='password123')

        # Create test teams
        team1 = Team.objects.create(name='Team Alpha')
        team1.members.add(user1, user2)

        # Create test activities
        Activity.objects.create(user=user1, activity_type='Running', duration=timedelta(minutes=30))
        Activity.objects.create(user=user2, activity_type='Cycling', duration=timedelta(hours=1))

        # Create test leaderboard entries
        Leaderboard.objects.create(user=user1, score=100)
        Leaderboard.objects.create(user=user2, score=150)

        # Create test workouts
        Workout.objects.create(name='Push-ups', description='Do 20 push-ups')
        Workout.objects.create(name='Sit-ups', description='Do 30 sit-ups')

        # Add more test users
        user3 = User.objects.create(username='alice_smith', email='alice@example.com', password='password123')
        user4 = User.objects.create(username='bob_jones', email='bob@example.com', password='password123')

        # Add more test teams
        team2 = Team.objects.create(name='Team Beta')
        team2.members.add(user3, user4)

        # Add more test activities
        Activity.objects.create(user=user3, activity_type='Swimming', duration=timedelta(minutes=45))
        Activity.objects.create(user=user4, activity_type='Hiking', duration=timedelta(hours=2))

        # Add more test leaderboard entries
        Leaderboard.objects.create(user=user3, score=200)
        Leaderboard.objects.create(user=user4, score=250)

        # Add more test workouts
        Workout.objects.create(name='Jumping Jacks', description='Do 50 jumping jacks')
        Workout.objects.create(name='Plank', description='Hold a plank for 1 minute')

        # Add even more test users
        user5 = User.objects.create(username='charlie_brown', email='charlie@example.com', password='password123')
        user6 = User.objects.create(username='diana_prince', email='diana@example.com', password='password123')

        # Add even more test teams
        team3 = Team.objects.create(name='Team Gamma')
        team3.members.add(user5, user6)

        # Add even more test activities
        Activity.objects.create(user=user5, activity_type='Yoga', duration=timedelta(minutes=60))
        Activity.objects.create(user=user6, activity_type='Weightlifting', duration=timedelta(minutes=90))

        # Add even more test leaderboard entries
        Leaderboard.objects.create(user=user5, score=300)
        Leaderboard.objects.create(user=user6, score=350)

        # Add even more test workouts
        Workout.objects.create(name='Burpees', description='Do 20 burpees')
        Workout.objects.create(name='Mountain Climbers', description='Do 30 mountain climbers')

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
