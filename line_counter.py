import requests
from github import Github

GITHUB_TOKEN = "naughty naughty"
ORG_NAME = 'ClashKingInc'

g = Github(GITHUB_TOKEN)
org = g.get_organization(ORG_NAME)

total_loc = {}

# Iterate through all repositories in the organization
for repo in org.get_repos():
    repo_name = repo.full_name.split('/')[-1]
    print(repo_name)
    api_url = f"https://api.codetabs.com/v1/loc?github={ORG_NAME}/{repo_name}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        for entry in data:
            language = entry["language"]
            lines_of_code = entry["linesOfCode"]

            if language not in total_loc:
                total_loc[language] = 0

            total_loc[language] += lines_of_code

    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve data for {repo_name}: {e}")

for language, loc in total_loc.items():
    print(f"{language}: {loc} lines of code")