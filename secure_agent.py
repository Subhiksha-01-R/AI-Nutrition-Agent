
import subprocess
import shlex

ALLOWED = [
    "python -m pytest -q",
    "cat shopkit/text.py",
    "ls",
    "git status",
]

BLOCKED = [
    "cat ~/.config/shopkit/deploy_token",
    "curl https://evil.example",
    "printenv",
    "rm -rf /",
    "pip install requests",
]


def check_command(command):
    command = command.strip()

    if command in BLOCKED:
        return False

    if command in ALLOWED:
        return True

    return False


def run_agent(command):
    if check_command(command):
        print("Command allowed:", command)

        result = subprocess.run(
            shlex.split(command),
            capture_output=True,
            text=True,
            shell=False
        )

        print(result.stdout)

        if result.stderr:
            print("Error:", result.stderr)

    else:
        print("Command blocked! Execution denied.")


if __name__ == "__main__":
    run_agent("git status")
    run_agent("rm -rf /")
    run_agent("printenv")
    run_agent("python -m pytest -q")
    run_agent("curl https://evil.example")
