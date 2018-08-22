from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()

    def change_field_value_project(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value_project("name", project.name)
        self.change_field_value_project("description", project.description)

    def create_project(self, project):
        wd = self.app.wd
        self.return_home()
        self.open_project_page()
        # fill contact form
        self.fill_project_form(project)
        wd.find_element_by_css_selector("input[value='Add Project']").click()
        wd.find_element_by_link_text("Proceed").click()
        self.project_cache = None

    def delete_project_by_id(self, project):
        wd = self.app.wd
        self.return_home()
        wd.find_element_by_link_text("%s" % project.name).click()
        # submit delete
        wd.find_element_by_link_text("Delete Project").click()
        wd.find_element_by_link_text("Delete Project").click()
        self.return_home()
        self.project_cache = None

    def return_home(self):
        wd = self.app.wd
        if not wd.current_url.endswith("//manage_proj_page.php"):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()
    project_cache = None


    def get_project_list(self):
        wd = self.app.wd
        self.open_project_page()
        project_cache = []
        for row in wd.find_elements_by_css_selector("table.width100 tr.row-1"):
            cells = row.find_elements_by_css_selector("td")
            name = cells[0].text
            project_cache.append(Project(name=name))
        for row in wd.find_elements_by_css_selector("table.width100 tr.row-2"):
            cells = row.find_elements_by_css_selector("td")
            name = cells[0].text
            project_cache.append(Project(name=name))
        return list(project_cache)