from PuppeteerLibrary.ikeywords.base_async_keywords import BaseAsyncKeywords
from abc import ABC, abstractmethod


class iPanelAsync(BaseAsyncKeywords, ABC):

    ##############################
    # Query Element
    ##############################
    @abstractmethod
    async def find_elements2(self, locator: str):
        pass