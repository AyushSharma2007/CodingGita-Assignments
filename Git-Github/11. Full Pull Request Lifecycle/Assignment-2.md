
### Assignment 2 – `feature/about-page` with Review & Rework (Mandatory)

**Goal:** Practice receiving a review comment, reworking the **same** branch, and updating the PR.

1. Create branch:  
   `git checkout -b feature/about-page`
2. Create `about.html` with only a basic heading (intentionally incomplete).
3. Commit and push:  
   ```bash
   git add .
   git commit -m "Add about page skeleton"
   git push -u origin feature/about-page
   ```
4. Open a Pull Request on GitHub.
5. **Simulate review:** Add a comment on the PR yourself (or ask a classmate/mentor) requesting:  
   *“Please add a short paragraph about the purpose of the about page and a simple team section placeholder.”*
6. Rework on the **same branch**:  
   ```bash
   git checkout feature/about-page
   # edit about.html as requested
   git add .
   git commit -m "Address review: add description and team section"
   git push origin feature/about-page
   ```
7. Confirm the PR on GitHub now shows the new commit.
8. Merge the PR, delete remote branch, update local main (`git fetch` + `git merge` or `git pull`), delete local branch.
9. Screenshot:  
   (a) PR conversation showing the review comment + your new commit  
   (b) merged PR

**Submit:** PR link showing review comment + rework commit, plus merged PR screenshot.

---
[PR link](https://github.com/AyushSharma2007/githubAssignment11/commit/e9e6c2c72f25c14012070b4bb690b588c6059cb7)
<img width="1722" height="603" alt="github11-02 (2)" src="https://github.com/user-attachments/assets/42d800f5-0cf6-4782-aed6-27548396093d" />
<img width="1310" height="856" alt="github11-02" src="https://github.com/user-attachments/assets/06ff9b99-e33d-49a5-8d64-abbac9a7ba44" />
