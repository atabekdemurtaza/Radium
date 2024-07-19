from pathlib import Path
import tempfile
import hashlib

import pytest
from aioresponses import aioresponses

from scripts.file import RepoDownloader, FileHasher, BASE_URL, FILES

CONTENT = {
    'all.toml': b'content of all.toml',
    'darglint.toml': b'content of darglint.toml',
    'editorconfig.toml': b'content of editorconfig.toml',
    'file-structure.toml': b'content of file-structure.toml',
    'flake8.toml': b'content of flake8.toml',
    'isort.toml': b'content of isort.toml',
    'pytest.toml': b'content of pytest.toml',
    'styleguide.toml': b'content of styleguide.toml'
}


@pytest.mark.asyncio
async def test_repo_downloader():
    with aioresponses() as m:
        for file, content in CONTENT.items():
            m.get(BASE_URL + file, body=content)

        with tempfile.TemporaryDirectory() as temp_dir:
            dest_dir = Path(temp_dir)
            downloader = RepoDownloader(BASE_URL, FILES)

            await downloader.download_all_files(dest_dir)

            for file, content in CONTENT.items():
                file_path = dest_dir / file
                assert file_path.exists()
                assert file_path.read_bytes() == content


def test_file_hasher():
    for file, content in CONTENT.items():
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(content)
            temp_file_path = Path(temp_file.name)

        expected_hash = hashlib.sha256(content).hexdigest()
        hasher = FileHasher()
        assert hasher.calculate_sha256(temp_file_path) == expected_hash

        temp_file_path.unlink()
