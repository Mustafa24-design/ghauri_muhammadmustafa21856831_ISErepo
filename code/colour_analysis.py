# File: colour_analysis.py

# Frequency ranges from Figure 1
colour_frequency_ranges = {
    'violet': (670, 790),
    'blue': (620, 669),
    'cyan': (600, 619),
    'green': (530, 599),
    'yellow': (510, 529),
    'orange': (480, 509),
    'red': (400, 479)
}

# Colour fun facts from Figure 2
colour_stones = {
    'violet': 'Amethyst',
    'blue': 'Opal',
    'cyan': 'Turquoise',
    'green': 'Emerald',
    'yellow': 'Topaz',
    'orange': 'Moonstone',
    'red': 'Garnet'
}

colour_music_notes = {
    'violet': 'B',
    'blue': 'A',
    'cyan': 'G',
    'green': 'F',
    'yellow': 'E',
    'orange': 'D',
    'red': 'C'
}

# Colour-emotion mappings
colour_emotions = {
    'violet': 'Bravery',
    'blue': 'Calm',
    'cyan': 'Calm',
    'green': 'Peaceful',
    'yellow': 'Happy',
    'orange': 'Happy',
    'red': 'Confidence'
}

# Constants
SPEED_OF_LIGHT = 3e8  # m/s

# Function: Get frequency range for a colour
def get_frequency_range(colour):
    return colour_frequency_ranges.get(colour.lower(), None)

# Example usage for testing
if __name__ == "__main__":
    print(get_frequency_range("Green"))
    print(get_frequency_range("Cyan"))