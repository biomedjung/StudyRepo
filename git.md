Repo = repository = folder tracked by git
# Comandos Git 
git --version
git config --global user.name xxxx
git config --global user.email xxxxx@gmail.com
git config user.name (or email to confirm)
cd ..
ls (to list)
mkdir
touch index.html (create the file)
Atom  index.html (to open on Atom)
rm index.html (remove)
rmdir test (remove test dir)

git init

git status (avalia o que está em qual estágio)

modified (green at Atom)

staged
git add index.html (staged)
git add . (add everything to staged)

commit = save point 
git commit (commit in logical points)
git rm --cached index.html (remove da área de staging)

git commit -m "fixed bug in header"  (-m messege)

git log (show record)
git log --oneline (resumido)

git checkout d8bc7eb 
git checkout master (volta)

Desfazendo problemas:
git revert d8bc7eb
wq na tela, enter

git reset d8bc7eb (não apaga, mas não está mais commited)
git reset d8bc7eb --hard (não leva em consideração o que foi mudado depois, posso reset o reset)

# Branches
MASTER - The first branch - the stable version
fork, then merge, can make multiple branches
git branch feature-1 (name of the branch) make branch
git branch -a (show the branches)
git checkout 'feature-1' (be on the branch)
work ond the branch the same way as in the MASTER
gith checkout 'master' (back to master)
git branch -d 'feature-1' (only once merged)
git branch -D 'feature-1' (delete)
git checkout -b 'feature-b' (makes new branch and change to it)
git merge feature-b

github
git clone https://github.com/biomedjung/mitocondria.git (link do repo no github - comando na pasta a ser clonada)

code . (abre visual studio)



## Conflicts
DONT EDIT THE MASTER

___
```
clone - duplicate repository that is alocated somewhere like github
push - upload commits to remote repo (github) 
pull - download changes from remote repo
