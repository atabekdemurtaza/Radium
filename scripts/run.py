import tempfile
import asyncio
from pathlib import Path
from file import RepoDownloader, FileHasher
from file import BASE_URL, FILES


async def main() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        dest_dir = Path(temp_dir)
        downloader = RepoDownloader(BASE_URL, FILES)
        await downloader.download_all_files(dest_dir)

        hasher = FileHasher()
        for file in dest_dir.rglob('*'):
            if file.is_file():
                print(f'{file.name}: {hasher.calculate_sha256(file)}')

if __name__ == '__main__':
    asyncio.run(main())
