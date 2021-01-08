from PuppeteerLibrary.utils.coverter import str2bool
from typing import Optional
from robot.libraries.BuiltIn import BuiltIn
from PuppeteerLibrary.ikeywords.ipanel_async import iPanelAsync


class PuppeteerPanel(iPanelAsync):

    def __init__(self, library_ctx):
        super().__init__(library_ctx)

    ##############################
    # Click
    ##############################
#    async def click_element(self, locator: str, noWaitAfter: str='False'):
#        element = await self.library_ctx.get_current_page().querySelector_with_selenium_locator(locator)
#        await element.click()
