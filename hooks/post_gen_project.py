from . import formatters
from . import git
from . import vscode

if __name__ == "__main__":
    print("Running post-gen hooks...")
    try:
        print(" 🟦 Formatting generated code...")
        formatters.run_formatters()
        print(" ✅ Formatted!")
    except Exception:  # noqa
        print(" ❌ Failed to format code!")
    if git.check_how_many_commits_exist() == 0:
        print(" 🟦 Creating git repo...")
        git.create_repo()
        print(" ✅ Created!")
        print(" 🟦 Committing all updates...")
        git.create_initial_commit()
        print(" ✅ Committed!")
    else:
        print(" 🟦 Committing all updates...")
        git.create_next_commit()
        print(" ✅ Committed!")

    print(" 🟦 Copying VSCode settings...")
    vscode.copy_default_files()
    print(" ✅ Copied!")
