import subprocess
import black
import ruff


def _run_black():
    black.main(".")


def _run_ruff():
    subprocess.run(["ruff", "--fix", "."])


def run_formatters():
    _run_black()
    _run_ruff()
