import subprocess


def _run_black():
    subprocess.run(["black", "."])


def _run_ruff():
    subprocess.run(["ruff", "--fix", "."])


def run_formatters():
    _run_black()
    _run_ruff()
