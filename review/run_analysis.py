import subprocess

def run_flake8_analysis(code_path):
    try:
        return subprocess.run(["flake8", code_path], capture_output=True, text=True).stdout
    except Exception as e:
        return str(e)

def run_pylint_analysis(code_path):
    try:
        return subprocess.run(["pylint", code_path], capture_output=True, text=True).stdout
    except Exception as e:
        return str(e)

def run_bandit_analysis(code_path):
    try:
        return subprocess.run(["bandit", "-r", code_path], capture_output=True, text=True).stdout
    except Exception as e:
        return str(e)