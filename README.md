# 📁 Tower of Hanoi Solver

> A recursive Python solution to the Tower of Hanoi puzzle, the final project before the freeCodeCamp Scientific Computing with Python certification exam.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![freeCodeCamp](https://img.shields.io/badge/freeCodeCamp-Certification%20Project-informational?logo=freecodecamp)
![DSA](https://img.shields.io/badge/Topic-Algorithms-red?logo=python&logoColor=white)

---

## 📌 About

This is the final freeCodeCamp Scientific Computing with Python certification project before the exam. The Tower of Hanoi is a classic computer science puzzle — move all discs from rod 1 to rod 3, one at a time, never placing a larger disc on top of a smaller one. The solution is elegantly recursive: to move `n` discs, move `n-1` out of the way, move the largest to the target, then move the `n-1` back on top. Built to consolidate everything learned across the certification — recursion, nested functions, `nonlocal`, and state tracking.

---

## 🧠 What I Learned

- **Pure recursion for puzzle solving** — The entire solution reduces to one insight: to move `n` discs, first move `n-1` out of the way, then move the biggest disc, then move `n-1` back. Writing that logic cleanly in code was the challenge
- **Nested functions** — Defining the recursive `move()` helper inside `hanoi_solver()` to keep the rod references in scope without passing them as arguments on every call
- **`nonlocal`** — Using `nonlocal result` inside the nested function so the accumulated move string persists across every recursive call rather than resetting each time — a subtle but essential detail
- **State tracking across recursion** — Capturing the state of all three rods after every disc move with `f"{rod1} {rod2} {rod3}\n"`, making the entire solution path visible step by step
- **`range()` in reverse** — Using `range(total_discs, 0, -1)` to initialize rod 1 from largest to smallest disc, matching the puzzle's starting configuration
- **Minimum moves formula** — Recognizing that the algorithm always solves Hanoi in exactly `2ⁿ - 1` moves, which is why the puzzle grows so dramatically: 3 discs = 7 moves, 5 discs = 31 moves, 20 discs = over 1 million moves

---

## 🛠️ Technologies Used

| Tool / Library | Purpose |
|---|---|
| Python 3.x | Core language |

---

## 💡 How It Works

```
hanoi_solver(2) — 3 moves (2² - 1)

[2, 1] [] []     ← starting state
[2] [] [1]       ← move disc 1 to rod 3
[] [2] [1]       ← move disc 2 to rod 2
[] [2, 1] []     ← wait...
[2, 1] [] []     

hanoi_solver(3) — 7 moves (2³ - 1)
[3, 2, 1] [] []
[3, 2] [1] []
[3] [1] [2]
...and so on until all discs reach rod 3
```

**Example output:**
```
[2, 1] [] []
[2] [] [1]
[] [2] [1]
[] [2, 1] []  ← disc 1 stacks on disc 2
[1] [2] []
[1] [] [2]
[] [] [2, 1]  ← solved ✅
```

---

## 🚀 Future Improvements

- [ ] Add a move counter to display the total moves taken alongside the solution
- [ ] Animate the solution step by step in the terminal using `time.sleep()`
- [ ] Visualize the rods and discs graphically using `matplotlib`
- [ ] Add input validation to reject negative disc counts or non-integer inputs

---

## 📂 Project Structure

```
tower-of-hanoi/
│
├── README.md
└── TowerOfHanoi.py    # hanoi_solver function with nested move() and example usage
```

---

*Part of my Python learning journey 🐍 — the final freeCodeCamp certification project, bringing together recursion, nested functions, and nonlocal state*
