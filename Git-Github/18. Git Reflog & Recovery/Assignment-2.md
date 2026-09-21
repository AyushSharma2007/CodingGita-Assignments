## 📋 Part 2: Reworking Old Commit (5 Points)

### Task
1. Create a new repository called `reflog-practice-part2`
2. Create 3 commits:
   - **C0:** `README.md` with just title
   - **C1:** `app.js` with basic function
   - **C2:** `utils.js` with helper functions
3. Realize you need to add description to README (C0) without losing C1 and C2
4. Create a branch at C0: `git switch -c rework/readme-update <C0-hash>`
5. Update README.md with description, commit
6. Merge the branch back to main
7. Verify C0, C1, and C2 are all preserved

### Deliverables
```
✅ Screenshot of: git log --oneline BEFORE creating branch
✅ Screenshot of: git branch output (showing both branches)
✅ Screenshot of: git log --oneline --graph (showing merge)
✅ Screenshot of: Final README.md content
✅ Push final repository to GitHub
```

### Expected Output
```bash
# Before rework
C0 ────── C1 ────── C2 (main)

# After rework + merge
      C3 (README update) ─┐
                          │
C0 ────── C1 ────── C2 ─── Merge (main)

All commits preserved!
```

***


<img width="1117" height="151" alt="git18-02" src="https://github.com/user-attachments/assets/5ef73a5c-fc7c-451e-ad4e-157c89b1548f" />
<img width="1102" height="110" alt="git18-02 (2)" src="https://github.com/user-attachments/assets/31c6d5e5-0a5c-4dd3-8489-9b223885b44e" />
<img width="1035" height="246" alt="git18-02 (4)" src="https://github.com/user-attachments/assets/7cd27456-8c25-4b8a-921a-59d0559ecc0e" />
<img width="1153" height="222" alt="git18-02 (3)" src="https://github.com/user-attachments/assets/ae4f3c37-4b58-4968-b80b-4cca4f1118d2" />


