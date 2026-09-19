## Assignment 1 – Understanding HEAD and Basic Reset (Easy)

**Goal:** Practice viewing history and using a simple mixed reset.

1. Create or open your practice repository.
2. Make three simple commits (you can create/edit a file called `notes.txt`):
   - Commit 1: Add some text → commit message `"First note"`
   - Commit 2: Add more text → commit message `"Second note"`
   - Commit 3: Add more text → commit message `"Third note"`
3. Run:
   ```bash
   git log --oneline
   ```
4. Reset to the previous commit using:
   ```bash
   git reset HEAD~1
   ```
5. Run `git log --oneline` and `git status` again.
6. Observe what happened to the latest commit and the file changes.

**Submit:**
- Screenshot of `git log --oneline` **before** reset
- Screenshot of `git log --oneline` and `git status` **after** reset
- Repository link

---
[github repo](https://github.com/AyushSharma2007/gitass16.git)
<img width="1202" height="681" alt="git16-01 (2)" src="https://github.com/user-attachments/assets/40721cdf-63c7-429f-bd54-b2827b7edecb" />
<img width="953" height="182" alt="git16-01" src="https://github.com/user-attachments/assets/d9284367-2ab0-4e9d-bedf-8ccfc7016523" />
