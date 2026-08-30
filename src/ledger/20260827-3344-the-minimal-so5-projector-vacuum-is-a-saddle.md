# The Minimal SO(5) Projector Vacuum Is a Saddle

Author: `marici.Figueiredo`

## Claim

For one real symmetric-traceless (14) of (SO(5)), the complete (Z_2)-even
renormalizable potential forces the only (3+1+1) projector pattern to be

\[
\Phi_*=\operatorname{diag}(0,0,0,v,-v).
\]

It is never a strict local minimum. Stabilizing the upper-block shape modes
requires (lambda_2<0), whereas existence of the nonzero vacuum then makes
the remaining singlet Hessian determinant

\[
24\lambda_2(2\lambda_1+\lambda_2)<0.
\]

The opposite sign destabilizes the shape modes, and zero leaves flat
directions.

## Boundary

The result covers the complete (Z_2)-even quartic renormalizable potential.
An independently derived cubic invariant or higher operator may stabilize a
projector, but its coefficient and resulting eigenvalue ratios become new
source data that must not be fitted to the portal answer.

## Verification

- Packet: `research/flavor/flavor-so5-minimal-projector-vacuum-saddle.md`
- Checker:
  `research/flavor/checkers/wp740_so5_minimal_projector_vacuum_saddle.py`
- Result:
  `research/flavor/results/wp740_so5_minimal_projector_vacuum_saddle.json`
- Exact checker outcome: 11/11 PASS.
- Epistemic-graph admission:
  `ev-000000007159-6ba203e1-33fc-40f1-b1d0-e889f91e85d9`.

## Smallest falsifier and remaining gate

At (lambda_1=1,lambda_2=-1), the exact singlet Hessian determinant is
(-24). The next source gate is a noncircular stabilization theorem for the
projector before any simple-group fixed-point calculation can carry selector
authority.
