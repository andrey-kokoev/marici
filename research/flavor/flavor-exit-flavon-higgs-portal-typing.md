# Exit-flavon Higgs-portal typing: WP684

## Identity check

The messenger exit field (X_i) is not the trace-adjoint scalar used in the
older dimuon portal. It is an (SU(3)_F) adjoint and an (SO(3)_P) vector.
Transporting the trace portal between these objects would conflate distinct
source fields.

## Linear-portal no-go

The vector representation of (SO(3)_P) has no invariant linear functional.
The flavor adjoint likewise has no trace singlet. Therefore a term linear in
the exit field,

\[
(H^\dagger H)X_i,
\]

does not descend under the declared source group.

The lowest ordinary Higgs portal is quadratic:

\[
V_p=\lambda_p(H^\dagger H)(X_i\mathbin{\cdot}X_i).
\]

After independently deriving a nonzero vacuum (X_i=x_{0i}+\chi_i), it would
contain

\[
2\lambda_p(H^\dagger H)(x_0\mathbin{\cdot}\chi).
\]

This can mix the radial exit mode with the Higgs and could generate the WP683
same-channel reference topology.

## Authority boundary

The current source registry explicitly leaves the complete mixed scalar
potential and common-frame vacuum unresolved. Neither (lambda_p) nor the
vacuum direction may be inferred from a desired interference signal. At
(lambda_p=0) or (x_0=0), the candidate reference vanishes exactly.

Thus this is the lowest legally typed repair, but not a presently admitted
reference amplitude. The next work must derive the complete invariant mixed
potential and its vacuum before computing interference.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp684_exit_flavon_higgs_portal_typing.py

Generated result: results/wp684_exit_flavon_higgs_portal_typing.json.
