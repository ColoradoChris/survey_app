from django.db import models

# Create your models here.
class Survey(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class SurveyQuestion(models.Model):
    question_text = models.CharField(max_length = 300)
    survey = models.ForeignKey(Survey, on_delete = models.CASCADE)

    def __str__(self):
        return self.question_text

class SurveyChoice(models.Model):
    choice_text = models.CharField(max_length = 300)
    surveyquestion = models.ForeignKey(SurveyQuestion, on_delete = models.CASCADE)
    surveychoice = models.ForeignKey(Survey, on_delete = models.CASCADE)
    selection_amount = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text
