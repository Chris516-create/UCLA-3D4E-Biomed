"""
distribute.py — the ONE main code file for 3D4E Biomed's Stress Pet build 🐣

All 12 parts of Momo the stress pet live inside this file.
Each member runs ONE command to write their part into the repo,
then commits, pushes and opens a pull request.

  MEMBERS
    python distribute.py                 show the parts and who has each one
    python distribute.py take 5          write Part 5 into its file (use YOUR number)
    python distribute.py take "Alex"     same, using your name from members.json
    python distribute.py check           see which parts are in and working

  ORGANIZER
    python distribute.py handouts        make one handout per member in handouts/
    python distribute.py codeowners      write .github/CODEOWNERS from members.json
    python distribute.py reset           put all 12 empty placeholders back
    python distribute.py solve           write all 12 parts at once (demo / backup)

  THEN RUN THE PET
    python stress-pet/server.py          and open http://localhost:8000

On a Mac, type python3 instead of python.
"""

import importlib
import json
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")  # emoji-safe on Windows
except Exception:
    pass

REPO = Path(__file__).resolve().parent
APP = REPO / "stress-pet"          # where the 12 part files go
MEMBERS_FILE = REPO / "members.json"


# ─────────────────────────────────────────────────────────────────────────────
#  THE 12 PARTS
#  Each part: number, file it goes in, role name, difficulty (1-3), and the code.
# ─────────────────────────────────────────────────────────────────────────────

PARTS = {}


def part(number, path, role, difficulty, code):
    PARTS[number] = {"path": path, "role": role, "difficulty": difficulty, "code": code.lstrip("\n")}


# ═════════════════════════════════════════════════════════════════════════════
# PART 1 · The Web Server · stress-pet/server.py
# ═════════════════════════════════════════════════════════════════════════════
part(1, "server.py", "The Web Server", 3, r'''
# PART 1 — server.py — The Web Server 🌐
# This file starts a tiny website on your computer and answers the
# webpage's questions ("how is the pet?", "set stress to heavy!").
# Run it with:   python server.py    then open  http://localhost:8000

import json
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse, parse_qs

from pet.pet import Pet
from pet.actions import do_action

PORT = 8000
WEB_FOLDER = Path(__file__).parent / "web"

pet = Pet()  # one pet, shared by everyone who opens the page


class PetHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # serve the files inside the web/ folder (index.html, style.css, ...)
        super().__init__(*args, directory=str(WEB_FOLDER), **kwargs)

    def send_json(self, data, status=200):
        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        url = urlparse(self.path)
        query = parse_qs(url.query)

        if url.path == "/api/pet":
            # "How is the pet doing?"
            self.send_json(pet.to_dict())

        elif url.path == "/api/stress":
            # "Set the stress level!"  e.g. /api/stress?level=heavy
            level = query.get("level", [""])[0]
            if pet.set_stress(level):
                self.send_json(pet.to_dict())
            else:
                self.send_json({"error": "Unknown stress level: " + level}, 400)

        elif url.path == "/api/action":
            # "Help the pet relax!"  e.g. /api/action?name=breathe
            name = query.get("name", [""])[0]
            message = do_action(pet, name)
            if message is None:
                self.send_json({"error": "Unknown action: " + name}, 400)
            else:
                data = pet.to_dict()
                data["message"] = message
                self.send_json(data)

        else:
            super().do_GET()  # anything else: send a file from web/

    def log_message(self, format, *args):
        pass  # keep the terminal quiet


if __name__ == "__main__":
    server = HTTPServer(("localhost", PORT), PetHandler)
    print("🐣 Your stress pet is alive at  http://localhost:" + str(PORT))
    print("   (press Ctrl + C to stop the server)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 Bye! The pet is sleeping now.")
''')


# ═════════════════════════════════════════════════════════════════════════════
# PART 2 · The Settings · stress-pet/pet/config.py
# ═════════════════════════════════════════════════════════════════════════════
part(2, "pet/config.py", "The Settings", 1, r'''
# PART 2 — pet/config.py — The Settings ⚙️
# Every other part reads these settings. Change them here and the
# whole pet changes!

PET_NAME = "Momo"

# The three stress levels, from calm to stressed (order matters!)
STRESS_LEVELS = ["light", "medium", "heavy"]

DEFAULT_LEVEL = "light"

# What each level looks like on screen
LEVEL_INFO = {
    "light": {"label": "Light", "color": "#8fd9a8", "weather": "🌤️"},
    "medium": {"label": "Medium", "color": "#ffd166", "weather": "🌥️"},
    "heavy": {"label": "Heavy", "color": "#ff8a80", "weather": "⛈️"},
}
''')


# ═════════════════════════════════════════════════════════════════════════════
# PART 3 · The Face Designer · stress-pet/pet/faces.py
# ═════════════════════════════════════════════════════════════════════════════
part(3, "pet/faces.py", "The Face Designer", 1, r'''
# PART 3 — pet/faces.py — The Face Designer 😊
# Decides what the pet's face looks like, and the little
# icon floating above its head, for each stress level.

FACES = {
    "light": "^ ‿ ^",
    "medium": "• _ •",
    "heavy": "> ﹏ <",
}

ACCESSORIES = {
    "light": "🌸",
    "medium": "💭",
    "heavy": "💦",
}


def get_face(level):
    return FACES.get(level, "o _ o")


def get_accessory(level):
    return ACCESSORIES.get(level, "")
''')


# ═════════════════════════════════════════════════════════════════════════════
# PART 4 · The Voice · stress-pet/pet/messages.py
# ═════════════════════════════════════════════════════════════════════════════
part(4, "pet/messages.py", "The Voice", 1, r'''
# PART 4 — pet/messages.py — The Voice 💬
# Things the pet says. Every few seconds it picks a random
# line that matches its stress level.

import random

MESSAGES = {
    "light": [
        "I feel great today!",
        "Life is good. Want a snack?",
        "So calm... like a cloud.",
        "Let's learn something fun!",
    ],
    "medium": [
        "Hmm, lots of homework...",
        "I'm a little tense.",
        "Maybe a short break would help?",
        "My heart is beating a bit faster.",
    ],
    "heavy": [
        "Too much! I'm overwhelmed!",
        "Can we take a deep breath together?",
        "My palms are sweaty...",
        "Please help me relax!",
    ],
}


def get_message(level):
    lines = MESSAGES.get(level, ["..."])
    return random.choice(lines)
''')


# ═════════════════════════════════════════════════════════════════════════════
# PART 5 · The Body Sensors · stress-pet/pet/stats.py
# ═════════════════════════════════════════════════════════════════════════════
part(5, "pet/stats.py", "The Body Sensors", 2, r'''
# PART 5 — pet/stats.py — The Body Sensors ❤️
# Fake "sensor readings" for the pet — the same signals our real
# stress wearable will measure: heart rate and skin conductance (GSR).

import random

BASE_STATS = {
    # heart_rate in beats per minute, gsr in microsiemens (µS)
    "light": {"heart_rate": 68, "gsr": 2.0, "happiness": 90, "energy": 85},
    "medium": {"heart_rate": 88, "gsr": 6.0, "happiness": 60, "energy": 60},
    "heavy": {"heart_rate": 112, "gsr": 12.0, "happiness": 25, "energy": 30},
}


def get_stats(level):
    base = BASE_STATS[level]
    # real sensors are a bit noisy, so we wiggle the numbers a little
    return {
        "heart_rate": base["heart_rate"] + random.randint(-3, 3),
        "gsr": round(base["gsr"] + random.uniform(-0.5, 0.5), 1),
        "happiness": base["happiness"],
        "energy": base["energy"],
    }
''')


# ═════════════════════════════════════════════════════════════════════════════
# PART 6 · The Pet's Brain · stress-pet/pet/pet.py
# ═════════════════════════════════════════════════════════════════════════════
part(6, "pet/pet.py", "The Pet's Brain", 3, r'''
# PART 6 — pet/pet.py — The Pet's Brain 🧠
# The Pet class remembers the current stress level and
# collects everything from Parts 2–5 into one package.

from pet.config import PET_NAME, STRESS_LEVELS, LEVEL_INFO, DEFAULT_LEVEL
from pet.faces import get_face, get_accessory
from pet.messages import get_message
from pet.stats import get_stats


class Pet:
    def __init__(self, name=PET_NAME):
        self.name = name
        self.level = DEFAULT_LEVEL

    def set_stress(self, level):
        """Change the stress level. Returns True if it worked."""
        if level not in STRESS_LEVELS:
            return False
        self.level = level
        return True

    def to_dict(self):
        """Everything the webpage needs to draw the pet."""
        return {
            "name": self.name,
            "level": self.level,
            "level_info": LEVEL_INFO[self.level],
            "face": get_face(self.level),
            "accessory": get_accessory(self.level),
            "message": get_message(self.level),
            "stats": get_stats(self.level),
        }
''')


# ═════════════════════════════════════════════════════════════════════════════
# PART 7 · The Care Kit · stress-pet/pet/actions.py
# ═════════════════════════════════════════════════════════════════════════════
part(7, "pet/actions.py", "The Care Kit", 2, r'''
# PART 7 — pet/actions.py — The Care Kit 🧘
# Ways to help the pet relax. Each action lowers the stress
# by one step (heavy -> medium -> light) and the pet says thanks.

from pet.config import STRESS_LEVELS

ACTIONS = {
    "breathe": "In... and out... That really helped!",
    "walk": "A little walk outside cleared my head!",
    "nap": "Zzz... I feel recharged!",
}


def calmer_level(level):
    index = STRESS_LEVELS.index(level)
    return STRESS_LEVELS[max(index - 1, 0)]


def do_action(pet, action_name):
    """Do a care action. Returns the pet's reply, or None if unknown."""
    if action_name not in ACTIONS:
        return None
    pet.set_stress(calmer_level(pet.level))
    return ACTIONS[action_name]
''')


# ═════════════════════════════════════════════════════════════════════════════
# PART 8 · The Page Skeleton · stress-pet/web/index.html
# ═════════════════════════════════════════════════════════════════════════════
part(8, "web/index.html", "The Page Skeleton", 2, r'''
<!DOCTYPE html>
<!-- PART 8 — web/index.html — The Page Skeleton 🦴 -->
<!-- Lays out every piece you see on the page. The CSS parts make  -->
<!-- it pretty, and the JavaScript parts make it move.             -->
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Stress Pet</title>
  <link rel="stylesheet" href="style.css">
  <link rel="stylesheet" href="pet.css">
</head>
<body data-level="light">
  <main class="device">
    <h1 class="device-title">STRESS PET</h1>

    <section class="screen">
      <div id="weather" class="weather">🌤️</div>
      <div id="speech" class="speech">Loading...</div>
      <div id="pet" class="pet level-light">
        <span id="accessory" class="accessory">🌸</span>
        <span id="face" class="face">^ ‿ ^</span>
      </div>
      <p class="pet-name"><span id="pet-name">Momo</span> · stress: <b id="level-label">Light</b></p>
    </section>

    <section class="sensors">
      <div class="sensor">❤️ <span id="heart-rate">--</span> bpm</div>
      <div class="sensor">💧 GSR <span id="gsr">--</span> µS</div>
      <canvas id="ecg" width="320" height="70"></canvas>
      <label>Happiness <span class="bar"><span id="happiness-bar"></span></span></label>
      <label>Energy <span class="bar"><span id="energy-bar"></span></span></label>
    </section>

    <section class="controls">
      <p class="controls-title">Set stress level</p>
      <div class="button-row">
        <button class="stress-btn" data-level="light">Light</button>
        <button class="stress-btn" data-level="medium">Medium</button>
        <button class="stress-btn" data-level="heavy">Heavy</button>
      </div>
      <p class="controls-title">Help Momo relax</p>
      <div class="button-row">
        <button class="care-btn" data-action="breathe">🌬️ Breathe</button>
        <button class="care-btn" data-action="walk">🚶 Walk</button>
        <button class="care-btn" data-action="nap">😴 Nap</button>
      </div>
    </section>
  </main>

  <script src="heartbeat.js"></script>
  <script src="app.js"></script>
</body>
</html>
''')


# ═════════════════════════════════════════════════════════════════════════════
# PART 9 · The Device Designer · stress-pet/web/style.css
# ═════════════════════════════════════════════════════════════════════════════
part(9, "web/style.css", "The Device Designer", 2, r'''
/* PART 9 — web/style.css — The Device Designer 🎨
   Makes the page look like a handheld Tamagotchi toy:
   the egg-shaped body, the screen, the buttons. */

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: "Trebuchet MS", "Segoe UI", sans-serif;
  background: #f3e9ff;
  transition: background 0.6s;
}

body[data-level="medium"] { background: #fff3d6; }
body[data-level="heavy"]  { background: #ffe1dc; }

.device {
  width: 340px;
  padding: 28px 24px 32px;
  border-radius: 48% 48% 42% 42% / 38% 38% 30% 30%;
  background: linear-gradient(160deg, #b388ff, #7c4dff);
  box-shadow: 0 16px 40px rgba(60, 20, 120, 0.35), inset 0 -6px 0 rgba(0, 0, 0, 0.15);
  text-align: center;
}

.device-title {
  margin: 4px 0 14px;
  font-size: 16px;
  letter-spacing: 4px;
  color: white;
}

.screen {
  position: relative;
  height: 230px;
  border-radius: 18px;
  border: 6px solid #4a2a8a;
  background: #e8f5e1;
  overflow: hidden;
}

.weather {
  position: absolute;
  top: 8px;
  right: 10px;
  font-size: 22px;
}

.speech {
  margin: 12px 34px 0;
  padding: 6px 10px;
  border-radius: 12px;
  background: white;
  font-size: 13px;
  min-height: 30px;
}

.pet-name {
  position: absolute;
  bottom: 6px;
  width: 100%;
  margin: 0;
  font-size: 12px;
  color: #4a2a8a;
}

.sensors {
  margin-top: 14px;
  padding: 10px;
  border-radius: 14px;
  background: rgba(255, 255, 255, 0.85);
  font-size: 13px;
  text-align: left;
}

.sensor {
  display: inline-block;
  width: 48%;
  font-weight: bold;
}

#ecg {
  width: 100%;
  height: 60px;
  margin: 6px 0;
  border-radius: 8px;
  background: #102018;
}

.sensors label {
  display: grid;
  grid-template-columns: 72px 1fr;
  align-items: center;
  margin-top: 4px;
}

.bar {
  flex: 1;
  height: 10px;
  border-radius: 5px;
  background: #ddd;
  overflow: hidden;
}

.bar span {
  display: block;
  height: 100%;
  width: 50%;
  background: #7c4dff;
  transition: width 0.6s;
}

.controls-title {
  margin: 14px 0 6px;
  font-size: 12px;
  font-weight: bold;
  color: white;
}

.button-row {
  display: flex;
  gap: 8px;
  justify-content: center;
}

button {
  flex: 1;
  padding: 8px 4px;
  border: none;
  border-radius: 999px;
  background: white;
  color: #4a2a8a;
  font-weight: bold;
  cursor: pointer;
  box-shadow: 0 3px 0 rgba(0, 0, 0, 0.2);
}

button:active {
  transform: translateY(2px);
  box-shadow: none;
}

button.active {
  background: #4a2a8a;
  color: white;
}
''')


# ═════════════════════════════════════════════════════════════════════════════
# PART 10 · The Animator · stress-pet/web/pet.css
# ═════════════════════════════════════════════════════════════════════════════
part(10, "web/pet.css", "The Animator", 2, r'''
/* PART 10 — web/pet.css — The Animator 💃
   Draws the pet's round body and gives it a different
   "dance" for each stress level. */

.pet {
  position: relative;
  width: 110px;
  height: 95px;
  margin: 26px auto 0;
  border-radius: 50% 50% 45% 45%;
  background: #8fd9a8;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: inset -8px -8px 0 rgba(0, 0, 0, 0.08);
  transition: background 0.6s;
}

.face {
  font-size: 22px;
  font-weight: bold;
  color: #333;
}

.accessory {
  position: absolute;
  top: -26px;
  font-size: 22px;
}

/* LIGHT stress: happy, slow bounce */
.pet.level-light {
  background: #8fd9a8;
  animation: bounce 1.6s ease-in-out infinite;
}

/* MEDIUM stress: nervous side-to-side sway */
.pet.level-medium {
  background: #ffd166;
  animation: sway 1s ease-in-out infinite;
}

/* HEAVY stress: fast shaking, and it gets a little smaller */
.pet.level-heavy {
  background: #ff8a80;
  animation: shake 0.25s linear infinite;
}

@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50%      { transform: translateY(-14px); }
}

@keyframes sway {
  0%, 100% { transform: rotate(-6deg); }
  50%      { transform: rotate(6deg); }
}

@keyframes shake {
  0%   { transform: translateX(0) scale(0.92); }
  25%  { transform: translateX(-4px) scale(0.92); }
  75%  { transform: translateX(4px) scale(0.92); }
  100% { transform: translateX(0) scale(0.92); }
}
''')


# ═════════════════════════════════════════════════════════════════════════════
# PART 11 · The Messenger · stress-pet/web/app.js
# ═════════════════════════════════════════════════════════════════════════════
part(11, "web/app.js", "The Messenger", 3, r'''
// PART 11 — web/app.js — The Messenger 📡
// Talks to the Python server (Part 1) and updates the page
// whenever the pet changes. Also makes the buttons work.

function render(pet) {
  document.body.dataset.level = pet.level;

  document.getElementById("pet").className = "pet level-" + pet.level;
  document.getElementById("face").textContent = pet.face;
  document.getElementById("accessory").textContent = pet.accessory;
  document.getElementById("speech").textContent = pet.message;
  document.getElementById("weather").textContent = pet.level_info.weather;
  document.getElementById("pet-name").textContent = pet.name;
  document.getElementById("level-label").textContent = pet.level_info.label;

  document.getElementById("heart-rate").textContent = pet.stats.heart_rate;
  document.getElementById("gsr").textContent = pet.stats.gsr;
  document.getElementById("happiness-bar").style.width = pet.stats.happiness + "%";
  document.getElementById("energy-bar").style.width = pet.stats.energy + "%";

  // highlight the button for the current stress level
  document.querySelectorAll(".stress-btn").forEach(function (button) {
    button.classList.toggle("active", button.dataset.level === pet.level);
  });

  // tell the heartbeat monitor (Part 12) how fast to beat
  if (window.setHeartRate) {
    window.setHeartRate(pet.stats.heart_rate);
  }
}

function askServer(url) {
  fetch(url)
    .then(function (response) { return response.json(); })
    .then(render)
    .catch(function (error) { console.log("Server problem:", error); });
}

document.querySelectorAll(".stress-btn").forEach(function (button) {
  button.addEventListener("click", function () {
    askServer("/api/stress?level=" + button.dataset.level);
  });
});

document.querySelectorAll(".care-btn").forEach(function (button) {
  button.addEventListener("click", function () {
    askServer("/api/action?name=" + button.dataset.action);
  });
});

askServer("/api/pet");                                   // draw the pet right away
setInterval(function () { askServer("/api/pet"); }, 4000); // check on it every 4 s
''')


# ═════════════════════════════════════════════════════════════════════════════
# PART 12 · The Heart Monitor · stress-pet/web/heartbeat.js
# ═════════════════════════════════════════════════════════════════════════════
part(12, "web/heartbeat.js", "The Heart Monitor", 3, r'''
// PART 12 — web/heartbeat.js — The Heart Monitor 📈
// Draws a hospital-style ECG line that beats faster when the
// pet is stressed. app.js (Part 11) calls setHeartRate(bpm).

var bpm = 70;
var canvas = document.getElementById("ecg");
var ctx = canvas.getContext("2d");
var SPEED = 0.12;            // pixels per millisecond
var x = 0;
var lastY = canvas.height / 2;
var clock = 0;               // pretend time, in milliseconds
var lastFrame = performance.now();

window.setHeartRate = function (newBpm) {
  bpm = newBpm;
};

// One heartbeat shape: small bump (P), big spike (R), dip (S), wave (T)
function heartSignal(msIntoBeat) {
  function bump(center, width, height) {
    var d = (msIntoBeat - center) / width;
    return height * Math.exp(-d * d);
  }
  return bump(60, 20, 0.15) + bump(150, 10, 1.0) - bump(175, 10, 0.3) + bump(330, 40, 0.25);
}

function lineColor() {
  var level = document.body.dataset.level;
  if (level === "heavy") return "#ff6b6b";
  if (level === "medium") return "#ffd166";
  return "#5ef08a";
}

function draw(now) {
  var pixels = Math.floor((now - lastFrame) * SPEED);
  if (pixels > 0) {
    lastFrame = now;
    ctx.strokeStyle = lineColor();
    ctx.lineWidth = 2;
    for (var i = 0; i < pixels; i++) {
      clock += 1 / SPEED;
      var beatLength = 60000 / bpm;
      var y = canvas.height * 0.65 - heartSignal(clock % beatLength) * canvas.height * 0.55;
      ctx.clearRect(x + 1, 0, 12, canvas.height); // erase just ahead of the line
      ctx.beginPath();
      ctx.moveTo(x, lastY);
      ctx.lineTo(x + 1, y);
      ctx.stroke();
      x += 1;
      lastY = y;
      if (x >= canvas.width) x = 0; // wrap around like a real monitor
    }
  }
  requestAnimationFrame(draw);
}

requestAnimationFrame(draw);
''')


# ─────────────────────────────────────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────────────────────────────────────

def load_members():
    """Read members.json. Returns {part number: {"name": ..., "github": ...}}."""
    try:
        data = json.loads(MEMBERS_FILE.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}, {}
    except json.JSONDecodeError as e:
        sys.exit("❌ members.json has a typo on line " + str(e.lineno) + ". Check the commas and quotes.")
    members = {}
    for m in data.get("members", []):
        members[int(m["part"])] = m
    return data, members


def stub_text(number):
    path = PARTS[number]["path"]
    msg = ("STUB for Part " + str(number) + ". Run:  python distribute.py take "
           + str(number) + "   (or paste your Part " + str(number) + " code here)")
    if path.endswith(".py"):
        return "# " + msg + "\n"
    if path.endswith(".html"):
        return "<!-- " + msg + " -->\n"
    if path.endswith(".css"):
        return "/* " + msg + " */\n"
    return "// " + msg + "\n"


def write_file(path, text):
    file = APP / path
    file.parent.mkdir(parents=True, exist_ok=True)
    with open(file, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def find_part(who):
    """Turn '5' or 'Alex' into a part number."""
    if who.isdigit() and int(who) in PARTS:
        return int(who)
    _, members = load_members()
    for number, m in members.items():
        if m.get("name", "").strip().lower() == who.strip().lower():
            return number
    sys.exit("❓ Can't find part '" + who + "'. Use a number from 1 to 12, or your name as written in members.json.")


def git_steps(number):
    role = PARTS[number]["role"]
    return [
        "git checkout -b part-" + str(number),
        "python distribute.py take " + str(number),
        "python distribute.py check",
        "git add .",
        'git commit -m "Add part ' + str(number) + ": " + role + '"',
        "git push -u origin part-" + str(number),
    ]


# ─────────────────────────────────────────────────────────────────────────────
#  MEMBER COMMANDS
# ─────────────────────────────────────────────────────────────────────────────

def cmd_list():
    _, members = load_members()
    print("\n🐣 3D4E Biomed · Stress Pet · 12 parts\n")
    print("  #   Role                  File                       Level  Member")
    print("  ──  ────────────────────  ─────────────────────────  ─────  ──────────")
    for n in sorted(PARTS):
        p = PARTS[n]
        name = members.get(n, {}).get("name", "") or "—"
        stars = "★" * p["difficulty"] + "☆" * (3 - p["difficulty"])
        print("  " + str(n).rjust(2) + "  " + p["role"].ljust(20) + "  " + ("stress-pet/" + p["path"]).ljust(25)
              + "  " + stars + "    " + name)
    print("\n  Get your part:   python distribute.py take <your number>\n")


def cmd_take(who):
    number = find_part(who)
    p = PARTS[number]
    _, members = load_members()
    name = members.get(number, {}).get("name", "")
    head = REPO / ".git" / "HEAD"
    if head.exists() and head.read_text().strip() in ("ref: refs/heads/main", "ref: refs/heads/master"):
        print("\n⚠️  You are on the main branch. Make your own branch first:")
        print("      git checkout -b part-" + str(number))
        print("   (then run this command again)\n")
        return
    write_file(p["path"], p["code"])
    print("\n✅ Part " + str(number) + " (" + p["role"] + ") written to stress-pet/" + p["path"])
    if name:
        print("   Nice work, " + name + "!")
    print("\nOpen that file in VS Code and read the comments: they explain your code.")
    print("Then finish with:\n")
    for step in git_steps(number)[2:]:
        print("   " + step)
    print("\nAfter that, open a pull request on GitHub. Only change YOUR file! 🙌\n")


MUST_CONTAIN = {
    1: ["PetHandler", "/api/stress", "/api/action"],
    2: ["STRESS_LEVELS", "LEVEL_INFO", "DEFAULT_LEVEL"],
    3: ["def get_face", "def get_accessory"],
    4: ["def get_message"],
    5: ["def get_stats"],
    6: ["class Pet", "def to_dict"],
    7: ["def do_action", "ACTIONS"],
    8: ['id="pet"', 'id="ecg"', "app.js", "heartbeat.js"],
    9: [".device", ".screen"],
    10: [".pet.level-light", ".pet.level-medium", ".pet.level-heavy", "@keyframes"],
    11: ["function render", "/api/pet", "setHeartRate"],
    12: ["window.setHeartRate", "requestAnimationFrame"],
}


def check_one(number):
    path = PARTS[number]["path"]
    file = APP / path
    if not file.exists():
        return "missing", "file not found"
    text = file.read_text(encoding="utf-8")
    if "STUB" in text:
        return "waiting", "still the empty placeholder"
    if "PART " + str(number) + " " not in text:
        return "error", "doesn't start with the 'PART " + str(number) + "' header. Wrong code in this file?"
    for needle in MUST_CONTAIN[number]:
        if needle not in text:
            return "error", "can't find '" + needle + "'. Was part of the code cut off?"
    if not path.endswith(".py"):
        return "ok", ""
    if number == 1:
        try:
            compile(text, path, "exec")
        except SyntaxError as e:
            return "error", "typo on line " + str(e.lineno) + ": " + str(e.msg)
        return "ok", ""
    try:
        importlib.import_module(path[:-3].replace("/", "."))
    except SyntaxError as e:
        return "error", "typo on line " + str(e.lineno) + ": " + str(e.msg)
    except ImportError as e:
        return "blocked", "needs another part to be merged first (" + str(e) + ")"
    except Exception as e:
        return "error", type(e).__name__ + ": " + str(e)
    return "ok", ""


def cmd_check():
    sys.path.insert(0, str(APP))
    icons = {"ok": "✅", "waiting": "⏳", "missing": "❓", "blocked": "🔗", "error": "❌"}
    print("\n🐣 Stress Pet · part check\n")
    done = 0
    for n in sorted(PARTS):
        status, note = check_one(n)
        done += status == "ok"
        print("  " + icons[status] + "  Part " + str(n).rjust(2) + "  " + PARTS[n]["role"].ljust(20)
              + "stress-pet/" + PARTS[n]["path"])
        if note:
            print("            → " + note)
    print("\n  " + str(done) + " / 12 parts ready\n")
    if done == 12:
        try:
            from pet.pet import Pet
            from pet.actions import do_action
            pet = Pet()
            for level in ["light", "medium", "heavy"]:
                assert pet.set_stress(level) and pet.to_dict()["level"] == level
            assert do_action(pet, "breathe") and pet.level == "medium"
            print("🎉 Everything works! Start the pet with:   python stress-pet/server.py\n")
        except Exception as e:
            print("⚠️  All 12 parts are in, but the final test failed: " + str(e) + "\n")


# ─────────────────────────────────────────────────────────────────────────────
#  ORGANIZER COMMANDS
# ─────────────────────────────────────────────────────────────────────────────

def cmd_handouts():
    data, members = load_members()
    repo_url = data.get("repo_url") or "<repo URL>"
    out = REPO / "handouts"
    out.mkdir(exist_ok=True)
    for n in sorted(PARTS):
        p = PARTS[n]
        name = members.get(n, {}).get("name", "") or "Member " + str(n)
        lang = {"py": "python", "html": "html", "css": "css", "js": "javascript"}[p["path"].rsplit(".", 1)[1]]
        lines = [
            "# Part " + str(n) + " · " + p["role"] + " · for " + name, "",
            "Your file: `stress-pet/" + p["path"] + "`  ·  Difficulty: " + "★" * p["difficulty"], "",
            "## Steps (VS Code → Terminal → New Terminal)", "", "```bash",
            "git clone " + repo_url, "cd 3D4E-Biomed", *git_steps(n), "```", "",
            "Then open a pull request on GitHub (yellow **Compare & pull request** button).", "",
            "After everything is merged:", "", "```bash",
            "git checkout main", "git pull", "python distribute.py check", "python stress-pet/server.py", "```", "",
            "## Your code (in case `take` doesn't work, paste this into your file)", "",
            "```" + lang, p["code"].rstrip("\n"), "```", "",
        ]
        file = out / ("part-" + str(n).zfill(2) + "-" + name.replace(" ", "-") + ".md")
        file.write_text("\n".join(lines), encoding="utf-8")
    print("📄 Wrote 12 handouts to handouts/  (this folder is not committed)")


def cmd_codeowners():
    data, members = load_members()
    lines = ["# Who reviews each part. Made by: python distribute.py codeowners", ""]
    org = data.get("organizer", {}).get("github", "").lstrip("@")
    if org:
        lines += ["*  @" + org, ""]
    for n in sorted(PARTS):
        gh = members.get(n, {}).get("github", "").lstrip("@")
        owners = " ".join("@" + u for u in [gh, org] if u)
        if owners:
            lines.append("/stress-pet/" + PARTS[n]["path"] + "  " + owners)
    file = REPO / ".github" / "CODEOWNERS"
    file.parent.mkdir(exist_ok=True)
    file.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("👥 Wrote .github/CODEOWNERS")


def cmd_reset():
    for n in PARTS:
        write_file(PARTS[n]["path"], stub_text(n))
    write_file("pet/__init__.py", '# This file tells Python that "pet" is a folder of code. Leave it as is!\n')
    print("🧹 All 12 parts are back to empty placeholders.")


def cmd_solve():
    for n in PARTS:
        write_file(PARTS[n]["path"], PARTS[n]["code"])
    write_file("pet/__init__.py", '# This file tells Python that "pet" is a folder of code. Leave it as is!\n')
    print("✨ All 12 parts written. Run:  python stress-pet/server.py")


if __name__ == "__main__":
    args = sys.argv[1:]
    command = args[0].lower() if args else "list"
    if command == "take":
        if len(args) < 2:
            sys.exit("Tell me your part:   python distribute.py take 5")
        cmd_take(" ".join(args[1:]))
    elif command in ("list", "help", "-h", "--help"):
        cmd_list()
    elif command == "check":
        cmd_check()
    elif command == "handouts":
        cmd_handouts()
    elif command == "codeowners":
        cmd_codeowners()
    elif command == "reset":
        cmd_reset()
    elif command == "solve":
        cmd_solve()
    else:
        print("Unknown command: " + command)
        print(__doc__)
