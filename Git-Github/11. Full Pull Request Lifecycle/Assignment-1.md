### Assignment 1 – Complete PR Lifecycle with `feature/contact-form` (Mandatory)

**Goal:** Practice the full cycle: branch → file → commit → push → PR → merge → cleanup.

1. Update main:  
   `git checkout main && git pull origin main`
2. Create branch:  
   `git checkout -b feature/contact-form`
3. Create file `contact.html` with a simple heading and a short paragraph about a contact form.
4. Stage, commit and push:  
   ```bash
   git add contact.html
   git commit -m "Add contact form page"
   git push -u origin feature/contact-form
   ```
5. On GitHub: Open a Pull Request (base = `main`, compare = `feature/contact-form`). Write a clear title and description.
6. Merge the Pull Request using **“Create a merge commit”**.
7. Delete the remote branch (GitHub “Delete branch” button or `git push origin --delete feature/contact-form`).
8. Update local main using the two-command method:  
   ```bash
   git checkout main
   git fetch origin main
   git merge origin/main
   ```
9. Delete local branch:  
   `git branch -d feature/contact-form`
10. Take screenshots of:  
    (a) the merged PR  
    (b) terminal after fetch + merge  
    (c) `git branch` showing the branch is gone

**Submit:** Merged PR link + the 3 screenshots listed above.

---
[merged PR link](https://github.com/AyushSharma2007/githubAssignment11/commit/a958cfa0bca17e67ae1773e5d728193bc49d65a6)
<img width="718" height="620" alt="github11-01" src="https://github.com/user-attachments/assets/ffcef718-102e-4c2a-a8eb-a0eca12ff21d" />
<img width="740" height="103" alt="github11-01 (2)" src="https://github.com/user-attachments/assets/2b4e51ad-ac80-478a-b702-04f8528f418a" />
<img width="661" height="913" alt="github11-01 (3)" src="https://github.com/user-attachments/assets/008e926b-4dfc-4ca7-81a8-b1cb9fd41a14" />
