
# 🎵 Esound to Deezer - Auto Like Music Bot

Ce projet Python automatise la récupération des titres que vous avez likés sur l'application **Esound** pour ensuite les rechercher et les liker automatiquement sur **Deezer**.  
Très utile pour synchroniser vos coups de cœur entre différentes plateformes de streaming musical 🎶

## Fonctionnalités

- ✅ Récupération des titres likés depuis Esound.
- ✅ Automatisation complète du like des titres sur Deezer.
- ✅ Gestion des titres non trouvés et en cas de doute.
- ✅ Cookies persistants pour éviter les reconnexions manuelles.
- ✅ Vérification de la popularité d’un titre pour éviter les faux positifs.
- ✅ Simulation réaliste pour limiter les risques de détection anti-bot.

## Prérequis

- Python 3.7 ou plus
- Navigateur Chrome
- Compte Deezer
- Compte Esound

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/ton-utilisateur/esound-to-deezer.git
   cd esound-to-deezer

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
