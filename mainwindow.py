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
from settingswindow import SettingsWindow
from settingsjson import JsonSettings

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Megascans Assets Importer")
        self.setMinimumSize(QSize(640, 480))

        self.json_settings = JsonSettings()
        self.json_settings.json_create_read()

        self.init_toolbars()

    def init_toolbars(self):
        self.status_bar: str = ""

        self.top_toolbar = QToolBar("Top Toolbar")
        self.top_toolbar.setMovable(False)
        self.addToolBar(Qt.TopToolBarArea, self.top_toolbar)

        self.settings_action = QPushButton("Settings")
        self.settings_action.clicked.connect(self.open_settings)
        self.top_toolbar.addWidget(self.settings_action)

        self.bottom_toolbar = QToolBar("Bottom Toolbar")
        self.bottom_toolbar.setMovable(False)
        self.addToolBar(Qt.BottomToolBarArea, self.bottom_toolbar)

        self.status_label = QLabel(self.status_bar)
        self.status_label.setContentsMargins(5, 0, 5, 0)
        self.bottom_toolbar.addWidget(self.status_label)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.bottom_toolbar.addWidget(spacer)

        self.export_btn = QPushButton("EXPORT")
        self.bottom_toolbar.addWidget(self.export_btn)

    def open_settings(self):
        dialog = SettingsWindow(self)
        if hasattr(self.json_settings, 'settings_data'):
            data = self.json_settings.settings_data
            dialog.port_input.setText(data.get("port", ""))
            dialog.path_input.setText(data.get("path", ""))
            app_index = dialog.app_combo.findText(data.get("app", ""))
            if app_index >= 0:
                dialog.app_combo.setCurrentIndex(app_index)
            quality_index = dialog.quality_combo.findText(data.get("quality", ""))
            if quality_index >= 0:
                dialog.quality_combo.setCurrentIndex(quality_index)

        if dialog.exec():
            new_data = dialog.get_input_data()
            self.json_settings.save_settings(new_data)
            self.json_settings.settings_data = new_data

            self.update_status("Settings saved successfully!")

    def update_status(self, message):
        self.status_label.setText(f"STATUS: {message}")
        print(f"[STATUS] {message}")