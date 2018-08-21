from model.project import Project

class ProjectHelper:


    def __init__(self, app):
        self.app = app

    def open_projects_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_proj_page.php"):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    def create_new_project(self, project):
        wd = self.app.wd
        self.open_projects_page()
        self.open_new_project_page()
        self.fill_new_project_form(project)
        wd.find_element_by_css_selector("input[value='Add Project']").click()
        wd.find_element_by_link_text("Proceed").click()

    def fill_new_project_form(self, project):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_xpath("//select[@name='status']/option[@value='%d']" % project.status).click()
        wd.find_element_by_xpath("//select[@name='view_state']/option[@value='%d']" % project.view_state).click()
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)


    def open_new_project_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()


    def get_project_list(self):
        wd = self.app.wd
        self.open_projects_page()
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

    def tmp_print(self, l):
        print('\n')
        lst = sorted(l, key=Project.id_or_max)
        for li in lst:
            print("project " + str(li))


    def delete_random_project(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_link_text("%s" % project.name).click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()