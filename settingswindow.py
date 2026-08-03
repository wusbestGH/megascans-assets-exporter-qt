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

from PySide6.QtWidgets import *

class SettingsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        print("Settings window opened.")
        self.setWindowTitle("Settings")
        self.setFixedSize(300, 220)

        self.layout = QVBoxLayout(self)

        self.port_layout = QHBoxLayout()
        self.port_label = QLabel("PORT:")
        self.port_input = QLineEdit()
        self.port_layout.addWidget(self.port_label)
        self.port_layout.addWidget(self.port_input)

        self.app_layout = QHBoxLayout()
        self.app_label = QLabel("APP:")
        self.app_combo = QComboBox()
        self.app_combo.addItems(["Blender", "Cinema 4D", "Maya", "Houdini"])
        self.app_layout.addWidget(self.app_label)
        self.app_layout.addWidget(self.app_combo)

        self.quality_layout = QHBoxLayout()
        self.quality_label = QLabel("QUALITY:")
        self.quality_combo = QComboBox()
        self.quality_combo.addItems(["1K", "2K", "4K", "8K"])

        self.quality_layout.addWidget(self.quality_label)
        self.quality_layout.addWidget(self.quality_combo)

        self.path_layout = QHBoxLayout()
        self.path_label = QLabel("PATH:")
        self.path_input = QLineEdit()
        self.path_layout.addWidget(self.path_label)
        self.path_layout.addWidget(self.path_input)

        self.save_btn = QPushButton("Save Settings")
        self.save_btn.clicked.connect(self.accept)

        self.layout.addLayout(self.port_layout)
        self.app_layout.addWidget(self.app_combo)
        self.layout.addLayout(self.app_layout)
        self.layout.addLayout(self.quality_layout)
        self.layout.addLayout(self.path_layout)
        self.layout.addWidget(self.save_btn)

    def get_input_data(self):
        return {
            "path": self.path_input.text(),
            "app": self.app_combo.currentText(),
            "quality": self.quality_combo.currentText(),
            "port": self.port_input.text()
        }
