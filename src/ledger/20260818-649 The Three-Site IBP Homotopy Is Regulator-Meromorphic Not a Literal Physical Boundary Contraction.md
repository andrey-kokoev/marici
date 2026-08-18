# 649 — The Three-Site IBP Homotopy Is Regulator-Meromorphic Not a Literal Physical Boundary Contraction

## Hard-to-vary claim

For the homogeneous one-loop three-site integral, the integration-by-parts
identities are geometrically justified in a regulator chamber where the
Cayley--Menger twist vanishes on the physical-chain boundary. At the
physical dimension they survive by meromorphic continuation, not by literal
boundary vanishing.

## Source exponent

The primary source defines the Cayley--Menger twist exponent by

\[
\gamma=\frac{d-n_s-L}{2}.
\]

For

\[
d=3+2\epsilon,
\qquad n_s=3,
\qquad L=1,
\]

this is

\[
\boxed{\gamma=\epsilon-\frac12}.
\]

Near a generic Cayley--Menger boundary component \(K=0\), the twist has
normal behavior

\[
K^\gamma=K^{\epsilon-1/2}.
\]

It vanishes literally only when

\[
\operatorname{Re}\epsilon>\frac12.
\]

At the physical limit,

\[
\epsilon\longrightarrow0,
\qquad
K^\gamma\longrightarrow K^{-1/2},
\]

which is locally integrable but does not vanish on the boundary.

## IBP typing

The source's equation for integration by parts is valid first in the
regulator chamber where Stokes boundary terms vanish and is then continued
meromorphically to the physical dimension. Thus

\[
\boxed{
\text{physical IBP identity}
=
\text{continued regulator identity},
}
\]

not a literal contraction of the physical semialgebraic boundary.

This does not invalidate the source master reduction or differential
equations. It restricts what may be inferred from them: an algebraic IBP
relation at \(\epsilon=0\) does not by itself provide a chain-level
nullhomotopy on the Cayley--Menger faces.

## Consequence for the elliptic comparison

Entries 644 and 646 exclude a conductor-supported or denominator-wall
boundary homotopy. The remaining Cayley--Menger-face homotopy is
regulator-meromorphic. Therefore a canonical physical elliptic projection
still requires one of:

- a regulator-compatible specialization theorem for the twisted cycle;
- an explicit finite-part chain homotopy at \(\epsilon=0\);
- independently specified analytic-continuation/Stokes data.

None is supplied merely by the IBP quotient.

The new datum, if required, is chain/coefficient framing. It is not a new
carrier incidence stratum.

## Scope

This entry establishes the exponent and the logical status of the IBP
boundary argument. It does not prove regulator dependence of the final
physical period or failure of every possible specialization map.

## Next falsifier

Take the explicit source IBP primitive for the \(q_{G_{12}}\) residue
sector, compute its Laurent expansion at

\[
\epsilon=0,
\]

and test whether the finite-part boundary functional is independent of
regulator path and primitive representative. Choice independence would
construct the missing physical-chain homotopy; surviving dependence would
exclude a canonical elliptic projection from the current source data.

## Evidence

- temp/arxiv-2408.16386-source/sections/method.tex, equations defining
  \(\gamma\), the twist boundary condition, and IBP;
- temp/arxiv-2408.16386-source/sections/applications.tex, the specialization
  \(d=3+2\epsilon\);
- Entry 646.
