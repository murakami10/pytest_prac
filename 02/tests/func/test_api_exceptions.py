import tasks

import pytest


def test_add_raises():
    with pytest.raises(TypeError):
        tasks.add(task="not a Task object")


def test_start_db_raises():
    with pytest.raises(ValueError) as excinfo:
        tasks.start_tasks_db("some/great/path", "mysql")
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "db_type must be a 'tiny' or 'mongo'"


@pytest.mark.smoke
def test_list_tasks_raises():
    with pytest.raises(TypeError):
        tasks.list_tasks(owner=123)


@pytest.mark.get
@pytest.mark.smoke
def test_get_raises():
    with pytest.raises(TypeError):
        tasks.get(task_id=TypeError)
        tasks.get(task_id="123")
