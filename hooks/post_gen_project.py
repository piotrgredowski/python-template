from hooks import formatters
from hooks import git
from hooks import vscode

if __name__ == "__main__":
    print("Running post-gen hooks...")
    print(" ▶️ Creating git repo...")
    git.create_repo()
    print(" ▶️ Commiting all files...")
    git.commit_everything()
    print(" ▶️ Copying VSCode default files...")
    vscode.copy_default_files()
    print(" ▶️ Formatting generated code...")
    try:
        formatters.run_formatters()
    except Exception:  # noqa
        print(" ❌ Failed to format code!")
