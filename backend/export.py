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

import os
import json
from pathlib import Path
from PySide6.QtCore import QThread, Signal, QSettings
from backend.config import settings

# Save button
class ExportAsset(QThread):
    def __init__(self):
        super().__init__()

    def export(self):
        print("Exporting asset")
        self.is_custom_port = False
        self.export_port = "" # Final export port
        selected_port = settings.settings_data.get("port", "")
        selected_app = settings.settings_data.get("app", "")

        # Check is custom port
        if selected_port == "":
            pass
        else:
            self.is_custom_port = True

        # Setting export port
        if self.is_custom_port == True:
            print("Custom port")
            self.export_port = selected_port
        else:
            if selected_app == "Blender":
                self.export_port = "0000"
            elif selected_app == "Cinema 4D":
                self.export_port = "0001"
            elif selected_app == "Maya":
                self.export_port = "0002"
            elif selected_app == "Houdini":
                self.export_port = "0003"
            else:
                print("Unknown app (what)")

            print(self.export_port)


