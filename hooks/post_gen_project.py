from hooks import git
from hooks import vscode

if __name__ == "__main__":
    git.create_repo()
    git.commit_everything()
    vscode.copy_default_files()
