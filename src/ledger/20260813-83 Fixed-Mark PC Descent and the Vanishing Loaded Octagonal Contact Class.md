# Fixed-Mark PC Descent and the Vanishing Loaded Octagonal Contact Class

## Record

Date: 2026-08-13

Status: exact eight-point theorem for the marked contact sector. The marked scalar transport of
entry 24 lies in a direct sum of fixed-mark associahedral face complexes. Entry 38's facewise
Pochhammer/Cousin chain map therefore acts on it without any dependent occurrence
specialization. Its ordinary and sign-twisted loaded octagonal contact classes vanish exactly.

This closes the marked-contact part of the eight-point worldsheet problem. It does **not** close
the unmarked coefficient summands of the full half-object.

Forward correction (entry 84): the final sentence above was too broad for the **polarity
comparison**. Entry 23's pole-grade decomposition is exhaustive: the double-pole sector is
polarity independent, the single-pole difference is entirely supported on the eight physical
factorization triangles, and the regular difference is exactly the marked contact sector closed
here. Hence there is no fourth unmarked coefficient remainder in
\(q^+-q^-\). The additive correspondence totalization below remains meaningful only as a
separately posed global atlas/gluing problem for the local primitive half-lines; it is not a
missing amplitude sector. Entry 84 also shows that lifting the triangle part to the PC complex
still requires one six-point occurrence/Gysin entry counit. Entry 85 reduces its invariant
obstruction to a single factorized residue scalar; strict chain-level zero is
representative-dependent.

It also corrects the final objective of entry 82. Consecutive regional cubes are related by
noninvertible residue/Gysin spans, not by canonical transition automorphisms. Thus

\[
T_7T_6\cdots T_0
\]

is not defined by the established data. The intrinsic global observable is an additive class in
the totalization of the horizontal correspondence diagram.

## The fixed-mark subcomplex

Let \(K_\alpha\) be the scalar associahedron and let

\[
K_\alpha^{(d)}
=
\{F\subset K_\alpha:d\text{ is present on every vertex of }F\}
\]

be the facet subcomplex carrying the scalar diagonal \(d\). Define

\[
C_*^{\rm mark}(K_\alpha)
=
\bigoplus_d X_d C_*^{\rm cell}(K_\alpha^{(d)}).
\]

The coefficient \(X_d\) is constant on its summand. It remains a scalar associated-grade
coefficient; it is not identified with the finite-loading factor \(q_d-1\).

Entry 38 gives an \(A\)-linear facewise chain map

\[
\mathbb P_{\alpha'}:
C_*^{\rm cell}(K_\alpha)
\longrightarrow
\operatorname{PC}_{\alpha'}(K_\alpha)
\]

at generic nonresonant \(\alpha'\). Restriction to each fixed-mark face therefore gives

\[
\boxed{
\chi_{\alpha'}^{\rm mark}
=
\bigoplus_d
X_d\,
\mathbb P_{\alpha'}\big|_{K_\alpha^{(d)}}.
}
\]

No route-chart coefficient pushforward occurs in this definition. The scalar grade is taken
first, the mark is retained, and the descended face is Pochhammer-loaded once.

## Fixed-mark path lemma

For every scalar-derived matching of entry 24, let

\[
T_0\longrightarrow T_1\longrightarrow T_2
\]

be one of its length-two geodesics, marked by \(d\). By construction,

\[
d\in T_0\cap T_2.
\]

Then

\[
\boxed{d\in T_1.}
\]

There is a structural proof. If the first flip removed \(d\), it would replace it by the unique
crossing diagonal \(e\). Since every other diagonal of \(T_0\) is compatible with \(d\), the only
second flip that can restore \(d\) removes \(e\); that is the inverse flip and returns to
\(T_0\). But the matched endpoint has rank-two physical core while the source has rank zero, so
the endpoint is not the source. Hence the first flip cannot remove \(d\).

Consequently every marked geodesic is a cellular path inside \(K_\alpha^{(d)}\), and the complete
entry-24 chain satisfies

\[
\boxed{
\widehat H_{\rm ct}
\in
C_1^{\rm mark}(K_\alpha).
}
\]

The exact census verifies this for both twenty-occurrence matchings and every one- or two-route
length-two path.

## Loaded contact primitive

Define

\[
\boxed{
H_{\rm ct}^{\rm PC}
=
\chi_{\alpha'}^{\rm mark}
(\widehat H_{\rm ct}).
}
\]

Since the facewise Pochhammer/Cousin map is a chain map,

\[
\boxed{
d_{\rm PC}H_{\rm ct}^{\rm PC}
=
\chi_{\alpha'}^{\rm mark}
(\partial\widehat H_{\rm ct}).
}
\]

This is precisely the marked-edge comparison requested in entry 24. All normal circles,
\((q_E-1)^{-1}\) contractions, orientation lines, and forced lower-face terms belong to
\(\mathbb P_{\alpha'}\). The \(-X_d\) contact weight stays outside that normal Koszul loading.

On a physical boundary, entry 38's strong monoidality gives

\[
\operatorname{Res}^{\rm PC}_D
H_{\rm ct}^{\rm PC}
=
\chi_{\alpha'_L}^{\rm mark}
\boxtimes
\chi_{\alpha'_R}^{\rm mark}
\left(
\operatorname{Res}^{\rm sc}_D
\widehat H_{\rm ct}
\right).
\]

The scalar contact residue is zero. Therefore

\[
\boxed{
\operatorname{Res}^{\rm PC}_D
H_{\rm ct}^{\rm PC}=0
\quad\text{for every physical }D.
}
\]

Thus the image lies in the residue-free marked contact subcomplex.

## Additive octagonal theorem

Let \(O\) be the residual eight-edge boundary of the quadrangulation compatibility complex. The
entry-24 transport has the stronger support property

\[
\operatorname{supp}H_{\rm ct}\cap\partial O=\varnothing.
\]

The facewise PC map is filtered by associahedral face support: a face tube contains that face and
the lower-face terms forced by its boundary, but it does not create a different horizontal
quadrangulation edge. Hence restriction to the octagonal edge grade commutes with
\(\chi_{\alpha'}^{\rm mark}\). It follows that

\[
\boxed{
\Theta_{O,\rm mark}^{\rm PC}
=
\left.H_{\rm ct}^{\rm PC}\right|_{\partial O}
=0.
}
\]

Because the restriction is already zero before parallel transport, this statement is independent
of the orientation voltage on the octagon. Both circulations vanish:

\[
\oint_{\partial O}H_{\rm ct}^{\rm PC}=0,
\qquad
\oint_{\partial O}^{\eta}H_{\rm ct}^{\rm PC}=0.
\]

Therefore the deck-odd contact class of entry 22 vanishes in the marked summand:

\[
\boxed{
\mathfrak o_{8,\rm mark}^{\rm PC}
=
[\Theta_{O,\rm mark}^{\rm PC}]
=0.
}
\]

One-step rotation exchanges the plus and minus marked matchings and rotates \(d\), while the
facewise PC map rotates the chamber and its normal orientation data. Hence

\[
r(H_{\rm ct}^{\rm PC})=-H_{\rm ct}^{\rm PC}.
\]

The cyclic equal-route chain uses \(1/2\) on the four ambiguous diameter squares. Integrally, the
intrinsic object belongs on the polarity/orientation double cover; over the characteristic-zero
nonresonant PC coefficient field, the descended cyclic chain is defined directly. This is the
expected sign-local-system structure, not torsion in the loaded contact class.

## Why multiplicative holonomy is mistyped

Write the residual octagon vertices as

\[
Q_i=\{d_i,d_{i+1}\}.
\]

Adjacent vertices share exactly one physical diagonal. Their two nonshared diagonals cross. Thus

\[
K_{Q_i}\cap K_{Q_{i+1}}=\varnothing
\]

as exact-core scalar faces. The established horizontal datum has the form of a correspondence

\[
\operatorname{PC}(K_{Q_i})
\xrightarrow{\operatorname{Res}_{d_{i+1}}}
\operatorname{PC}(K_{d_{i+1}})
\xleftarrow{\operatorname{Res}_{d_{i+1}}}
\operatorname{PC}(K_{Q_{i+1}}),
\]

with the appropriate Gysin degree shifts and normal orientation lines. Neither leg is generally
invertible. It does not canonically determine

\[
T_i:
\operatorname{PC}(K_{Q_i})
\longrightarrow
\operatorname{PC}(K_{Q_{i+1}}).
\]

Therefore the product proposed in entry 82,

\[
H_{\rm oct}^{\rm PC}=T_7\cdots T_0,
\]

is not a falsification test until additional equivalences are constructed. Assigning identities,
signs, or monodromy units to the \(T_i\) would add structure not supplied by scalar incidence or
PC monoidality.

This is the same lesson already visible in entry 69: the vertical full-core suspension and the
horizontal Möbius compatibility carrier are different axes.

## The surviving global problem

Forward retyping (entry 84): this section does not describe a surviving summand of the
eight-point polarity difference. Its object may still govern coherent gluing of regional
half-lines or a Jordan-valued atlas, but \(\Theta_{O,\rm full}^{\rm PC}\) cannot be inferred from
pole-grade exhaustion alone and is withdrawn as a polarity-descent obstruction.

The marked contact summand is now closed. The full half-symbol contains additional coefficient
summands not represented by \(\widehat H_{\rm ct}\). Their horizontal assembly should be defined
as a derived correspondence or constructible cosheaf on the Möbius carrier, not as a local
system of isomorphisms.

For the eight octagon vertices and their shared rank-one cuts, form the additive totalization

\[
\boxed{
\mathcal T_O^{\rm PC}
=
\operatorname{Tot}
\left[
\bigoplus_i\operatorname{PC}(K_{Q_i})
\xrightarrow{\delta_{\rm Res/Gys}}
\bigoplus_i\operatorname{PC}(K_{d_i})
\longrightarrow\cdots
\right].
}
\]

The next obstruction is an additive class

\[
\boxed{
[\Theta_{O,\rm full}^{\rm PC}]
\in
H^\bullet(\mathcal T_O^{\rm PC}),
}
\]

whose marked projection is now proved to vanish. The unmarked projection may:

1. vanish strictly;
2. be null-homotopic through a higher Jordan coherence cell;
3. survive on the rank-one Möbius \(H_1\) class.

This is the correctly typed global eight-point falsification target.

## Exact audit

Run:

    rustc --edition=2021 -D warnings -O research/nima/check_marked_octagon_pc_descent.rs

The Rust certificate verifies:

1. all \(132\) scalar triangulations and \(12\) quadrangulations;
2. the four zero-core sources and both twenty-occurrence marked matchings;
3. fixed-mark support at source, middle, and endpoint of every selected scalar path;
4. one-step deck exchange of the plus and minus matchings;
5. sixteen unique quotient geodesics and four two-route square ambiguities;
6. disjointness from all eight residual-octagon edges;
7. the \(12\)-vertex, \(24\)-edge, eight-triangle/four-square Möbius carrier;
8. integral boundary ranks \(\operatorname{rank}d_1=11\) and
   \(\operatorname{rank}d_2=12\), leaving \(H_1\cong\mathbb Z\);
9. empty exact-core intersection for every adjacent octagon pair.

Certificate SHA-256:

    cfac476a9a1ed17af92d9bb789b935feb4b57583d6975976904f731f068c0396

## Epistemic boundary

Established:

1. every marked scalar geodesic lies in a fixed-mark associahedral face;
2. entry 38's facewise PC map acts on the entire marked chain without dependent coefficient
   specialization;
3. the image is a chain primitive with the required boundary;
4. its physical residues vanish;
5. it is deck odd;
6. its ordinary and sign-twisted additive octagonal circulations vanish;
7. the corresponding marked loaded contact class is zero;
8. adjacent regional cubes supply noninvertible correspondences, not transition automorphisms.

Not established:

1. horizontal assembly of every unmarked/full-symbol coefficient summand;
2. vanishing of \([\Theta_{O,\rm full}^{\rm PC}]\);
3. a preferred tubular-current, collar, or smooth twisted-form representative;
4. an extension through resonance after forgetting the filtered nearby-cycle object;
5. identification of the remaining full-symbol coherence differential with the Jordan identity;
6. an all-arity theorem for the additive correspondence totalization.

Reject:

> The marked eight-point worldsheet obstruction remains open because the dependent pentagon
> coefficient comparison is missing.

Also reject:

> Local target-first symbols canonically determine invertible transitions around the residual
> octagon.

Epistemic-graph event:

    ev-000000000021-1f31ed08-0a10-4682-af36-64cd3e1b2100

## Decision

Promote:

> Descent before loading sends the intrinsic fixed-mark scalar transport to a residue-free,
> deck-odd PC chain whose loaded octagonal contact class vanishes exactly.

The primary frontier is now:

> build the additive residue/Gysin correspondence totalization for the full scalar half-symbol
> and compute its unmarked octagonal class.
