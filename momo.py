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

# Part 6 · The Care Kit 🧘
# Ways to help Momo relax. Each one lowers stress by one step
# (heavy -> medium -> light) and Momo says thanks.

ACTIONS = {
    "breathe": "In... and out... That really helped!",
    "walk": "A little walk outside cleared my head!",
    "nap": "Zzz... I feel recharged!",
}


def calmer_level(level):
    index = STRESS_LEVELS.index(level)
    return STRESS_LEVELS[max(index - 1, 0)]


def do_action(pet, action_name):
    """Do a care action. Returns Momo's reply, or None if the action is unknown."""
    if action_name not in ACTIONS:
        return None
    pet.set_stress(calmer_level(pet.level))
    return ACTIONS[action_name]


# ───── end of Part 6 ───────────────────────────────────────────────────────

# ═════════════════════════════════════════════════════════════════════════════
#  PART 7 · The Page Skeleton
# ═════════════════════════════════════════════════════════════════════════════

# TODO: delete this line and paste Part 7 here

# ───── end of Part 7 ───────────────────────────────────────────────────────

# ═════════════════════════════════════════════════════════════════════════════
#  PART 8 · The Device Designer
# ═════════════════════════════════════════════════════════════════════════════

# TODO: delete this line and paste Part 8 here

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

# Part 11 · The Heart Monitor 📈
# JavaScript that draws a hospital-style ECG line. It beats faster and
# changes color when Momo is stressed.

HEARTBEAT_JS = r"""
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
"""


# ───── end of Part 11 ───────────────────────────────────────────────────────

# ═════════════════════════════════════════════════════════════════════════════
#  PART 12 · The Web Server
# ═════════════════════════════════════════════════════════════════════════════

# Part 12 · The Web Server 🌐
# Starts a tiny website on your laptop. It sends the page (Parts 7–11) to the
# browser and answers its questions: "how is Momo?", "set stress to heavy!"

PAGES = {
    "/": ("PAGE_HTML", "text/html"),
    "/style.css": ("DEVICE_CSS", "text/css"),
    "/pet.css": ("PET_CSS", "text/css"),
    "/app.js": ("APP_JS", "text/javascript"),
    "/heartbeat.js": ("HEARTBEAT_JS", "text/javascript"),
}


class PetHandler(BaseHTTPRequestHandler):
    def send(self, text, content_type, status=200):
        body = text.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type + "; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def send_pet(self, message=None):
        data = momo.to_dict()
        if message:
            data["message"] = message
        self.send(json.dumps(data), "application/json")

    def do_GET(self):
        url = urlparse(self.path)
        query = parse_qs(url.query)

        if url.path == "/api/pet":                       # "How is Momo?"
            self.send_pet()
        elif url.path == "/api/stress":                  # "Set stress to heavy!"
            level = query.get("level", [""])[0]
            if momo.set_stress(level):
                self.send_pet()
            else:
                self.send(json.dumps({"error": "Unknown level: " + level}), "application/json", 400)
        elif url.path == "/api/action":                  # "Help Momo relax!"
            reply = do_action(momo, query.get("name", [""])[0])
            if reply:
                self.send_pet(reply)
            else:
                self.send(json.dumps({"error": "Unknown action"}), "application/json", 400)
        elif url.path in PAGES:                          # the page itself
            variable, content_type = PAGES[url.path]
            self.send(globals()[variable], content_type)
        else:
            self.send("Not found", "text/plain", 404)

    def log_message(self, format, *args):
        pass  # keep the terminal quiet


def run_server():
    global momo
    momo = Pet()
    server = HTTPServer(("localhost", PORT), PetHandler)
    print("🐣 " + PET_NAME + " is alive at  http://localhost:" + str(PORT))
    print("   (press Ctrl + C to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 Bye! " + PET_NAME + " is sleeping now.")


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
