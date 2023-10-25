import os
import pathlib
import subprocess

THIS_REPO_NAME = "python-template"
THIS_REPO_URL = "https://github.com/piotrgredowski/python-template"


def _run_black():
    subprocess.run(["black", "."])


def _run_ruff():
    subprocess.run(["ruff", "--fix", "."])


def run_formatters():
    _run_black()
    _run_ruff()


def create_repo():
    p = subprocess.Popen("git init -b main".split(" "))
    p.wait()


def check_how_many_commits_exist():
    p = subprocess.Popen("git rev-list --all --count".split(" "), stdout=subprocess.PIPE)
    if not p.stdout:
        return 0
    output = p.stdout.read().decode("utf-8").strip()

    try:
        return int(output)
    except ValueError:
        return 0


def get_commit_id_of_template_repo():
    old_path = os.getcwd()
    os.chdir(os.getenv("PWD", ""))
    commit_id = subprocess.check_output("git rev-parse HEAD", shell=True).decode("utf-8").strip()
    os.chdir(old_path)
    return commit_id


def get_commit_message(commit_message: str):
    commit_id = get_commit_id_of_template_repo()

    if commit_id:
        commit_message += f"""

Automatically created from: [{THIS_REPO_NAME}]({THIS_REPO_URL}).
Source commit: {commit_id[:10]}
"""
    return commit_message


def _add_all_files():
    p = subprocess.Popen(["git", "add", "."])
    p.wait()


def create_initial_commit():
    _add_all_files()

    p = subprocess.Popen(["git", "commit", "-n", "-m", get_commit_message("Initial commit")])
    p.wait()


def create_next_commit():
    _add_all_files()

    p = subprocess.Popen(["git", "commit", "-n", "-m", get_commit_message("Update template")])
    p.wait()


def copy_default_files():
    for file_ in pathlib.Path(".vscode").iterdir():
        if ".default" not in file_.name:
            continue
        new_file_name = file_.name.replace(".default", "")
        new_file = pathlib.Path(".vscode") / new_file_name
        new_file.write_text(file_.read_text())
        print(f"Created {new_file}")


if __name__ == "__main__":
    print("Running post-gen hooks...")
    try:
        print(" 🟦 Formatting generated code...")
        run_formatters()
        print(" ✅ Formatted!")
    except Exception:  # noqa
        print(" ❌ Failed to format code!")
    if check_how_many_commits_exist() == 0:
        print(" 🟦 Creating git repo...")
        create_repo()
        print(" ✅ Created!")
        print(" 🟦 Committing all updates...")
        create_initial_commit()
        print(" ✅ Committed!")
    else:
        print(" 🟦 Committing all updates...")
        create_next_commit()
        print(" ✅ Committed!")

    print(" 🟦 Copying VSCode settings...")
    copy_default_files()
    print(" ✅ Copied!")
