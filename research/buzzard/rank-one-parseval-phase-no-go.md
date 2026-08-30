# Rank-one Parseval phase no-go: Lean packet

Source: `research/grothendieck/rank-one-parseval-phase-no-go.md`.

For an arbitrary real input `u`, the module defines

\[
c(u)=\frac{1-u^2}{1+u^2},\qquad
q(u)=\frac{2u}{1+u^2}.
\]

`rationalParseval_identity` proves `c(u)^2+q(u)^2=1` for every `u`.
`parsevalSineCoordinate_eq_zero_iff` proves `q(u)=0` exactly when `u=0`.
Consequently, pointwise application to an arbitrary function imports that
function's zero set without any restriction from Parseval normalization.

`parseval_orientation_reversal` proves that replacing `u` by `-u` preserves
`c` and `q^2` while reversing `q`; the positive transfer defect therefore
forgets the oriented first-order sign. `rankOneParseval_zeroSet_hostile`
exhibits two inputs with different zero behavior satisfying the same Parseval
axiom.

Typing boundary: the parametrization is pointwise over `ℝ`. This is the
algebraic non-discrimination theorem, not a claim that every global analytic
Parseval pair admits one rational chart. Global circle-phase lifting requires
a specified interval/topology and endpoint convention. The Riemann--Siegel
phase, prime/archimedean scattering identity, and noncircular source derivation
of any phase remain analytic/source interfaces. No Xi-derived phase is assumed.

Verification boundary: Nima's active no-build instruction remains in force.
Only bounded static scans were run; the module remains outside
`MariciFormal.lean`.
