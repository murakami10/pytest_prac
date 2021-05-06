import tasks
from tasks import Task

import pytest


@pytest.fixture(scope="session", params=["tiny", "mongo"])
def tasks_db_session(tmpdir_factory, request):
    temp_dir = tmpdir_factory.mktemp("temp")
    tasks.start_tasks_db(str(temp_dir), request.param)
    yield
    tasks.stop_tasks_db()


@pytest.fixture()
def tasks_db(tasks_db_session):
    tasks.delete_all()


@pytest.fixture(scope="session")
def tasks_just_a_few():
    return (
        Task("Writesomecode", "Brian", True),
        Task("CodereviewBrian'scode", "Katie", False),
        Task("FixwhatBriandid", "Michelle", False),
    )


@pytest.fixture(scope="session")
def tasks_mult_per_owner():
    return (
        Task("Makeacookie", "Raphael"),
        Task("Useanemoji", "Raphael"),
        Task("MovetoBerlin", "Raphael"),
        Task("Create", "Michelle"),
        Task("Inspire", "Michelle"),
        Task("Encourage", "Michelle"),
        Task("Doahandstand", "Daniel"),
        Task("Writesomebooks", "Daniel"),
        Task("Eaticecream", "Daniel"),
    )


@pytest.fixture()
def db_with_3_tasks(tasks_db, tasks_just_a_few):
    for t in tasks_just_a_few:
        tasks.add(t)


@pytest.fixture()
def db_with_multi_per_owner(tasks_db, tasks_mult_per_owner):
    for t in tasks_mult_per_owner:
        tasks.add(t)
