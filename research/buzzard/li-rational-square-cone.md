# Li rational-square cone packet

## Grothendieck source

This formalizes the unconditional algebraic content of
`research/grothendieck/li-mobius-weil-test-cone.md`.

## Formal objects

- `liCoordinate s=(s-1)/s` is the coordinate already forced by the rigidity
  packet.
- `liCoordinate_reflection` proves `u(1-s)=u(s)^(-1)` away from the two
  endpoints.
- `liCoordinate_coboundary_weight` proves that the coordinate forces the
  weight `1/(s*(1-s))`.
- `liRationalSquareTest p s` is the pulled-back square test.
- `liRationalSquareTest_reflection` proves invariance for one fixed evaluator
  `p`; polynomial structure is not needed for this symmetry theorem.

## Assumptions and coefficient type

The identities hold over an arbitrary field. Evaluation excludes `s=0` and
`s=1`, exactly the poles involved in the rational formulas.

## Hostile and positivity gate

At the rational center, the constant test has value four. The linear readout
`hostileConeReadout=-id` evaluates it negatively. This does not model the
arithmetic explicit formula; it proves the typing point that an algebraic
rational-square cone cannot confer positivity on an otherwise unconstrained
functional.

The source must still construct the pair-normalized arithmetic functional
from endpoint, gamma, and prime-power data and prove it nonnegative on every
test in the cone. Critical-line pointwise positivity or evaluation on a real
zero divisor cannot be used to establish that source theorem without
circularity. Li Toeplitz positivity and RH remain gated.

## Verification boundary

Static placeholder checks are permitted. Lean elaboration is withheld under
Nima's active no-build instruction.
