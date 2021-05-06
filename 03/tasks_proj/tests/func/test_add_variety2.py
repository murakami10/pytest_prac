import tasks
from tasks import Task

import pytest

tasks_to_try = (
    Task("sleep", done=True),
    Task("wake", "brian"),
    Task("breathe", "BRIAN", True),
    Task("exercise", "BrIaN", False),
)
task_ids = [f"Task({t.summary},{t.owner},{t.done})" for t in tasks_to_try]


def equivalent(t1, t2):
    return (
        (t1.summary == t2.summary) and (t1.owner == t2.owner) and (t1.done == t2.done)
    )


@pytest.fixture(params=tasks_to_try)
def a_task(request):
    return request.param


def test_add_a(tasks_db, a_task):
    task_id = tasks.add(a_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, a_task)


@pytest.fixture(params=tasks_to_try, ids=task_ids)
def b_task(request):
    return request.param


def test_add_b(tasks_db, b_task):
    task_id = tasks.add(b_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, b_task)


@pytest.fixture(
    params=tasks_to_try,
    ids=lambda fixture_value: f"Task({fixture_value.summary},{fixture_value.owner},{fixture_value.done})",
)
def c_task(request):
    return request.param


def test_add_c(tasks_db, c_task):
    task_id = tasks.add(c_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, c_task)
