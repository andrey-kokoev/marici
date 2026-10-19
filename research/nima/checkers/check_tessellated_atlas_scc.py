"""SCC Python entrypoint; the scientific regression is implemented in Node."""
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[3]
if __name__ == "__main__":
    subprocess.run(
        ["node", "research/nima/checkers/check_tessellated_atlas.mjs"],
        cwd=ROOT,
        check=True,
    )
