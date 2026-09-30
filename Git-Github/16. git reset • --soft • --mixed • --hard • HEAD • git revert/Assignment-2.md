## Assignment 2 – Difference between --soft, --mixed and --hard (Medium)

**Goal:** Clearly see how the three reset modes behave differently.

1. Create a new file `demo.txt` and make **two commits** on it.
2. Perform the following one by one (create fresh commits each time if needed):

   **A. Soft Reset**
   ```bash
   git reset --soft HEAD~1
   git status
   ```

   **B. Mixed Reset**
   ```bash
   git reset --mixed HEAD~1
   git status
   ```

   **C. Hard Reset**
   ```bash
   git reset --hard HEAD~1
   git status
   ```

3. write the short answers in your own words in your notebook:
   - What is the difference between `--soft`, `--mixed`, and `--hard`?
   - Which one keeps changes staged?
   - Which one discards the changes completely?
   - When should you avoid `--hard`?

**Submit:**
- Screenshots of `git status` after each type of reset (`--soft`, `--mixed`, `--hard`)
- Photos of written answers.
- Repository link

---
[github repo](https://github.com/AyushSharma2007/gitass16.git)
<img width="1033" height="351" alt="git16-02 (3)" src="https://github.com/user-attachments/assets/47f11266-d2fa-4bd1-87b5-a6beb01f6fe0" />
<img width="1093" height="495" alt="git16-02 (2)" src="https://github.com/user-attachments/assets/b0b980ba-58eb-4df7-b55d-8bee0248eb65" />
<img width="971" height="488" alt="git16-02" src="https://github.com/user-attachments/assets/586a8cf6-abff-4438-8db3-04d0b7b9e776" />
<img width="1600" height="1200" alt="16-02" src="https://github.com/user-attachments/assets/30c43d31-75cb-42e6-a42e-7be35231095c" />

