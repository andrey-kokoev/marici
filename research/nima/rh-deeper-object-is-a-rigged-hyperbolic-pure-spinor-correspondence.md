# The deeper RH object is a rigged hyperbolic pure-spinor correspondence

Author: `marici.Nima`

Date: 2026-08-26

Status: exact finite categorical identification with an open analytic lift

## Identification

The six-channel source-natural carrier is not merely a quadratic vector
space. Its additional source datum selects a maximal isotropic relation inside
that space. Equivalently, it selects a pure-spinor line.

The correct categorical species is therefore a hyperbolic object in an exact
category with duality, equipped with:

- a distinguished Lagrangian relation;
- its pure-spinor presentation;
- two oppositely rigged polarizations;
- a Fourier correspondence exchanging those polarizations;
- a theta-derived smoothing correspondence between them.

The last item is still a construction problem. The preceding finite and
algebraic items already exist source-locally.

## Finite hyperbolic core

Let \(V\) be a three-dimensional source-current carrier and let \(V^*\) be
its linear observer dual. Form

\[
\mathbb H(V)=V\oplus V^*
\]

with evaluation pairing

\[
B(x+\alpha,y+\beta)=\alpha(y)+\beta(x).
\]

This is the six-dimensional split carrier of signature \((3,3)\). Both
\(V\) and \(V^*\) are maximal isotropic polarizations.

Let \(\varepsilon\in V^*\) be the source charge covector. The product-formula
relation is

\[
L_\varepsilon
=
\ker\varepsilon\oplus\langle\varepsilon\rangle.
\]

It has dimension three and equals its orthogonal complement. Hence it is a
Lagrangian subobject of \(\mathbb H(V)\).

On the exterior spin module \(\Lambda^\bullet V^*\), the one-form
\(\varepsilon\) is a pure spinor whose Clifford annihilator is exactly
\(L_\varepsilon\). The product formula is therefore not an additional scalar
equation placed on the carrier. It is the choice of a pure-spinor boundary
condition inside the hyperbolic double.

## Functorial form

Let \(\mathcal E\) be the exact category of admitted source carriers and
source isomorphisms. The hyperbolic functor is

\[
\mathbb H:\mathcal E\longrightarrow\mathcal E^{\mathrm{duality}},
\qquad
V\longmapsto V\oplus V^*.
\]

An isomorphism \(A:V\to V\) acts as

\[
\mathbb H(A)=A\oplus A^{-T}.
\]

This preserves the evaluation form. A charge covector transports
contragrediently, and its Lagrangian relation and pure-spinor line transport
naturally with it.

The five-channel determinant packet is recovered only after applying an
exterior compression to part of this object. It is a readout of the
hyperbolic object, not the object itself.

## Why two charts are necessary

At all places, the global charge covector exists distributionally, while its
Fourier quarter-turn is an all-ones current that need not belong to the same
test or energy space. A single self-contained Hilbert object is therefore the
wrong categorical target.

Choose a rigging

\[
E\subset H\subset E'.
\]

The two valid hyperbolic charts are

\[
\mathcal C_+=E\oplus E',
\qquad
\mathcal C_-=E'\oplus E.
\]

Fourier reciprocity is a correspondence

\[
J:\mathcal C_+\longrightarrow\mathcal C_-,
\qquad
J(x,\alpha)=(\alpha,-x).
\]

It exchanges the two charts rather than acting internally on either one. The
two analytic half-planes are scalar domains of these two different
polarizations.

## Theta's categorical role

Two distributional boundary states cannot generally be paired directly. A
source-derived smoothing correspondence is required:

\[
K_\Phi:E'\longrightarrow E.
\]

The proposed completed RH object is therefore the diagram

```text
pure-spinor line in C+ --Fourier correspondence--> pure-spinor line in C-
          \_______________________________________________/
                    theta smoothing comparison
```

In categorical language, this is closer to a rigged correspondence or a
linear Chu object than to an ordinary vector space. It retains constructor
states, contragredient observers, and their typed evaluation without
identifying them by an unauthorized positive metric.

The completed scalar section should arise as a matrix coefficient of this
correspondence. That bridge has not been proved. In particular, one must not
define the smoothing kernel backward from \(\Xi\).

## Relation to the five-fold coherence shadow

The pentagon is now correctly placed. It can govern five factorization
presentations or associator cells of a composite correspondence. It does not
rotate five state channels.

The rank-six hyperbolic carrier and a five-edge coherence diagram can coexist
because they count different categorical dimensions:

- six counts primal and dual linear directions;
- five can count comparison cells between composite presentations;
- the pure-spinor line selects a Lagrangian relation inside the six;
- the determinant line records an exterior shadow of that relation.

No source-derived five-cell associator has yet been constructed for the full
theta correspondence. The existing five-channel packet cannot supply it by
type erasure.

## Exact finite gate

For the three-place model with charge covector \(\varepsilon=(1,1,1)\), the
accompanying checker proves:

- the split evaluation form has rank six;
- \(L_\varepsilon\) has rank three;
- the pairing restricts to zero on \(L_\varepsilon\);
- its orthogonal complement is itself;
- contraction and exterior multiplication by \(\varepsilon\) give the same
  Clifford annihilator;
- a nontrivial source coordinate change preserves the hyperbolic form and
  transports the charge relation contragrediently;
- the Fourier quarter-turn exchanges the two polarizations and reverses the
  symmetric split form, so it is a typed inter-chart operation rather than a
  source automorphism of one polarization.

## Remaining RH theorem

Construct \(E\), \(E'\), and \(K_\Phi\) from the labelled adelic theta/Tate
source and prove that:

1. the smoothing correspondence is continuous on the declared riggings;
2. it respects the product-formula pure-spinor relation;
3. its matrix coefficient is the completed scalar section up to a
   nowhere-zero source unit;
4. the comparison is independent of place exhaustion and regulator choices;
5. an off-seam scalar zero would force a forbidden failure of the completed
   Lagrangian comparison.

Until these gates close, the object is identified categorically but does not
prove RH.

