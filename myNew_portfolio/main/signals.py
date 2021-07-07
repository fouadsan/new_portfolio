from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.files.storage import default_storage

from .models import Profile,  Project, Service


@receiver(post_delete, sender=Profile)
def post_delete_picture_and_cv(sender, instance, *args, **kwargs):
    default_storage.delete(f'{instance.picture}')
    default_storage.delete(f'{instance.cv}')


@receiver(post_delete, sender=Service)
def post_delete_service_image(sender, instance, *args, **kwargs):
    default_storage.delete(f'{instance.image}')


@receiver(post_delete, sender=Project)
def post_delete_project_image(sender, instance, *args, **kwargs):

    default_storage.delete(f'{instance.image_one}')
    if instance.image_two:
        default_storage.delete(f'{instance.image_two}')
        if instance.image_three:
            default_storage.delete(f'{instance.image_three}')
            if instance.image_four:
                default_storage.delete(f'{instance.image_four}')
                if instance.image_five:
                    default_storage.delete(f'{instance.image_five}')
                    if instance.image_six:
                        default_storage.delete(f'{instance.image_six}')
                        if instance.image_seven:
                            default_storage.delete(f'{instance.image_seven}')
                            if instance.image_eight:
                                default_storage.delete(
                                    f'{instance.image_eight}')
                                if instance.image_nine:
                                    default_storage.delete(
                                        f'{instance.image_nine}')
                                    if instance.image_ten:
                                        default_storage.delete(
                                            f'{instance.image_ten}')
                                        if instance.image_eleven:
                                            default_storage.delete(
                                                f'{instance.image_eleven}')
