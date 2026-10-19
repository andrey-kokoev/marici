# Hodge iteration 2: actual cycle packets and the closure-only obstruction

## Result

A supplied algebraic cycle admits a concrete packet presentation by oriented fundamental chains. Its codimension-one faces cancel; comparison homotopies preserve its homology class. This supplies a **cycle-indexed topological dictionary and necessity lemma**, not an algorithm generating algebraic cycles from Hodge classes or a full higher witnessed-identity package.

There is also a scoped negative result:

> The existence of a finite rational oriented chain with cancelling faces cannot obstruct algebraicity of a rational Hodge class. Every rational cohomology class already has such a representative by Poincare duality and simplicial homology.

This rejects only the **bare-chain-closure** route. A stronger, algebraic-specific coherence obstruction remains an open possibility requiring an independently defined invariant and an all-cycle necessity theorem.

## Actual typed dictionary

Fix smooth projective X of complex dimension d and codimension p. Put k=d-p.

A cycle-supplied packet consists of:

- an actual algebraic cycle Z=sum q_j Z_j, not merely a string saying 'algebraic';
- compatible finite triangulations of X and its algebraic supports;
- the complex orientation on the regular part of each Z_j;
- rational multiplicities q_j and the mapped, oriented 2k-dimensional simplices;
- boundaries, subdivision data and any supplied chain comparisons.

The triangulations are classical imported mathematical structure. Their existence is not a derivation from the finite packet operation library of the foundational conjecture. The subvarieties Z_j are inputs; this construction does not discover them from an arbitrary cohomology class.

The maps are:

    algebraic cycle packet ----support----> Z^p(X)_Q
               |                              |
        mapped fundamental chain          cycle class
               |                              |
               v                              v
    ker(boundary:C_2k->C_(2k-1)) --> H_2k(X,Q) --PD--> H^{2p}(X,Q).

The triangle commutes: PD([c_Z])=cl(Z). On algebraic inputs the final class has type (p,p). Rational equivalences have zero homological cycle class. None of these statements asserts injectivity of the cycle-class map.

The types distinguish real topological facet dimension from complex algebraic codimension. For a codimension-two surface in a complex fourfold, the fundamental chain has real dimension four, and its facets have real dimension three. Those facets are not codimension-one complex subvarieties. Packet arity is not identified with either number.

## Necessity lemma and proof

**Lemma.** Every supplied codimension-p rational algebraic cycle on smooth projective X admits the packet data above with boundary c_Z=0. Its homology class is independent of compatible triangulation, and its Poincare dual is the standard cycle class.

**Proof, using stated standard facts.** The projective variety and a finite set of algebraic supports admit compatible finite semialgebraic triangulations. A pure k-dimensional complex component has its complex orientation on the regular locus. Its singular locus has real dimension at most 2k-2. Consequently each top-chain facet of dimension 2k-1 is a manifold facet: the two incident top simplices induce opposite orientations. Their contributions cancel. Rational linear combinations preserve cancellation. The resulting oriented fundamental homology class is the one used in the standard homological cycle-class construction. Compatible subdivisions and common refinements preserve this class by the usual subdivision chain homotopy. Poincare duality on the smooth compact ambient X gives cl(Z). This uses imported triangulation, fundamental-class and homology-comparison theorems; it is not a new formal proof of those results.

These are necessary data for algebraic cycles. They are not sufficient data for algebraicity. In particular the forgetful packet, retaining its actual mapped chain but discarding its algebraic-support evidence, also makes sense for nonalgebraic topological cycles.

## A codimension-two algebraic packet, explicitly checked

Let

    X=(P1_C)^4,
    Z=P1_C x P1_C x {pt} x {pt}.

X is a smooth projective complex fourfold and Z is an algebraic surface of complex codimension two. Identify each varying P1 topologically with an oriented sphere, triangulated by the boundary of a tetrahedron. Fix the sphere orientation to match its complex orientation. The cross product uses the six (2,2) shuffle simplices for each pair of triangular faces.

The checker constructs all 96 oriented four-simplices and verifies exact face cancellation. The f-vector is

    (16,84,216,240,96),

with Euler characteristic 4. This is an actual topological triangulation of the supplied algebraic surface, not an abstract non-Hodge counterexample model. The standard P1-sphere identification and algebraic embedding are imported; their rational chart maps are not numerically reconstructed by this checker.

All six coordinate P1 x P1 surfaces give a middle-degree algebraic basis of X by the standard product cohomology description. Their complementary-intersection matrix is nondegenerate. Thus this fourfold is a positive control, not an unresolved candidate for refuting Hodge.

Deleting one four-simplex produces a nonzero boundary. Erasing orientation signs also produces a nonzero boundary. The retained incidence and orientation data genuinely matter to recovery of the chain.

## Explicit comparison witness

For an oriented simplex [v0,...,vr], form its prism chain

    P([v0,...,vr]) = sum_i (-1)^i
      [(v0,0),...,(vi,0),(vi,1),...,(vr,1)].

The exact identity is

    boundary P(c) + P(boundary c) = c_top - c_bottom.

The checker verifies it on open simplices and the closed sphere, circle, algebraic-surface and torus chains. For the four-chain surface, the prism has 480 five-simplices and its boundary is precisely the difference of the two endpoint chains. It retains a comparison witness rather than merely asserting equal endpoint classes.

This constructs a finite chain-level comparison. General compatible refinements rely on the imported subdivision theorem. Neither this prism nor equality in homology supplies the entire foundational programme's independent higher fillers, their comparisons and licensed continuations.

## Closed faces do not imply algebraic support

Take E_i=C/(Z+iZ), a square-lattice elliptic curve, and X=E_i x E_i. Its standard complex-torus uniformization and algebraicity are imported. Let T be the product of the real x-circles in the two factors. Triangulating each circle with three edges gives a product triangulation with 9 vertices, 27 edges and 18 oriented triangles. All boundaries cancel.

In real period-one coordinates (x1,y1,x2,y2), orient T by dx1 wedge dx2 and X by dx1 wedge dy1 wedge dx2 wedge dy2. Its integral Poincare dual is

    alpha = -dy1 wedge dy2.

Writing dz_j=dx_j+i dy_j gives a nonzero (2,0) coefficient +1/4, with a nonzero conjugate (0,2) coefficient. Equivalently J*alpha=-dx1 wedge dx2 differs from alpha. These constant forms are parallel and harmonic for the flat product metric, so the nonzero components persist in cohomology; this is not merely a representative-level mismatch. Thus the real degree-two class is not of type (1,1).

It therefore cannot be an algebraic divisor class, despite having a finite oriented, face-coherent chain representative. **It is not a Hodge-conjecture counterexample**, because it fails the necessary Hodge-type hypothesis. The exact checker computes the exterior-form expansion, complex-structure action and dual-orientation sign.

## Why the bare-closure route cannot detect even a genuine Hodge candidate

Let alpha be any rational degree-2p class on smooth projective X. Poincare duality gives a rational homology class of degree 2(d-p). Singular homology is defined by finite rational cycles modulo boundaries; a finite triangulation of X computes the same homology. Hence alpha has a finite rational simplicial representative c with boundary c=0.

This argument does not use Hodge type or algebraicity. Therefore a detector that reports nonalgebraicity solely because no such closed chain exists has no nonzero cases on rational Hodge classes. The criterion is rejected globally at this stated topological scope.

This says nothing against obstructions depending on additional algebraic, holomorphic or Hodge-theoretic structure. It does require that such structure be supplied and proved necessary for every algebraic cycle. Restricting the allowed topological packet library can create presentation failures, but those failures are not Hodge obstructions unless algebraic cycles are proved to lie in that restricted library.

## Net disposition

- `packet-coherence-dictionary`: constructed at the cycle-supplied fundamental-chain/necessity scope.
- `bare-chain-closure-obstruction`: a new explicitly rejected candidate, retained as a nongating control for future obstruction work.
- The full source-generation and higher witnessed-identity claims remain unproved.
- No genuine rational Hodge candidate or obstruction is selected.
- `literature-boundary-audit` is the next executable action before candidate selection.

## Reproduce

    python research/voevodsky/checkers/check_hodge_cycle_packet_dictionary.py

Contract: `research/conjecture_net/contracts/hodge-cycle-packet-dictionary.v1.json`.
Receipt: `research/voevodsky/results/hodge-cycle-packet-dictionary-v1.json`.

Nine checks pass. The mathematical result is the written necessity/no-go argument using explicitly imported standard theorems, with exact finite chain and differential-form controls. This is not proof-assistant certification or new evidence against rational Hodge.
