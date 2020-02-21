# audio_sifter
a quick UI for cleaning audio files for network training

- Not polished for general use.
- Made to quickly sift 5 second audio files for target training data
- Accepts a folder full of audio files
- Generates a keep and toss subfolder in the given folder
- Plays audio files from the given folder, providing quick keep/toss hotkeys
- By default plays audio starting after 1.5 seconds and stopping after 3.5seconds
 - This is to ensure the target audio survives timeshifting and pitch shifting during augmentation
- Has playback speed & volume controls
- Has an undo button

- Requires PyQt5, built on Qt framework

Example audio files were sourced from the [he Macaulay Library](https://www.macaulaylibrary.org/).
Example audio files are named as A_B_C_D.wav, where:
 - A is the genus name
 - B is species name
 - C is accession number
 - D is a 5 second subsample number cut from larger full audio file.
