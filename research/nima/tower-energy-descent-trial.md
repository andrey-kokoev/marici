# Trial energy descent on a nested 12-to-4 tower

## Definitions

Take nested Euclidean spaces V_r = span(e_1,...,e_r) inside R^12.
A rung restriction removes the last coordinate, recording it separately.
Let C=E[x x^T] be the second-moment matrix (including any nonzero mean),
and let g>0 be a fixed conversion from squared amplitude to energy.

    E_r = g tr(P_r C),
    R_r = g tr((I-P_r) C),
    E_r + R_r = E_12.

The exact one-step loss is g C_rr when going from r to r-1, with indices
numbered from 1. This construction supplies a trial nested projection tower.
It does not identify R^r with a derived carrier state space or its Gram rank.

## Uniform distribution

If C_ii=sigma^2 for every direction, then

    E_r/E_12 = r/12,
    E_(r-1)/E_r = (r-1)/r.

Isotropic C=sigma^2 I is sufficient. Equal diagonal entries in the chosen
restriction basis suffice; arbitrary off-diagonal correlations do not affect
this trace calculation. Isotropy makes the result independent of the choice
of retained subspace of a given dimension.

| Rung | Retained fraction | Recorded fraction |
|---:|---:|---:|
| 12 | 1 | 0 |
| 11 | 11/12 | 1/12 |
| 10 | 5/6 | 1/6 |
| 9 | 3/4 | 1/4 |
| 8 | 2/3 | 1/3 |
| 7 | 7/12 | 5/12 |
| 6 | 1/2 | 1/2 |
| 5 | 5/12 | 7/12 |
| 4 | 1/3 | 2/3 |

## Relation to Q_r P_r/T_r

The dimensional energy scale Q_r P_r/T_r needs a dynamical interpretation
and a dimensionless coefficient before it can be identified with E_r above.
A compatible scale assignment is Q_r/Q_12=P_r/P_12=sqrt(r/12), with fixed
T_r=T_12 and fixed coefficient. This is one assignment, not an independent
consequence of projection. Here P_r as a momentum scale must be distinguished
from P_r as the projector in the trace equations.

For example, equal-frequency harmonic modes obey E=omega*J in terms of
action J. Additive equal action per retained mode gives E_r proportional to r.
A generic coordinate-momentum product qp is not the instantaneous conserved
oscillator action. Physical time, frequency, and action normalization still
need identification in the carrier dynamics.

## Uneven energy and restriction order

For the coherent seed x=(1,2,...,12), total squared amplitude is 650.
Retaining the first four coordinates keeps 30, giving E_4/E_12=3/65.
Retaining the last four keeps 446, giving E_4/E_12=223/325.
A seed concentrated entirely in the retained space gives ratio 1; one entirely
in the removed space gives ratio 0. Thus rank loss alone permits the full
interval [0,1] for the bottom-rung retained fraction.

The total retained-plus-record budget stays constant in every case. Calling
the retained fraction an energy decay means specifying which degrees of
freedom remain in the observable subsystem.

## Conditional GeV calibration

For an externally identified reference rung s with retained energy E_ref,

    E_r = (r/s) E_ref,
    E_total = (12/s) E_ref,
    R_r = ((12-r)/s) E_ref.

A calibration trial identifies the whole retained rung-4 budget with the
125 GeV Higgs energy quoted in the public documentation. That identification
is an extra hypothesis. A Higgs excitation energy is not automatically the
entire energy of a four-dimensional retained subsystem.

Under this trial the energy per direction is 31.25 GeV and total is 375 GeV.

| Rung | Retained GeV | Recorded GeV |
|---:|---:|---:|
| 12 | 375 | 0 |
| 11 | 343.75 | 31.25 |
| 10 | 312.5 | 62.5 |
| 9 | 281.25 | 93.75 |
| 8 | 250 | 125 |
| 7 | 218.75 | 156.25 |
| 6 | 187.5 | 187.5 |
| 5 | 156.25 | 218.75 |
| 4 | 125 | 250 |

Assigning the same reference value to rung12 instead gives total125 GeV and
E4=125/3 GeV. Thus 375 GeV is a conditional calibration output, not a derived
absolute energy or a new particle mass prediction. The trial inherits the
uniform-energy, nested-Euclidean-projection, and fixed-normalization assumptions.
The clock and action remain separately unidentified.

Verification:

    python research/nima/checkers/check_tower_gev_calibration.py

## Audit of the Higgs anchor

Inspection of check_higgs_mass.py shows that it calculates coefficients
125=11^2+4 and 246=2*11^2+4, labels them GeV, and compares with measurements.
It supplies no rung restriction map, carrier Hamiltonian, mode occupancy,
or equation identifying the Higgs excitation with the full rung4 budget.

A conventional scalar effective potential illustrates the distinction. In
natural units, V(phi)=lambda*(phi^2-v^2)^2/4+C has curvature
m_H^2=2*lambda*v^2 at phi=v for every constant C. The constant has energy-density
units GeV^4; converting potential density to total energy also requires a
volume. Excitation energies additionally depend on occupation. The same Higgs
mass therefore does not fix a whole subsystem's total energy. In a gravitational
model the offset can have physical consequences; those dynamics must then fix
it, rather than the Higgs curvature alone.

An explicit electroweak calibration can instead use the external input
v_ref=246.22 GeV already cited by the old checker. With the candidate ratio
m_H/v=125/246, this gives a coefficient scale v_ref/246=1.000894308943 GeV
and m_H=125.111788617886 GeV. This calibrates the candidate Higgs formula,
not the tower budget. It remains conditional on that ratio and consistent
physical parameter definitions; no precision or statistical claim is made.

The 375 GeV table above remains an illustration of an assumed anchor. The
existing Higgs construction supplies no physical justification for that anchor.

Verification:

    python research/nima/checkers/check_higgs_tower_identification.py

## Remaining construction

To apply the r/12 result to the carrier tower, specify the rung state spaces,
restriction maps, energy metric, distribution of excitation, and physical
clock. A non-Euclidean metric or a change of normalization between rungs
changes the calculation. The present trial gives a conditional linear law
and exact counterexamples to a universal rank-only law.

## Verification

    python research/nima/checkers/check_tower_energy_descent.py

Standard-library rational arithmetic verifies all nine rungs, one-step losses,
record conservation, uniform scaling, and uneven-state counterexamples.
