import random
import os


def random_string(num, folder="config", filename="config.txt"):
    # Ensure the folder exists
    if not os.path.exists(folder):
        os.makedirs(folder)

    file_path = os.path.join(folder, filename)
    with open(file_path, "w") as f:
        for i in range(num):
            f.write(chr(random.randint(32, 126)))  # Using printable characters


def git_branch(branch_name, checkout=False):
    os.system("git branch " + branch_name)
    if checkout:
        os.system("git checkout " + branch_name)


def git_commit(commit_name):
    os.system("git add .")
    os.system(f"git commit -m '{commit_name}'")  # Add quotes around commit name
    os.system("git push")


def remove_branch(branch_name):
    os.system("git branch -D " + branch_name)


def main():
    # for i in range(10):
    #     branch_name = "branch" + str(i)
    #     git_branch(branch_name, True)
    #     for j in range(10):
    #         random_string(1000)
    #         commit_msg = f"{branch_name} commit {j}"
    #         git_commit(commit_msg)
    # os.system("git checkout master")

    for i in range(10):
        remove_branch("branch" + str(i))


main()

