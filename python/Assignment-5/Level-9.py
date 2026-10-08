# LEVEL 8 (Using tuples to simulate serial inputs safely)
# Q62
exp62, tot62, max62, min62 = (250, 180, 400, 120, 300), 0, -1, 9999
for v in exp62:
    tot62 += v
    if v > max62: 
      max62 = v
    if v < min62: 
      min62 = v
print(f"Q62:\nTotal: {tot62}\nHighest: {max62}\nLowest: {min62}")

# Q63
marks63, tot63, mmax63, mmin63, n63 = (78, 65, 92, 81, 74), 0, -1, 999, 0
for m in marks63:
    tot63 += m; n63 += 1
    if m > mmax63: 
      mmax63 = m
    if m < mmin63: 
      mmin63 = m
print(f"Q63:\nTotal: {tot63}\nAverage: {tot63/n63}\nHighest: {mmax63}\nLowest: {mmin63}")

# Q64
att64, p64, a64, t64 = ("P", "P", "A", "P", "A", "P"), 0, 0, 0
for s in att64:
    if s == "P": 
      p64 += 1
    if s == "A": 
      a64 += 1
    t64 += 1
print(f"Q64:\nPresent: {p64}\nAbsent: {a64}\nAttendance: {(p64/t64)*100:.2f}%")

# Q65
units65, tot65, over65 = (8, 12, 15, 7, 13), 0, 0
for u in units65:
    tot65 += u
    if u > 10: 
      over65 += 1
print(f"Q65:\nTotal Units: {tot65}\nDays Above 10: {over65}")

# Q66
prices66, bill66, c66 = (450, 1200, 800, 2500, 600), 0, 0
for p in prices66:
    bill66 += p
    if p > 1000: 
      c66 += 1
print(f"Q66:\nTotal Bill: {bill66}\nProducts Above 1000: {c66}")

# Q67
logins67, sc67, fl67, t67 = ("success", "failed", "success", "failed", "success"), 0, 0, 0
for s in logins67:
    if s == "success": 
      sc67 += 1
    if s == "failed": 
      fl67 += 1
    t67 += 1
print(f"Q67:\nSuccessful: {sc67}\nFailed: {fl67}\nSuccess Rate: {(sc67/t67)*100}%")
