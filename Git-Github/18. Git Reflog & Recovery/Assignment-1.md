## 📋 Part 1: Recovery After `git reset --hard` (5 Points)

### Task
1. Create a new repository called `reflog-practice-part1`
2. Create 3 commits:
   - **C0:** `README.md` with project title
   - **C1:** `index.html` with `<h1>Welcome</h1>`
   - **C2:** `style.css` with basic styling
3. Accidentally delete C1 and C2 using `git reset --hard <C0-commit-hash>`
4. Use `git reflog` to find the lost C2 commit
5. Recover C2 (and C1) using detached HEAD + branch + merge
6. Verify all commits are restored

### Deliverables
```
✅ Screenshot of: git log --oneline BEFORE reset
✅ Screenshot of: git log --oneline AFTER reset (showing lost commits)
✅ Screenshot of: git reflog output (highlighting the commit you recovered)
✅ Screenshot of: git log --oneline AFTER recovery (showing all commits restored)
✅ Push final repository to GitHub
```

### Expected Output
```bash
# Initial state
C0 ────── C1 ────── C2 (main)

# After reset --hard
C0 (main)    [C1 & C2 lost from log]

# After recovery
C0 ────── C1 ────── C2 (main)  ← All restored!
```

***

<img width="1098" height="142" alt="git18-01" src="https://github.com/user-attachments/assets/60bc242f-bfb7-486d-baa5-a7b7fc0cd4f2" />
<img width="1163" height="285" alt="git18-01 (2)" src="https://github.com/user-attachments/assets/54e77cea-cbbb-41cc-8681-51739882138d" />
<img width="1157" height="328" alt="git18-01 (3)" src="https://github.com/user-attachments/assets/98e4b1cb-fb26-40a3-9ab8-7c42a2e06163" />
