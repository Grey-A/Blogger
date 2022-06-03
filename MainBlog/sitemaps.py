from django.contrib.sitemaps import Sitemap

from blog.models import Post, Category, Subscribe

class CategorySitemap(Sitemap):
    def items(self):
        return Category.objects.all()

class PostSitemap(Sitemap):
    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.date_added
    
class SubscribeSitemap(Sitemap):
    def items(self):
        return Subscribe.objects.all()