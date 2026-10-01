# /// script
# dependencies = ["numpy>=2,<3"]
# ///
"""Numerical spectrum of the closed 159-coordinate comparison sweep.

Run with: uv run research/nima/checkers/check_comparison_sweep_spectrum.py
Phases are per scheduled sweep, not physical frequencies. No artifact writes.
"""
from pathlib import Path
import runpy
import numpy as np

source = runpy.run_path(str(Path(__file__).with_name('check_comparison_energy_spectrum.py')))
rows = np.asarray(source['rows'], dtype=float)
d = 6 + len(rows)
U = np.eye(d)
for i, r in enumerate(rows):
    u = r / np.linalg.norm(r)
    longitudinal = u @ U[:6, :]
    record = U[6+i, :].copy()
    U[:6, :] += np.outer(u, record-longitudinal)
    U[6+i, :] = longitudinal
assert np.max(np.abs(U.T @ U-np.eye(d))) < 1e-12
values, vectors = np.linalg.eig(U.astype(complex))
assert np.max(np.abs(np.abs(values)-1)) < 1e-12
assert np.max(np.abs(U @ vectors-vectors*values)) < 1e-12
phases = np.angle(values)
positive = sorted((float(phases[i]), float(np.sum(np.abs(vectors[:6, i])**2)))
                  for i in range(d) if phases[i] > 1e-8 and phases[i] < np.pi-1e-8)
plus = int(np.sum(np.abs(values-1) < 1e-8))
minus = int(np.sum(np.abs(values+1) < 1e-8))
assert plus+minus+2*len(positive) == d
print(f'Spectrum: +1 modes={plus}, -1 modes={minus}, rotation pairs={len(positive)}')
print('Smallest positive phases: radians/sweep, period/sweeps, carrier participation')
for theta, weight in positive[:10]:
    print(f'{theta:.12g}  {2*np.pi/theta:.12g}  {weight:.12g}')

# Group equal eigenvalues. QR supplies orthonormal bases within eigenspaces,
# including degeneracies. Spectral projectors avoid basis-dependent averages.
remaining = set(range(d))
projectors = []
while remaining:
    i = min(remaining)
    group = sorted(j for j in remaining if abs(values[j]-values[i]) < 1e-8)
    remaining.difference_update(group)
    Q, _ = np.linalg.qr(vectors[:, group])
    projectors.append(Q @ Q.conj().T)
assert np.max(np.abs(sum(projectors)-np.eye(d))) < 1e-8
# Initial covariance and measured observable both equal carrier projector P.
# Cesaro mean tr(P U^n P U^-n) = sum_g ||P E_g P||_F^2.
mean = sum(float(np.sum(np.abs(E[:6, :6])**2)) for E in projectors)
print(f'Infinite-time Cesaro carrier trace (spectral grouping tolerance 1e-8): {mean:.12g}')
assert 0 <= mean <= 6
# Independent finite-time check via eigenbasis; use a smaller six-column state
# and evaluate its carrier block without multiplying full matrices each step.
coeff = np.linalg.solve(vectors, np.eye(d)[:, :6])
factors = np.ones(d, dtype=complex)
total = 0.0
for step in range(1, 20001):
    factors *= values
    block = (vectors[:6, :]*factors) @ coeff
    trace = float(np.sum(np.abs(block)**2))
    total += trace
print(f'20000-sweep mean carrier trace: {total/20000:.12g}')
assert abs(total/20000-mean) < 0.01
print('Orthogonality, eigen-residuals, spectral resolution, and long-window average checked.')
print('Phase rates depend on the update schedule; physical clock and energy scale remain inputs.')
