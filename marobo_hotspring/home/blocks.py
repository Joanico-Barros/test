from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class homeRichBlock(blocks.StructBlock):
    text = blocks.RichTextBlock(help_text='lsknlknflknlas dlajs lajs lajs f')
    align = blocks.ChoiceBlock(choices=(('left','Left'), ('right', 'Right'), ('center', 'Center'), ('justify', 'Justify')))

    class Meta:
        template = 'home/blocks/home_rich_block.html'


class PageLinkBlock(blocks.StructBlock):
    """
    Block that holds a page.
    """
    page = blocks.PageChooserBlock()

    class Meta:
        template = 'marobo_hotspring/templates/includes/header.html'

