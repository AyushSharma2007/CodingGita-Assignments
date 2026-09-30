### Assignment 1 
**Conflict during `git pull`**

**Goal:** Face and resolve a conflict that appears when you run `git pull origin main`.

1. On GitHub (remote `main`), create a file `welcome.txt` with the content:  
   `Welcome to Git class`
2. Commit it directly on GitHub.
3. On your **local main**, create the same file `welcome.txt` with different content:  
   `Welcome to Day 13`
4. Run:
   ```bash
   git add welcome.txt
   git commit -m "Add welcome.txt locally"
   git pull origin main
   ```
5. A conflict will appear. Resolve it by keeping **both** lines (or any final version you prefer).
6. Remove all conflict markers, then:
   ```bash
   git add welcome.txt
   git commit -m "Resolve pull conflict in welcome.txt"
   git push origin main
   ```

**Submit:**
- Screenshot of the conflict markers
- Screenshot of the final resolved file on GitHub
- Repository link

---
[github repo link](https://github.com/AyushSharma2007/githubAssignment13.git)
<img width="1887" height="577" alt="git13-01 (2)" src="https://github.com/user-attachments/assets/d50f4528-f014-4e64-a7c3-dc291c2ff8c1" />
<img width="1407" height="385" alt="git13-01" src="https://github.com/user-attachments/assets/ba607817-8b11-4397-b813-7661658c0de3" />
