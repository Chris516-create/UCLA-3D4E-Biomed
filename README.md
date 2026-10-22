# UCLA-3D4E-Biomed 🐣

Club build session: 12 members build **Momo**, a Tamagotchi-style stress pet, together in **one file**.
Set the stress to **Light**, **Medium** or **Heavy** and Momo's face, dance, heart rate and
skin conductance (GSR) change. It's a preview of our stress-management wearable: later,
real heart-rate and GSR sensors replace the buttons.

You only need **Python 3**, **Git** and **VS Code**. Nothing to install.

## How it works

`momo.py` is the only code file. It starts with the basic setup already done, then has
**12 empty slots**, one per member:

```python
# ═══════════════════════════════════════════
#  PART 5 · The Pet's Brain
# ═══════════════════════════════════════════

# TODO: delete this line and paste Part 5 here

# ───── end of Part 5 ───────────────────────
```

The organizer gives each member a **code piece**. You paste it into your own slot, replacing
the TODO line. Because everyone edits a different slot, all 12 pull requests merge cleanly.

## Members: your steps

Open VS Code → **Terminal → New Terminal** (use your own number instead of 5; on a Mac type `python3`):

```bash
git clone https://github.com/Chris516-create/UCLA-3D4E-Biomed.git
cd UCLA-3D4E-Biomed
git checkout -b part-5               # 1. your own branch
```

2. Open `momo.py`, press **Ctrl/Cmd + F**, search `PART 5`.
3. Delete the TODO line in your slot, paste your code piece there, save.

```bash
python momo.py                       # 4. your part should show ✅
git add momo.py
git commit -m "Add part 5"           # 5. save it
git push -u origin part-5            # 6. send it to GitHub
```

Then on GitHub click **Compare & pull request → Create pull request**.

When all 12 are merged:

```bash
git checkout main
git pull
python momo.py                       # 12 / 12, then open http://localhost:8000
```

## The 12 parts

| Part | Role | What it adds |
|---|---|---|
| 1 | The Settings | Name, stress levels, colors |
| 2 | The Face Designer | Momo's face for each level |
| 3 | The Voice | What Momo says |
| 4 | The Body Sensors | Fake heart rate and GSR |
| 5 | The Pet's Brain | The `Pet` class that ties 1–4 together |
| 6 | The Care Kit | Breathe, walk, nap |
| 7 | The Page Skeleton | The webpage layout (HTML) |
| 8 | The Device Designer | The toy's look (CSS) |
| 9 | The Animator | Bounce, sway, shake (CSS) |
| 10 | The Messenger | Buttons and live updates (JavaScript) |
| 11 | The Heart Monitor | The ECG line (JavaScript) |
| 12 | The Web Server | Serves the page at localhost:8000 |

The `full-test` branch has all 12 parts already filled in, so the organizer can check that Momo works.
