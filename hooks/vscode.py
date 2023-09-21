import pathlib


def copy_default_files():
    for file_ in pathlib.Path(".vscode").iterdir():
        if ".default" not in file_.name:
            continue
        new_file_name = file_.name.replace(".default", "")
        new_file = pathlib.Path(".vscode") / new_file_name
        new_file.write_text(file_.read_text())
        print(f"Created {new_file}")
