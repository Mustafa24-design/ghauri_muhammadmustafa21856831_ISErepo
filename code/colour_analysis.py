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

# Function: Convert frequency (THz) to wavelength (nm)
def frequency_to_wavelength(frequency_thz):
    return round(300000 / frequency_thz, 2)

# Function: Convert wavelength (nm) to frequency (THz)
def wavelength_to_frequency(wavelength_nm):
    return round(300000 / wavelength_nm, 2)

# Function: Check spectral range of frequency
def get_spectrum_range(frequency_thz):
    if 400 <= frequency_thz <= 790:
        return "Visible"
    elif 791 <= frequency_thz <= 30000:
        return "Ultraviolet"
    elif 1 <= frequency_thz <= 399:
        return "Infrared"
    else:
        return "Out of Range"

# Function: Determine colour by frequency
def frequency_to_colour(frequency_thz):
    for colour, (low, high) in colour_frequency_ranges.items():
        if low <= frequency_thz <= high:
            return colour
    if frequency_thz < 400:
        return "Below Red (Infrared)"
    elif frequency_thz > 790:
        return "Above Violet (Ultraviolet)"
    return "Unknown"

# Example usage for testing
if __name__ == "__main__":
    print(get_frequency_range("Green"))
    print(get_frequency_range("Cyan"))
    print(frequency_to_wavelength(500))          
    print(wavelength_to_frequency(600))   
    print(get_spectrum_range(830))  
    print(get_spectrum_range(630))              
    print(frequency_to_colour(710))  
    print(frequency_to_colour(510))             