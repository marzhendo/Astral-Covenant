import time
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def type_text(text, delay=0.035):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(delay)
    print()


# ======================
# GENERIC MAGIC CIRCLE
# ======================
CIRCLE = r"""
        ✧        ✦        ✧
    ╔════════════════════════╗
    ║      ASTRAL GATE       ║
    ║        OPENING         ║
    ║    ◇      ✦      ◇     ║
    ║      INVOCATION        ║
    ╚════════════════════════╝
        ✦        ✧        ✦
"""

# ======================
# UNIQUE SERVANT VISUALS
# ======================

ARTORIA = r"""
            ✦
         ✧     ✦
            /\
           /  \
          /====\
           ||||
           ||||
        ✧  ||||  ✦
            ||
"""

EMIYA = r"""
        ✦        ✦
            /\
           /  \    →
      ----/====\--------
           \  /
            \/
        ✦        ✦
"""

MASH = r"""
          ╔══════╗
        ╔═╝      ╚═╗
       ║            ║
       ║   SHIELD   ║
       ║            ║
        ╚═╗      ╔═╝
          ╚══════╝
            ✦ ✧ ✦
"""


# ======================
# UNIQUE ANIMATION CORE
# ======================

def _base_intro():
    clear()
    print(CIRCLE)
    time.sleep(1)

    type_text("\nThe Astral Gate resonates...", 0.04)
    time.sleep(0.6)

    type_text("Mana converges into form...", 0.04)
    time.sleep(0.6)

    type_text("\nA heroic spirit responds...", 0.05)
    time.sleep(1)


def _reveal(name, art):
    clear()
    print(art)
    time.sleep(0.8)

    clear()
    print(art)
    print("\n")
    type_text("COVENANT FORMED WITH:", 0.04)
    time.sleep(0.5)

    print(f"\n        ✦ {name.upper()} ✦\n")
    time.sleep(1.2)
    input("(Press ENTER)")


# ======================
# SERVANT-SPECIFIC
# ======================

def summon_artoria(name):
    _base_intro()
    type_text("\nA golden radiance pierces the sky...", 0.05)
    time.sleep(0.6)
    type_text("The sword of promised victory answers.", 0.05)
    time.sleep(0.8)
    _reveal(name, ARTORIA)


def summon_emiya(name):
    _base_intro()
    type_text("\nSteel echoes across the void...", 0.05)
    time.sleep(0.6)
    type_text("Countless blades trace a crimson horizon.", 0.05)
    time.sleep(0.8)
    _reveal(name, EMIYA)


def summon_mash(name):
    _base_intro()
    type_text("\nA gentle light shields your soul...", 0.05)
    time.sleep(0.6)
    type_text("A guardian steps forward to protect you.", 0.05)
    time.sleep(0.8)
    _reveal(name, MASH)


# ======================
# MAIN ROUTER
# ======================

def summon_animation(servant_name):

    if "Artoria" in servant_name:
        summon_artoria(servant_name)

    elif "Emiya" in servant_name:
        summon_emiya(servant_name)

    elif "Mash" in servant_name:
        summon_mash(servant_name)

    else:
        # fallback generic
        _base_intro()
        _reveal(servant_name, "✦")