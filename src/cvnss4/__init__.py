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
            "Please install Node.js (LTS) and ensure `node` is in PATH, then retry."
        )
    return node


def _converter_js_path() -> str:
    """
    Return absolute path to converter.js shipped inside the Python package.
    """
    p = resources.files("cvnss4").joinpath("converter.js")
    return str(p)


def convert(text: str, mode: Mode = "cqn") -> Dict[str, str]:
    """
    Convert text using the bundled JS converter (via Node.js).

    Parameters
    ----------
    text : str
        Input text.
    mode : {"cqn","cvn","cvss"}
        - "cqn"  : input is CQN  -> outputs {"cqn","cvn","cvss"}
        - "cvn"  : input is CVN  -> outputs {"cqn","cvn","cvss"}
        - "cvss" : input is CVSS -> outputs {"cqn","cvn","cvss"}

    Returns
    -------
    dict
        {"cqn": str, "cvn": str, "cvss": str}
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if mode not in ("cqn", "cvn", "cvss"):
        raise ValueError("mode must be one of: 'cqn', 'cvn', 'cvss'")

    node = _require_node()
    conv_path = _converter_js_path()

    # Node script:
    # - Read input from stdin (UTF-8)
    # - Take last 2 argv items: [converter_path, mode]
    #   (robust against any argv index shifts)
    js = r"""
const fs = require("fs");
const path = require("path");

const argv = process.argv;
const mode = argv.length >= 2 ? argv[argv.length - 1] : "cqn";
const convPath = argv.length >= 3 ? argv[argv.length - 2] : null;

if (!convPath) {
  console.error("Missing converter.js path argument.");
  process.exit(2);
}

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
        [node, "-e", js, conv_path, mode],
        input=text,
        text=True,
        encoding="utf-8",   # IMPORTANT: avoid Windows cp1252 issues
        errors="strict",
        capture_output=True,
    )

    if p.returncode != 0:
        raise RuntimeError((p.stderr or "").strip() or f"Node failed with code {p.returncode}")

    try:
        data = json.loads(p.stdout)
    except Exception as e:
        raise RuntimeError(f"Failed to parse JS output as JSON: {p.stdout!r}") from e

    # Ensure stable keys exist
    return {
        "cqn": data.get("cqn", ""),
        "cvn": data.get("cvn", ""),
        "cvss": data.get("cvss", ""),
    }


def convert_cqn(text: str) -> Dict[str, str]:
    return convert(text, mode="cqn")


def convert_cvn(text: str) -> Dict[str, str]:
    return convert(text, mode="cvn")


def convert_cvss(text: str) -> Dict[str, str]:
    return convert(text, mode="cvss")


__all__ = ["convert", "convert_cqn", "convert_cvn", "convert_cvss"]
