# Deadlock Anki Flashcard Generator

Generate Anki Flashcards for the items in Deadlock using info from https://www.deadlock-api.com and https://www.deadlock.wiki.

# Download
`git clone xxx`
or
Download the master branch from github

# Installation
You must have python3 installed.

## create a venv

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

The flashcard images must be copied from `build/collection.media` to your Anki user folder. Look [here](https://docs.ankiweb.net/files.html#file-locations) to find where yours is.

## Step 2: Deck File
The deck file is located at `build/deadlock_anki_import.txt`. Import it into the Anki desktop client.
