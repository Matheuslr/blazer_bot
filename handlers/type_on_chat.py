from random import choice, randint
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


FIRST_CHAT_MESSAGES = [
    # -------------------------
    # Friendly / neutral (EN)
    # -------------------------
    "hey chat 👋",
    "yo everyone",
    "what's up chat",
    "hello folks",
    "sup guys",
    "hey everyone",
    "good vibes here",
    "nice stream",
    "glhf everyone",
    "hi all",

    # -------------------------
    # Stream-related (EN)
    # -------------------------
    "first time here",
    "just joined the stream",
    "new here 👀",
    "found this stream randomly",
    "this stream is chill",
    "loving the vibe",
    "cool channel",
    "nice setup",
    "stream looks clean",
    "audio is good",

    # -------------------------
    # Gamer-style (EN)
    # -------------------------
    "let's gooo 🔥",
    "that was clean",
    "nice play",
    "good moves",
    "solid gameplay",
    "well played 👏",
    "that was smooth",
    "big brain play",
    "clutch moment",
    "insane round",

    # -------------------------
    # Casual / chatty (EN)
    # -------------------------
    "how's everyone doing?",
    "hope everyone's having a good day",
    "anyone else watching from mobile?",
    "just chilling here",
    "grabbing some snacks",
    "late night stream?",
    "perfect background stream",
    "this is relaxing",
    "time to lurk 😄",

    # -------------------------
    # Short & safe (EN)
    # -------------------------
    "yo",
    "gg",
    "nice",
    "clean",
    "solid",
    "wp",
    "cool",
    "chill",
    "fun",
    "🔥",

    # -------------------------
    # Slight personality (EN)
    # -------------------------
    "this popped up on my feed",
    "algorithm did something right",
    "glad I found this stream",
    "stream's underrated",
    "deserves more viewers",
    "this is actually fun to watch",
    "good energy here",
    "chat seems cool",

    # -------------------------
    # Lurker-friendly (EN)
    # -------------------------
    "mostly lurking 👀",
    "just watching",
    "lurking but had to say hi",
    "silent viewer here",
    "listening while working",
    "watching from work 😅",

    # -------------------------
    # Time-based (EN)
    # -------------------------
    "good morning chat",
    "good evening everyone",
    "good night stream",
    "late hours gang",
    "early squad",

    # -------------------------
    # Portuguese – Friendly
    # -------------------------
    "salve chat 👋",
    "e aí pessoal",
    "fala galera",
    "opa chat",
    "boa noite chat",
    "bom dia chat",
    "boa tarde pessoal",
    "cheguei agora",
    "salve salve",
    "tamo junto",

    # -------------------------
    # Portuguese – Stream related
    # -------------------------
    "primeira vez aqui",
    "acabei de chegar na live",
    "novo por aqui 👀",
    "caí aqui por acaso",
    "live bem tranquila",
    "curtindo a vibe",
    "canal top",
    "stream bem limpa",
    "áudio tá bom",
    "qualidade boa da live",

    # -------------------------
    # Portuguese – Gamer style
    # -------------------------
    "bela play",
    "jogada limpa",
    "mandou bem demais",
    "muito bem jogado",
    "que jogada",
    "play insana",
    "clutch demais",
    "jogada bonita",
    "skill pura",
    "absurdo isso aí",

    # -------------------------
    # Portuguese – Casual / chat
    # -------------------------
    "como tá o chat?",
    "como vcs estão?",
    "só de boa aqui",
    "assistindo de boa",
    "só acompanhando",
    "cheguei pra dar uma olhada",
    "bem tranquilo por aqui",
    "live boa pra relaxar",
    "ficar lurkando aqui",

    # -------------------------
    # Portuguese – Short & safe
    # -------------------------
    "salve",
    "gg",
    "nice",
    "boa",
    "top",
    "show",
    "clean",
    "massa",
    "brabo",
    "🔥",

    # -------------------------
    # Portuguese – Lurker vibes
    # -------------------------
    "só lurkando 👀",
    "mais assistindo mesmo",
    "na miúda aqui",
    "só de olho",
    "quietinho no chat",
    "trabalhando e assistindo 😅",

    # -------------------------
    # Mixed / natural
    # -------------------------
    "salve chat, nice play",
    "gg demais isso",
    "boa demais essa play",
    "nice demais",
    "clean demais",
    "gg wp",
    "brabo demais 🔥",
]


def type_on_chat(driver, logger, message=None, timeout=10):
    """
    Types a random first-message into the chat and sends it.
    """
    if not message: 
        message = choice(FIRST_CHAT_MESSAGES)
    logger.info(f"sending first chat message: '{message}'")

    chat_box = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//div[@contenteditable='true' and contains(@data-placeholder, 'Chat')]"
        ))
    )

    chat_box.click()
    sleep(randint(1, 2))

    chat_box.send_keys(Keys.CONTROL + "a")
    chat_box.send_keys(Keys.BACKSPACE)

    for char in message:
        chat_box.send_keys(char)
        sleep(randint(25, 90) / 1000)

    sleep(randint(1, 2))
    chat_box.send_keys(Keys.ENTER)

    logger.info("chat message sent")
