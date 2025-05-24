import random

# Dictionary mapping moods to emojis
EMOJI_DICT = {
    "happy": ["😊", "😄", "😁"],
    "sad": ["😢", "😭", "😞"],
    "angry": ["😠", "😡", "🤬"],
    "love": ["❤️", "😍", "😘"],
    "confused": ["😕", "🤔", "😵"],
    "excited": ["🤩", "😃", "🥳"],
    "tired": ["😴", "🥱", "😪"],
    "bored": ["😐", "😑", "🙄"],
    "random": ["😂", "🤪", "😎", "👻", "💩", "🫠"]
}

# Dictionary mapping moods to messages
MOOD_MESSAGES = {
    "happy": ["Keep smiling!", "Happiness is contagious!", "Your vibe is awesome!"],
    "sad": ["It's okay to feel sad. Brighter days are coming.", "Sending virtual hugs 💙"],
    "angry": ["Take a deep breath... and maybe some chocolate 🍫", "Smash stress with kindness!"],
    "love": ["Love is in the air!", "Someone loves you!"],
    "confused": ["When in doubt, take a nap 😴", "Confusion is just learning in progress!"],
    "excited": ["Woohoo! Keep up the energy!", "You’re on fire today! 🔥"],
    "tired": ["Nap > Everything.", "Get some rest. You’ve earned it!"],
    "bored": ["Try something new!", "Boredom is creativity waiting to happen."],
    "random": ["You're unpredictable and fun!", "Chaos is your superpower! 🌀"]
}

def get_emoji(mood: str) -> str:
    """
    Return a random emoji for the given mood.
    """
    mood = mood.lower()
    return random.choice(EMOJI_DICT.get(mood, ["🤷 Mood not found"]))

def get_mood_message(mood: str) -> str:
    """
    Return a mood-based message with an emoji.
    """
    mood = mood.lower()
    if mood in EMOJI_DICT and mood in MOOD_MESSAGES:
        emoji = random.choice(EMOJI_DICT[mood])
        message = random.choice(MOOD_MESSAGES[mood])
        return f"{emoji} {message}"
    return "🤷 Mood not found, but you're still awesome!"
