from invoke import task, Context
from typing import Optional


DOCKER_EXEC = "docker compose exec dev"


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def run(
        ctx: Context,
        cmd: str,
        print_terminal: bool = True,
        container: bool = False,
) -> None:
    
    if container:
        cmd_exec = f"{DOCKER_EXEC} {cmd}"
    else:
        cmd_exec = cmd
    
    if print_terminal:
        print(f"{bcolors.OKBLUE}{cmd_exec}{bcolors.ENDC}")

    ctx.run(cmd_exec)



# Define a simple task that runs Django's migration

@task
def makemigrations(ctx):
    run(ctx,
        "python manage.py makemigrations",
        container=True,
        )

@task
def migrate(ctx):

    run(ctx,
        "python manage.py migrate",
        container=True,
        )

# Define a task to start the Django development server
@task
def runserver(ctx):
    print("Starting Django development server...")

    run(ctx,
        "python manage.py runserver 0.0.0.0:8000",
        container=True,
        )

@task
def build(ctx):
    ctx.run("docker compose build")

@task
def up(ctx):
    ctx.run("docker compose up -d")

@task
def down(ctx):
    ctx.run("docker compose down")

@task
def shell(ctx):
    run(ctx,
        "python manage.py shell",
        container=True,
    )