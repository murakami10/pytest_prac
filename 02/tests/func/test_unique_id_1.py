import tasks
from tasks import Task

import pytest


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    tasks.start_tasks_db(str(tmpdir), "tiny")

    yield

    tasks.stop_tasks_db()


@pytest.mark.xfail(
    tasks.__version__ < "0.2.0",
    reason="not supported until version 0.2.0",
)
def test_unique_id_1():
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2


def test_unique_id_2():
    ids = []
    ids.append(tasks.add(Task("one")))
    ids.append(tasks.add(Task("two")))
    ids.append(tasks.add(Task("three")))

    uid = tasks.unique_id()

    assert uid not in ids
