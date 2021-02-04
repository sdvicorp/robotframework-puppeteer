from PuppeteerLibrary.base.robotlibcore import keyword
from PuppeteerLibrary.base.librarycomponent import LibraryComponent
from PuppeteerLibrary.ikeywords.ipanel_async import iPanelAsync


class PanelKeywords(LibraryComponent):

    def __init__(self, ctx):
        super().__init__(ctx)

    def get_async_keyword_group(self) -> iPanelAsync:
        return self.ctx.get_current_library_context().get_async_keyword_group(type(self).__name__)

    ##############################
    # Misc
    ##############################
    @keyword
    def click_off_element(self):
        """Clicks element identified by ``locator``.
        """
        self.loop.run_until_complete(self.get_async_keyword_group().click_off_element())

    @keyword
    def get_attribute(self, element, attribute):
        return self.loop.run_until_complete(self.get_async_keyword_group().get_attribute(element, attribute))

    ##############################
    # Settings Page
    ##############################
    @keyword
    def browse_to_access_settings(self):
        """Clicks element identified by ``locator``.
        """
        self.loop.run_until_complete(self.get_async_keyword_group().browse_to_access_settings())

    @keyword
    def get_access_authentication_method(self):
        """Clicks element identified by ``locator``.
        """
        return self.loop.run_until_complete(self.get_async_keyword_group().get_access_authentication_method())

    @keyword
    def get_access_api_token(self):
        """Clicks element identified by ``locator``.
        """
        return self.loop.run_until_complete(self.get_async_keyword_group().get_access_api_token())

    @keyword
    def set_access_authentication_method(self, authtype, token=None):
        """Clicks element identified by ``locator``.
        """
        self.loop.run_until_complete(self.get_async_keyword_group().set_access_authentication_method(authtype, token))

    @keyword
    def get_access_api_hostname(self):
        """Clicks element identified by ``locator``.
        """
        return self.loop.run_until_complete(
            self.get_async_keyword_group().get_access_api_hostname())

    @keyword
    def set_access_api_hostname(self, hostname):
        """Clicks element identified by ``locator``.
        """
        self.loop.run_until_complete(self.get_async_keyword_group().set_access_api_hostname(hostname))

    @keyword
    def open_preferred_workorders_list(self):
        """Clicks element identified by ``locator``.
        """
        self.loop.run_until_complete(self.get_async_keyword_group().open_preferred_workorders_list())

    @keyword
    def get_preferred_workorders_list(self):
        """Clicks element identified by ``locator``.
        """
        return self.loop.run_until_complete(
            self.get_async_keyword_group().get_preferred_workorders_list())

    @keyword
    def clear_selected_preferred_workorders(self):
        """Clicks element identified by ``locator``.
        """
        self.loop.run_until_complete(self.get_async_keyword_group().clear_selected_preferred_workorders())

    @keyword
    def select_preferred_workorders_by_name(self, presets, deselect_existing=False):
        self.loop.run_until_complete(self.get_async_keyword_group().select_preferred_workorders_by_name(presets, deselect_existing))

    @keyword
    def select_at_least_one_preferred_workorder(self):
        """Clicks element identified by ``locator``.
        """
        self.loop.run_until_complete(self.get_async_keyword_group().select_at_least_one_preferred_workorder())

    @keyword
    def save_access_settings_changes(self):
        """Clicks element identified by ``locator``.
        """
        self.loop.run_until_complete(self.get_async_keyword_group().save_access_settings_changes())

    @keyword
    def cancel_access_settings_changes(self):
        """Clicks element identified by ``locator``.
        """
        self.loop.run_until_complete(self.get_async_keyword_group().cancel_access_settings_changes())

    ##############################
    # Workorders Page
    ##############################
    @keyword
    def browse_to_access_workorders(self):
        self.loop.run_until_complete(self.get_async_keyword_group().browse_to_access_workorders())

    @keyword
    def open_my_tasks(self):
        self.loop.run_until_complete(self.get_async_keyword_group().open_my_tasks())

    @keyword
    def open_my_group_tasks(self):
        self.loop.run_until_complete(self.get_async_keyword_group().open_my_group_tasks())

    @keyword
    def open_all_unassigned_tasks(self):
        self.loop.run_until_complete(self.get_async_keyword_group().open_all_unassigned_tasks())

    @keyword
    def get_visible_workorder_jobs_for_task(self, presetname):
        return self.loop.run_until_complete(self.get_async_keyword_group().get_visible_workorder_jobs_for_task(presetname))

    @keyword
    def get_workorder_table_job_details(self, presetname=None, jobindex=None, jobid=None):
        return self.loop.run_until_complete(self.get_async_keyword_group().get_workorder_table_job_details(presetname, jobindex, jobid))

    @keyword
    def open_workorder_by_job_id(self, jobid):
        return self.loop.run_until_complete(
            self.get_async_keyword_group().open_workorder_by_job_id(jobid))

    @keyword
    def open_workorder_by_preset_and_asset_name(self, presetname, assetname):
        return self.loop.run_until_complete(
            self.get_async_keyword_group().open_workorder_by_preset_and_asset_name(presetname, assetname))

    ##############################
    # Metadata Page
    ##############################
    @keyword
    def wait_for_qc_event_tree_to_load(self, timeout=30):
        self.loop.run_until_complete(
            self.get_async_keyword_group().wait_for_qc_event_tree_to_load(timeout))

    @keyword
    def save_workorder_changes(self, savedelay=5):
        self.loop.run_until_complete(
            self.get_async_keyword_group().save_workorder_changes(savedelay))

    @keyword
    def get_qc_event_tree_categories(self):
        return self.loop.run_until_complete(self.get_async_keyword_group().get_qc_event_tree_categories())

    @keyword
    def collapse_all_event_categories(self):
        self.loop.run_until_complete(self.get_async_keyword_group().collapse_all_event_categories())

    @keyword
    def expand_all_event_categories(self):
        self.loop.run_until_complete(self.get_async_keyword_group().expand_all_event_categories())

    @keyword
    def expand_event_category(self, category):
        self.loop.run_until_complete(self.get_async_keyword_group().expand_event_category(category))

    @keyword
    def select_event_by_event_title(self, category, title):
        self.loop.run_until_complete(self.get_async_keyword_group().select_event_by_event_title(category, title))

    @keyword
    def deselect_event_by_event_title(self, category, title):
        self.loop.run_until_complete(self.get_async_keyword_group().deselect_event_by_event_title(category, title))