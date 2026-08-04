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

import json, os

# Create settings.json, read settings, or change settings
class JsonSettings:
    def __init__(self, filename="settings.json"):
        self.filename = filename
        self.settings_data = {}
        self.load_settings()

    def load_settings(self):
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0: # File exists and its not empty
            with open('settings.json', 'r') as file:
                self.settings_data = json.load(file) # Load json settings from file
                print("Settings:", self.settings_data)
        else:
            with open('settings.json', 'w') as file:
                json.dump({}, file) # Create settings.json
                print("Settings:", self.settings_data)

    def save_settings(self, data):
        print("Saving to JSON:", data)
        with open('settings.json', 'w') as file:
            json.dump(data, file) # Update settings from settings window

settings = JsonSettings()