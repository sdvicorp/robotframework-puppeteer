from PuppeteerLibrary.ikeywords.base_async_keywords import BaseAsyncKeywords
from abc import ABC, abstractmethod


class iPanelAsync(BaseAsyncKeywords, ABC):

    ##############################
    # Query Element
    ##############################
    @abstractmethod
    async def browse_to_access_settings(self):
        pass