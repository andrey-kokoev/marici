# Scalar Coorientation and Vanishing Octagonal Contact Curvature

## Record

Date: 2026-08-13

Status: the eight-point marked distance-two matching is now derived without QTDS target input.
Alternating scalar geometry canonically coorients the eight physical diagonals, a unique-sink rule
constructs the contact slots of every quadrangulation, and scalar flip distance gives a unique
marked assignment. The induced local edge transport has exactly zero ordinary and
orientation-twisted circulation on the octagon.

The scalar presentation antecedent of the deck-odd octagonal contact class therefore vanishes.

Forward completion (entry 83): every selected length-two path retains its mark at the middle
vertex, so the entire chain lies in a direct sum of fixed-mark associahedral face complexes.
Entry 38's facewise Pochhammer/Cousin map acts there without dependent occurrence
specialization. It follows that the marked worldsheet class
\(\mathfrak o_{8,\rm mark}^{\rm PC}\) vanishes exactly. Only the unmarked/full-symbol horizontal
correspondence remains open.

## Alternating coorientation

Fix one sheet of the alternating cyclic cover, with even vertices carrying the first polarity.
Every physical diagonal joins vertices of opposite parity. Orient it from its even endpoint to
its odd endpoint and choose the same transverse side of that oriented chord.

For a canonically written physical diagonal \(D=(a,b)\), \(a<b\), denote the increasing-arc side
by \(0\) and its complement by \(1\). The two coorientation patterns are

\[
\nu_+(D)=
\begin{cases}
1,&a\ \text{even},\\
0,&a\ \text{odd},
\end{cases}
\qquad
\nu_-(D)=1-\nu_+(D).
\]

One-step rotation exchanges \(\nu_+\) and \(\nu_-\), including the geometric transport of the
chosen side.

## The directed dual-tree rule

Let \(Q\) be an octagon quadrangulation. Its three quadrilateral regions form a three-vertex dual
tree. For every \(D\in Q\), direct the corresponding dual edge toward the region on side
\(\nu_\epsilon(D)\).

If the directed tree has a unique sink \(R\), define

\[
\operatorname{Slot}_\epsilon(Q)
=
\{\text{the two scalar diagonals of }R\}.
\]

If the directed tree has two sinks, set

\[
\operatorname{Slot}_\epsilon(Q)=\varnothing.
\]

This construction uses only:

1. the cyclic octagon;
2. its alternating coloring;
3. the physical/scalar parity distinction;
4. the incidence of quadrilateral regions.

It uses neither QTDS numerators nor the contact table of entry 23.

## Finite uniqueness theorem

There are \(2^8\) possible coorientations of the eight physical diagonals. Apply the same
unique-sink rule to each pattern. Impose scalar marked-contact conservation:

\[
\operatorname{multiset}
\left\{
d:\ d\in T,\ \rho(T)=\varnothing
\right\}
=
\operatorname{multiset}
\left\{
d:\ d\in\operatorname{Slot}(Q)
\right\}.
\]

The left side contains the twenty marked occurrences supplied by the four zero-core scalar
triangulations.

Exact enumeration gives precisely two solutions among all \(256\) patterns:

\[
\nu_+,\qquad \nu_-.
\]

Independently, requiring one-step rotation to reverse the coorientation selects precisely the
same two patterns.

Thus:

> Within the local directed-dual-tree ansatz, scalar contact conservation and cyclic deck
> covariance uniquely derive the two alternating contact-slot systems.

## Scalar-only marked matching

For every zero-core scalar triangulation \(T\) and mark \(d\in T\), and every target slot
\((Q,d)\), define

\[
\operatorname{dist}_d(T,Q)
=
\min_{\substack{T'\in\pi_{\rm core}^{-1}(Q)\\d\in T'}}
\operatorname{dist}_{K(\alpha_8)}(T,T'),
\]

where the distance is measured in the scalar octagon associahedron.

For each mark separately, minimize the total distance over bijections between source occurrences
and scalar-derived target slots. The exact assignment problem has:

1. one and only one minimizer for each polarity;
2. twenty matched occurrences;
3. distance exactly two for every occurrence;
4. exact exchange of the two matchings by one-step rotation.

Only after deriving these matchings was their target support compared with the actual QTDS
numerators. Both twenty-element sets agree exactly.

This closes the representational circularity in entry 23. QTDS is now a verification target,
not an input to the matching.

## Lift before core forgetting

For each matched triple \((T,d,Q^\epsilon)\), there is a unique endpoint refinement

\[
\widehat Q^\epsilon_{T,d}
\in
\pi_{\rm core}^{-1}(Q^\epsilon)
\]

containing \(d\) at scalar flip distance two from \(T\). There can be one or two shortest paths,
but when there are two they differ only by the order of commuting flips and have the same
endpoint.

Let \(\widehat\gamma^\epsilon_{T,d}\) be the equal average of those scalar paths. Then

\[
\widehat H_{\rm ct}
=
\sum_{(T,d)}
-X_d
\left(
\widehat\gamma^+_{T,d}
-
\widehat\gamma^-_{T,d}
\right)
\]

is a genuine cellular one-chain in the scalar octagon associahedron, not merely in the
quadrangulation quotient. Its common zero-core endpoint cancels term by term, and

\[
\partial\widehat H_{\rm ct}
=
\sum_{(T,d)}
-X_d
\left(
\widehat Q^+_{T,d}
-
\widehat Q^-_{T,d}
\right).
\]

It is exactly deck odd under one-step rotation. This is the preferred source chain for a future
facewise Pochhammer/Cousin comparison. Core forgetting sends its endpoint boundary to the contact
boundary below.

## Local oriented edge transport

Pair the plus and minus destinations of the same scalar source occurrence:

\[
(T,d)
\longmapsto
\left(Q^-_{T,d},Q^+_{T,d}\right).
\]

In the twelve-vertex quadrangulation flip graph, every pair has distance two. Orient its geodesic
from \(Q^-_{T,d}\) to \(Q^+_{T,d}\) and give it coefficient \(-X_d\). If two geodesics exist,
take their equal average. Define

\[
H_{\rm ct}
=
\sum_{(T,d)}
-X_d\,
\operatorname{Avg}
\operatorname{Geo}_2
\left(Q^-_{T,d},Q^+_{T,d}\right).
\]

The exact cellular boundary is

\[
\boxed{
\partial H_{\rm ct}=K^+-K^-.
}
\]

The transport consists of sixteen unique two-edge geodesics and four two-route ambiguities. The
four ambiguities occur exactly for the diameter marks

\[
(0,4),\qquad(1,5),\qquad(2,6),\qquad(3,7),
\]

and their two routes are the two halves of the corresponding scalar-labelled square.

Multiplying the coefficient on an edge by its shared physical channel writes this transport in
the local form required by entry 19, with no repair pole. Its channel residue is zero, as
appropriate for the contact subcomplex.

## The route torsor and its \(\mathbb Z_2\) monodromy

Choosing one route in each diameter square gives sixteen integral transports. None is
one-step-cyclic and deck odd.

Under one-step rotation, polarity reverses, so a directed path is rotated and then reversed. The
two routes are either preserved or exchanged. Transport through the full four-diameter orbit
exchanges the two initial routes: the total route-swap parity is odd. Therefore no absolute
integral section exists.

If \(\lambda_i\) is the weight of the first route in square \(i\), cyclic covariance transports it
as either

\[
\lambda_{i+1}=\lambda_i
\]

or

\[
\lambda_{i+1}=1-\lambda_i.
\]

Odd monodromy forces

\[
\lambda_i=\frac12
\]

for every square. Consequently the equal-route transport is the unique rational
cyclic-equivariant one, and

\[
r(H_{\rm ct})=-H_{\rm ct}
\]

under one-step rotation.

This is not a defect of the all-fibers object. It is the concrete realization of the polarity
torsor anticipated in entry 18: an absolute route section fails, while the deck-aware transport
exists.

## Octagonal calculation

Let \(O\) be the eight-edge boundary of the missing global face. The scalar-derived transport is
supported on sixteen flip edges and satisfies the stronger statement

\[
\operatorname{supp}H_{\rm ct}\cap\partial O=\varnothing.
\]

Hence

\[
\oint_{\partial O}H_{\rm ct}=0.
\]

The exact audit also constructs a representative \(\eta\) of the unique nontrivial rank-one sign
local system on the projective-plane presentation complex. Transporting every edge coefficient
to one basepoint gives

\[
\boxed{
\oint_{\partial O}^{\eta}H_{\rm ct}=0.
}
\]

Both equations hold for the cyclic half-sum. The ordinary equation also holds for all sixteen
integral square-route choices.

Therefore:

> The deck-odd octagonal contact curvature vanishes exactly in the scalar presentation
> coefficient complex. The first apparent global obstruction reduces to the nontrivial route
> torsor, and that torsor is precisely what the alternating/sign enrichment retains.

## What this does and does not prove

Established:

1. target-independent scalar contact slots;
2. uniqueness of the two alternating coorientations within the local dual-flow ansatz;
3. the unique scalar marked distance-two matching;
4. exact agreement with independently calculated QTDS contacts;
5. a local oriented contact transport with the correct boundary;
6. an explicit deck-odd lift on actual scalar associahedron edges;
7. its cyclic half-sum and integral route torsor after core forgetting;
8. zero ordinary and sign-twisted octagonal contact circulation.

Not established at the time of this entry:

1. a filtered facewise Pochhammer/Cousin image of this transport;
2. a chain-level inverse scalar pairing at resonant boundaries;
3. vanishing of the corresponding class after applying an unconstructed worldsheet comparison;
4. uniqueness of a twisted-form primitive modulo residue-free exact terms;
5. identification of the square transport or octagonal equation with the Jordan identity;
6. an all-multiplicity construction of the directed-dual-tree transfer.

Entry 83 completes items 1 and 3 in the marked contact sector. Items 2, 4, and 5 remain open at
the stated stronger levels; full-symbol horizontal assembly is also still open.

If a future filtered comparison is a genuine local chain map, it must send the zero scalar
octagonal curvature to zero. A nonzero worldsheet \(\mathfrak o_8\) would therefore diagnose a
comparison, regularization, or order-of-limits anomaly rather than a failure of the finite scalar
contact geometry.

## Sharpened worldsheet handoff

At generic nonresonant \(\alpha'\), generalized Pochhammer regularization supplies a map from
locally finite twisted homology to compact twisted homology and turns the ordered real chamber
into a loaded associahedral cycle. It also organizes field-theory localization by associahedron
faces.

At the time of this entry, that established map was not yet known to be the morphism required
here. The new source is the marked
one-chain \(\widehat H_{\rm ct}\), not merely the top-dimensional loaded chamber or its homology
class. The missing comparison must assign a loaded current to every scalar flip edge and satisfy

\[
\partial_{\nabla}
\chi_{\alpha'}(\widehat H_{\rm ct})
=
\chi_{\alpha'}(\partial\widehat H_{\rm ct}),
\]

\[
\operatorname{Res}_D
\chi_{\alpha'}(\widehat H_{\rm ct})=0,
\]

and

\[
\chi_{\alpha'}(r\widehat H_{\rm ct})
=
-r\chi_{\alpha'}(\widehat H_{\rm ct}).
\]

It must then commute with the selected scalar \(t\)-grade and the nearby-cycle/finite-part
operation. Standard top-cycle regularization alone proves none of these marked-edge statements.

Forward completion (entry 83): the fixed-mark path lemma puts every summand of
\(\widehat H_{\rm ct}\) in \(X_dC_1(K_\alpha^{(d)})\). The facewise PC map of entry 38 therefore
satisfies all three displayed equations on this chain. No dependent route coefficient
specialization is needed for the marked summand.

## Reproducible audit

Run:

    python research/nima/check_scalar_edge_transport.py

The standard-library script checks all \(256\) coorientation patterns, both scalar-derived
twenty-element matchings, their independent QTDS verification, every local geodesic, all sixteen
integral square routings, cyclic route monodromy, exact contact boundary, deck oddness, and both
octagonal circulations.

## Decision

Promote:

> The eight-point marked contact transfer is intrinsic to alternating scalar flip geometry, and
> its deck-odd octagonal curvature vanishes at presentation level.

The primary frontier at this point moved one categorical layer upward:

> construct the filtered scalar-to-worldsheet comparison on this explicit edge transport and
> test whether it preserves the proven zero octagonal curvature in the residue-free nearby-cycle
> complex.

Entry 83 completes this objective for the marked contact sector and replaces the surviving
full-symbol objective by an additive residue/Gysin correspondence totalization.

Forward update: entry 25 shows that the same scalar rule survives ten-point QTDS verification and
a twelve-point scalar-only stress test. This promotes the all-arity Catalan/discrete-Morse
transfer to the primary Nima theorem target while retaining the filtered comparison as the
parallel worldsheet target.

## Source

- [Mizera, *Combinatorics and Topology of Kawai--Lewellen--Tye Relations*](https://arxiv.org/abs/1706.08527)
  supplies the generic generalized-Pochhammer regularization of loaded associahedral twisted
  cycles and their face localization. The marked scalar edge chain, the historical comparison
  gap in this entry, and its fixed-mark resolution in entry 83 are Marici results.
