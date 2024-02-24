from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post


class LatestEntriesFeed(Feed):
    title = "blog nrewst post"
    link = "/rss/feed"
    description = "Updates on changes and additions to blog post."

    def items(self):
        return Post.objects.filter(status=True)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:100]

    # # item_link is only needed if NewsItem has no get_absolute_url method.
    # def item_link(self, item):
    #     return reverse("news-item", args=[item.pk])