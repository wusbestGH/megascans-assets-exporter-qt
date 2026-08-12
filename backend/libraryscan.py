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
from PySide6.QtCore import QThread, Signal
from backend.config import settings


class LibraryAssets(QThread):
    status_changed = Signal(str)
    assets_found = Signal(list)

    def __init__(self):
        super().__init__()

    def run(self):
        json_settings = settings.settings_data
        folder_path = json_settings.get("path", "")

        if not folder_path or not os.path.exists(folder_path):
            self.status_changed.emit("Error: Invalid library path!")
            return

        self.status_changed.emit("Scanning library...")
        found_assets = []
        path_obj = Path(folder_path)

        for json_file in path_obj.rglob("*.json"):
            if "cloud_library" in json_file.name or json_file.stem.startswith("Asset_"):
                continue

            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    raw_data = json.load(f)

                    asset_info = raw_data[0] if isinstance(raw_data, list) else raw_data

                    if "id" in asset_info and "name" in asset_info:
                        preview_path = self._find_preview(json_file.parent)

                        found_assets.append({
                            "id": asset_info["id"],
                            "name": asset_info["name"],
                            "type": asset_info.get("type", "unknown"),
                            "path": str(json_file.parent),
                            "preview": preview_path
                        })
            except Exception as e:
                continue

        self.assets_found.emit(found_assets)
        self.status_changed.emit(f"Found {len(found_assets)} assets.")

    def _find_preview(self, folder: Path) -> str:
        for img in folder.glob("*.png"):
            if "preview" in img.name.lower():
                return str(img)
        return ""
