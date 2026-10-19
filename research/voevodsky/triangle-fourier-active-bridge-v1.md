# Iteration 2: actual triangle-history transport connects to the Fourier active plane

## Constructed connection

Obligation: attachment transport and route compatibility. Retain the exact
native history backend and the previously established transported-section rule.
Do not replace its discrete tick by the order-four source cycle.

In cyclic Fourier-port coordinates let F send e_j to e_(j+1 mod4), and let
D=F-F^(-1). Define u=e0-e2 and v=e1-e3=Fu. Then Du=2v, Dv=-2u.
The existing triangle-history generator and declared active metric are

  A=[[0,2/sqrt3],[-2sqrt3,0]], H=diag(3,1).

An explicit adapter is

  B=[sqrt3 u, -v]/sqrt20.

It satisfies DB=BA and B^T(10I+J)B=H. The denominator fixes agreement with
the already declared coefficient Gram; it is not an independent analytic
Hilbert normalization of comb distributions. Signs and the starting cyclic
port follow iteration 1's chosen attachment.

For each actual history stage, use its prior endpoint-derived reader P_n,
transported section E_n and generator L_n=E_n A P_n. The new analytic
coefficient reader is R_n=B P_n. Exactly,

  R_n L_n=D R_n,
  R_n^T(10I+J)R_n=P_n^T H P_n.

Composing R_n with iteration 1's distribution basis B_a gives a concrete map
from retained histories to the odd Fourier-comb sector. Composing further with
oriented radialization and the prior Mellin operator gives the already derived
Tate gamma-matrix presentation on that image. These operations use the existing
analytic identities, not a new fitted gamma factor.

## Discrete operations differ

Fresh source inspection gives the actual history tick

  C=[[-1/2,1/2],[-3/2,-1/2]], C^3=I,
  C=-I/2+(sqrt3/4)A=exp((pi/3)A).

On the active Fourier plane, F=exp((pi/4)D). Thus the continuous generators
match, but one native tick has angle pi/3 and one Fourier step angle pi/4.
There is NO nonzero map X with FX=XC: the two spectra are disjoint. The exact
checker solves all eight linear unknowns, obtaining only zero.

For the actual native extension T_n, the prior square P_(n+1)T_n=C P_n gives

  R_(n+1)T_n=exp((pi/3)D)R_n,

not F R_n. The exponential on this active image equals -I/2+(sqrt3/4)D.
That polynomial is used only on the active image, not as the full four-port
flow on the stationary complement. Four native ticks and three Fourier ticks
must not be equated either: matching total angle requires 3 native ticks and
4 Fourier ticks (both angle pi), which return the active state but not the
retained history. No physical time calibration is implied.

## Two components remain outside this reader

The vectors (1,1,1,1) and (1,-1,1,-1) complete B to a full four-dimensional
basis. Both are killed by D, but F fixes the first and negates the second.
These are the common and alternating Fourier characters. Iteration 1's direct
12-to-4 map retains both; this rank-two history reader does not supply them.

They may be added as explicitly retained data, but cannot be claimed to have
been recovered from P_n alone. On the analytic orbit the active distributions
are proportional to P_a-P_(1-a) and C_-a-C_a. Their endpoint atom cancels;
the full four-port orbit, including its even sectors, still needs iteration
1's endpoint handling. The Riemann-zeta even specialization is therefore not
established by this odd-sector bridge alone.

## Verification

`uv run research/voevodsky/checkers/check_triangle_fourier_active_bridge.py`
imports `retained_path_successor` and `photon_native_spatial_step` without
running source-owner result writers. It constructs the actual four history
stages of sizes 10,16,26,42, follows the existing section transport, verifies
generator/metric/hidden squares, and tests both the correct angle and the
incorrect Fourier-tick substitution. Source hashes of iteration 1 are checked.

Result: `results/triangle-fourier-active-bridge-v1.json`. This closes the
continuous active-sector connection; it does not identify the two discrete
successors or the full four-dimensional history/analytic interface.

Next executable gate: test the existing six-step reducing schedule for the
FULL source permutation rather than just D12. Its stationary directions may
mix the common and alternating characters; their separate retention must be
checked, not presumed from generator invariance.
