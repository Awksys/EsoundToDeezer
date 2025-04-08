
# 🎵 Esound Playlist Extractor

Extract all songs (titles and artists) from an **Esound web app** playlist or favorites directory.

Run the script directly in your browser console and export your entire music list to a `.json` file.

---

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

---

## 📂 Output

The exported JSON file will look like this:

```json
[
  {
    "titre": "Song Title 1",
    "artiste": "Artist Name 1"
  },
  {
    "titre": "Song Title 2",
    "artiste": "Artist Name 2"
  }
  // ...and so on
]
```

---

## 💡 Notes

- Avoid refreshing the page after running the script, or you'll lose collected data.
- The export works at any time — but make sure to scroll until the end of the list for a complete export!
- No installation needed — pure browser script.

---

## 🛠️ Disclaimer

This tool is intended for personal use only.
Respect Esound’s terms of service and copyright laws when exporting your playlists.
