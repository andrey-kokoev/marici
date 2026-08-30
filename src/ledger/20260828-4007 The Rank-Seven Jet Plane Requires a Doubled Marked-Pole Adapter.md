# 4007 — The Rank-Seven Jet Plane Requires a Doubled Marked-Pole Adapter

## Question

Entry 4005 constructed the canonical occurrence transition on the repaired rank-26 simple-pole quotient. The remaining gate was to reconstruct (A_7) directly in that quotient.

## Strict reconstruction rule

Use the source covariant-jet constructor, but accept a jet in the repaired quotient only if complete ambient exact reduction lands entirely in the 36-dimensional simple-pole sector. Then reduce by the ten internal low relations.

No surviving ambient coordinate may be discarded.

## Result

The reconstruction fails at the first non-low residual in both (G_{12}) and (G_{31}), at primes (32009) and (32003).

The surviving labelled direction is

[
(0,1,2,1,2,1;(0,0)).
]

Thus the obstruction has:

- no Cayley–Menger pole increase;
- doubled marked poles in the second and fourth marked factors;
- zero fiber monomial degree;
- identical labelled form in both occurrence charts.

The old (A_7) census obtained a rank-seven annihilator only after ambient reduction followed by retention of selected low coordinates. The strict audit shows that the covariant-jet operation itself does not descend to the repaired simple-pole quotient.

## Conclusion

(A_7) is not currently an intrinsic object of the repaired rank-26 simple-pole quotient.

Its missing constructor is now specific: a source-derived adapter or relative comparison involving the doubled marked-pole sector represented by

[
(0,1,2,1,2,1;(0,0)).
]

Until that adapter is derived, (A_7/L_5) is not a typed quotient and has no occurrence action. Adding a projection that discards this direction would repeat the defect retracted in Entry 3987.

This is not a new carrier divisor. It is a coefficient/operation-closure obstruction between pole-depth sectors over the existing marked carrier.

## Artifacts

- `research/benincasa/checkers/check_repaired_low_A7_reconstruction.py`
- `research/benincasa/checkers/run_repaired_low_A7_reconstruction.ps1`
- `research/benincasa/results/repaired-low-A7-gate-g12-p32009.json`
- `research/benincasa/results/repaired-low-A7-gate-g31-p32009.json`
- corresponding prime-32003 packets

Sequence claim: `seqclaim-91819e9c32285ca242478c43`.
