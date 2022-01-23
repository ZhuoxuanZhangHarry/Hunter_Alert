from django.db import models
from django.utils import timezone
from accounts.models import CustomUser


class Post(models.Model):

    class DeptName(models.TextChoices):
        Africana_Studies = "Africana Studies"
        Anthropology = "Anthropology"
        Archaeological_Studies = "Archaeological Studies"
        Art_History = "Art History"
        Studio_Art = "Studio Art"
        Athletics_and_Physical_Education = "Athletics and Physical Education"
        Biology = "Biology"
        Chemistry_and_Biochemistry = "Chemistry and Biochemistry"
        Cinema_Studies = "Cinema Studies"
        Classics = "Classics"
        Comparative_American_Studies = "Comparative American Studies"
        Comparative_Literature = "Comparative Literature"
        Computer_Science = "Computer Science"
        Creative_Writing = "Creative Writing"
        Dance = "Dance"
        Chinese = "Chinese"
        Japanese = "Japanese"
        East_Asian_Studies = "East Asian Studies"
        Economics = "Economics"
        Engineering = "Engineering"
        English = "English"
        Environmental_Studies = "Environmental Studies"
        French = "French"
        Italian = "Italian"
        Gender_Sexuality_and_Feminist_Studies = "Gender, Sexuality, and Feminist Studies"
        Geology = "Geology"
        German_Language_and_Literatures = "German Language and Literatures"
        Hispanic_Studies = "Hispanic Studies"
        History = "History"
        Jewish_Studies = "Jewish Studies"
        Latin_American_Studies = "Latin American Studies"
        Law_and_Society = "Law and Society"
        Learning_Across_Disciplines = "Learning Across the Disciplines"
        Mathematics = "Mathematics"
        Middle_East_and_North_Africa_Studies = "Middle East and North Africa Studies"
        Musical_Studies = "Musical Studies"
        Neuroscience = "Neuroscience"
        Philosophy = "Philosophy"
        Physics = "Physics"
        Astronomy = "Astronomy"
        Politics = "Politics"
        Psychology = "Psychology"
        Religion = "Religion"
        Rhetoric_and_Composition = "Rhetoric and Composition"
        Russian_Language_Literature_and_Culture = "Russian Language, Literature and Culture"
        Russian_and_East_European_Studies = "Russian and East European Studies"
        Sociology = "Sociology"
        Theater = "Theater"
        Non_Academic = "Other than academic"


    # blank = true -> it is required section, null = true -> attribute in database can be null
    User = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    Your_Name = models.CharField(max_length=120, null=True)
    Title = models.CharField(max_length=120, null=True)
    Description = models.TextField(blank=False, null=True)
    Department = models.CharField(max_length=120, choices=DeptName.choices, default=DeptName.Non_Academic)
    Requirement = models.TextField(blank=False, null=True)
    Deadline = models.CharField(max_length=120, null=True)
    Date_Posted = models.DateTimeField(default=timezone.now)
    Email = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.Title
