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

from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Dict
import json

@dataclass
class Asset:
    name: str
    path: Path
    category: str
    asset_type: str
    preview: Optional[Path] = None
    json_path: Optional[Path] = None
    textures: List[Path] = None

    def __post_init__(self):
        if self.textures is None:
            self.textures = []

class AssetScanner:
    def __init__(self, root_path: str):
        self.root = Path(root_path)
        self.assets: List[Asset] = []

    def scan(self) -> List[Asset]:
        self.assets = []

        for main_dir in ['Custom', 'Downloaded']:
            main_path = self.root / main_dir
            if not main_path.exists():
                continue

            for category_path in main_path.iterdir():
                if category_path.is_dir():
                    self._scan_category(category_path, main_dir)

        temp_path = self.root / 'temp'
        if temp_path.exists():
            for asset_path in temp_path.iterdir():
                if asset_path.is_dir():
                    self._add_asset(asset_path, 'temp', self._detect_asset_type(asset_path))

        return self.assets

    def _scan_category(self, category_path: Path, main_dir: str):
        category_name = category_path.name

        for asset_path in category_path.iterdir():
            if not asset_path.is_dir():
                continue

            asset_type = self._detect_asset_type(asset_path)
            self._add_asset(asset_path, f"{main_dir}/{category_name}", asset_type)

    def _detect_asset_type(self, asset_path: Path) -> str:
        if (asset_path / 'source').exists() or (asset_path / 'textures').exists():
            return '3d_asset'

        json_files = list(asset_path.glob('*.json'))
        if json_files:
            return 'texture'

        if list(asset_path.rglob('*.fbx')) or list(asset_path.rglob('*.obj')):
            return '3d_asset'

        return 'unknown'

    def _add_asset(self, asset_path: Path, category: str, asset_type: str):
        name = asset_path.name

        json_files = list(asset_path.glob('*.json'))
        json_path = json_files[0] if json_files else None

        preview = None
        textures = []

        texture_extensions = ['.jpg', '.jpeg', '.png', '.tga', '.exr']
        for ext in texture_extensions:
            textures.extend(asset_path.glob(f'*{ext}'))
            textures.extend(asset_path.glob(f'*/*{ext}'))

        if textures:
            preview = textures[0]

        asset = Asset(
            name=name,
            path=asset_path,
            category=category,
            asset_type=asset_type,
            preview=preview,
            json_path=json_path,
            textures=textures[:10]
        )

        self.assets.append(asset)

    def get_assets_by_type(self, asset_type: str) -> List[Asset]:
        return [a for a in self.assets if a.asset_type == asset_type]

    def get_assets_by_category(self, category: str) -> List[Asset]:
        return [a for a in self.assets if category in a.category]

    def load_asset_json(self, asset: Asset) -> Dict:
        if not asset.json_path or not asset.json_path.exists():
            return {}

        with open(asset.json_path, 'r') as f:
            return json.load(f)