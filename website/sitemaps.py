from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5 #! یعنی چقدر اولویت داره که این سایت زودتر از بقیه ایندکس بشه
    changefreq = "daily" #! به ازای بازه زمانی چقدر طول میکشه که این سایت آپدیت بشه روزانه یا هفتگی یا ماهانه و غیره

    def items(self):
        return ["website:home", "website:myContact"]

    def location(self, item):
        return reverse(item)