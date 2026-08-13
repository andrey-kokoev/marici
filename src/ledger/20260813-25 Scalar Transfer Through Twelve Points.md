# Scalar Transfer Through Twelve Points

## Record

Date: 2026-08-13

Status: the alternating directed-dual-tree rule survives its ten-point falsification without a
repair and its first twelve-point scalar-only stress test without a repair. At ten points, an
exhaustive audit derives seventy marked contacts from scalar geometry and agrees exactly with an
independent symbolic QTDS numerator expansion. At twelve points, a compiled exhaustive scalar
audit derives 252 marked contacts, a unique distance-four matching, unique full-core endpoints,
square-connected route families, and an exact deck-odd averaged chain. A separate symbolic audit
then agrees with all 252 twelve-point QTDS contacts for both polarities.

The evidence now supports a precise all-arity Catalan/discrete-Morse conjecture. It is not yet an
all-arity theorem.

## Frozen rule

Let \(n=2m\). Color the cyclic polygon alternately and call a diagonal physical when it joins
opposite colors. Give every physical diagonal the same transverse coorientation as in entry 24:

\[
\nu_+(a,b)=
\begin{cases}
1,&a\text{ even},\\
0,&a\text{ odd},
\end{cases}
\qquad
\nu_-=1-\nu_+.
\]

For a quadrangulation \(Q\), direct its dual tree toward the cooriented side of every physical
diagonal. If the directed tree has a unique sink quadrilateral \(R\), assign to \(Q\) the two
scalar diagonals of \(R\). Otherwise assign no contact slots.

No ten- or twelve-point clause is added. In particular, the number of dual-tree vertices changes,
but the rule does not.

## Ten-point coorientation audit

The decagon has fifteen physical diagonals and hence \(2^{15}\) possible local coorientations.
There are ten zero-core scalar triangulations, each with seven marked scalar diagonals. Their
source multiset therefore contains seventy occurrences.

Exact enumeration of all 32,768 coorientation patterns gives:

1. scalar marked-contact conservation selects exactly two patterns;
2. they are precisely \(\nu_+\) and \(\nu_-\);
3. either pattern has thirty-five unique-sink quadrangulations and hence seventy slots.

There is one important refinement of the eight-point uniqueness statement. The fifteen physical
decagon diagonals have two cyclic orbits: ten short diagonals and five diameters. Requiring
one-step rotation to reverse coorientation leaves an independent seed on each orbit and therefore
selects four patterns, not two. Intersecting this four-element set with scalar contact
conservation leaves exactly the alternating pair.

Thus cyclic deck covariance alone ceases to be sufficient at ten points. The scalar source
multiset is the condition correlating the independent chord-orbit polarities.

## Ten-point marked matching

For every zero-core triangulation \(T\), mark \(d\in T\), and scalar-derived target slot
\((Q,d)\), use the same marked flip distance as entry 24:

\[
\operatorname{dist}_d(T,Q)
=
\min_{\substack{T'\in\pi_{\rm core}^{-1}(Q)\\d\in T'}}
\operatorname{dist}_{K(\alpha_{10})}(T,T').
\]

For each of the twenty scalar diagonal labels, solve the finite assignment problem between source
and target occurrences. For each polarity the exact result is

\[
70\text{ sources}
\longleftrightarrow
70\text{ slots},
\]

with one and only one global minimizer. Every matched transfer has distance

\[
\boxed{3}.
\]

One-step rotation exchanges the two seventy-element matchings exactly.

## Independent ten-point QTDS verification

Only after the scalar matching is complete, expand all fifty-five ten-point QTDS diagrams in the
formal thirty-five-variable planar kinematic ring. Select their polynomial contact monomials.

For both polarities the recursion produces exactly seventy occurrences, each with coefficient
\(-1\). Diagram, marked diagonal, and coefficient agree occurrence by occurrence with the
scalar-derived matching:

\[
\boxed{
\operatorname{Contact}_{10}^{\epsilon}(Q,d)
=
\operatorname{SinkSlot}_{10}^{\epsilon}(Q,d).
}
\]

The comparison is non-circular. The scalar construction sees only alternating polygon geometry,
parity cores, and associahedral distance; the verification target is the independently expanded
quartic numerator recursion.

## Ten-point lift before core forgetting

Every one of the seventy matched targets has a unique closest full-core scalar refinement
containing its mark. The shortest paths to that endpoint occur with the following multiplicities,
for either polarity:

| number of shortest paths | marked occurrences |
|---:|---:|
| 1 | 10 |
| 3 | 40 |
| 6 | 20 |

The graph connecting two paths when they differ by one commuting-flip square has profiles

\[
(1,0)^{\times 10},
\qquad
(3,2)^{\times 40},
\qquad
(6,6)^{\times 20},
\]

where \((v,e)\) records route vertices and square-move edges. Every route graph is connected.

Let \(\operatorname{Geo}^{\epsilon}(T,d)\) be the complete shortest-path set to the unique marked
endpoint. Define

\[
\widehat\gamma_{T,d}^{\epsilon}
=
\frac{1}{|\operatorname{Geo}^{\epsilon}(T,d)|}
\sum_{\gamma\in\operatorname{Geo}^{\epsilon}(T,d)}\gamma
\]

and

\[
\widehat H_{{\rm ct},10}
=
\sum_{(T,d)}-X_d
\left(
\widehat\gamma^+_{T,d}
-
\widehat\gamma^-_{T,d}
\right).
\]

The exact audit verifies its endpoint boundary and deck parity:

\[
\partial\widehat H_{{\rm ct},10}=K_{10}^+-K_{10}^-,
\qquad
r\widehat H_{{\rm ct},10}=-\widehat H_{{\rm ct},10}.
\]

After cancellation, the marked edge coefficients have reduced denominators only \(1,3,6\).
Thus the eight-point half-sum was the first member of an all-geodesic averaging construction, not
an isolated square trick.

## Ten-point factorization naturality

Cut a unique-sink directed dual tree along any of its three physical edges. The edge orientation
distinguishes its source and target components. In every one of 105 directed cut incidences per
polarity:

1. the target component has the original global sink as its unique sink;
2. the source component has the cut-adjacent source cell as its unique sink;
3. the target component's scalar slots are exactly the uncut global slots.

This is the finite local form of cut naturality for the contact selector. It does not by itself
construct the filtered worldsheet residue map.

## Twelve-point scalar-only stress test

The Rust audit generates the dodecagon objects directly as bitsets and obtains

\[
16{,}796\text{ scalar triangulations},
\]

\[
28\text{ zero-core cells},
\qquad
252\text{ marked sources},
\]

\[
273\text{ quadrangulations},
\qquad
32\text{ scalar refinements per full core}.
\]

For either alternating polarity, 126 quadrangulations have a unique sink and supply exactly 252
slots. Their multiplicity agrees label by label with the scalar source multiset.

The physical dodecagon diagonals have two rotation orbits, of chord lengths three and five. All
four rotation-reversing orbit-polarity patterns are tested. Exactly the two globally opposite
alternating patterns conserve scalar contacts.

The thirty marked assignment problems have unique optima. All 252 transfers have distance

\[
\boxed{4},
\]

all have unique closest full-core refinements, and one-step rotation exchanges the two matchings.

This construction is scalar-only: no twelve-point QTDS contact support or numerator coefficient
is used to derive it. The next audit treats QTDS only as an independent verification target.

## Independent twelve-point QTDS verification

Expand all 273 QTDS diagrams in the formal 54-variable planar kinematic ring. For either
polarity, the polynomial sector contains exactly 252 marked contact occurrences. With the same
amplitude convention as the lower-point audits, every coefficient is (-1).

The complete occurrence table agrees with the scalar sink table:

\[
\boxed{
\operatorname{Contact}_{12}^{\epsilon}(Q,d)
=
\operatorname{SinkSlot}_{12}^{\epsilon}(Q,d).
}
\]

The aggregate label multiplicity also equals the marked zero-core scalar grade, whose 252 source
coefficients are independently all (-1). Thus both support and coefficient survive the
twelve-point falsification.

## Twelve-point route coherence

For either polarity, the shortest-path multiplicities and their square-move graphs are

| paths | square edges | occurrences |
|---:|---:|---:|
| 1 | 0 | 12 |
| 4 | 3 | 60 |
| 6 | 6 | 30 |
| 12 | 15 | 120 |
| 24 | 36 | 30 |

Every route graph is connected. Averaging every shortest route therefore gives a canonical
rational scalar chain without choosing a linear extension. Pairing the two polarities produces

\[
\widehat H_{{\rm ct},12}
=
\sum_{(T,d)}-X_d
\left(
\operatorname{AvgGeo}_4^+(T,d)
-
\operatorname{AvgGeo}_4^-(T,d)
\right).
\]

The compiled audit verifies

\[
\partial\widehat H_{{\rm ct},12}=K_{12}^+-K_{12}^-,
\qquad
r\widehat H_{{\rm ct},12}=-\widehat H_{{\rm ct},12}.
\]

Its nonzero marked edge coefficients have reduced denominators dividing twelve. The underlying
route averages were accumulated over path families of sizes dividing \(4!=24\); cancellation
removes denominator twenty-four from the final chain.

## Catalan law exposed by the audits

Write \(n=2m\). Through twelve points, the scalar counts obey

\[
|Z_{2m}|=2C_{m-2},
\]

where \(Z_{2m}\) is the zero-core triangulation set and \(C_k\) is the Catalan number. Hence the
number of marked sources is

\[
(2m-3)|Z_{2m}|
=
2(2m-3)C_{m-2}.
\]

The alternating directed-dual-tree rule gives

\[
|U_{2m}^{\epsilon}|
=
(2m-3)C_{m-2}
\]

unique-sink quadrangulations, each with two slots. A full quadrangulation core has

\[
2^{m-1}
\]

scalar triangulation refinements. The observed marked distance is

\[
m-2=\frac{n-4}{2}.
\]

The relevant finite data are:

| \(n\) | zero-core cells | marked sources | quadrangulations | unique sinks per polarity | marked distance |
|---:|---:|---:|---:|---:|---:|
| 6 | 2 | 6 | 3 | 3 | 1 |
| 8 | 4 | 20 | 12 | 10 | 2 |
| 10 | 10 | 70 | 55 | 35 | 3 |
| 12 | 28 | 252 | 273 | 126 | 4 |

These formulas suggest a direct bijection rather than a lucky sequence of assignment solutions.

## Candidate all-arity theorem

The finite evidence now motivates the following precise target.

> For every \(n=2m\geq6\) and either alternating polarity, marked zero-core scalar
> triangulations \((T,d)\) are canonically bijective with unique-sink quadrangulation slots
> \((Q,d)\). The bijection is the unique minimum of marked scalar flip distance, has distance
> \(m-2\), admits a unique closest full-core refinement, and its shortest routes form a connected
> square-move graph. The all-route average is a factorization-natural deck-odd contracting
> homotopy. Its target slots are the contact sector of the complete QTDS period.

The last sentence is verified independently through twelve points, not at all arity.

## Proof route now visible

The computational pattern suggests five concrete lemmas.

1. **Catalan source encoding.** Encode a zero-core triangulation as a sheet choice and a binary
   tree with \(m-2\) internal nodes, proving \(|Z_{2m}|=2C_{m-2}\).
2. **Rooted sink encoding.** Root a cooriented quadrangulation at its unique sink and mark one of
   the sink's two diagonals. Construct an explicit inverse to the marked zero-core encoding.
3. **Flip normal form.** Show that the inverse pair differs by exactly \(m-2\) physicalizing
   flips and that every other target assignment has larger total inversion number.
4. **Dependency poset.** Associate to each marked pair the partial order of legal physicalizing
   flips. Its linear extensions are precisely the shortest scalar paths. Adjacent swaps of
   incomparable flips give the observed square-move graph and prove its connectedness.
5. **QTDS induction.** Root the quartic tree at the sink and show recursively that the two sink
   diagonals are exactly the polynomial contacts selected by the alternating QTDS numerator.

Lemmas 1--4 would establish the scalar discrete-Morse transfer. Lemma 5 would promote the
twelve-point scalar prediction to an all-arity QTDS theorem.

## What is established

1. exhaustive ten-point uniqueness among all \(2^{15}\) local coorientations;
2. the unique seventy-element distance-three matching for both polarities;
3. coefficient-level agreement with all ten-point QTDS contacts;
4. unique marked scalar endpoints and square-connected geodesics at ten points;
5. an exact deck-odd ten-point scalar contact chain;
6. local directed-cut naturality at ten points;
7. the complete twelve-point scalar counts and rotation-orbit audit;
8. the unique 252-element distance-four matching for both polarities;
9. unique twelve-point endpoints and square-connected route families;
10. an exact deck-odd twelve-point scalar contact chain;
11. coefficient-level agreement with all twelve-point QTDS contacts.

## What remains open

1. an all-arity proof of the Catalan marked bijection;
2. uniqueness among all \(2^{24}\) twelve-point coorientations rather than among the four
   rotation-reversing orbit patterns;
3. identification of the route dependency poset in closed form;
4. extension from contact chains to the complete core-filtered transfer at arbitrary arity;
5. the filtered scalar-to-Pochhammer/Cousin chain map;
6. identification of the resulting worldsheet class with \((\operatorname{Pf}'A)^2\);
7. a proof that the square coherences are the combinatorial shadow of the Jordan identity.

## Reproducible audits

Ten points:

    python research/nima/check_ten_point_falsification.py

This standard-library script exhausts all 32,768 coorientations, solves both marked assignment
families, expands the symbolic QTDS recursion, constructs the averaged scalar chain, and checks
factorization restriction.

Twelve points on PowerShell:

    python research/nima/check_twelve_point_qtds.py
    rustc --edition=2021 -O research/nima/check_twelve_point_scalar.rs -o "$env:TEMP\marici-check-twelve.exe"
    & "$env:TEMP\marici-check-twelve.exe"

The Python audit independently expands every QTDS diagram and compares its contact table with the
scalar sink rule. The Rust audit generates all scalar cells, builds the flip graph, solves the
marked assignments by exact subset dynamic programming, enumerates every shortest path, verifies
square-move connectedness, and constructs the scaled exact deck-odd chain.

## Decision

Promote:

> Alternating scalar flip geometry carries a stable marked contact-transfer mechanism through
> twelve points and reproduces the independently expanded QTDS contact sector at both ten and
> twelve points.

The primary Nima frontier is now the all-arity Catalan/discrete-Morse theorem. In parallel, the
explicit eight-, ten-, and twelve-point scalar chains provide increasingly stringent source data
for the filtered worldsheet comparison.

Forward update: entry 26 proves the conjectured all-arity theorem by an explicit direct/inverse
Catalan map and a vertex-local QTDS cancellation argument. Entry 27 extends it from the contact
layer to every partial physical core. The remaining problem is global chain assembly across core
incidences, not construction of the coefficient transfer.
