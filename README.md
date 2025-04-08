
# 🎵 Esound to Deezer - Auto Like Music Bot

This Python project automates the retrieval of tracks you've liked on the **Esound** app and then searches for and likes them automatically on **Deezer**. It's perfect for syncing your favorite music across different streaming platforms 🎶

## Features

- ✅ Retrieves liked tracks from Esound.
- ✅ Fully automates liking tracks on Deezer.
- ✅ Handles unfound tracks and ambiguous matches.
- ✅ Persistent cookies to avoid manual re-logins.
- ✅ Popularity check to avoid false positives.
- ✅ Realistic simulation to minimize anti-bot detection risks.

## Prerequisites

- Python 3.7 or higher
- Chrome browser
- Deezer account
- Esound account

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/esound-to-deezer.git
   cd esound-to-deezer
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables for Deezer and Esound credentials.

## ⚙️ How to Use

1. **Open the Esound web app**
   Go to the playlist or favorites section you want to export.

2. **Open your browser console**
   - Chrome: `Ctrl + Shift + J` (Windows/Linux) or `Cmd + Option + J` (Mac)
   - Firefox: `Ctrl + Shift + K` (Windows/Linux) or `Cmd + Option + K` (Mac)

3. **Copy and paste the script into the console**, then press `Enter`.

4. **Manually scroll through the full playlist**
   Scroll all the way down to let the app load new songs progressively.
   ✅ The script runs in the background and collects each song as they load.

5. **Export your music list**
   Once you’ve finished scrolling to the bottom of the list, type the following command in the console and press `Enter`:

   ```javascript
   exportMusiques();
   ```

   This will download a `musiques.json` file containing all the tracks you collected.

## 📂 Output

The exported JSON file will look like this:

```json
[
  {
    "title": "Song Title 1",
    "artist": "Artist Name 1"
  },
  {
    "title": "Song Title 2",
    "artist": "Artist Name 2"
  }
  // ...and so on
]
```

This JSON file should then be used with the script located in the GitHub repository to automate the process of liking the tracks on Deezer. You can find the script [here](https://github.com/Awksys/EsoundToDeezer/edit/main/LikeOnDeezer.py).

## 💡 Notes

- Avoid refreshing the page after running the script, or you'll lose collected data.
- The export works at any time — but make sure to scroll until the end of the list for a complete export!
- No installation needed — pure browser script.

## 🛠️ Disclaimer

This tool is intended for personal use only. Respect Esound’s terms of service and copyright laws when exporting your playlists.
