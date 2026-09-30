### Assignment 1 – Create and Resolve a Merge Conflict on GitHub (Mandatory)

**Goal:** Create a real conflict with two feature branches and resolve it using the GitHub browser editor.

1. Create/clone a repository and on `main` create `tasks.txt`:

```text
My Tasks
1. Study Git
2. Complete assignment
3. Review notes
```

2. Commit and push to `main`.
3. Create branch `feature/tasks-A` → change line 3 to `Practice merge conflicts` → commit → push → open PR (do **not** merge yet).
4. Switch back to `main`, create branch `feature/tasks-B` → change line 3 to `Watch Git tutorial` → commit → push → open second PR.
5. Merge the first PR successfully.
6. Merge the second PR → conflict appears.
7. Resolve the conflict on GitHub:
   - Understand Current vs Incoming
   - Decide final text (keep one, both, or write your own)
   - Remove all conflict markers
   - Mark as resolved → Commit merge → Merge the PR
8. Delete both remote feature branches.
9. Update local main and delete local branches:
   ```bash
   git checkout main
   git pull origin main
   git branch -D feature/tasks-A
   git branch -D feature/tasks-B
   ```

**Submit:**
- Repository link
- Screenshot of the conflict editor (showing markers)
- Screenshot of the successfully merged second PR
- Screenshot of `git log --oneline` after pull

---
[repo link](https://github.com/AyushSharma2007/githubass12again.git)

<img width="1872" height="1027" alt="12-01" src="https://github.com/user-attachments/assets/e6dcf1ff-ec1a-489d-abb8-8e8f273c4368" />
<img width="1196" height="253" alt="12-01 (2)" src="https://github.com/user-attachments/assets/15e89d2f-cb9a-47a3-9b72-236fec572a6b" />
<img width="1877" height="1066" alt="12-01 (3)" src="https://github.com/user-attachments/assets/a9289f51-8366-4ade-92e3-b3c7000e898e" />
