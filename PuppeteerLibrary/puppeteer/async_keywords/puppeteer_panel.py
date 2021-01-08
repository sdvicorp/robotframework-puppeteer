from PuppeteerLibrary.utils.coverter import str2bool
from typing import Optional
from robot.libraries.BuiltIn import BuiltIn
from PuppeteerLibrary.ikeywords.ipanel_async import iPanelAsync


class PuppeteerPanel(iPanelAsync):

    ##############################
    # Locators
    ##############################

    settingsPageButton = "css:[testtag='settings-page']"
    settingsWorkorderList = "css:[testtag='settings-workorders-list']"
    settingsAuthRadioGroup = "css:[testtag='settings-auth-radio-group']"
    workordersPageButton = "css:[testtag='workorder-page']"

    def __init__(self, library_ctx):
        super().__init__(library_ctx)

    ##############################
    # Navigate to Settings Page
    ##############################
    async def browse_to_access_settings(self):
        try:
            return await self.library_ctx.get_current_page().waitForSelector_with_selenium_locator(self.settingsWorkorderList, 0.1, visible=True, hidden=False)
        except:
            element = await self.library_ctx.get_current_page().querySelector_with_selenium_locator(self.settingsPageButton)
            await element.click()
        finally:
            await self.library_ctx.get_async_keyword_group('WaitingKeywords').wait_until_page_contains('Rally Settings')
