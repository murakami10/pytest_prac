from tasks import Task


def test_asdict():
    t_task = Task("do something", "okken", True, 21)
    t_dict = t_task._asdict()
    expect = {
        "summary": "do something",
        "owner": "okken",
        "done": True,
        "id": 21,
    }
    assert t_dict == expect


def test_replace():
    t_before = Task("finish book", "brian", False)
    t_after = t_before._replace(id=10, done=True)
    t_expect = Task("finish book", "brian", True, 10)
    assert t_after == t_expect
