# The full four-endpoint boundary is principal and adds no algebraic column

## Exact principal splitter

For the infinity elliptic curve, let

\[
D_+=p_\infty^+-p_0^+,
\qquad
D_-=p_\infty^--p_0^-.
\]

The odd endpoint boundary of the sign-weighted physical interval is

\[
\tau=D_+-D_-.
\]

Ledger entry 3637 gives the explicit source function

\[
\boxed{
f=\frac{W-xt^2+y}{t}
}
\]

with

\[
\operatorname{div}(f)=\tau.
\]

Thus \(\tau\) is principal integrally, not merely rationally or modulo two.

## Consequence for endpoint sewing

The full four-endpoint relative boundary admits a source-defined integral splitter. Its endpoint correction is zero in absolute \(\operatorname{Pic}^0\), so it cannot add either \(e_6\) or \(v_{\rm alg}\) to an ambient algebraic column.

Combining this with the finite common-endpoint cancellation gives:

\[
2m_{\rm walls+all\ endpoints}
=0\cdot e_6+2\cdot v_{\rm alg}.
\]

Therefore all wall and endpoint data together have trivial parity

\[
(0,0)\in(\mathbb Z/2)^2.
\]

## What remains—and a correction

This still does not by itself produce the ambient elliptic thimble lift. The closed elliptic part of the four-mark interval has period vector \((1,1)\), but the known physical Leray covector annihilates \(\langle e_6,v_{\rm alg}\rangle\). A functional that annihilates the kernel cannot determine how an integral elliptic cycle lifts through that kernel.

Hence the previous phrase “the infinity endpoint correction may flip the bit” is withdrawn: the endpoint correction is integrally principal and cannot flip it. The only remaining possible nontrivial column is the extension class of the **closed elliptic lift itself** through

\[
0\to\mathcal A_{--}
\to H^2(S\setminus D_\infty;\mathbb Z)
\to H^1(D_\infty;\mathbb Z)(-1)
\to0.
\]

## Obtained partial result

Every source-normalized relative boundary contribution is now accounted for and has even algebraic parity. Thus any nonzero integral thimble/Gysin column must be intrinsic to the ambient infinity-Gysin extension, not to finite-wall or endpoint sewing.

Verification:

- `research/voevodsky/checkers/check_full_endpoint_principal_column.py`
- `research/voevodsky/results/full_endpoint_principal_column.json`
