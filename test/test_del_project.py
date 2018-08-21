from model.project import Project
import random

def test_del_project(app):
    app.session.login("administrator", "root")
    app.project.open_projects_page()
    old_projects = app.project.get_projects_list()
    project = random.choice(old_projects)
    app.project.delete_random_project(project)
    new_projects = app.project.get_projects_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(new_projects, key=lambda p: p.name) == sorted(old_projects, key=lambda p: p.name)

