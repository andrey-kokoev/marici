# Left-right exchange completion (WP311)

## Representation repair

Embed the right-handed quarks in an $SU(2)_R$ doublet with

\[
Y=T^3_R+\frac{B-L}{2},
\qquad B-L=\frac13.
\]

The two hypercharge eigenvalues are then $2/3$ and $-1/3$. The exact Weyl
representative conjugates $T^3_R$ to $-T^3_R$ and exchanges those
eigenvalues. WP310's representation mismatch is therefore repaired in the
enlarged unbroken source.

## Equivariant matching is not selection

Use two generation-space couplings with bidoublet-type matching

\[
M_u=v_1Y+v_2Z,
\qquad
M_d=v_2Y+v_1Z.
\]

Exchanging $v_1$ and $v_2$ exchanges $M_u$ and $M_d$, so the matching
is equivariant. It does not force the vacuum onto the fixed locus.

The exact hostile packet takes $v_1=2,v_2=1$,
$Y=\operatorname{diag}(1,2,4)$, and $Z=\operatorname{diag}(1,3,9)$. It gives
an up/down hierarchy ratio $17/22$, not 1. At the symmetric vacuum
$v_1=v_2$, the two mass packets coincide and the reciprocal fixed condition
holds.

## Classification

The enlarged source supplies a legal upstream exchange and equivariant
matching architecture. It is not yet a hierarchy selector. Selection authority
now resides in the symmetry-breaking vacuum operation.

A progressive successor must derive a stable, non-answer-coded potential that
selects the $v_1=v_2$ orbit, while also producing realistic gauge breaking,
anomaly cancellation, thresholds, CKM mixing, and a calibrated `physical16`
readout.

Run `uv run --with sympy python
research/flavor/checkers/wp311_left_right_exchange_completion.py` to regenerate
the exact representation and matching audit.
