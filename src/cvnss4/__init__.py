from __future__ import annotations

import json
import shutil
import subprocess
from importlib import resources
from typing import Dict, Literal

Mode = Literal["cqn", "cvn", "cvss"]


def _require_node() -> str:
    node = shutil.which("node")
    if not node:
        raise RuntimeError(
            "Node.js is required to use cvnss4 from Python.\n"
            "Please install Node.js (LTS) and ensure `node` is on PATH."
        )
    return node


def _converter_js_path() -> str:
    # converter.js is bundled as package-data (see pyproject.toml)
    p = resources.files("cvnss4").joinpath("converter.js")
    return str(p)


def convert(text: str, mode: Mode = "cqn") -> Dict[str, str]:
    """
    Convert text using the bundled JS converter (via Node.js).

    mode:
      - 'cqn'  : input is CQN -> outputs {cqn, cvn, cvss}
      - 'cvn'  : input is CVN -> outputs {cqn, cvn, cvss}
      - 'cvss' : input is CVSS -> outputs {cqn, cvn, cvss}
    """
    if mode not in ("cqn", "cvn", "cvss"):
        raise ValueError("mode must be one of: 'cqn', 'cvn', 'cvss'")

    node = _require_node()
    conv_path = _converter_js_path()

    # Read input from stdin to avoid command-length limits
    js = r"""
const fs = require("fs");
const path = require("path");

const convPath = process.argv[2];
const mode = process.argv[3] || "cqn";

const input = fs.readFileSync(0, "utf8");
const conv = require(path.resolve(convPath));

if (!conv || typeof conv.convert !== "function") {
  console.error("converter.js must export a function: convert(text, mode)");
  process.exit(2);
}

const out = conv.convert(input, mode);
process.stdout.write(JSON.stringify(out));
""".strip()

    p = subprocess.run(
        [node, "-e", js, "--", conv_path, mode],
        input=text,
        text=True,
        encoding="utf-8",
        errors="strict",
        capture_output=True,
    )

    if p.returncode != 0:
        raise RuntimeError((p.stderr or "").strip() or f"Node failed with code {p.returncode}")

    return json.loads(p.stdout)


__all__ = ["convert"]
