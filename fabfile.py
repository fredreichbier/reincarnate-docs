from fabric.api import run

def regenerate():
    run('make html')
