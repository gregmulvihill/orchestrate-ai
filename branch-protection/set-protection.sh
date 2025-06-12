#!/bin/bash
# Script to set up branch protection for CogentEcho.ai repositories

# Define repositories
REPOS=(
  "gregmulvihill/orchestrate-ai"
  "gregmulvihill/automated-dev-agents"
  "gregmulvihill/multi-tiered-memory-architecture"
  "gregmulvihill/mcp-manager"
)

# Define branch protection settings in JSON format
PROTECTION_SETTINGS='{
  "required_status_checks": null,
  "enforce_admins": true,
  "required_pull_request_reviews": {
    "dismissal_restrictions": {},
    "dismiss_stale_reviews": true,
    "require_code_owner_reviews": false,
    "required_approving_review_count": 1
  },
  "restrictions": null
}'

# Loop through repositories and set branch protection
for REPO in "${REPOS[@]}"; do
  echo "Setting branch protection for $REPO..."
  
  # Extract owner and repo name
  OWNER=$(echo $REPO | cut -d '/' -f 1)
  REPO_NAME=$(echo $REPO | cut -d '/' -f 2)
  
  # Set branch protection using GitHub API
  curl -X PUT \
    -H "Accept: application/vnd.github+json" \
    -H "Authorization: Bearer $GITHUB_TOKEN" \
    -H "X-GitHub-Api-Version: 2022-11-28" \
    "https://api.github.com/repos/$REPO/branches/main/protection" \
    -d "$PROTECTION_SETTINGS"
  
  echo "Branch protection set for $REPO"
done

echo "Branch protection has been set for all repositories."
