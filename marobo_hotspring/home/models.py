from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from .blocks import homeRichBlock, PageLinkBlock


class HomePage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = StreamField(
            [
                ('text', homeRichBlock()),
            ])

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
    ]


class Navbar(Page):
    """
    Model that represents website navigation bars.  Can be modified through the
    snippets UI. 
    """
    name = models.CharField(max_length=255)

    menu_items = StreamField([
        ('page_link', PageLinkBlock()),
        ],)

    panels = [
        StreamFieldPanel('name'),
        StreamFieldPanel('menu_items')
    ]

    def __str__(self):
        return self.name
