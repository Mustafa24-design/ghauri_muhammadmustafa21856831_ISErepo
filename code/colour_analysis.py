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

# Function: Compare two frequencies
def compare_frequencies(freq1, freq2):
    col1 = frequency_to_colour(freq1)
    col2 = frequency_to_colour(freq2)
    if "Red" in col1 or "Violet" in col1 or "Unknown" in col1 or \
       "Red" in col2 or "Violet" in col2 or "Unknown" in col2:
        return f"One or both frequencies are outside the visible range: {col1}, {col2}"
    elif col1 == col2:
        return f"Both frequencies represent the same colour: {col1}"
    else:
        return f"Different colours: {col1} and {col2}"

# Function: Get stone associated with a colour
def get_stone(colour):
    return colour_stones.get(colour.lower(), "Invalid colour")

# Function: Get music note associated with a colour
def get_music_note(colour):
    return colour_music_notes.get(colour.lower(), "Invalid colour")

# Function: Get emotion associated with a colour
def get_emotion(colour):
    return colour_emotions.get(colour.lower(), "Invalid colour")

def display_valid_colours():
    print("Valid colours: violet, blue, cyan, green, yellow, orange, red")
    
def read_frequency_from_file(filename):
    """Reads a frequency value from a text file (first line only)."""
    with open(filename, 'r') as file:
        return int(file.readline().strip())


def main():
    while True:
        print("\nColour Analysis Tool")
        print("1. Get frequency range for a colour")
        print("2. Convert frequency (THz) to wavelength (nm)")
        print("3. Convert wavelength (nm) to frequency (THz)")
        print("4. Determine spectrum range of a frequency")
        print("5. Determine colour from frequency")
        print("6. Compare two frequencies")
        print("7. Get gemstone for a colour")
        print("8. Get musical note for a colour")
        print("9. Get emotion associated with a colour")
        print("10. Load frequency from file and determine colour")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_valid_colours()
            colour = input("Enter colour name: ").strip().lower()
            print("Frequency range:", get_frequency_range(colour))

        elif choice == "2":
            freq = float(input("Enter frequency in THz: "))
            print("Wavelength (nm):", frequency_to_wavelength(freq))

        elif choice == "3":
            wavelength = float(input("Enter wavelength in nm: "))
            print("Frequency (THz):", wavelength_to_frequency(wavelength))

        elif choice == "4":
            freq = float(input("Enter frequency in THz: "))
            print("Spectrum range:", get_spectrum_range(freq))

        elif choice == "5":
            freq = float(input("Enter frequency in THz: "))
            print("Associated colour:", frequency_to_colour(freq))

        elif choice == "6":
            freq1 = float(input("Enter first frequency in THz: "))
            freq2 = float(input("Enter second frequency in THz: "))
            print(compare_frequencies(freq1, freq2))

        elif choice == "7":
            display_valid_colours()
            colour = input("Enter colour name: ").strip().lower()
            print("Gemstone:", get_stone(colour))

        elif choice == "8":
            display_valid_colours()
            colour = input("Enter colour name: ").strip().lower()
            print("Music note:", get_music_note(colour))

        elif choice == "9":
            display_valid_colours()
            colour = input("Enter colour name: ").strip().lower()
            print("Emotion:", get_emotion(colour))
            

        elif choice == "10":
            filename = input("Enter filename: ")
            try:
                freq = read_frequency_from_file(filename)
                print("Frequency read:", freq)
                print("Associated colour:", frequency_to_colour(freq))
            except Exception as e:
                print("Error reading file:", e)

        elif choice == "0":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
