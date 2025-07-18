# Development Workflow

## Branching Strategy
- Use `main` for stable releases
- Use `dev` for ongoing development
- Feature branches: `feature/<name>`
- Bugfix branches: `bugfix/<name>`
- Pull requests required for merging to `main`

## CI/CD Pipeline
- Automated tests on push and pull requests
- Linting and formatting checks
- Build and deploy scripts for releases
- Use GitHub Actions for automation

## Code Review Process
- All changes via pull requests
- At least one reviewer required
- Use comments for feedback
- Ensure tests pass before merging

## Issue Tracking
- Use GitHub Issues for bugs/features
- Label issues for priority and type
- Assign issues to contributors

## Release Process
- Update `CHANGELOG.md`
- Tag releases in Git
- Announce new releases in documentation
