import os

from PIL import Image
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from slugify import slugify

from mainapp.models import *

MEDIA_URL = '/media/'

'''
class Membership(models.Model):
    time = models
    amount =
'''


def profile_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s"(slugify(instance.name, to_lower=True), ext)

    return os.path.join('profile/{user}/').format(user=User.username)


def profile_thumb_name(instance, filename):
    original_image_path = str(instance.skin).rsplit('/', 1)[0]
    return os.path.join(original_image_path, filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    subscription = models.BooleanField(default=False)
    skin = models.ImageField(upload_to='media/profile/', default='media/profile/steve.png')
    skin_thumb = models.CharField('Thumbnail image', max_length=255, blank=True, default="media/profile\steve_100x100.png")
    is_media = models.BooleanField(default=False)

    #    email = models.EmailField(blank=True)
    #    products_list = models.ManyToManyField(Product, blank=True)

    def __init__(self, *args, **kwargs):
        super(Profile, self).__init__(*args, **kwargs)
        self.__original_skin = self.skin.url

    def __str__(self):
        return self.user.username

    def get_thumb_image_url(self):
        return MEDIA_URL + self.skin_thumb

    def save(self, *args, **kwargs):
        if self.skin.url != self.__original_skin:
            size = {'height': 100, 'width': 100}
            super(Profile, self).save(*args, **kwargs)

            extension = str(self.skin.path).rsplit('.', 1)[1]  # получаем расширение загруженного файла
            filename = str(self.skin.path).rsplit(os.sep, 1)[1].rsplit('.', 1)[0]  # получаем имя загруженного файла (без пути к нему и расширения)
            fullpath = str(self.skin.path).rsplit(os.sep, 1)[0]  # получаем путь к файлу (без имени и расширения)

            if extension in ['jpg', 'jpeg', 'png']:  # если расширение входит в разрешенный список
                im = Image.open(str(self.skin.path))  # открываем изображение
                im = im.crop((8, 8, 16, 16))
                im = im.resize((size['width'], size['height']),
                               resample=Image.NEAREST)  # создаем миниатюру указанной ширины и высоты (важно - im.thumbnail сохраняет пропорции изображения!)
                thumbname = filename + "_" + str(size['width']) + "x" + str(
                    size['height']) + '.' + extension  # имя нового изображения в формате oldname_60x60.jpg
                im.save(fullpath + os.sep + thumbname)  # сохраняем полученную миниатюру
                self.skin_thumb = profile_thumb_name(self, thumbname)  # записываем путь к ней в поле image_thumb в модели
                super(Profile, self).save(*args, **kwargs)
        else:
            super(Profile, self).save(*args, **kwargs)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


post_save.connect(update_user_profile, sender=settings.AUTH_USER_MODEL)
