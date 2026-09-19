
## Assignment 3 – `.gitignore` + `git rm --cached`

**Goal:** Properly ignore sensitive files and practice stopping Git from tracking a file using `git rm --cached`.

1. Create a file named `config.env` with sample secret data:
```env
DB_PASSWORD=SuperSecretPass999
API_KEY=sk-test-abc123xyz789
```

2. **Intentionally** add and commit it (to practice the fix):
```bash
git add config.env
git commit -m "Accidentally commit config.env"
```

3. Create a folder named `vendor` and put any dummy file inside it.

4. Create a `.gitignore` file and add:
```gitignore
vendor/
config.env
```

5. Stop tracking `config.env` but **keep the file on your computer**:
```bash
git rm --cached config.env
```

6. Run `git status` and observe that `config.env` is staged for removal from Git (but the file still exists locally).

7. Commit the fix:
```bash
git add .gitignore
git commit -m "Stop tracking config.env and add .gitignore"
git push origin main
```

8. Confirm on GitHub that `config.env` is **no longer visible** in the repository, while the file still exists on your local machine.

9. Create a file named `why-gitignore.txt` and answer:
- Why should we ignore folders like `vendor` or `node_modules`?
- Why should we ignore files like `config.env` or `.env`?
- What does `git rm --cached` do?
- Why should we **not** add `.gitignore` inside `.gitignore`?

**Submit:**
- Screenshot of `git status` after using `git rm --cached`
- Screenshot showing that `config.env` is ignored / removed from GitHub
- Content of `why-gitignore.txt`
- Repository link (make sure `config.env` is **not** visible on GitHub)

---
[repo link](https://github.com/AyushSharma2007/githubass15.git)
<img width="1367" height="591" alt="git15-03 (3)" src="https://github.com/user-attachments/assets/49fd6f38-4971-4ecd-85a9-77426b932ef7" />
<img width="1003" height="402" alt="git15-03 (2)" src="https://github.com/user-attachments/assets/30166ccf-9e96-4b71-99a6-59208e8d9d8b" />
<img width="1347" height="503" alt="git15-03" src="https://github.com/user-attachments/assets/1461abf5-7709-4841-9111-a7e2b1f68590" />
