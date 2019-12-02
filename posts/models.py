from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify # new

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
CATEGORY = (
    (0,"Electronic"),
    (1,"Furniture"),
    (2,"Major Appliance"),
    (3,"Kitchen"),
    (4,"Books"),
    (5,"Motors")
)
CONDITION = {
    (0,"Brand New"),
    (1, "Used - Like New"),
    (2, "Used - Good"),
    (3, "Used - working"),
    (4, "Used - Not Working")
}

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(null=True)
    slug = models.SlugField(null=False, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    category = models.IntegerField(choices=CATEGORY, default=0)
    cover = models.ImageField(upload_to='media/images/', null=True, blank=True)
    condition = models.IntegerField(choices=CONDITION , default = 4)
    price = models.FloatField(null=True ,blank=True)
    @property
    def dollar_amount(self):
        return "$%s" % self.price if self.price else ""

    class Meta:
        ordering = ['-created_on']


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
