from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


def main() -> int:
    root = Path(os.environ.get("LIANGMU_TOOL_ROOT", r"D:\企业知识萃取"))
    python = root / ".venv" / "Scripts" / "python.exe"
    package = root / "liangmu"
    if not root.is_dir() or not python.is_file() or not package.is_dir():
        print(
            "错误：找不到良木知识萃取工具。请设置 LIANGMU_TOOL_ROOT，"
            "其目录必须包含 .venv 和 liangmu。",
            file=sys.stderr,
        )
        return 2
    if not sys.argv[1:]:
        print("错误：缺少命令。可用命令：setup, folders, extract, associate, reindex, query, check", file=sys.stderr)
        return 2
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    return subprocess.call([str(python), "-m", "liangmu", *sys.argv[1:]], cwd=root, env=env)


if __name__ == "__main__":
    raise SystemExit(main())

