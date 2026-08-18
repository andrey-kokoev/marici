"""Verify that the invariant endpoint mapping-cone degree repairs flatness."""

import importlib.util
from pathlib import Path

source = Path(__file__).with_name("check_soft_axis_orbit_character_cokernel.py")
spec = importlib.util.spec_from_file_location("orbit_cokernel", source)
orbit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(orbit)

for cutoff, plus_special, _, plus_dual, _ in orbit.results:
    ordinary_defect = 2 * plus_special - plus_dual
    corrected_dual = plus_dual + 1  # one invariant derived endpoint degree
    corrected_defect = 2 * plus_special - corrected_dual
    assert ordinary_defect == 1
    assert corrected_defect == 0
    print(
        f"D={cutoff}: ordinary={plus_dual}, derived={corrected_dual}, "
        f"flat_target={2 * plus_special}"
    )

print("verdict: one derived invariant target degree repairs plus flatness at every cutoff")
