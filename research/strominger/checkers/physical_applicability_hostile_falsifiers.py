"""Compatibility alias for the corrected twelve-gate hostile checker."""
import pathlib, runpy
runpy.run_path(str(pathlib.Path(__file__).with_name("completed_physical_engine_hostile_falsifiers.py")),run_name="__main__")
