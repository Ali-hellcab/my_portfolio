from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):

    
    # The title of the project. This will be a short string.
    title = models.CharField(max_length=200)
    
    # A detailed description of the project.
    description = models.TextField()
    
    # The URL or link to the project (e.g., GitHub repo, live site).
    link = models.URLField(max_length=200)
    
    # An image for the project, such as a screenshot or a logo.
    # Note: To use ImageField, you'll need to install Pillow (pip install Pillow)
    # and configure MEDIA_ROOT and MEDIA_URL in your settings.py.
    image = models.ImageField(upload_to='project_images/')
    
    # A timestamp for when the project was added.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a human-readable string representation of the object.
        """
        return self.title

    class Meta:
        # Orders the projects by creation date in descending order.
        # The most recent project will appear first.
        ordering = ['-created_at']


class Aboutme(models.Model):
    # The title, e.g., "My Story" or "Skills."
    title = models.CharField(max_length=100)
    
    # A detailed description of the section.
    description = models.TextField()

    def __str__(self):
        """
        Returns a human-readable string representation of the object.
        """
        return self.title


class Profilepic(models.Model):
    # The profile picture image.
    image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    # A timestamp for when the image was uploaded.
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a human-readable string representation of the object.
        """
        return "Main Profile Picture"
    
class Resume(models.Model):
    title = models.CharField(max_length=100, help_text="A brief title for the resume, e.g., 'My Resume'")
    file = models.FileField(upload_to='resume_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
