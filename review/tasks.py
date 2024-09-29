from celery import shared_task
from .github_utils import fetch_code_from_github
from .run_analysis import run_flake8_analysis, run_pylint_analysis, run_bandit_analysis
import os



@shared_task
def analyze_code(repo_url):
    code_dir = fetch_code_from_github(repo_url)

    analysis_results = {}

    for root, dirs, files in os.walk(code_dir):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                flake8_results = run_flake8_analysis(file_path)
                pylint_results = run_pylint_analysis(file_path)
                bandit_results = run_bandit_analysis(file_path)

                analysis_results[file] = {
                    'flake8': flake8_results,
                    'pylint': pylint_results,
                    'bandit': bandit_results,
                }

    return analysis_results

