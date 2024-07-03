# home/models.py
from django.db import models

class Inquiry(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20)
    question = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee_name} - {self.employee_id}"



































# class Inquiry(models.Model):
#     employee_name = models.CharField(max_length=100)
#     employee_id = models.CharField(max_length=100)
#     question = models.TextField()

#     def __str__(self):
#         return f"{self.employee_name} ({self.employee_id})"


# class Inquiry(models.Model):
#     employee_name = models.CharField(max_length=100)
#     employee_id = models.CharField(max_length=50)
#     question = models.TextField()

#     def __str__(self):
#         return self.question[:50]  # Display first 50 characters of the question

# home/models.py

# from django.db import models
# # home/models.py

# from django.db import models

# class Inquiry(models.Model):
#     employee_name = models.CharField(max_length=100)
#     employee_id = models.CharField(max_length=20)
#     question = models.TextField()
#     submitted_at = models.DateTimeField(auto_now_add=True)


# class Inquiry(models.Model):
#     employee_name = models.CharField(max_length=255)
#     employee_id = models.CharField(max_length=50)
#     question = models.TextField()
#     submitted_at = models.DateTimeField(auto_now_add=True)

# def __str__(self):
#     return f"Inquiry by {self.employee_name} (ID: {self.employee_id})"
