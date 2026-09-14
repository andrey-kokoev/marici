# Prior research reduces Evans promotion to one adjoint residual

Date: 2026-09-08

## Exact range classification

For centered prime incidence

\[
B_\Sigma:U_{\rm ar}\to H,
\]

the retained distinct seam-wall coordinates make `B_Sigma` injective.  The theta forcing satisfies the strict classification

\[
\Phi
\in
\overline{\operatorname{ran}B_\Sigma}
\setminus
\operatorname{ran}B_\Sigma.
\]

Indeed one-prime vectors give approximants to `Phi`, but any exact lift would have to erase every distinct prime-wall jump, forcing all source coefficients to zero.

Consequently the theta forcing must remain in its own port

\[
V:\mathbb C_\theta\to H,
\qquad V1=\Phi.
\]

## Unchanged Evans state

The Evans history already solves

\[
(A-z)u_z=V1.
\]

In the three-port first row

\[
(A-z)u_z=V1+B_\Sigma x,
\]

injectivity forces `x=0`.  The arithmetic source law therefore cannot cancel the lower residual without changing the history and its Xi seam mismatch.

## One residual, not two

Closure of the theta line inside the arithmetic incidence range gives

\[
\ker B_\Sigma^\dagger
\subseteq
\ker V^\dagger.
\]

Hence the two lower equations

\[
V^\dagger u_z=0,
\qquad
B_\Sigma^\dagger u_z=0
\]

reduce to the single condition

\[
B_\Sigma^\dagger u_z=0.
\]

If it holds at every Xi zero, the Green identity forces the centered real parameter to vanish.  It is therefore already an RH confinement theorem.

## Consequence for alternative repairs

The bounded compression `V^dagger B_Sigma` exists as a mixed Gram readout but is not an authorized direct dynamic block.  Adding it to the source pencil cannot repair the residual without a separate constructor.  Likewise, choosing `D_U` to cancel `B_Sigma^dagger u_z` at divisor points would fit the arithmetic law to Xi.

A modified history with nonzero arithmetic coordinate remains possible only through a new divisor-preserving chain comparison between its matching complex and the original Evans complex.

## Disposition

Prior research has reduced the unchanged-state promotion problem to one well-defined vector identity and proved that no exact theta forcing lift into the centered arithmetic incidence exists.  There is no remaining auxiliary source coordinate available to cancel the residual.  Further progress requires either proving the prime-shell identities for `B_Sigma^dagger u_z` or constructing a genuinely new divisor-preserving modified-history chain map.

## Evidence

- `research/nima/distinct-seam-walls-make-the-centered-incidence-injective-and-exclude-an-exact-theta-lift.md`
- `research/nima/closure-of-the-theta-line-makes-the-arithmetic-adjoint-residual-dominate-the-theta-residual.md`
- `research/nima/evans-to-green-promotion-is-one-vector-valued-arithmetic-interpolation-residual.md`
- `research/nima/the-cross-reservoir-map-is-the-theta-source-compression-of-the-labelled-incidence.md`
