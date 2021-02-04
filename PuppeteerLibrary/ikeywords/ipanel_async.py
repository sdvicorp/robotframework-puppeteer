from PuppeteerLibrary.ikeywords.base_async_keywords import BaseAsyncKeywords
from abc import ABC, abstractmethod


class iPanelAsync(BaseAsyncKeywords, ABC):

    ##############################
    # Misc
    ##############################
    @abstractmethod
    async def click_off_element(self):
        pass

    @abstractmethod
    async def get_attribute(self):
        pass

    ##############################
    # Settings Page
    ##############################
    @abstractmethod
    async def browse_to_access_settings(self):
        pass

    @abstractmethod
    async def get_access_authentication_method(self):
        pass

    @abstractmethod
    async def get_access_api_token(self):
        pass

    @abstractmethod
    async def set_access_authentication_method(self, authtype: str, token: str = None):
        pass

    @abstractmethod
    async def get_access_api_hostname(self):
        pass

    @abstractmethod
    async def set_access_api_hostname(self, hostname: str):
        pass

    @abstractmethod
    async def open_preferred_workorders_list(self):
        pass

    @abstractmethod
    async def get_preferred_workorders_list(self):
        pass

    @abstractmethod
    async def clear_selected_preferred_workorders(self):
        pass

    @abstractmethod
    async def select_preferred_workorders_by_name(self, presets: list, deselect_existing: bool = False):
        pass

    @abstractmethod
    async def select_at_least_one_preferred_workorder(self):
        pass

    @abstractmethod
    async def save_access_settings_changes(self):
        pass

    @abstractmethod
    async def cancel_access_settings_changes(self):
        pass

    ##############################
    # Workorders Page
    ##############################
    @abstractmethod
    async def browse_to_access_workorders(self):
        pass

    @abstractmethod
    async def open_my_tasks(self):
        pass

    @abstractmethod
    async def open_my_group_tasks(self):
        pass

    @abstractmethod
    async def open_all_unassigned_tasks(self):
        pass

    @abstractmethod
    async def get_visible_workorder_jobs_for_task(self, presetname: str):
        pass

    @abstractmethod
    async def get_workorder_table_job_details(self, presetname: str = None, jobindex: int = None, jobid: str = None):
        pass

    @abstractmethod
    async def open_workorder_by_job_id(self, jobid: str):
        pass

    @abstractmethod
    async def open_workorder_by_preset_and_asset_name(self, presetname: str, assetname: str):
        pass

    ##############################
    # Metadata Page
    ##############################
    @abstractmethod
    async def wait_for_qc_event_tree_to_load(self, timeout: int = 30):
        pass

    @abstractmethod
    async def browse_to_workorder_metadata(self):
        pass

    @abstractmethod
    async def save_workorder_changes(self, savedelay: int = 5):
        pass

    @abstractmethod
    async def get_qc_event_tree_categories(self):
        pass

    @abstractmethod
    async def collapse_all_event_categories(self):
        pass

    @abstractmethod
    async def expand_all_event_categories(self):
        pass

    @abstractmethod
    async def expand_event_category(self, category: str):
        pass

    @abstractmethod
    async def select_event_by_event_title(self, category: str, title: str):
        pass

    @abstractmethod
    async def deselect_event_by_event_title(self, category: str, title: str):
        pass