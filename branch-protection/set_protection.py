# Python script to set up branch protection for all CogentEcho.ai repositories
import requests
import json
import os
import sys

def set_branch_protection(token, owner, repo, branch="main"):
    """
    Set branch protection rules using GitHub API.
    
    Args:
        token (str): GitHub personal access token with repo permissions
        owner (str): Repository owner/organization name
        repo (str): Repository name
        branch (str): Branch name to protect (default: "main")
    
    Returns:
        bool: True if successful, False otherwise
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/branches/{branch}/protection"
    
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    
    # Branch protection settings
    data = {
        "required_status_checks": None,
        "enforce_admins": True,
        "required_pull_request_reviews": {
            "dismissal_restrictions": {},
            "dismiss_stale_reviews": True,
            "require_code_owner_reviews": False,
            "required_approving_review_count": 1
        },
        "restrictions": None
    }
    
    # Make API request
    try:
        response = requests.put(url, headers=headers, json=data)
        response.raise_for_status()
        print(f"✅ Branch protection set for {owner}/{repo}/{branch}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to set branch protection for {owner}/{repo}/{branch}: {e}")
        return False

def main():
    # Check for GitHub token
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Error: GitHub token not found. Set the GITHUB_TOKEN environment variable.")
        print("Example: export GITHUB_TOKEN=your_token_here")
        sys.exit(1)
    
    # List of CogentEcho.ai repositories
    repositories = [
        {"owner": "gregmulvihill", "repo": "orchestrate-ai"},
        {"owner": "gregmulvihill", "repo": "automated-dev-agents"},
        {"owner": "gregmulvihill", "repo": "multi-tiered-memory-architecture"},
        {"owner": "gregmulvihill", "repo": "mcp-manager"}
    ]
    
    # Set branch protection for each repository
    success_count = 0
    for repo_info in repositories:
        success = set_branch_protection(
            token=token,
            owner=repo_info["owner"],
            repo=repo_info["repo"]
        )
        if success:
            success_count += 1
    
    # Print summary
    print(f"\nBranch protection set for {success_count}/{len(repositories)} repositories")

if __name__ == "__main__":
    main()
