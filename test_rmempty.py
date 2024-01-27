from click.testing import CliRunner

from rmempty.__main__ import cli

runner = CliRunner()


def test_rmempty(tmp_path):
    dir = tmp_path / "dir"
    dir.mkdir()
    (dir / "sub").mkdir()

    assert (tmp_path / "dir").exists()
    assert (tmp_path / "dir" / "sub").exists()

    result = runner.invoke(cli, [str(tmp_path)])

    assert result.exit_code == 0

    assert not (tmp_path / "dir" / "sub").exists()
    assert not (tmp_path / "dir").exists()
