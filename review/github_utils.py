from github import Github
import os


def fetch_code_from_github(repo_url, branch='main'):
    g = Github("YOUR_GITHUB_ACCESS_TOKEN")
    repo = g.get_repo(repo_url)
    contents = repo.get_contents("", ref=branch)


    local_repo_dir = f'/tmp/{repo.name}'
    os.makedirs(local_repo_dir, exist_ok=True)


    for content_file in contents:
        if content_file.type == 'file':
            file_content = content_file.decoded_content.decode('utf-8')
            file_path = os.path.join(local_repo_dir, content_file.path)

            with open(file_path, 'w') as f:
                f.write(file_content)

    return local_repo_dir


