"""SCC entrypoint for the Node source-replay execution-plan regression."""
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[3]
if __name__ == "__main__":
    subprocess.run(
        ["node", "research/nima/checkers/check_atlas_execution_plans.mjs"],
        cwd=ROOT,
        check=True,
    )
