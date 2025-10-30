import os
import csv
import requests

# Resolve path relative to script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(SCRIPT_DIR, "attrition_user_stories.csv")

# Ask the user for necessary inputs
GITHUB_TOKEN = input("Enter your GitHub Personal Access Token: ")
REPO_OWNER = "illusio666"
REPO_NAME = "employee_attrition_analysis"

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def get_milestone_id(name):
    """Fetch milestone ID from GitHub based on title"""
    if not name:
        return None
    url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/milestones'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        for m in response.json():
            if m['title'].strip().lower() == name.strip().lower():
                return m['number']
    return None

def create_issue(title, body, labels, milestone_name, assignees):
    url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues'

    labels_list = [label.strip() for label in labels.split(',')] if labels else []
    assignees_list = [assignee.strip() for assignee in assignees.split(',')] if assignees else []
    milestone_id = get_milestone_id(milestone_name)

    data = {
        'title': title,
        'body': body,
        'labels': labels_list,
        'assignees': assignees_list
    }
    if milestone_id:
        data['milestone'] = milestone_id

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print(f'✅ Created: {title} | Labels: {labels_list} | Assignees: {assignees_list}')
    else:
        print(f'❌ Failed: {title} | {response.status_code} - {response.text}')

def import_issues(CSV_FILE):
    with open(CSV_FILE, newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Skip empty or malformed rows
            if not row['title'] or not row['body']:
                continue
            # Replace placeholder objectives if needed
            title = row['title'].replace('<objective', 'Objective').replace('>', '').strip()
            body = row['body'].replace('<objective', 'Objective').replace('>', '').strip()
            create_issue(title, body, row['labels'], row['milestone'], row['assignees'])

if __name__ == '__main__':
    import_issues(CSV_FILE)