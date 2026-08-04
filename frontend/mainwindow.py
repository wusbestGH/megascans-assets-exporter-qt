# Copyright (C) 2026 wusbestGH
# SPDX-License-Identifier: GPL-3.0-only
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from frontend.settingswindow import SettingsWindow
from backend.config import settings

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Megascans Assets Importer")
        self.setMinimumSize(QSize(640, 480))

        self.init_toolbars() # Initialize toolbars (bottom and top)

    def init_toolbars(self):
        # Status variable
        self.status_bar: str = ""

        # Top Toolbar
        self.top_toolbar = QToolBar("Top Toolbar")
        # self.top_toolbar.setMovable(False)
        self.addToolBar(Qt.TopToolBarArea, self.top_toolbar)

        # Settings button
        self.settings_action = QPushButton("Settings")
        self.settings_action.clicked.connect(self.open_settings)
        self.top_toolbar.addWidget(self.settings_action)

        # Bottom Toolbar
        self.bottom_toolbar = QToolBar("Bottom Toolbar")
        self.bottom_toolbar.setMovable(False)
        self.addToolBar(Qt.BottomToolBarArea, self.bottom_toolbar)

        # Status Label
        self.status_label = QLabel(self.status_bar)
        self.status_label.setContentsMargins(5, 0, 5, 0)
        self.bottom_toolbar.addWidget(self.status_label)

        # Spacer
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.top_toolbar.addWidget(spacer)

        # Export button
        self.export_btn = QPushButton("EXPORT")
        self.top_toolbar.addWidget(self.export_btn)

    # Click settings to open settings window
    def open_settings(self):
        dialog = SettingsWindow(self) # Initialize SettingsWindow

        # Save new settings when click button Save Settings
        if dialog.exec():
            new_data = dialog.get_input_data() # Get settings from SettingsWindow.get_input_data
            settings.save_settings(new_data) # Function to save new settings
            settings.settings_data = new_data # Update json variable

            self.update_status("Settings saved successfully!")

    def update_status(self, message):
        self.status_label.setText(f"STATUS: {message}") # Change status in bottom toolbar
        print(f"[STATUS] {message}")