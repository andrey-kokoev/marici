"""Conditional GeV calibration of the equal-direction tower.

Trial identification: the entire retained rung-4 budget is 125 GeV.
This uses the documented Higgs value as an input; it does not derive that
identification, the Higgs mass, or a universal physical tower energy.
"""
from fractions import Fraction as F

reference_rung = 4
reference_gev = F(125)
per_direction = reference_gev/reference_rung
full_gev = 12*per_direction
assert full_gev == 375
print('ASSUMPTIONS: equal directional energy, fixed metric/clock, E4=125 GeV.')
print('r | retained GeV | recorded GeV | total GeV')
for r in range(12, 3, -1):
    retained = r*per_direction
    recorded = (12-r)*per_direction
    assert retained+recorded == full_gev
    assert retained/full_gev == F(r, 12)
    assert retained/reference_gev == F(r, reference_rung)
    print(f'{r:2} | {float(retained):8.2f} | {float(recorded):8.2f} | {float(full_gev):8.2f}')
# Reference identifications change the answer: same 125 GeV at rung12 yields
# total125 GeV and rung4=125/3 GeV. Neither anchor is selected by dimension.
assert 12*reference_gev/12 == 125
assert 4*reference_gev/12 == F(125, 3)
print('Same input assigned to rung12 instead: total125 GeV, E4=125/3 GeV.')
print('Calibration checks passed exactly. The anchor-to-rung identification remains a physical assumption.')
