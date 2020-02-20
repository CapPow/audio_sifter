# audio_sifter
a quick UI for cleaning audio files for network training

- Not polished for general use.
- Made to quickly sift 5 second audio files for target training data
- Accepts a folder full of audio files
- Generates a keep and toss subfolder in the given folder
- Plays audio files from the given folder, providing quick keep/toss hotkeys
- Only plays audio starting after 1 second and stopping at 4 seconds
- Has playback speed & volume controls
- Has an undo button

- Requires PyQt5, built on Qt framework
