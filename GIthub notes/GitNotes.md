## [Remote](https://gist.github.com/alifhasnain/68890cd026f54c7960b0d42bc25ebba0#remote)

#### Add new remote
`git remote add <origin_name> <url_of_the_remote_repo>`

#### Update existing remote
`git remote set-url <origin> <url_of_the_remote_repo>`

#### To see remotes names
`git remote`

#### To see remotes with source url
`git remote -v`

#### Update a remote name
`git remote rename <current_remote_name> <updated_remote_name>`

#### Delete a remote
`git remove <remote_name>`


## [Fetch/Pull/Merge](https://gist.github.com/alifhasnain/68890cd026f54c7960b0d42bc25ebba0#fetchpullmerge)

#### Fetch remote tracking branch without merging
`git fetch <remote_name>`

#### Fetch the latest upstream from a branch
`git fetch <remote_name> <branch_name>`

#### Merge with the upstream that was fetched locally
`git merge <remote_name>/<branch_name>`

#### Rebase (Same as merge but without the merge commit)
`git rebase <branch_name>`

#### Pulls the latest upstream from remote (Fetches & then merges)
`git pull`

`git pull <remote_name>`

`git pull <remote_name> <branch_name>`

`git pull origin master` fetches commits from the master branch of the origin remote (into the local origin/master branch), and then it merges origin/master into the branch you currently have checked out.

`git pull` only works if the branch you have checked out is tracking an upstream branch. For example, if the branch you have checked out tracks origin/master, `git pull` is equivalent to `git pull origin master`

#### Merge without checkout
```
# Merge remote branch origin/foo into local branch foo,
# without having to checkout foo first:
git fetch origin foo:foo
```

## [Branch](https://gist.github.com/alifhasnain/68890cd026f54c7960b0d42bc25ebba0#branch)

#### List branches
`git branch -a`

#### Switch to existing branch
`git checkout <existing_branch>`

#### Switch & create new branch if doesn't exist
`git checkout -b <branch_name>`

#### Switch to a specific commit
`git checkout <commit_hash>`

#### Create new branch from a commit/branch (when current head is at a specific commit / branch)
`git switch -c "in-app-messaging-fix"`

#### Clone a branch
`git clone -b <branch_name> <remote_repo>`

#### Delete a branch locally
`git branch -d <branchname>`

#### Clone a specific branch (skips fetching other branches on this repo)
`git clone -b <branch_name> --single-branch <remote_repo>`

#### Delete a local branch
 - [Non-Force] `git branch -d <branch_name>`
 - [Force] `git branch -D <branch_name>`
 
 #### Delete a remote branch
 `git push <remote_name> --delete <branch_name>`
 
  or
 
 `git push <remote_name> :<branch_name>`


## [Cache](https://gist.github.com/alifhasnain/68890cd026f54c7960b0d42bc25ebba0#cache)

#### Clear cache for specific file
`git rm --cached filename`

#### Clear your entire Git cache
`git rm -r --cached .`

## [Miscellaneous](https://gist.github.com/alifhasnain/68890cd026f54c7960b0d42bc25ebba0#miscellaneous)

#### Shows last commit history
`git log`

`git log -<number_of_history>`

`git log --oneline`

#### Related to `git log` or `git diff`
`q` to exit and `z` to navigate next page

#### Shows diff comparing last commit
`git diff`

`git commit --amend`

`git log --graph`