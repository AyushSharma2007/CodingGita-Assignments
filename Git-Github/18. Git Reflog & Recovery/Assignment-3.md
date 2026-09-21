
## 📋 Part 3: Reflog Exploration 

### Task
1. In either repository, run `git reflog`
2. Document at least 5 different HEAD movements
3. For each movement, explain what command caused it

### Deliverables
```
✅ Screenshot of: git reflog output
✅ Written explanation (in README or written answer in notebook) for 5 HEAD movements:
   - HEAD@{0}: What happened?
   - HEAD@{1}: What happened?
   - HEAD@{2}: What happened?
   - HEAD@{3}: What happened?
   - HEAD@{4}: What happened?
```

### Example Format
```markdown
## Reflog Analysis

- **HEAD@{0}**: `git log` - Just viewing history (no movement)
- **HEAD@{1}**: `git checkout main` - Switched to main branch
- **HEAD@{2}**: `git merge rework/readme` - Merged rework branch
- **HEAD@{3}**: `git commit -m "Updated README"` - Made a commit
- **HEAD@{4}**: `git switch -c rework/readme abc1234` - Created branch at C0
```

***

<img width="1296" height="252" alt="git18-03" src="https://github.com/user-attachments/assets/44b9ff5a-176c-4f6f-b16d-418f88ee0cea" />
