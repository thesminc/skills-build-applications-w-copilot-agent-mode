from django.core.management.base import BaseCommand # type: ignore
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.test_data import get_test_data

def populate_db():
    test_data = get_test_data()

    # Populate users
    for user in test_data['users']:
        User.objects.create(**user)

    # Populate teams
    for team in test_data['teams']:
        Team.objects.create(**team)

    # Populate activities
    for activity in test_data['activities']:
        user = User.objects.get(username=activity.pop('user'))
        Activity.objects.create(user=user, **activity)

    # Populate leaderboard
    for entry in test_data['leaderboard']:
        user = User.objects.get(username=entry.pop('user'))
        Leaderboard.objects.create(user=user, **entry)

    # Populate workouts
    for workout in test_data['workouts']:
        Workout.objects.create(**workout)

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        populate_db()
        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))