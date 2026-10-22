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

# # Part 5 · The Pet's Brain 🧠
# The Pet remembers its stress level and packs everything from
# Parts 1–4 into one bundle for the webpage.


class Pet:
    def __init__(self):
        self.name = PET_NAME                            # from Part 1
        self.level = DEFAULT_LEVEL

    def set_stress(self, level):
        """Change the stress level. Returns True if it worked."""
        if level not in STRESS_LEVELS:
            return False
        self.level = level
        return True

    def to_dict(self):
        """Everything the webpage needs to draw Momo."""
        return {
            "name": self.name,
            "level": self.level,
            "level_info": LEVEL_INFO[self.level],      # from Part 1
            "face": get_face(self.level),              # from Part 2
            "accessory": get_accessory(self.level),    # from Part 2
            "message": get_message(self.level),        # from Part 3
            "stats": get_stats(self.level),            # from Part 4
        }


# ───── end of Part 5 ───────────────────────────────────────────────────────

# ═════════════════════════════════════════════════════════════════════════════
#  PART 6 · The Care Kit
# ═════════════════════════════════════════════════════════════════════════════

# TODO: delete this line and paste Part 6 here

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
