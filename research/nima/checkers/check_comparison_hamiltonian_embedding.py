# /// script
# dependencies = ["numpy>=2,<3"]
# ///
"""A Hamiltonian embedding of two closed sweeps, with explicit free choices.

Adds one stationary coordinate to pair the odd-dimensional fixed sector.
Principal two-sweep phases are a choice, not a derived physical clock.
"""
from pathlib import Path
import runpy
import numpy as np

s = runpy.run_path(str(Path(__file__).with_name('check_comparison_sweep_spectrum.py')))
U, values, V = s['U'], s['values'], s['vectors']
Vi = np.linalg.inv(V)
angles = np.angle(values**2)
angles[np.abs(angles) < 1e-8] = 0
assert np.sum(angles == 0) == 7

def real_matrix(diagonal):
    out = (V*diagonal) @ Vi
    assert np.max(np.abs(out.imag)) < 1e-8
    return out.real

B0 = real_matrix(1j*angles)
K0 = real_matrix(np.abs(angles))
J0 = real_matrix(1j*np.sign(angles))
assert np.max(np.abs(B0+B0.T)) < 1e-8
assert np.max(np.abs(K0-K0.T)) < 1e-8
assert np.max(np.abs(real_matrix(np.exp(1j*angles))-U@U)) < 1e-8
# Extend by one static coordinate to give an even-dimensional fixed sector.
B, K, J = (np.zeros((160, 160)) for _ in range(3))
B[:159, :159], K[:159, :159], J[:159, :159] = B0, K0, J0
_, singular, vh = np.linalg.svd(B)
null = vh[singular < 1e-8].T
assert null.shape == (160, 8)
for i in range(0, 8, 2):
    a, b = null[:, i], null[:, i+1]
    J += np.outer(a, b)-np.outer(b, a)
assert np.max(np.abs(J+J.T)) < 1e-8
assert np.max(np.abs(J@J+np.eye(160))) < 1e-8
assert np.max(np.abs(J@K-B)) < 1e-8
assert np.linalg.eigvalsh(K).min() > -1e-8
assert np.max(np.abs(B.T@K+K@B)) < 1e-8
# Explicit alternative phase branch: add one full turn to each nonzero mode.
alt_angles = angles+2*np.pi*np.sign(angles)
assert np.max(np.abs(real_matrix(np.exp(1j*alt_angles))-U@U)) < 1e-8
assert np.max(np.abs(real_matrix(np.abs(alt_angles))-K0)) > 1
print('Two-sweep Hamiltonian embedding: 160 real coordinates, 76 rotating pairs, 4 zero-frequency pairs.')
print('B=J K; J skew, J^2=-I; K positive semidefinite; exp(B)=diag(U^2,1).')
print('A different positive rotation branch reproduces the same sampled map.')
print('For duration T and action scale S: H=(S/2T) x^T K x, Poisson tensor J/S.')
print('T, S, phase branch, added coordinate, and fixed-sector pairing are explicit choices.')
