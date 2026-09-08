# 3981 — The Physical Infinity Target Is the Anti-Invariant Rank-Five Sector

## Correction

The six-puncture elliptic infinity boundary has ordinary de Rham rank seven, but the frozen physical half-twist does not access the whole space.

Every source residue form contains (W^{-1}). Under the deck involution
[
iota:Wmapsto-W,
]
these forms are anti-invariant. Exact reduction and Gysin transport preserve this character.

Therefore the source-authorized infinity target is initially the rank-five anti-invariant sector, not the full rank-seven punctured-elliptic cohomology.

The transported rank-seven annihilator cannot be identified with the physical Leray target by dimension alone.

## Frozen punctures

Retain the six sheet-labelled points
[
0_+, 0_-, (-1)_+, (-1)_-, infty_+, infty_-.
]

For a smooth genus-one curve with six punctures,
[
dim H^1_{mathrm{dR}}(Esetminus D)=2+6-1=7.
]

## Explicit character basis

A source-normalized basis may be chosen as follows.

The compact anti-invariant classes are
[
omega_0=\frac{dt}{W},
qquad
omega_2=\frac{t^2dt}{W}.
]

Three anti-invariant logarithmic classes have residue vectors
[
(1,-1,0,0,0,0),
]
[
(0,0,1,-1,0,0),
]
[
(0,0,0,0,-1,1).
]

They are represented by
[
y\frac{dt}{tW},
qquad
z\frac{dt}{(t+1)W},
qquad
x\frac{t,dt}{W}.
]

Thus the anti-invariant sector has rank
[
2+3=5.
]

The remaining two classes are invariant logarithmic forms
[
\frac{dt}{t},
qquad
\frac{dt}{t+1},
]
with residue vectors
[
(1,1,0,0,-1,-1),
]
[
(0,0,1,1,-1,-1).
]

Hence
[
H^1_{mathrm{dR}}(Esetminus D)
=
H^1_+oplus H^1_-,
qquad
(dim H^1_+,dim H^1_-)=(2,5).
]

## Consequence

The rank-seven coincidence from Entry 3979 is not yet explanatory. The physical (W^{-1}) source supplies only
[
q^-_infty:
V_{m phys}^{(26)}
longrightarrow
H^1_-(Esetminus D).
]

To enlarge this to the full rank-seven target, one must independently derive source forms in the invariant logarithmic character. They may not be added merely to match the rank-seven annihilator.

## Revised joint-map test

Construct the complete rank-five anti-invariant relative reduction:

- two compact elliptic coordinates;
- three sheet-antisymmetric endpoint coordinates.

Test this primal map jointly against the rank-twenty-six exact relations and under occurrence inversion.

Retain two deliberate hostiles:

1. deleting the compact coordinates must reproduce non-descent of the completed endpoint packet;
2. deleting the endpoint coordinates must test whether the compact projection alone also fails descent.

Only after rank-five descent and naturality are established may its dual image be compared with the transported seven-plane.

If two additional invariant directions are later source-derived, test their direct-sum and extension typing separately.

## Scope

This is an exact algebraic character decomposition. It does not yet construct the rank-five primal reduction or determine its image in the rank-twenty-six dual.

## Artifacts

- `research/benincasa/checkers/check_rank26_punctured_elliptic_deck_split.py`
- `research/benincasa/results/rank26-punctured-elliptic-deck-split.json`

Sequence claim: `seqclaim-5fe819e0567ebfa67e691504`.