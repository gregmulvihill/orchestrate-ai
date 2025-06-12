# Branch Protection Configuration

This branch contains a GitHub Actions workflow for setting up branch protection rules for the CogentEcho.ai repositories.

## Branch Protection Rules

The workflow sets up the following protection rules for the main branch:

1. Require pull request reviews before merging
2. Dismiss stale pull request approvals when new commits are pushed
3. Require at least 1 approving review
4. Include administrators in the protection rules

## How to Use

1. Merge this branch to the main branch
2. Go to the "Actions" tab in the repository
3. Select the "Set Branch Protection" workflow
4. Click "Run workflow" and confirm
5. The workflow will set up branch protection for the main branch

## Apply to Other Repositories

To apply similar branch protection to other repositories in the CogentEcho.ai ecosystem:

1. Copy the `.github/workflows/set-branch-protection.yml` file to each repository
2. Update the owner and repo values in the workflow file if needed
3. Run the workflow in each repository

## Repositories Requiring Protection

- [Orchestrate-AI](https://github.com/gregmulvihill/orchestrate-ai)
- [Automated-Dev-Agents](https://github.com/gregmulvihill/automated-dev-agents)
- [Multi-Tiered Memory Architecture](https://github.com/gregmulvihill/multi-tiered-memory-architecture)
- [MCP-Manager](https://github.com/gregmulvihill/mcp-manager)

## Verification

After running the workflow, verify the branch protection settings by:

1. Going to Settings > Branches in each repository
2. Checking that the main branch has protection rules enabled
