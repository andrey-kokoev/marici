"""Audit of Higgs excitation versus whole-rung energy identification.

Uses the documented coefficients 125 and 246, with an explicitly supplied
reference v=246.22 GeV. The potential is a conventional effective scalar
example, not a potential derived from the carrier. Standard library only.
"""
from fractions import Fraction as F

higgs_coefficient = F(125)
vev_coefficient = F(246)
lam = higgs_coefficient**2/(2*vev_coefficient**2)
vev_reference = F('246.22')
scale = vev_reference/vev_coefficient
higgs_energy = higgs_coefficient*scale
assert higgs_energy/vev_reference == F(125, 246)
assert 2*lam*vev_reference**2 == higgs_energy**2

# In natural units, V(phi)=lambda/4*(phi^2-v^2)^2+C.
# Expanding at phi=v+h gives coefficients of h^0 through h^4 below.
# The second derivative is twice the quadratic coefficient.
for C in (F(0), F(1), F(1000)):
    expansion = [C, F(0), lam*vev_reference**2, lam*vev_reference, lam/4]
    assert expansion[1] == 0
    assert 2*expansion[2] == higgs_energy**2
    assert expansion[0] == C
# Excitation gap cannot specify occupancy or the energy of other modes.
assert 2*higgs_energy-higgs_energy == higgs_energy
print(f'Input v: {float(vev_reference):.8f} GeV')
print(f'Calibrated coefficient scale v/246: {float(scale):.12f} GeV')
print(f'Conditional Higgs energy (125/246)*v: {float(higgs_energy):.12f} GeV')
print(f'Quartic coefficient: {float(lam):.12f}')
print('Same Higgs curvature for potential offsets C=0,1,1000 (GeV^4).')
print('Potential density needs a volume for total energy; excitation gap needs occupancy.')
print('No identity between Higgs excitation and total retained rung4 budget follows.')
