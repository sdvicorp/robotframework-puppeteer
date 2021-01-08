from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.ikeywords.ipanel_async import iPanelAsync


class PanelKeywords(LibraryComponent):

    def __init__(self, ctx):
        super().__init__(ctx)

    def get_async_keyword_group(self) -> iPanelAsync:
        return self.ctx.get_current_library_context().get_async_keyword_group(type(self).__name__)

    ##############################
    # Action
    ##############################
    @keyword
    def browse_to_access_settings(self):
        """Clicks element identified by ``locator``.

        The ``noWaitAfter`` argument specifies skip wait for animation after click.
        Only support for webkit and safari (Puppeteer)

        Example:

        | `Click Element`         | id:register          |            |
        | `Click Element`         | id:register          | ${True}    |
        """
        self.loop.run_until_complete(self.get_async_keyword_group().browse_to_access_settings())