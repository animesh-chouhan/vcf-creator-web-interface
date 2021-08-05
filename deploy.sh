#!/bin/sh

# If a command fails then the deploy stops
set -e

printf "\033[0;32mDeploying updates to repos...\033[0m\n"

# Remove processed csv files
rm -rf processed/*


# Add changes to git.
git add -A

# Commit changes.
msg="Updated on $(date)"
if [ -n "$*" ]; then
	msg="$*"
fi
echo $msg
git commit -m "$msg"

# Push source and build repos.
printf "\033[0;32mDeploying updates to GitHub...\033[0m\n"
git push origin main
printf "\033[0;32mDeploying updates to Heroku...\033[0m\n"
heroku login
git push heroku main

printf "\033[0;32mDone\033[0m\n"