"""Compatibility alias for the corrected completed-engine master checker."""
import pathlib, runpy
runpy.run_path(str(pathlib.Path(__file__).with_name("completed_physical_engine_master_checks.py")),run_name="__main__")
