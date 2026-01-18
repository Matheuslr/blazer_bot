import os
import random
import string

ZOHO_DOMAIN = os.getenv("ZOHO_DOMAIN")

def generate_password(length=12):
    if length < 8:
        raise ValueError("Password length should be at least 8")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%"
    
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols),
    ]

    all_chars = lowercase + uppercase + digits + symbols

    password += random.choices(all_chars, k=length - 4)

    random.shuffle(password)

    return "".join(password)


FIRST_NAME_WORDS = [
    "blaze", "frost", "shadow", "viper", "phantom", "rogue", "drake", "pixel",
    "storm", "ghost", "sniper", "slash", "venom", "cinder", "knight", "havoc",
    "inferno", "titan", "nova", "raven", "spike", "wraith", "hunter", "onyx",
    "turbo", "blitz", "fang", "vortex", "grim", "reaper", "ace", "fury",
    "dagger", "crimson", "specter", "chaos", "echo", "stryke", "bolt",
    "shiver", "phaze", "feral", "shade", "gale", "mystic", "iron", "talon",
    "clash", "drift", "volt", "rift", "ember", "snare", "warp", "grinder",
    "revolt", "hawk", "lunar", "crypt", "blight", "shroud", "vex", "infer",
    "glitch", "obsidian", "stormy", "drakon", "myst", "nexus", "claw", "ember",
    "lynx", "rune", "shard", "flame", "ashen", "havok", "frosty", "phantas",
    "ranger", "skull", "blade", "talus", "void", "sable", "rifted", "zephyr",
    "arcane", "pyro", "emberly", "dusk", "auric", "quill", "embera", "shadee",
    "glimmer", "echoes", "fable", "cinder", "hollow", "venom", "drifted", "shroud",
    "silva", "thorne", "relic", "stormer", "shadee", "lumen", "spire", "onyxia",
    "blazef", "grith", "talos", "raveny", "shiver", "grimly", "phazem", "crypta",
    "vortex", "runez", "frostl", "emberr", "night", "dusked", "tundra", "clove",
    "falcon", "hunter", "ashen", "sorrel", "gale", "wyrm", "pyros", "relics",
    "lore", "cairn", "storm", "skye", "shade", "rune", "myst", "gloom",
    "lynx", "void", "spike", "ember", "talon", "fable", "drake", "nox"
]

SECOND_NAME_WORDS = [
    "runner", "striker", "wander", "slicer", "breaker", "hunter", "stalker", "blader",
    "seeker", "sentry", "warden", "shadow", "sniper", "phantom", "rogue", "drifter",
    "treader", "vandal", "vortex", "storm", "spirit", "mystic", "blade", "ember",
    "gale", "frost", "cinder", "shade", "raven", "hawk", "wolf", "grim",
    "talon", "spike", "ghost", "reaper", "claw", "sable", "fury", "rift",
    "flame", "lynx", "onyx", "shard", "echo", "veil", "skye", "auric",
    "pyro", "dusk", "lore", "crypt", "zephyr", "spire", "blight", "hollow",
    "sorrel", "wyrm", "falcon", "tundra", "quill", "arcane", "shadowy", "blaze",
    "glimmer", "night", "lumen", "cairn", "shiver", "embera", "myst", "thorne",
    "clove", "phoenix", "ranger", "relic", "drakon", "sylph", "nyx", "phantas",
    "stormer", "shadee", "fable", "obsidian", "huntery", "skully", "talosy", "raveny",
    "grimly", "crypta", "vortexa", "frostl", "emberr", "dusky", "tundra", "clover",
    "falcony", "huntera", "ashen", "sorrely", "galea", "wyrmy", "pyros", "relics",
    "loree", "cairny", "stormy", "skyee", "shadey", "rune", "mysty", "glooma",
    "lynxy", "voida", "spikey", "emberly", "talona", "fablee", "drakey", "noxa",
    "phantomy", "strikera", "wandera", "slicera", "breakera", "huntere", "stalkera", "bladera",
    "seekera", "sentrya", "wardena", "shadowa", "snipera", "roguea", "driftera", "treadera",
    "vandala", "vortexa", "storma", "spirita", "mystica", "bladea", "embera", "galea",
    "frosta", "cindera", "shadea", "ravena", "hawka", "wolfa", "grima", "talona"
]



def generate_user():
    first = random.choice(FIRST_NAME_WORDS).lower()
    last = random.choice(SECOND_NAME_WORDS).lower()

    username = f"{first}{last}"
    email = f"{first}_{last}@{ZOHO_DOMAIN}"
    password = generate_password()

    return username,email,password