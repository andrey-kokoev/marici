# Arbitrary-n one-loop MHV physical-pole survival

## Theorem

For every `n>=4`, each cyclic local propagator

$$
P_i:=\langle AB\,i(i+1)\rangle=0,
\qquad i\in\mathbb Z/n\mathbb Z,
$$

is a genuine codimension-one pole of the one-loop MHV Kermit sum

$$
\mathcal A_n^{(2),1}=\sum_{1<a<b<n}K[a;b].
$$

Its generic residue is nonzero.

## Incidence count

Let

$$
I_n=\{2,3,\ldots,n-1\}.
$$

For an internal cyclic edge `(i,i+1)` with `i in I_n`, the physical factor appears as the middle denominator of every Kermit cell whose unordered index pair contains `i`. The second index can be any element of `I_n\setminus\{i\}`. Hence exactly

$$
|I_n|-1=n-3
$$

cells meet that physical boundary.

For the two anchor-adjacent physical edges, the same count follows directly:

- `langle AB12 rangle` occurs in `K[2;b]` for `3<=b<=n-1`;
- `langle ABn1 rangle` occurs in `K[a;n-1]` for `2<=a<=n-2`.

Thus every cyclic physical divisor has incidence `n-3`.

## Boundary canonical form

Each Kermit term is the canonical form of an oriented one-loop BCFW cell. On a local propagator boundary, the `n-3` incident cells restrict to the induced triangulation of that external boundary. Unlike an internal anchor facet, this boundary has no partner on its opposite side. The induced orientations agree with the outward physical-boundary orientation.

Therefore

$$
\operatorname{Res}_{P_i=0}\mathcal A_n^{(2),1}
=
\sum_{r=1}^{n-3}\Omega_{i,r},
$$

where the `Omega_(i,r)` are the canonical forms of the boundary cells.

Choose positive external data and a point in the positive interior of this boundary. Every `Omega_(i,r)` evaluates with the same sign and at least one cell is nonempty. Their sum is therefore strictly nonzero there. Since the residue is rational, being nonzero at one generic positive point proves that it is not the zero rational form. Consequently it is nonzero on a Zariski-open set of the physical divisor.

Hence every cyclic local propagator survives in the complete Kermit sum.

## Contrast with spurious boundaries

- Physical divisor: `n-3` cells with the same outward orientation.
- Spurious anchor divisor: `2(n-4)` cells paired by
  $$
  K[\{k-1,r\}]\leftrightarrow K[\{k,r\}]
  $$
  with opposite orientations.

This orientation distinction is the combinatorial origin of physical survival versus spurious cancellation.

## Executable evidence

`check_one_loop_mhv_kermit_pole_census.py` verifies exact incidence `n-3` and nonzero generic rational residues on every cyclic physical pole for `5<=n<=8`. The four-point case is the single box form and is immediate.

## Claim boundary

This proves generic codimension-one physical-pole survival for the pre-integration one-loop MHV integrand. It does not normalize the residue as a forward limit, analyze simultaneous cuts, choose an integration contour, or regulate infrared divergences.
