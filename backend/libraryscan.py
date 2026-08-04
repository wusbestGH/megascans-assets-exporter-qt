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

import os, json

from backend.config import settings


class LibraryAssets():
    def __init__(self):
        pass

    # Scanning folder for assets
    def libraryscan(self):
        json_settings = settings.settings_data
        data = json.loads(json_settings) # Load json settings
        folder_path = data["path"] # Folder path

        library_files = os.listdir(folder_path)
        for file_name in library_files:
            pass