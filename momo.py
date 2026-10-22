"""
momo.py · Momo the Stress Pet 🐣 · UCLA 3D4E Biomed

The whole pet lives in this ONE file. It has 12 empty slots, one per member.
Find YOUR slot (search for "PART 5" with Ctrl/Cmd + F), delete the TODO line
inside it, and paste the code piece you were given. Don't touch other slots.

Run:   python momo.py          (Mac: python3 momo.py)
       It shows which parts are in. When all 12 are in, open http://localhost:8000
"""

# ═════════════════════════════════════════════════════════════════════════════
#  BASIC SETUP · already done for you
# ═════════════════════════════════════════════════════════════════════════════

import json
import random
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

try:
    sys.stdout.reconfigure(encoding="utf-8")  # lets Windows print emoji
except Exception:
    pass

# ═════════════════════════════════════════════════════════════════════════════
#  PART 1 · The Settings
# ═════════════════════════════════════════════════════════════════════════════

# TODO: delete this line and paste Part 1 here

# ───── end of Part 1 ───────────────────────────────────────────────────────

# ═════════════════════════════════════════════════════════════════════════════
#  PART 2 · The Face Designer
# ═════════════════════════════════════════════════════════════════════════════

# TODO: delete this line and paste Part 2 here

# ───── end of Part 2 ───────────────────────────────────────────────────────

# ═════════════════════════════════════════════════════════════════════════════
#  PART 3 · The Voice
# ═════════════════════════════════════════════════════════════════════════════

# TODO: delete this line and paste Part 3 here

# ───── end of Part 3 ───────────────────────────────────────────────────────

# ═════════════════════════════════════════════════════════════════════════════
#  PART 4 · The Body Sensors
# ═════════════════════════════════════════════════════════════════════════════

# TODO: delete this line and paste Part 4 here

# ───── end of Part 4 ───────────────────────────────────────────────────────

# ═════════════════════════════════════════════════════════════════════════════
#  PART 5 · The Pet's Brain
# ═════════════════════════════════════════════════════════════════════════════

# TODO: delete this line and paste Part 5 here

# ───── end of Part 5 ───────────────────────────────────────────────────────

# ═════════════════════════════════════════════════════════════════════════════
#  PART 6 · The Care Kit
# ═════════════════════════════════════════════════════════════════════════════

# TODO: delete this line and paste Part 6 here

# ───── end of Part 6 ───────────────────────────────────────────────────────

# ═════════════════════════════════════════════════════════════════════════════
#  PART 7 · The Page Skeleton
# ═════════════════════════════════════════════════════════════════════════════

# Part 7 · The Page Skeleton 🦴
# Lays out every piece you see on the page: screen, speech bubble, pet,
# sensor panel and buttons. Each piece has an id so the JavaScript can find it.

PAGE_HTML = r"""
<!DOCTYPE html>
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
"""

# ───── end of Part 7 ───────────────────────────────────────────────────────

# ═════════════════════════════════════════════════════════════════════════════
#  PART 8 · The Device Designer
# ═════════════════════════════════════════════════════════════════════════════

# Part 8 · The Device Designer 🎨
# Makes the page look like a handheld Tamagotchi toy: the egg-shaped
# body, the screen, the bars and the round buttons.

DEVICE_CSS = r"""
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
"""

# ───── end of Part 8 ───────────────────────────────────────────────────────

# ═════════════════════════════════════════════════════════════════════════════
#  PART 9 · The Animator
# ═════════════════════════════════════════════════════════════════════════════

# TODO: delete this line and paste Part 9 here

# ───── end of Part 9 ───────────────────────────────────────────────────────

# ═════════════════════════════════════════════════════════════════════════════
#  PART 10 · The Messenger
# ═════════════════════════════════════════════════════════════════════════════

# TODO: delete this line and paste Part 10 here

# ───── end of Part 10 ───────────────────────────────────────────────────────

# ═════════════════════════════════════════════════════════════════════════════
#  PART 11 · The Heart Monitor
# ═════════════════════════════════════════════════════════════════════════════

# TODO: delete this line and paste Part 11 here

# ───── end of Part 11 ───────────────────────────────────────────────────────

# ═════════════════════════════════════════════════════════════════════════════
#  PART 12 · The Web Server
# ═════════════════════════════════════════════════════════════════════════════

# TODO: delete this line and paste Part 12 here

# ───── end of Part 12 ───────────────────────────────────────────────────────


# ═════════════════════════════════════════════════════════════════════════════
#  BASIC SETUP · checks the 12 parts and wakes Momo up · don't edit below
# ═════════════════════════════════════════════════════════════════════════════

REQUIRED = [
    (1, "The Settings", "LEVEL_INFO"),
    (2, "The Face Designer", "get_face"),
    (3, "The Voice", "get_message"),
    (4, "The Body Sensors", "get_stats"),
    (5, "The Pet's Brain", "Pet"),
    (6, "The Care Kit", "do_action"),
    (7, "The Page Skeleton", "PAGE_HTML"),
    (8, "The Device Designer", "DEVICE_CSS"),
    (9, "The Animator", "PET_CSS"),
    (10, "The Messenger", "APP_JS"),
    (11, "The Heart Monitor", "HEARTBEAT_JS"),
    (12, "The Web Server", "run_server"),
]


def show_progress():
    done = 0
    for number, role, name in REQUIRED:
        ready = name in globals()
        done += ready
        print(("  ✅" if ready else "  ⏳") + "  Part " + str(number).rjust(2) + "  " + role)
    print("\n  " + str(done) + " / 12 parts ready\n")
    return done


def self_test():
    pet = Pet()
    for level in STRESS_LEVELS:
        assert pet.set_stress(level), "set_stress('" + level + "') failed"
        assert pet.to_dict()["level"] == level
    assert do_action(pet, "breathe") and pet.level == "medium", "breathe should calm heavy to medium"


if __name__ == "__main__":
    print("\n🐣 Momo the Stress Pet\n")
    if show_progress() < 12:
        print("Momo wakes up when all 12 parts are in.\n")
        sys.exit(0)
    try:
        self_test()
    except Exception as error:
        sys.exit("⚠️  All 12 parts are in, but something is off: " + str(error))
    if "check" in sys.argv:
        print("🎉 Everything works! Run  python momo.py  to wake Momo up.\n")
    else:
        run_server()
