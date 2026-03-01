from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator

class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]

    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        null=False,
        blank=False
    )

class Club(models.Model):
    club_id = models.BigAutoField(primary_key=True)
    club_name = models.CharField(max_length=200)

class Player(models.Model):
    player_id = models.BigAutoField(primary_key=True)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100)
        ]
    )

    # Deleting FK will automatically delete reference row in foreign table
    club_id = models.ForeignKey(Club, on_delete=models.CASCADE) 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

# class Session(models.Model):
#     session_id = models.BigAutoField(primary_key=True)
#     date = models.DateField(default=datetime.date.today)
#     venue = CharField(max_length=200)
#     active = models.BooleanField(default=True)
#     number_of_courts = models.CharField(
#         max_length=20,
#         choices=[1, 2, 3, 4],
#         null=False,
#         blank=False
#     )

# class Match(models.Model):
#     match_id = models.BigAutoField(primary_key=True)
#     session_id = models.ForeignKey(Session, on_delete=models.CASCADE)
#     court = models.PositiveIntegerField(default=1)
#     score = ArrayField(
#         base_field=models.IntegerField(
#             validators=[MinValueValidator(0), MaxValueValidator(21)]
#         ),
#         size=2,          # exactly 2 elements
#         null=True,       # allows NULL
#         blank=True
#     )
#     winning_team = models.CharField(
#         max_length=20,
#         choices=[1, 2],
#         null=False,
#         blank=False
#     )
#     finished = models.BooleanField(default=False)

# class MatchParticipant(models.Model):
#     match_participant_id = models.BigAutoField(primary_key=True)
#     match_id = models.ForeignKey(Match, on_delete=DO_NOTHING)
#     player_id = models.ForeignKey(Player, on_delete=DO_NOTHING)
#     team = models.CharField(
#         max_length=20,
#         choices=[1, 2],
#         null=False,
#         blank=False
#     )

# class PlayerSession(models.Model):
#     player_session_id = models.BigAutoField(primary_key=True)
#     session_id = models.ForeignKey(Session, on_delete=DO_NOTHING)
#     player_id = models.ForeignKey(Player, on_delete=DO_NOTHING)
#     pause = models.BooleanField(default=False)