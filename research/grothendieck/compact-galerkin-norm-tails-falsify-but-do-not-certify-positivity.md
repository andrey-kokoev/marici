# Compact Galerkin norm tails falsify but do not certify positivity

## Correction

The prior claim that a positive finite compression plus a small operator-norm tail can certify full nonnegativity was false.

If `A_M=P_M A P_M` is extended by zero on the orthogonal complement, then zero belongs to its spectrum. Therefore

`inf spectrum(A) >= min(0,lambda_min(A_M))-||A-A_M||`,

not `lambda_min(A_M)-||A-A_M||` when the finite matrix is positive.

## Exact counterexample

For any cutoff `M` and `epsilon>0`, take a diagonal compact self-adjoint operator whose first `M` diagonal entries are positive, whose `(M+1)` entry is `-epsilon`, and whose remaining entries tend to zero. The `M`-mode compression is positive, and the norm tail can be arbitrarily small, yet the full operator is negative.

Thus no finite positive compression plus nonzero unsigned tail estimate proves positivity of a compact operator whose spectrum accumulates at zero.

## What remains valid

A finite negative eigenvalue separated from zero can be certified. If

`lambda_min(A_M)+epsilon_M<0`,

where `epsilon_M>=||A-A_M||`, then the full operator has negative spectrum.

This makes the Sobolev Galerkin programme a rigorous finite falsifier.

## What a proof requires

To certify positivity one needs sign-sensitive information on the complement, for example:

1. a proof that the tail block `C_M` is nonnegative;
2. a Schur estimate controlling the off-diagonal block against positive reserves in both diagonal blocks;
3. a monotone positive decomposition of the tail;
4. an exact factorization `A=T^*T` derived from the arithmetic source.

Norm decay alone supplies none of these.

## Consequence for RH

The compact local Sobolev realization simplifies domain and falsification questions but does not turn RH into a convergent sequence of ordinary finite positivity checks. Negative spectrum is finitely detectable; absence of negative spectrum remains an infinite sign problem.

## Disposition

The two-sided Galerkin certification claim is withdrawn. The quantitative Sobolev tail bounds survive only as negative-eigenvalue certification and as input to a future sign-preserving Schur or factorization argument.
