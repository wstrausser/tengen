from commitizen.providers import VersionProvider  # type: ignore
from pathlib import Path
import os


class Provider(VersionProvider):
    file = Path(os.environ["TENGEN_DIR"], "src", ".version")

    def get_version(self) -> str:
        return self.file.read_text()

    def set_version(self, version: str) -> None:
        self.file.write_text(version)
