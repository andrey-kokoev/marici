# The finite endpoint sewing does not flip the even v_alg wall column

## Endpoint input

The two literal physical walls begin at the common point

\[
a=x+z,
\qquad b=y+z,
\]

where the Cayley--Menger square root is nonzero in the strict triangle chamber. Ledger entry 3857 computes the oriented endpoint residues

\[
\rho_{g_1}=-\rho,
\qquad
\rho_{g_2}=+\rho,
\]

with

\[
\rho=
\frac{2z}
{(x-y-z)^2(x-y+z)^2(x+y+z)(x+y+3z)}.
\]

Hence

\[
\rho_{g_1}+ho_{g_2}=0.
\]

The endpoint pole is removed by source Čech sewing, not by introducing a new absolute algebraic class.

## Consequence for the partial thimble column

The oriented wall pieces already contribute

\[
2v_{\rm alg}.
\]

Because the common endpoint correction is the cancellation of equal and opposite scalar germs on a locus where the cover is unramified, it contributes no unmatched component-difference or algebraic-kernel generator. Therefore finite-endpoint sewing leaves the partial column

\[
2v_{\rm alg}
\]

and its parity zero unchanged.

This closes the finite endpoint part of the requested lift.

## Remaining infinity port

The only possible parity-changing correction is now the open infinity port. Existing source results show:

1. the closed physical infinity Leray covector is \((1,1)\) on \((\omega_0,\omega_2)\);
2. its pullback annihilates both \(e_6\) and \(v_{\rm alg}\);
3. the two-sheet open branch-gap sequence is a nonsplit order-two deck extension;
4. that branch-gap calculation explicitly does not close the full four-endpoint relative contour.

Thus the endpoint-marked infinity lift, not finite wall sewing, is the sole remaining source of a possible odd algebraic correction.

## Current column

For the wall-plus-finite-endpoint subchain,

\[
\boxed{
2m_{\rm finite}=0\cdot e_6+2\cdot v_{\rm alg},
}
\]

so modulo two its algebraic column is

\[
(0,0).
\]

The closed thimble column equals this value if and only if the full four-endpoint infinity lift contributes even parity in \(\langle e_6,v_{\rm alg}\rangle\).

Verification:

- `research/voevodsky/checkers/check_finite_endpoint_valg_column.py`
- `research/voevodsky/results/finite_endpoint_valg_column.json`
