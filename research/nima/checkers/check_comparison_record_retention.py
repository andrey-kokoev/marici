# /// script
# dependencies = ["numpy>=2,<3"]
# ///
"""Record retention sweep; attenuation is applied before each record exchange.

A returned record amplitude is rho*w. Exported squared budget is
(1-rho^2)*w^2. This models a passive export port for 0<=rho<=1.
"""
from pathlib import Path
import runpy
import numpy as np

s = runpy.run_path(str(Path(__file__).with_name('check_comparison_energy_spectrum.py')))
rows = np.asarray(s['rows'], dtype=float)
rows /= np.linalg.norm(rows, axis=1)[:, None]
d = 6+len(rows)


def sweep(X, rho):
    X = X.copy()
    exported = 0.0
    for i, u in enumerate(rows):
        old = X[6+i].copy()
        a = u @ X[:6]
        exported += (1-rho*rho)*float(old @ old)
        X[:6] += np.outer(u, rho*old-a)
        X[6+i] = a
    return X, exported


print('rho | spectral radius | amplitude e-fold sweeps | carrier at1000 | total at1000 | exported')
for rho in (0., .25, .5, .75, .9, .99, 1.):
    M, loss = sweep(np.eye(d), rho)
    assert abs(np.sum(M*M)+loss-d) < 1e-10
    radius = float(np.max(np.abs(np.linalg.eigvals(M))))
    assert radius <= 1+1e-10
    if rho < 1:
        assert radius < 1
    else:
        assert np.max(np.abs(M.T@M-np.eye(d))) < 1e-12
    X = np.eye(d)[:, :6]
    exported = 0.
    first = None
    for step in range(1000):
        before = float(np.sum(X*X))
        X, drop = sweep(X, rho)
        exported += drop
        after = float(np.sum(X*X))
        assert abs(before-after-drop) < 1e-10
        assert abs(after+exported-6) < 1e-9
        if step == 0:
            first = X.copy()
    # Empty initial records imply the first sweep is independent of retention.
    if rho == 0:
        reference_first = first
    assert np.max(np.abs(first-reference_first)) < 1e-14
    efold = 'infinite' if rho == 1 else f'{-1/np.log(radius):.6g}'
    print(f'{rho:.2f} | {radius:.12g} | {efold:>10} | '
          f'{np.sum(X[:6]**2):.9g} | {np.sum(X**2):.9g} | {exported:.9g}')
print('Spectra, per-sweep conservation including export, and first-sweep equivalence checked.')
print('rho attenuates amplitude; retained record budget fraction is rho^2.')
print('No drive is supplied. The asymptotic state for rho<1 is zero in this full-rank constraint model.')
