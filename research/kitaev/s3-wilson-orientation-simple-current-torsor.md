# Wilson orientation is the B-simple-current torsor, not a braided gauge

Owner: `marici.Kitaev`

## Bottom-level identification

Let (B) be the invertible sign charge. Exact Verlinde fusion gives

\[
B\otimes(A,B,C,D,E,F,G,H)
=(B,A,C,E,D,F,G,H).
\]

This is exactly the hidden Wilson permutation

\[
\sigma=(A\ B)(D\ E).
\]

Thus the apparent orientation reversal is translation by the order-two simple
current (B), not an unexplained relabelling.

## Why Wilson coordinates forget the origin

For every Wilson type (x),

\[
W_x(B\otimes a)=\chi_B(x)W_x(a),
\]

where

\[
\chi_B(D)=\chi_B(E)=-1,
\qquad \chi_B(x)=1\quad\text{otherwise}.
\]

After the signs of the (D/E) coordinates are allowed to reverse, Wilson
readout sees the two sheets related by (B\otimes-) but supplies no preferred
origin. Its natural object is a (C_2) torsor.

## The symmetry fails before F and R

Translation by (B) preserves quantum dimensions but is not a monoidal
autoequivalence because it moves the tensor unit:

\[
\sigma(A)=B.
\]

The smallest fusion witness is

\[
A\otimes A=A,
\]

which would have to map to (B\otimes B=B); actually

\[
B\otimes B=A.
\]

The exact fusion tensor has 32 violated entries under simultaneous relabelling.
The symmetry also fails modular-(S) relabelling invariance and twist
preservation; in particular (	heta_D=1) while (	heta_E=-1).

Therefore no (F)- or (R)-symbol calculation is needed to disprove braided
gauge equivalence. The failure already occurs at the distinguished-unit and
based-fusion-ring layer.

## Mathematical versus operational origin

Mathematically the tensor unit (A) fixes the torsor origin. Operationally,
the local torus Hamiltonian and syndrome do not select a logical ground-state
sector. Naming (A) is not yet preparing or reading (A).

A noncircular physical resolution must provide at least one of:

1. a source-derived tensor-unit preparation/readout;
2. an oriented (D/E) twist calibration;
3. another constructor odd under (B\otimes-).

## Carrier versus quantum lens

The two-sheet torsor, its quotient, and the requirement for an origin are
shared Carrier geometry. The quantum coefficient lens identifies the deck
action as fusion with (B), distinguishes tensor unit (A), and supplies the
fusion and twist observables that break it.

## Falsifiers

- (B\otimes-) does not equal ((A\ B)(D\ E)).
- The Wilson intertwining character differs from (-1) exactly on (D,E).
- Translation by (B) preserves the tensor unit or all fusion coefficients.
- Local torus syndrome already supplies a preferred ground-sector origin.

## Artifacts

- Checker: `checkers/check_s3_wilson_orientation_simple_current_torsor.py`
- Result: `results/s3-wilson-orientation-simple-current-torsor.json`
- Result SHA256:
  `553DB7BE3D887F4A1661088AC248C423A48A697BDC77BA22EA5A49E2B1371008`
- Graph admission: `ev-000000003525-7ca24ec1-40df-40ea-8433-5c004b63c0b2`
- Ledger: entry 2528, `seqclaim-62fa62bf5d4a09b26ef2ee97`
