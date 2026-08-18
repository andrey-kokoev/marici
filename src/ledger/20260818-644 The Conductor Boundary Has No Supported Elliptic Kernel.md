---
authors:
  - marici.Nima
date: 2026-08-18
---
# The Conductor Boundary Has No Supported Elliptic Kernel

## Hard-to-vary claim

On the nonsoft open, the wall-conductor term in the physical localization
triangle has no geometrically supported morphism to the elliptic infinity
term.  Any nonzero elliptic comparison of the full relative class would
therefore require additional bulk-extension or physical-chain data; it
cannot be induced by the conductor boundary alone.

## Support calculation

Let

\[
i_C:C\hookrightarrow S_E,
\qquad
i_\infty:D_\infty\hookrightarrow S_E
\]

denote the conductor support of the marked walls and the elliptic infinity
divisor.  Entry 595 proves, on the nonsoft open \(xyz\ne0\), that

\[
C\cap D_\infty=\varnothing.
\]

Indeed the three conductor equations have nonzero values at infinity

\[
R_1(\infty)=-x,
\qquad
R_2(\infty)=y,
\qquad
R_3(\infty)=z.
\]

Proper/support base change therefore gives

\[
i_\infty^!i_{C*}=0.
\]

Equivalently, every kernel whose source is supported on \(C\) and whose
target is supported on \(D_\infty\) vanishes.  This conclusion is
independent of the rank-twenty presentation of the marked residue object:
refining the conductor term by normalization, Cech intersections, or local
systems does not create an intersection of its support with infinity.

## Localization-triangle consequence

The physical class belongs to the relative object of Entries 592--596,
schematically

\[
H^2(S_E\setminus W)
\longrightarrow
\bigoplus_i H^1(W_i^\nu\setminus C_i)(-1)
\longrightarrow
\bigoplus_{i<j}H^0(W_i\cap W_j)(-2).
\]

For a morphism from this localization triangle to the elliptic infinity
triangle, the component sourced purely by the conductor boundary must be
zero.  Hence

\[
\boxed{\operatorname{rank}(C\text{-supported}\to
\mathbb V_{\rm ell}(-1))=0.}
\]

This is stronger than saying that the ordinary absolute infinity-Gysin map
is inadmissible: it excludes the conductor boundary itself as the missing
elliptic carrier.

## What is not proved

The vanishing supported component does **not** by itself prove that the full
relative physical class has zero elliptic image.  A morphism of triangles
could still contain a bulk map together with a compatible nullhomotopy.  But
that datum is not supplied by the wall support and is not determined by the
rank-thirty-five census.

Thus the remaining question is no longer the rank of a wall-to-infinity
map.  It is whether the primary physical integration chain canonically
supplies the required extension datum.

## Updated frontier

Construct the physical relative-chain realization of the rank-thirty-five
source summand and compute the induced nullhomotopy against the conductor
boundary.  The falsifier is:

\[
\boxed{
\text{does the chain-derived bulk map descend independently of choices?}
}
\]

If it does not, the physical class has no canonical elliptic projection. If
it does, its elliptic image comes from chain framing rather than conductor
support.

## Evidence

- `research/benincasa/physical_g12_conductor_infinity_support.py`;
- Entries 592--596;
- the disjoint-support identity \(i_\infty^!i_{C*}=0\).

## Outcome contract

~~~json
{
  "claim": "The physical conductor boundary itself can map nontrivially to the elliptic infinity sector through a geometrically supported kernel.",
  "status": "falsified_on_nonsoft_open",
  "support_intersection": "empty",
  "supported_boundary_to_elliptic_rank": 0,
  "full_relative_elliptic_image_determined": false,
  "remaining_datum": "chain-derived bulk map with compatible nullhomotopy",
  "next_experiment": "Construct the physical relative-chain realization and test choice-independent descent of its bulk map."
}
~~~
