from django.db import models


class Profile(models.Model):
    full_name = models.CharField(max_length=30, null=True, blank=True)
    picture = models.ImageField(upload_to='profile_pics')
    about_me = models.TextField(max_length=500)
    birthday = models.DateField()
    phone = models.CharField(max_length=17)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    education_degree = models.CharField(max_length=20)
    cv = models.FileField(upload_to='cv', blank=True, null=True)

    def __str__(self):
        return self.full_name


class Skill(models.Model):
    name = models.CharField(max_length=50)
    percentage = models.PositiveBigIntegerField()
    color = models.CharField(max_length=20)
    is_field = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Resume(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    place = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-start_date', )


class Education(Resume):
    pass


class Experience(Resume):
    pass


class Service(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='services')
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)

    class CATEGORIES(models.TextChoices):
        web = 'web',
        mobile = 'mobile',
        desktop = 'desktop',
        upcoming = 'upcoming'
    category = models.CharField(
        max_length=20,
        choices=CATEGORIES.choices,
        default='Web apps'
    )
    description = models.TextField(max_length=500)
    image_one = models.ImageField(upload_to='projects')
    image_two = models.ImageField(
        upload_to='projects', blank=True, null=True)
    image_three = models.ImageField(
        upload_to='projects', blank=True, null=True)
    image_four = models.ImageField(
        upload_to='projects', blank=True, null=True)
    image_five = models.ImageField(
        upload_to='projects', blank=True, null=True)
    image_six = models.ImageField(
        upload_to='projects', blank=True, null=True)
    image_seven = models.ImageField(
        upload_to='projects', blank=True, null=True)
    image_eight = models.ImageField(
        upload_to='projects', blank=True, null=True)
    image_nine = models.ImageField(
        upload_to='projects', blank=True, null=True)
    image_ten = models.ImageField(
        upload_to='projects', blank=True, null=True)
    image_eleven = models.ImageField(
        upload_to='projects', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-id', )


class Social (models.Model):
    my_facebook = models.URLField()
    my_twitter = models.URLField()
    my_linkedin = models.URLField()

    def __str__(self):
        return 'Social Media'
