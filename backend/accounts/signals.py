from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from accounts.models.user import User
from accounts.models.profiles.administrator import administrator_profile
from accounts.models.profiles.teacher import teacher_profile
from accounts.models.profiles.student import student_profile


@receiver(post_save, sender=User)
def create_profile(sender, instance=None, created=False, **kwargs):
    if created:
        if instance.mode == 1:
            student = student_profile.objects.create(user=instance)
        if instance.mode == 2:
            teacher = teacher_profile.objects.create(user=instance)
        if instance.mode == 3:
            administrator = administrator_profile.objects.create(user=instance)
