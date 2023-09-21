from src.{{ cookiecutter.package_name }} import main


def test_example():
    assert 1 == 1


def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello from {{ cookiecutter.project_name }}!" in captured.out

