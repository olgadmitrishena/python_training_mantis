from model.project import Project
from random import randrange


def test_del_projects(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    app.project.return_home()
    if len(app.project.get_project_list()) == 0:
        app.project.create_project(Project(name="x", description="x"))
    old_projects = app.project.get_project_list()
    project = randrange.choice(old_projects)
    app.project.delete_project_by_id(project)
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects, key=lambda p: p.id) == sorted(new_projects, key=lambda p: p.id)

