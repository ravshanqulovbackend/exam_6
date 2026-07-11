from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategoriya nomi")

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Maqola sarlavhasi")
    body = models.TextField(verbose_name="Maqola matni")
    image = models.ImageField(upload_to='post_images/', blank=True, null=True, verbose_name="Asosiy rasm (Orqa fon)")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', null=True, blank=True, verbose_name="Kategoriyasi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")

    class Meta:
        verbose_name = "Maqola"
        verbose_name_plural = "Maqolalar"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images', verbose_name="Maqola")
    image = models.ImageField(upload_to='post_gallery/', verbose_name="Rasm yuklash")

    class Meta:
        verbose_name = "Maqola rasmi"
        verbose_name_plural = "Maqola rasmlari"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name="Maqola")
    name = models.CharField(max_length=100, verbose_name="Ismi")
    email = models.EmailField(verbose_name="Email manzili")
    body = models.TextField(verbose_name="Izoh matni")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yozilgan vaqti")

    class Meta:
        verbose_name = "Izoh"
        verbose_name_plural = "Izohlar"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.post.title}"
