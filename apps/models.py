from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

#personal information
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True)
    bio = models.TextField(blank=True)
    designation = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        # Update the 'updated' field whenever the object is saved
        self.updated = timezone.now()
        super().save(*args, **kwargs)
        
#social media information
class Social(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social')
    image = models.ImageField(upload_to='social_images/', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True)
    link = models.URLField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Social Profile"

    def save(self, *args, **kwargs):
        # Update the 'updated' field whenever the object is saved
        self.updated = timezone.now()
        super().save(*args, **kwargs)
     
#projects information   
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=200, blank=True)
    code = models.URLField(max_length=200, blank=True)
    framework = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)

    def __str__(self):
        return f"Image for {self.project.name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
#skills
class Language(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='language_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Frontend(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='frontend_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Backend(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='backend_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Database(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='database_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
  
#education information      
class TenthDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='tenth_details')
    school_name = models.CharField(max_length=100)
    board = models.CharField(max_length=50)
    year_of_passing = models.PositiveSmallIntegerField()
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s 10th Details"

class TwelfthDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='twelfth_details')
    school_name = models.CharField(max_length=100)
    board = models.CharField(max_length=50)
    year_of_passing = models.PositiveSmallIntegerField()
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s 12th Details"

class CollegeDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='college_details')
    college_name = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    year_of_graduation = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s College Details"
    
#feedback 
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    gmail = models.EmailField()
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.name} ({self.gmail})"
    
#resume
class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='resume')
    resume = models.FileField(upload_to='resumes/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Resume of {self.user.username}"

    def save(self, *args, **kwargs):
        # Update the 'updated_at' field whenever the object is saved
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='education')
    qualification = models.CharField(max_length=100)
    institute_name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100, null=True)
    board_name = models.CharField(max_length=100)
    percentage = models.CharField(max_length=4)
    admission_year = models.DateTimeField()
    passing_year = models.DateTimeField()
    image = models.ImageField(upload_to="institute_images/" , null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Education of {self.user.username}"

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)
