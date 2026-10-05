# Deadlock Anki Flashcard Generator

Generate Anki Flashcards for the items in Deadlock using info from https://www.deadlock-api.com and https://www.deadlock.wiki.

<img width="270" height="490" alt="Screenshot_20261005_184836_Firefox" src="https://github.com/user-attachments/assets/20b36796-a3ce-4374-8953-23eb0b107377" />


# Download
Use the cards live [here](https://ankiweb.net/shared/info/157173328).

Follow the below instructions to generate your own version of the cards.

# Installation
You must have python3 installed.

## Create a venv

`python3 -m venv .mw`

### Linux / Mac
`. .mw/bin/activate`

### Windows

`.mw\Scripts\activate`

## Install Python Dependencies
`pip install -r requirements.txt`

# Usage

`python3 gen_cards.py`

# Output

All contents are placed in the `build` folder. You must import the deck file's .txt and the images separately.

## Step 1: Images

Copy the flashcard images folder from `build/collection.media` to your Anki user folder. Look [here](https://docs.ankiweb.net/files.html#file-locations) to find where yours is.

## Step 2: Deck File
The deck file is located at `build/deadlock_anki_import.txt`. Import it into the Anki desktop client.

# Contact

discord: @allocsb
https://www.reddit.com/u/LavaSalesman/
