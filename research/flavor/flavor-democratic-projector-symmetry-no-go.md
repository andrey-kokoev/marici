# Democratic projector-symmetry no-go (WP349)

## Natural coefficient selector

Impose a common permutation symmetry on the three projector channels
(P,Q,R). The invariant coefficient vectors form the democratic ray, so each
sector lift has the form

\[
Y_f=a_fI+b_f(P+Q+R).
\]

This is a genuine symmetry restriction of the coefficient family. It is not a
fitted scalar choice.

## Exact obstruction

Both sector matrices are polynomials in the same Hermitian matrix
(K=P+Q+R). Their Hermitian covariants therefore commute identically:

\[
[H_u,H_d]=0,
\qquad
\operatorname{Tr}([H_u,H_d]^3)=0.
\]

This occurs even though the individual projectors do not commute. The common
democratic coefficient selector erases the relative-sector geometry needed for
mixing and CP violation.

## Disposition

The symmetry is a coefficient-direction rigidifier and a coarse selector of a
proper coefficient subspace, but it is not a viable `physical16` selector. A
progressive source must select distinct nonparallel coefficient vectors for the
two sectors without installing their numerical values from flavor readout.

Run `uv run --with sympy python
research/flavor/checkers/wp349_democratic_projector_symmetry_no_go.py` to
regenerate the exact no-go.
