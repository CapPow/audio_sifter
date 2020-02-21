#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#    This program is free software; you can redistribute it and/or
#    modify it under the terms of the GNU General Public License
#    as published by the Free Software Foundation; either version 3
#    of the License, or (at your option) any later version.
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

"""
    Audio Sifter - a quick a dirty program built to quickly sift audio files
"""

__author__ = "Caleb Powell"
__credits__ = ["Caleb Powell"]
__email__ = "calebadampowell@gmail.com"
__status__ = "Alpha"
__version__ = 'v0.0.1-alpha'

import os
import sys
import glob
from shutil import move as shutil_move

# UI libs
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer

# UI elements
from src.main_window import Ui_MainWindow


if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class appWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.mainWindow = Ui_MainWindow()
        self.mainWindow.setupUi(self)
        self.player = QMediaPlayer()
        
        # class variables
        self.audio_files = []
        self.initial_audio_count = 0
        self.current_audio_file = ""
        self.audio_file_index = 0
        self.dir_path = ""
        self.toss_path = ""
        self.keep_path = ""
        self.previous_path = ""

         # setup static UI buttons
        self.mainWindow.folder_toolButton.pressed.connect(self.read_folder)
        self.mainWindow.skip_toolButton.pressed.connect(self.skip_current_audio)
        self.mainWindow.toss_toolButton.pressed.connect(self.toss_current_audio)
        self.mainWindow.keep_toolButton.pressed.connect(self.keep_current_audio)
        self.mainWindow.play_toolButton.pressed.connect(self.set_current_audio)
        self.mainWindow.back_toolButton.pressed.connect(self.back_button)
        
        # initialize widget based settings 
        self.toggle_play_entire(1)
        self.set_vol(75)
        
    def back_button(self):
        # used to revert or undo a choice
        # first move the file back
        base_name = os.path.basename(self.previous_path)
        dst_path = os.path.join(self.dir_path +"/"+ base_name)
        shutil_move(self.previous_path, dst_path)
        self.audio_files.insert(self.audio_file_index, dst_path)
        self.set_current_audio()
        # update the progress bar
        self.update_progress_bar

    def toss_current_audio(self):
        base_name = os.path.basename(self.current_audio_file)
        toss_dst = os.path.join(self.toss_path +"/"+ base_name)
        shutil_move(self.current_audio_file, toss_dst)
        self.previous_path = toss_dst
        self.remove_current_item()
        
    def keep_current_audio(self):
        base_name = os.path.basename(self.current_audio_file)
        keep_dst = os.path.join(self.keep_path +"/"+ base_name)
        shutil_move(self.current_audio_file, keep_dst)
        self.previous_path = keep_dst
        self.remove_current_item()
        
    def remove_current_item(self):
        self.audio_files.pop(self.audio_file_index)
        self.set_current_audio()
        # update the progress bar
        self.update_progress_bar()
    
    def update_progress_bar(self):
        len_audio_files = len(self.audio_files)
        initial_audio_count = self.initial_audio_count
        completed_audio_count = initial_audio_count - len_audio_files
        progress_value = int( (completed_audio_count / initial_audio_count) * 100 )
        self.mainWindow.progressBar.setValue(progress_value)

    def read_folder(self):
        dir_path = QtWidgets.QFileDialog.getExistingDirectory(self,
                                                            "Select Audio Directory")
        self.dir_path = dir_path
        # set the toss and keep paths, and be sure they exist
        toss_path = os.path.join(dir_path + "/toss")
        if not os.path.exists(toss_path ):
            os.makedirs(toss_path )
        self.toss_path = toss_path
        
        keep_path = os.path.join(dir_path + "/keep")
        if not os.path.exists(keep_path):
            os.makedirs(keep_path )
        self.keep_path = keep_path 
        self.set_audio_files()

    def set_audio_files(self):
        
        # get the audio files
        audio_files = list(set(glob.glob(f"{self.dir_path}/*.wav", recursive=False)))
        self.audio_files = audio_files

        # get the initial count of audio files
        self.initial_audio_count = len(audio_files)

        # set the current audio
        self.set_current_audio()

        # set the progress bar
        self.update_progress_bar()

    def set_current_audio(self):
        # identify which audio file to target
        try:
            current_audio_file = self.audio_files[self.audio_file_index]
        except IndexError:
            # if the list is empty, we are done!
            if len(self.audio_files) < 1:
                 self.mainWindow.name_label.setText("All Done!")
                 return
            else:
                # otherwise cycle back to 0 position in audio_files list
                self.audio_file_index = 0
                current_audio_file = self.audio_files[self.audio_file_index]
        # set the sci name text
        base_name = os.path.basename(current_audio_file)
        try:
            split_base = base_name.split("_")
            split_len = min(len(split_base), 4)
            label_name = " ".join(split_base[:split_len])
        except:
            label_name = base_name
        self.current_audio_file = current_audio_file
        self.mainWindow.name_label.setText(label_name)
        
        # now play the audio
        self.load_audio()
        self.player.play()

    def setInterval(self, path, start, end):
        """
            path: path of video
            start: time in ms from where the playback starts
            end: time in ms where playback ends
        """
        self.player.stop()
        self.player.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile(path)))
        self.player.setPosition(start)
        self._end = end
        self.player.play()

    def toggle_play_entire(self, _):
        if self.mainWindow.play_entire_checkBox.isChecked():
            self.start_pos = 0
            self.end_pos = 5000
        else:
            self.start_pos = 1500
            self.end_pos = 3500

    def load_audio(self):
        sound = QMediaContent(QtCore.QUrl.fromLocalFile(self.current_audio_file))
        self.player.setMedia(sound)
        self.player.setPosition(self.start_pos)
        
    @QtCore.pyqtSlot('qint64')
    def on_positionChanged(self, position):
        """
        Is called each time the player position changes....
        """
        if self.player.state() == QMediaPlayer.PlayingState:
            if position > self.end_pos:
                self.player.stop()
        
    def skip_current_audio(self):
        # iterage the index
        self.audio_file_index += 1
        # set the new current audio
        self.set_current_audio()
        
    def set_vol(self, level):
        self.vol = level
        self.player.setVolume(level)

    def set_playback(self, mul):
        speed = round(mul / 100, 3)
        self.mainWindow.playback_speed_label.setText(str(speed))
        self.player.setPlaybackRate(speed)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = appWindow()
    w.show()
    sys.exit(app.exec_())
