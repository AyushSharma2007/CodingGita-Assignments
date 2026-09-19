## Assignment 2 – `rm` vs `git rm`

**Goal:** Understand the difference between normal delete and Git delete.

1. Make sure `profile.txt` is committed on `main`.
2. Delete the file using normal system command:
```bash
rm profile.txt
```
3. Run `git status` and observe the output.
4. Recover the file using:
```bash
git restore profile.txt
```
5. Now delete it properly with Git:
```bash
git rm profile.txt
```
6. Run `git status` again and observe the difference.
7. Commit the deletion:
```bash
git commit -m "Remove profile.txt using git rm"
```
8. Create a short file named `delete-difference.txt` and write in your own words:
- What is the difference between `rm` and `git rm`?
- When should you use `git rm`?

**Submit:**
- Screenshots of `git status` after `rm` and after `git rm`
- Content of `delete-difference.txt`
- Repository link

---
[repo link](https://github.com/AyushSharma2007/githubass15.git)
<img width="950" height="360" alt="git15-02" src="https://github.com/user-attachments/assets/b88f4737-620b-4d82-b2ce-935f794f4e56" />
<img width="1092" height="391" alt="git15-02 (2)" src="https://github.com/user-attachments/assets/86fc833d-f903-47df-a59e-7c737cff30f2" />
<img width="1367" height="205" alt="git15-02 (3)" src="https://github.com/user-attachments/assets/dba11941-eea5-449c-8205-d402cb0bfa79" />
