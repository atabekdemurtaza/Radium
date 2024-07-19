import asyncio
import aiohttp
import hashlib
from typing import List
from pathlib import Path

BASE_URL = 'https://gitea.radium.group/radium/project-configuration/src/branch/master/nitpick/'
FILES = [
    'all.toml',
    'darglint.toml',
    'editorconfig.toml',
    'file-structure.toml',
    'flake8.toml',
    'isort.toml',
    'pytest.toml',
    'styleguide.toml'
]


class RepoDownloader:
    def __init__(self, base_url: str, files: List[str]):
        self.base_url = base_url
        self.files = files

    async def download_file(self, session: aiohttp.ClientSession, url: str, dest: Path) -> None:
        async with session.get(url) as response:
            response.raise_for_status()
            content = await response.read()
            dest.write_bytes(content)

    async def download_all_files(self, dest_dir: Path) -> None:
        file_urls = [self.base_url + file for file in self.files]
        async with aiohttp.ClientSession() as session:
            tasks = [
                self.download_file(session, url, dest_dir / Path(url).name) for url in file_urls
            ]
            await asyncio.gather(*tasks)


class FileHasher:
    @staticmethod
    def calculate_sha256(file_path: Path) -> str:
        sha256 = hashlib.sha256()
        with file_path.open('rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                sha256.update(chunk)
        return sha256.hexdigest()
