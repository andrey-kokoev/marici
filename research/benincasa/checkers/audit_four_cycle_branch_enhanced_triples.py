"""Compatibility entrypoint for the corrected forced-branch-node audit."""
import runpy
from pathlib import Path

runpy.run_path(
    str(Path(__file__).with_name("audit_four_cycle_forced_branch_nodes.py")),
    run_name="__main__",
)
