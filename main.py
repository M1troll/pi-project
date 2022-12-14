from git.repo import Repo
from git import Remote
from local_config import BASE_DIR

repo = Repo(BASE_DIR)
repo.index.commit("First try to commit from python script")

origin = repo.remotes[0]
origin.push()


def commit(origin: Remote, message: str):
    """Make commit."""
    repo.index.commit("First try to commit from python script")

def main():
    """."""


if __name__ == "__main__":
    main()