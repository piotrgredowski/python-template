import os
import subprocess

THIS_REPO_NAME = "python-template"
THIS_REPO_URL = "https://github.com/piotrgredowski/python-template"


def create_repo():
    p = subprocess.Popen("git init -b main".split(" "))
    p.wait()


def get_commit_id_of_template_repo():
    old_path = os.getcwd()
    os.chdir(os.getenv("PWD", ""))
    commit_id = subprocess.check_output("git rev-parse HEAD", shell=True).decode("utf-8").strip()
    os.chdir(old_path)
    return commit_id


def get_commit_message():
    commit_message = "Initial commit"
    commit_id = get_commit_id_of_template_repo()

    if commit_id:
        commit_message += f"""

Automatically created from: [{THIS_REPO_NAME}]({THIS_REPO_URL}).
Source commit: {commit_id[:10]}
"""
    return commit_message


def commit_everything():
    p = subprocess.Popen(["git", "add", "."])
    p.wait()

    p = subprocess.Popen(["git", "commit", "-n", "-m", get_commit_message()])
    p.wait()
