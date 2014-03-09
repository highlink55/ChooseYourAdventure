from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User)
    favoritedStories = models.ForeignKey('Story')
    description = models.CharField(max_length=100)
    favoritedStories.blank = True
    favoritedStories.null = True
    def __unicode__(self):  
        return self.description
    
class Story(models.Model):  
    title = models.CharField(max_length=200)
    author = models.OneToOneField('Profile')
    isPublished = models.BooleanField()
    isVisible = models.BooleanField()
    isComplete = models.BooleanField()
    PublishDate = models.DateField()
    UpdatedDate = models.DateField()
    initialSegment = models.OneToOneField('StorySegment')
    
    def __unicode__(self):  
        return self.title
    
    
class StorySegment(models.Model):
    text = models.TextField()
    level = models.IntegerField()
    choice = models.OneToOneField('Choice')
    choice.blank = True
    choice.null = True
    #story = models.OneToOneField('Story')
    
    def __unicode__(self):  
        return self.text
     
    def addChoice(self, choiceType):
        if (choiceType == "poll"):
            self.choice = Poll()
        elif (choiceType == "split"):
            self.choice = Split()
        else:
            print 'Choice Type not valid'
            raise

class Choice(models.Model):
    path = models.ForeignKey('StorySegment', related_name="relatedSegements")    

         
class Poll(Choice):
    options = models.CharField(max_length=200)

#     
class Split(Choice):
    options = models.CharField(max_length=200)

    