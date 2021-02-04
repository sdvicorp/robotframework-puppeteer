import json
from PuppeteerLibrary.utils.coverter import str2bool
from typing import Optional
from robot.libraries.BuiltIn import BuiltIn
from time import sleep
from PuppeteerLibrary.ikeywords.ipanel_async import iPanelAsync


class PuppeteerPanel(iPanelAsync):

    ##############################
    # Locators
    ##############################

    accessLogo = "css:[class='logo']"
    settingsPageButton = "css:[testtag='settings-page']"
    workordersPageButton = "css:[testtag='workorder-page']"

    settingsWorkorderList = "css:[testtag='settings-workorders-list']"
    settingsAuthRadioGroup = "css:[testtag='settings-auth-radio-group']"
    settingsApiToken = "css:[testtag='settings-auth-api-token']"
    settingsApiHostname = "css:[testtag='settings-api-hostname']"
    settingsWorkordersOptions = "css:[testtag='settings-workorders-options']"
    settingsSaveButton = "css:[testtag='settings-save']"
    settingsCancelButton = "css:[testtag='settings-cancel']"

    workordersMyTasksButton = "css:[testtag='workorder-mytasks-button']"
    workordersMyGroupTasksButton = "css:[testtag='workorder-mygrouptasks-button']"
    workordersAllUnassignedTasksButton = "css:[testtag='workorder-unassignedtasks-button']"
    workordersTableTask = "css:[testtag='workorders-table-task']"
    workordersTableJob = "css:[testtag='workorders-table-job']"

    metadataQcEventCategory = "css:[testtag='qc-category']"
    workorderMetadataButton = "css:[testtag='workorder-metadata']"
    workorderSaveButton = "css:[testtag='workorder-save']"


    def __init__(self, library_ctx):
        super().__init__(library_ctx)

    ##############################
    # Common Keywords
    ##############################
    async def click_off_element(self):
        await self.library_ctx.get_async_keyword_group('ElementKeywords').click_element(self.accessLogo)

    async def get_attribute(self, element, attribute: str):
        return await element.executionContext.evaluate(f'element => element.getAttribute("{attribute}")', element)


    ##############################
    # Settings Page
    ##############################
    async def browse_to_access_settings(self):
        try:
            await self.library_ctx.get_async_keyword_group('ElementKeywords').element_should_be_visible(self.settingsWorkorderList)
        except AssertionError:
            await self.library_ctx.get_async_keyword_group('ElementKeywords').click_element(self.settingsPageButton)
        finally:
            await self.library_ctx.get_async_keyword_group('WaitingKeywords').wait_until_page_contains('Rally Settings')

    async def get_access_authentication_method(self):
        await self.library_ctx.get_async_keyword_group('ElementKeywords').element_should_be_visible(self.settingsAuthRadioGroup)
        return await self.library_ctx.get_async_keyword_group('JavascriptKeywords').execute_javascript("document.querySelector(\"[testtag='settings-auth-radio-group'] .mat-radio-checked\").getAttribute('value');")

    async def get_access_api_token(self):
        await self.library_ctx.get_async_keyword_group('ElementKeywords').element_should_be_visible(self.settingsAuthRadioGroup)
        return await self.library_ctx.get_async_keyword_group('ElementKeywords').get_value(self.settingsApiToken)

    async def set_access_authentication_method(self, authtype: str = 'token', token: str = None):
        assert authtype in ('token', 'okta')
        await self.library_ctx.get_async_keyword_group('ElementKeywords').element_should_be_visible(
            self.settingsAuthRadioGroup)
        await self.library_ctx.get_async_keyword_group('ElementKeywords').click_element(
            f"{self.settingsAuthRadioGroup}>[value='{authtype}']")
        if token:
            await self.library_ctx.get_async_keyword_group('FormElementKeywords').input_text(self.settingsApiToken, token)

    async def get_access_api_hostname(self):
        await self.library_ctx.get_async_keyword_group('ElementKeywords').element_should_be_visible(self.settingsApiHostname)
        return await self.library_ctx.get_async_keyword_group('ElementKeywords').get_value(self.settingsApiHostname)

    async def set_access_api_hostname(self, hostname: str):
        await self.library_ctx.get_async_keyword_group('ElementKeywords').element_should_be_visible(self.settingsApiHostname)
        await self.library_ctx.get_async_keyword_group('FormElementKeywords').input_text(self.settingsApiHostname, hostname)
        assert hostname == self.get_access_api_hostname()

    async def open_preferred_workorders_list(self):
        try:
            await self.library_ctx.get_async_keyword_group('ElementKeywords').element_should_be_visible(
                self.settingsWorkordersOptions)
        except AssertionError:
            await self.library_ctx.get_async_keyword_group('ElementKeywords').click_element(self.settingsWorkorderList)
            await self.library_ctx.get_async_keyword_group('WaitingKeywords').wait_until_element_is_visible(
                self.settingsWorkordersOptions, timeout='3s')
        finally:
            sleep(.5)

    async def get_preferred_workorders_list(self):
        await self.open_preferred_workorders_list()
        workorders = await self.library_ctx.get_async_keyword_group('ElementKeywords').find_elements(self.settingsWorkordersOptions)
        workorderState = []
        for option in workorders:
            nameProp = await (await option.getProperty('innerText')).jsonValue()
            selected = await self.get_attribute(option, 'aria-selected')
            workorderState.append({'name': nameProp,
                                  'selected': selected == 'true'})
        await self.click_off_element()
        sleep(.5)
        return workorderState

    async def clear_selected_preferred_workorders(self):
        await self.open_preferred_workorders_list()
        selectedPresets = await self.library_ctx.get_current_page().querySelectorAll_with_selenium_locator(self.settingsWorkordersOptions+'.mat-selected')
        print(f'Got {len(selectedPresets)} Selected Presets')
        for preset in selectedPresets:
            print(f"Clicking {await (await preset.getProperty('innerText')).jsonValue()}")
            await preset.click()
            sleep(.5)
        assert len(await self.library_ctx.get_async_keyword_group('ElementKeywords').find_elements(self.settingsWorkordersOptions+'.mat-selected')) == 0
        await self.click_off_element()
        sleep(.5)

    async def select_preferred_workorders_by_name(self, presets: list, deselect_existing: bool = False):
        if deselect_existing:
            await self.clear_selected_preferred_workorders()
        await self.open_preferred_workorders_list()
        if not isinstance(presets, list):
            print(f'Attempting to convert {presets} from {type(presets)}')
            try:
                presets = json.loads(presets)
            except Exception:
                try:
                    presets = eval(presets)
                except Exception as e:
                    raise e
        for preset in presets:
            try:
                await self.library_ctx.get_async_keyword_group('ElementKeywords').click_element(self.settingsWorkordersOptions+f"[testinfo='{preset}']:not(.mat-selected)")
            except Exception as e:
                print(f'Encountered exception {e} trying to click {preset}')
        await self.click_off_element()
        sleep(.5)

    async def select_at_least_one_preferred_workorder(self):
        await self.open_preferred_workorders_list()
        selectedPresets = await self.library_ctx.get_current_page().querySelectorAll_with_selenium_locator(
            self.settingsWorkordersOptions + '.mat-selected')
        if len(selectedPresets) == 0:
            workorders = await self.library_ctx.get_async_keyword_group('ElementKeywords').find_elements(self.settingsWorkordersOptions)
            await workorders[0].click()
        await self.click_off_element()
        sleep(.5)

    async def save_access_settings_changes(self):
        await self.library_ctx.get_async_keyword_group('ElementKeywords').click_element(self.settingsSaveButton)
        sleep(3)

    async def cancel_access_settings_changes(self):
        await self.library_ctx.get_async_keyword_group('ElementKeywords').click_element(self.settingsCancelButton)

    ##############################
    # Workorders Page
    ##############################
    async def browse_to_access_workorders(self):
        try:
            await self.library_ctx.get_async_keyword_group('ElementKeywords').element_should_be_visible(self.workordersMyTasksButton)
        except AssertionError:
            await self.library_ctx.get_async_keyword_group('ElementKeywords').click_element(self.workordersPageButton)
        finally:
            await self.library_ctx.get_async_keyword_group('WaitingKeywords').wait_until_page_contains('My Tasks')

    async def open_my_tasks(self):
        await self.library_ctx.get_async_keyword_group('ElementKeywords').click_element(self.workordersMyTasksButton)

    async def open_my_group_tasks(self):
        await self.library_ctx.get_async_keyword_group('ElementKeywords').click_element(self.workordersMyGroupTasksButton)

    async def open_all_unassigned_tasks(self):
        await self.library_ctx.get_async_keyword_group('ElementKeywords').click_element(self.workordersAllUnassignedTasksButton)

    async def get_visible_workorder_jobs_for_task(self, presetname: str):
        tasks = await self.library_ctx.get_current_page().querySelectorAll_with_selenium_locator(self.workordersTableTask+f"[testinfo='{presetname}'] "+self.workordersTableJob.strip('css:'))
        jobs = []
        for task in tasks:
            jobname = await task.executionContext.evaluate('element => element.innerText', task)
            jobid = await self.get_attribute(task, 'testinfo')
            print(f'task name: {jobname.splitlines()[0]}, task id: {jobid}')
            jobs.append({"name":jobname.splitlines()[0], "id": jobid})
        return jobs

    async def get_workorder_table_job_details(self, presetname: str = None, jobindex: int = None, jobid: str = None):
        if not jobid:
            tasks = await self.library_ctx.get_current_page().querySelector_with_selenium_locator(self.workordersTableTask+f"[testinfo='{presetname}']")
            jobid = await tasks.querySelectorAllEval(self.workordersTableJob.strip('css:'), f'element => element[{jobindex if jobindex else 0}].getAttribute("testinfo")')
        jobElement = await self.library_ctx.get_current_page().querySelector_with_selenium_locator(self.workordersTableJob+f"[testinfo='{jobid}']")
        jobname = await (await jobElement.getProperty('innerText')).jsonValue()
        jobname = jobname.splitlines()[0]
        return {"name":jobname, "id":jobid}

    async def open_workorder_by_job_id(self, jobid: str):
        await self.library_ctx.get_async_keyword_group('ElementKeywords').click_element(f"css:[testinfo='{jobid}']")
        await self.wait_for_qc_event_tree_to_load()

    async def open_workorder_by_preset_and_asset_name(self, presetname: str, assetname: str):
        jobs = await self.get_visible_workorder_jobs_for_task(presetname)
        for job in jobs:
            if assetname in job['name']:
                await self.library_ctx.get_async_keyword_group('ElementKeywords').click_element(
                    f"css:[testinfo='{job['id']}']")
                await self.wait_for_qc_event_tree_to_load()
                break
            else:
                continue

    ##############################
    # Metadata Page
    ##############################
    async def wait_for_qc_event_tree_to_load(self, timeout: int = 30):
        await self.library_ctx.get_async_keyword_group('WaitingKeywords').wait_until_page_contains_element(self.metadataQcEventCategory, timeout)

    async def browse_to_workorder_metadata(self):
        await self.library_ctx.get_async_keyword_group('ElementKeywords').click_element(self.workorderMetadataButton)
        await self.wait_for_qc_event_tree_to_load()

    async def save_workorder_changes(self, savedelay: int = 5):
        await self.library_ctx.get_async_keyword_group('ElementKeywords').click_element(self.workorderSaveButton)
        await self.library_ctx.get_async_keyword_group('WaitingKeywords').wait_until_element_is_hidden("css:.mat-spinner", timeout=30)
        sleep(savedelay)

    async def get_qc_event_tree_categories(self):
        categoryDicts = {}
        categories = await self.library_ctx.get_current_page().querySelectorAll_with_selenium_locator(self.metadataQcEventCategory)
        for category in categories:
            name = await self.get_attribute(category, 'testinfo')
            parent = await self.get_attribute(category, 'testparent')
            level = int(await category.executionContext.evaluate(f'element => element.parentElement.getAttribute("ng-reflect-level")', category))
            categoryDicts.setdefault(level, [])
            categoryDicts[level].append({"name":name, "parent":parent})
        return categoryDicts

    async def collapse_all_event_categories(self):
        categoryDicts = await self.get_qc_event_tree_categories()
        for level in reversed(categoryDicts):
            for category in categoryDicts[level]:
                print(f'collapsing category: {level}.{category["name"]}')
                try:
                    await self.library_ctx.get_async_keyword_group('ElementKeywords').click_element(
                        self.metadataQcEventCategory+f"[testinfo='{category['name']}'] [testtag='qc-category-collapse']")
                except Exception as e:
                    print(f'Encountered error: {e}')
                    pass
        sleep(.5)

    async def expand_all_event_categories(self):
        categoryDicts = await self.get_qc_event_tree_categories()
        for level in categoryDicts:
            for category in categoryDicts[level]:
                print(f'expanding category: {level}.{category["name"]}')
                try:
                    await self.library_ctx.get_async_keyword_group('ElementKeywords').click_element(
                        self.metadataQcEventCategory+f"[testinfo='{category['name']}'] [testtag='qc-category-expand']")
                except Exception as e:
                    print(f'Encountered error: {e}')
                    pass
        sleep(.5)

    async def expand_event_category(self, category: str):
        try:
            await self.library_ctx.get_async_keyword_group('ElementKeywords').element_should_be_visible(
                self.metadataQcEventCategory+f"[testinfo='{category}']")
        except AssertionError as e:
            print(f'Category: {category} failed with {e}')
            parentCat = await self.library_ctx.get_async_keyword_group('JavascriptKeywords').execute_javascript(
                f"document.querySelector(\"[testtag='qc-category'][testinfo='{category}']\").getAttribute('testparent')")
            await self.expand_event_category(parentCat)
        finally:
            try:
                await self.library_ctx.get_async_keyword_group('ElementKeywords').click_element(
                    self.metadataQcEventCategory + f"[testinfo='{category}'] [testtag='qc-category-expand']")
            except:
                pass

    async def select_event_by_event_title(self, category: str, title: str):
        await self.expand_event_category(category)
        try:
            await self.library_ctx.get_async_keyword_group('JavascriptKeywords').execute_javascript(
                f"document.querySelector(\"[testtag='qc-category'][testinfo='{category}']\").querySelector(\"[testtag='qc-event'][testinfo='{title}']:not(.selected)\").querySelector(\"[testtag='qc-event-select']\").click()"
            )
        except Exception as e:
            print(f'Unable to select due to {e}')

    async def deselect_event_by_event_title(self, category: str, title: str):
        await self.expand_event_category(category)
        try:
            await self.library_ctx.get_async_keyword_group('JavascriptKeywords').execute_javascript(
                f"document.querySelector(\"[testtag='qc-category'][testinfo='{category}']\").querySelector(\"[testtag='qc-event'][testinfo='{title}'].selected\").querySelector(\"[testtag='qc-event-select']\").click()"
            )
        except Exception as e:
            print(f'Unable to deselect due to {e}')

    async def edit_event_by_event_title(self, category: str, title: str):
        await self.expand_event_category(category)
