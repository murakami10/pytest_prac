from . import cheese


def test_def_prefs_change_home(tmpdir, monkeypatch):
    fake_home_dir = tmpdir.mkdir("home")
    monkeypatch.setattr(
        cheese.os.path, "expanduser", (lambda x: x.replace("~", str(fake_home_dir)))
    )
    cheese.write_default_cheese_preferences()
    expected = cheese._default_prefs
    actual = cheese.read_cheese_preferences()
    assert expected == actual
