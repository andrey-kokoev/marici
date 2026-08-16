---
authors:
  - marici.Benincasa
date: 2026-08-15
---
# Wall Residue Has No Canonical Absolute Nine-Master Coordinates

## Record

Status: the weight-\(-1\) logarithmic wall class of entry 235 cannot be
assigned canonical coordinates in the absolute equation-(58) nine-master
module using the frozen source maps. Its parent master is \(e_6\), but that
is ancestry data, not an absolute cohomology coordinate.

Entry 236's zero infinity-Gysin image remains valid. This entry sharpens its
conditional phrase “whenever pushed”: the required pushforward is not among
the frozen canonical arrows.

No splitting, projector, support summand, carrier cell, or normalization is
added.

## Deutsch--Popperian conjecture tested

The hard-to-vary claim was

\[
\boxed{
\text{the frozen marked geometry canonically pushes the weight }-1
\text{ wall residue into }\mathcal M_q^{(9)}.
}
\]

The finite falsifier was a type-and-variance audit of the localization
sequence before selecting any master coordinates.

## Frozen coefficient types

Let \(S\) denote the \(q_{\mathcal G_{12}}\)-residue surface and let
\(W\) denote the finite wall supplied by the actual lower denominator
marks. Put

\[
U=S\setminus W.
\]

The equation-(58) module computed in entry 169 is the absolute residue
surface object

\[
\mathcal M_q^{(9)}\subset H^2_{\rm dR}(S;\mathcal K).
\]

Entry 169 explicitly does not insert the additional finite denominator
marks into that module. The complete occurrence lift instead defines a
marked meromorphic class on \(U\). Taking its logarithmic residue along the
wall gives

\[
[F_{-1}]\in H^1_{\rm dR}(W;\mathcal K|_W)(-1).
\]

The degree follows directly from the calculation: a two-form in
\((r,n)\) leaves a one-form in \(n\) after \(\operatorname{Res}_{r=0}\).

## Localization gate

The frozen localization sequence contains

\[
H^2(S;\mathcal K)
\xrightarrow{j^*}
H^2(U;\mathcal K)
\xrightarrow{\operatorname{Res}_W}
H^1(W;\mathcal K|_W)(-1)
\xrightarrow{\operatorname{Gys}_W}
H^3(S;\mathcal K).
\]

Therefore the canonical continuation from the wall residue is

\[
H^1(W)(-1)\longrightarrow H^3(S),
\]

not

\[
H^1(W)(-1)\longrightarrow H^2(S).
\]

Hence

\[
\boxed{
\text{there is no canonical frozen arrow }
[F_{-1}]\longrightarrow\mathcal M_q^{(9)}.
}
\]

A map in that direction would require a splitting of localization, a
contracting homotopy, or a separately derived physical relative-realization
map. Choosing one after seeing the desired \(e_6\), \(v_{\rm alg}\), or
\(L_1\) target is prohibited.

## What the \(e_6\) ancestry does and does not say

The complete form used in entries 234--235 is

\[
-\frac12\frac{K_1\,da\wedge db}{K^{3/2}}D_{\rm low},
\]

whose equation-(58) parent is the double-pole master \(e_6\). Thus the
wall class has the source-defined ancestry label

\[
\boxed{\operatorname{parent}[F_{-1}]=e_6.}
\]

But the residue operation has changed both support and cohomological degree.
Erasing \(D_{\rm low}\) or declaring the resulting wall one-form to be an
\(e_6\) two-form would reverse the canonical localization arrow. Therefore

\[
\boxed{
e_6\text{ ancestry}\not\Rightarrow e_6\text{ coordinate in }
\mathcal M_q^{(9)}.
}
\]

In particular, the invariance of \(\langle e_6\rangle\) under the absolute
Gauss--Manin connection does not resolve this type mismatch.

## Relation to infinity Gysin

Entry 236 proved scheme-theoretic disjointness between the finite wall and
the anticanonical infinity divisor. Thus the supported class has zero direct
elliptic boundary image:

\[
R_\infty([F_{-1}])=0.
\]

That support theorem does not manufacture an absolute nine-master lift.
Consequently it is safe to exclude a direct Legendre boundary component,
but it is not safe to select coordinates in the rank-seven kernel.

## Verdict

The canonical-pushforward conjecture is falsified in the frozen category:

\[
\boxed{
\text{the weight }-1\text{ wall class is relative/support data, not an
absolute nine-master vector.}
}
\]

This is a smaller surviving statement than entry 236's conditional kernel
placement. The class remains coefficient complexity over the existing
marked carrier. No new carrier incidence is required.

## Classification

- existing carrier: unchanged finite marked wall and exceptional model;
- absolute coefficient object: \(\mathcal M_q^{(9)}\subset H^2(S)\);
- wall coefficient object: \(H^1(W)(-1)\);
- parent-master ancestry: \(e_6\);
- direct Legendre/infinity-Gysin image: zero;
- canonical rank-seven-kernel coordinates: absent;
- missing datum: physical relative-realization or another predeclared
  localization splitting;
- genuinely new carrier datum: none.

## Exact evidence

- `research/benincasa/check_wall_to_absolute_type_gate.rs`;
- `research/benincasa/wall-to-absolute-type-gate.json`;
- source master ordering and marked-denominator exclusion of entry 169;
- complete \(e_6D_{\rm low}\) form of entries 234--235;
- warnings-denied optimized Rust compilation and execution.

## Next finite falsifier

Remain in the correctly typed marked relative category. Construct the
nearby/localization morphism from the wall object

\[
H^1(W)(-1)
\]

to the physical relative-chain realization of the full occurrence-labelled
integrand, not to absolute \(H^2(S)\). Test whether the source symmetric wall
cycle kills the entire class or only its current scalar period.

Concretely:

1. retain both endpoints and the lower-half-plane Leray germ;
2. compute the relative cohomology class modulo exact one-forms on the
   punctured wall curve;
3. determine whether oddness in \(n\) makes \([F_{-1}]\) cohomologically
   trivial or merely annihilated by the symmetric physical cycle;
4. only after deriving a realization map compare its image with the
   absolute algebraic kernel.

A nontrivial relative class with zero physical pairing would prove that the
integrated chain forgets genuine supported coefficient data. Exactness of
the wall one-form would instead remove the apparent correction before any
nine-master comparison.

## Outcome contract

~~~json
{
  "claim": "The frozen marked geometry canonically pushes the weight -1 wall residue into the absolute nine-master module.",
  "status": "falsified_by_type_and_variance",
  "absolute_object": "H2(S), containing M_q^(9)",
  "wall_object": "H1(W)(-1)",
  "canonical_sequence": "H2(S)->H2(U)->H1(W)(-1)->H3(S)",
  "canonical_wall_to_absolute_H2_arrow": false,
  "parent_master_ancestry": "e6",
  "ancestry_is_coordinate": false,
  "direct_infinity_gysin_image": 0,
  "new_carrier_incidence": false,
  "next_experiment": "Determine the relative cohomology class of the wall one-form and its physical-cycle annihilator."
}
~~~
