from PuppeteerLibrary.ikeywords.base_async_keywords import BaseAsyncKeywords
from abc import ABC, abstractmethod


class iPanelAsync(BaseAsyncKeywords, ABC):

    ##############################
    # Query Element
    ##############################
    @abstractmethod
    async def click_element_too(self, locator: str, noWaitAfter: str='False'):
        pass