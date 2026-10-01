"""Closed deterministic record feedback: bounded numerical experiment.

Evolve six orthonormal carrier seeds with initially empty records. Summing
squared amplitudes gives covariance traces for unit initial carrier covariance.
No random injection, resets, measured constants, or physical clock.
"""
from pathlib import Path
import runpy

source = runpy.run_path(str(Path(__file__).with_name('check_comparison_energy_spectrum.py')))
rows = source['rows']
norms = [sum(x*x for x in r) for r in rows]
# Each coordinate stores its amplitudes for six independent initial seeds.
q = [[float(i == j) for j in range(6)] for i in range(6)]
z = [[0.0]*6 for _ in rows]


def budget():
    carrier = sum(x*x for v in q for x in v)
    memory = sum(n*sum(x*x for x in v) for n, v in zip(norms, z))
    return carrier, memory


def sweep(reverse=False):
    indices = reversed(range(len(rows))) if reverse else range(len(rows))
    for i in indices:
        r, n = rows[i], norms[i]
        a = [sum(r[j]*q[j][k] for j in range(6))/n for k in range(6)]
        for j in range(6):
            for k in range(6):
                q[j][k] += r[j]*(z[i][k]-a[k])
        z[i] = a


samples = []
for step in range(1, 1001):
    sweep()
    carrier, memory = budget()
    assert abs(carrier+memory-6) < 1e-9
    samples.append(carrier)
    if step in (1, 2, 12, 100, 1000):
        print(f'Sweep {step}: carrier trace={carrier:.12g}, record budget={memory:.12g}')
assert samples[1] > samples[0]  # backflow for this initial covariance and order
for _ in range(1000):
    sweep(reverse=True)
error = max(abs(q[i][j]-(i == j)) for i in range(6) for j in range(6))
assert error < 1e-9
assert sum(n*sum(x*x for x in v) for n, v in zip(norms, z)) < 1e-16
print(f'Sweeps 101..1000: carrier trace min={min(samples[100:]):.12g}, '
      f'max={max(samples[100:]):.12g}, mean={sum(samples[100:])/900:.12g}')
print(f'1000 reverse sweeps restore initial state: max error={error:.3g}')
print('Finite-window statistics describe this seed ensemble and schedule, not an asymptotic floor.')
