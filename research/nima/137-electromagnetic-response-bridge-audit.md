# From normalized mismatch response to electromagnetic coupling

## What the equilibrium calculation fixes

The closed-record model with mixing schedule fixes the relative mismatch
variance to1/137 at equilibrium with positive active budget. Multiplying the
readout by any common gain multiplies every variance by its square and leaves
this fraction unchanged. Thus the fraction alone supplies no absolute probe
response coefficient.

## Explicit source/field interface test

As a trial interface use the complete four-state graph with Laplacian
L=4I-J, a zero-sum external charge vector j, and scalar potential phi.
Define a static variational functional

    V(phi;j) = (kappa/2) phi^T L phi - g j^T phi,

with kappa>0 the field stiffness and g the source coupling. On the zero-sum
potential space the solution is

    phi = (g/kappa) L^+ j,
    L^+ = I/4 - J/16.

The positive stored field energy is g^2/(2*kappa) j^T L^+ j. The minimized
functional is the negative of this quantity; the source-work convention must
be distinguished from stored field energy. For j=(1,-1,0,0), the stored field
energy is g^2/(4*kappa).

Choices (kappa,g)=(1,1),(1,2),(2,1) give energies1/4,1,1/8. All preserve common
potential-shift symmetry and can accompany the same zero-source normalized
comparison share. This is an explicit family of possible probe interfaces,
not a derivation of an interface from the record dynamics. It demonstrates
what remains free without such a derivation.

## Remaining electromagnetic construction

The trial graph has equal pair resistance1/2 for all six distinct vertex pairs.
It contains no derived physical spatial separation or Coulomb1/r Green function.
Constant-shift invariance of a scalar potential is not a construction of local
U(1) gauge dynamics, conserved matter current, or Maxwell propagation.

A physical bridge needs a carrier-derived field/current action whose normalized
kinetic and interaction coefficients fix the coupling. In a Maxwell-like
normalization, the analogue of g^2/kappa is the relevant response strength;
geometric and unit conventions then determine its relation to alpha. They
cannot be supplied by relabelling the relative mismatch fraction.

The next source construction should therefore identify (1) a current/charge
observable of records, (2) its action on the comparison state, and (3) the
field response operator and its normalization. A feedback or susceptibility
calculation must use that actual interaction rather than an appended arbitrary
source gain.

## Status

Equal relative mismatch response is derived conditionally in the closed-record
model. Its electromagnetic interpretation remains a hypothesis. The static
counterfamily shows that stationary slot statistics alone do not force a
charge-interaction coefficient or the measured decimal correction.

## Verification

    python research/nima/checkers/check_137_electromagnetic_bridge.py

Exact fractions check the graph inverse on a neutral charge, source equation,
field-energy values, constant-shift invariance, readout-gain invariance of the
normalized137-slot fraction, and equal pair resistances. No measured constants
or physical units enter this trial interface.
