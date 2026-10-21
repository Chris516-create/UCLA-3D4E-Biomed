# UCLA-3D4E-Biomed 🐣

Club build session: 12 members build **Momo**, a Tamagotchi-style stress pet, one part each.
Set the stress to **Light**, **Medium** or **Heavy** and Momo's face, dance, heart rate and
skin conductance (GSR) change. It's a preview of our stress-management wearable: later,
real heart-rate and GSR sensors replace the buttons.

You only need **Python 3**, **Git** and **VS Code**. Nothing to install with pip.

## Members: your 5 steps

Open VS Code → **Terminal → New Terminal**, then (use your own number instead of 5; on a Mac type `python3`):

```bash
git clone https://github.com/Chris516-create/UCLA-3D4E-Biomed.git
cd UCLA-3D4E-Biomed
git checkout -b part-5               # 1. your own branch
python distribute.py take 5          # 2. writes your part into its file
python distribute.py check           # 3. your line should show ✅
git add .
git commit -m "Add part 5"           # 4. save it
git push -u origin part-5            # 5. send it to GitHub
```

Then on GitHub click **Compare & pull request → Create pull request**.

When the organizer has merged all 12:

```bash
git checkout main
git pull
python distribute.py check           # 12 / 12
python stress-pet/server.py          # open http://localhost:8000
```

## What's in the repo

```
3D4E-Biomed/
├── distribute.py        ← the one main code file: holds all 12 parts and hands them out
├── members.json         ← who has which part (organizer fills this in)
├── stress-pet/          ← where the 12 parts land (empty placeholders at the start)
│   ├── server.py              Part 1   The Web Server
│   ├── pet/config.py          Part 2   The Settings
│   ├── pet/faces.py           Part 3   The Face Designer
│   ├── pet/messages.py        Part 4   The Voice
│   ├── pet/stats.py           Part 5   The Body Sensors
│   ├── pet/pet.py             Part 6   The Pet's Brain
│   ├── pet/actions.py         Part 7   The Care Kit
│   ├── web/index.html         Part 8   The Page Skeleton
│   ├── web/style.css          Part 9   The Device Designer
│   ├── web/pet.css            Part 10  The Animator
│   ├── web/app.js             Part 11  The Messenger
│   └── web/heartbeat.js       Part 12  The Heart Monitor
├── .github/             ← pull request checklist (+ CODEOWNERS once generated)
└── .vscode/             ← editor settings so everyone's files look the same
```

Because each person changes a different file, all 12 pull requests merge without conflicts.

## Organizer commands

| Command | What it does |
|---|---|
| `python distribute.py` | Table of parts, difficulty, and who has each |
| `python distribute.py handouts` | One Markdown handout per member in `handouts/` (not committed) |
| `python distribute.py codeowners` | Writes `.github/CODEOWNERS` from GitHub usernames in `members.json` |
| `python distribute.py solve` | Writes all 12 parts at once, for your demo or a rescue |
| `python distribute.py reset` | Puts the 12 empty placeholders back |

**Setup:** fill in `members.json` (names, GitHub usernames, `repo_url`), commit and push it,
add all 12 people under **Settings → Collaborators**, and make sure they accept the invite before the event.
To demo the finished pet without touching `main`, run `solve` on a scratch branch.
