# Complete Occurrence-Resolved Eight-Point PC Polarity Homotopy

## Record

Date: 2026-08-14

Status: exact formal PC/normal-cone theorem at generic nonresonant loading.  The exhaustive
eight-point polarity difference has a complete occurrence-resolved primitive

\[
\boxed{
H_8^{\rm PC}
=
\sum_{D\in\mathcal D_{\rm phys}}
\operatorname{Ins}^{\rm PC}_D(H_{6,D}^{\rm mark})
+H_{\rm ct}^{\rm PC}.
}
\]

Here \(G_Q\) is reserved for entry 23's double-pole full-core sector.
\(\operatorname{Ins}^{\rm PC}_D\) denotes the channel insertion.  The subscript on
\(H_{6,D}^{\rm mark}\) is essential: the six-point chamber, polarity, complementary
four-point factor, and side order are induced by the cut \(D\).

The exact certificate proves the full boundary, physical cut table, vanishing of all double
residues, forbidden-residue zero, marked-contact residue zero, and complete dihedral/deck
covariance.  No coefficient sector remains outside \(G/R/K\).

This is a theorem in entry 38's canonical facewise Pochhammer/Cousin normal-cone complex over
the characteristic-zero nonresonant coefficient field.  As in entry 38, a literal tubular
current is defined only up to filtered chain homotopy.

## Exhaustion by pole grade

For each polarity and every quadrangulation \(Q\), entry 23's diagram decomposes as

\[
q_Q^\epsilon
=G_Q+\sum_{D\in Q}R_{Q,D}^\epsilon+K_Q^\epsilon.
\]

The new Rust certificate independently reconstructs all twenty-variable QTDS numerators and all
132 scalar octagon triangulations.  It partitions every Laurent monomial by its exact negative
support.  For each polarity the diagramwise occurrence census is

\[
(G,R,K)=(96,96,20).
\]

The three sets are pairwise disjoint.  Every \(G_Q\) monomial has precisely the two denominators
of \(Q\), every \(R_{Q,D}\) monomial has precisely \(X_D^{-1}\), and every \(K_Q\) monomial is
regular.  The scalar-cell census is independently

\[
132=96\ (|\rho|=2)+32\ (|\rho|=1)+4\ (|\rho|=0).
\]

The certificate checks, separately for \(+\) and \(-\),

\[
\sum_{Q\ni D}R_{Q,D}^\epsilon=H_D,
\qquad
\sum_QK_Q^\epsilon=Z,
\qquad
\sum_Qq_Q^\epsilon=\sum_Ts_T.
\]

Consequently the polarity comparison contains exactly two nonzero parts:

1. the \(R\)-difference on the eight physical factorization triangles;
2. the \(K\)-difference in the marked contact sector.

The double-pole \(G_Q\) sector cancels pointwise.  There is no fourth unmarked remainder.

## The marked six-point insertion

Let \((x_0,\ldots,x_5)\) be the scalar short diagonals of the hexagon induced by \(D\), with
physical facets \((D_0,D_1,D_2)\).  The scalar-derived six-point primitive is not one unmarked
tripod with the summed coefficient vector.  It is the direct sum of the even- and odd-center
marked saturated tripods with separate vectors

\[
a^{\rm even}
=
(x_0-x_4,\ x_4-x_2,\ x_2-x_0),
\]

\[
a^{\rm odd}
=
(x_1-x_3,\ x_5-x_1,\ x_3-x_5).
\]

Both sum to zero.  Their sum is the complete lower polarity boundary

\[
q_{6,+}-q_{6,-}
=
(x_0+x_1-x_3-x_4,\
x_4+x_5-x_1-x_2,\
x_2+x_3-x_5-x_0).
\]

Occurrence-wise, for each of the three marks \(d\) at either center, let
\(\lambda_{\epsilon,d}\) be the saturated leg to the unique sink-compatible polarity facet.
Then

\[
H_6^{\rm mark}
=
\sum_{d\text{ at even center}}-X_d
(\lambda_{+,d}-\lambda_{-,d})
+
\sum_{d\text{ at odd center}}-X_d
(\lambda_{+,d}-\lambda_{-,d}).
\]

Every saturated tail is the forced half-sum of its two codimension-one flags.  One embedded
chain has six disjoint marked occurrences, three at each center, and 72 nonzero oriented edges.
The certificate checks its boundary first on the marked direct sum, then separately on the two
centers, and only then after augmentation.  Thus the proof never replaces the two vectors above
by one unmarked tripod.

## Normalization and channel insertion

Let \(c_4\) denote the positively normalized two-occurrence four-point cycle.  With the rooted
QTDS convention used in entries 23 and 86,

\[
q_4=-c_4.
\]

For the ordered normal line \([dX_D]\), put

\[
h_D=\frac{\ell_D}{q_D-1},
\qquad
\widehat h_D=2\pi i\alpha' h_D,
\qquad
\operatorname{gr}^{-1}_{V_D}\widehat h_D=\frac1{X_D},
\]

and define

\[
\boxed{
\operatorname{Ins}^{\rm PC}_D(c)
=
-\widehat h_D(c_4\boxtimes c)\otimes[dX_D]
=
\widehat h_D(q_4\boxtimes c)\otimes[dX_D].
}
\]

This convention exactly reproduces the independently calculated single-pole difference on
every one of the 24 triangle vertices:

\[
\boxed{
R^+_{Q,D}-R^-_{Q,D}
=
\frac{q_4\boxtimes(q^+_{6,Q/D}-q^-_{6,Q/D})}{X_D}.
}
\]

Equivalently, if \(c_4\) rather than rooted \(q_4\) is displayed, the coefficient is
\(-c_4/X_D\).  This accounts for the apparent sign ambiguity: it is a normalization change,
not a discrepancy in the insertion.

## Complete boundary

Entry 38's facewise map is a chain map on every saturated flag, while entry 83 supplies the
fixed-mark loaded contact primitive.  Hence

\[
d_{\rm PC}\operatorname{Ins}^{\rm PC}_D(H_{6,D}^{\rm mark})
=
\sum_{Q\ni D}(R^+_{Q,D}-R^-_{Q,D}),
\]

\[
d_{\rm PC}H_{\rm ct}^{\rm PC}=K^+-K^-.
\]

The checker compares the sum diagram by diagram, not only after total amplitude summation, and
obtains

\[
\boxed{
d_{\rm PC}H_8^{\rm PC}
=
\sum_Q(q_Q^+-q_Q^-).
}
\]

## Derived physical cut table

Orient each physical chord from its even endpoint to its odd endpoint.  Four cuts have side
order \((4,6)\), and four have side order \((6,4)\).  With that side order retained, the primary
residue is

\[
\boxed{
\operatorname{Res}^{\rm PC}_D H_8^{\rm PC}
=
q_4\boxtimes H_{6,D}^{\rm mark}.
}
\]

For a compatible second channel \(E\ne D\), the only possible contribution reduces to the
occurrence-decorated entry residue of \(H_{6,D}^{\rm mark}\).  Entry 86's counit is reconstructed
on both sheets.  In side-zero/side-one tensor order each sheet is the same four-occurrence
cycle

\[
c_L\boxtimes c_R=4g_L\boxtimes g_R.
\]

Thus its primitive-dual periods are \(4\) and \(4\), and

\[
\operatorname{Res}^{\rm PC}_E H_{6,D}^{\rm mark}
=0
\]

strictly on the occurrence vector.  In any filtered tubular realization this gives the specified
null-homotopy.  There are 24 ordered compatible pairs.

If \(E\) crosses \(D\), it is absent from the induced hexagon and the residue is zero.  There
are 32 such ordered pairs.  Entry 83's contact chain is regular and has zero residue in all eight
physical channels.  Consequently every ordered double physical residue of \(H_8^{\rm PC}\)
vanishes.  Reversing the ordered normal word changes the two-normal symbol by the ordinary
Koszul sign \(-1\).

## Marked contact term

The contact term is exactly entry 83's object

\[
H_{\rm ct}^{\rm PC}
=
\chi_{\alpha'}^{\rm mark}(\widehat H_{\rm ct}).
\]

The certificate derives both twenty-occurrence scalar matchings from the alternating directed
sink rule and the per-mark minimum-distance assignment.  Every selected length-two path retains
its mark at source, middle, and endpoint.  One- and two-route paths are averaged exactly; the
two-route coefficient is \(1/2\).  The common source endpoints cancel occurrence by occurrence,
and core forgetting gives precisely \(K^+-K^-\).  All coefficients are regular, so all physical
residues vanish before PC loading and hence after entry 38's monoidal facewise map.

## Deck and dihedral covariance

The checker acts on coefficients, faces, marked occurrences, saturated edges, contact paths,
and ordered channel labels by all 16 elements of \(D_8\).  The base reflection reverses the
rooted cyclic QTDS order, and an odd rotation reverses the alternating sheet.  Their combined
sheet character determines whether \(+\) and \(-\) are exchanged.

The complete \(H_6^{\rm mark}\) and \(H_{\rm ct}\) chains transform with that deck character,
not merely their endpoint sets.  Restriction to each cut gives the induced \(D_6\) covariance,
including the reflections which force the saturated \((1/2,1/2)\) weights.  The full boundary
transforms with the same character.

## Exact certificate

Run:

    rustfmt --check research/nima/check_eight_point_pc_homotopy.rs
    rustc --edition=2021 -D warnings -O research/nima/check_eight_point_pc_homotopy.rs -o "$env:TEMP\marici-eight-pc-homotopy.exe"
    & "$env:TEMP\marici-eight-pc-homotopy.exe"

The executable checks:

1. all 132 scalar octagon triangulations and all 12 quadrangulations;
2. independent exact QTDS numerators for both polarities;
3. pairwise-disjoint exhaustive \(G/R/K\) Laurent support and the \((96,96,20)\) census;
4. all eight factorization triangles and all 24 triangle vertices;
5. six separate marked occurrences and the \(3+3\) even/odd center split on every inserted
   hexagon;
6. all 576 nonzero saturated insertion edges and every \((1/2,1/2)\) tail;
7. the full diagramwise boundary equality;
8. eight primary side-ordered residues;
9. 24 compatible nested residue differences with periods \(4-4=0\);
10. 32 crossing/unsupported ordered residues and eight contact residues equal to zero;
11. all double residues equal to zero with the ordered-normal Koszul sign;
12. both twenty-occurrence entry-83 matchings and their complete fixed-mark chains;
13. all 16 \(D_8\) transforms of the Laurent sectors, marked saturated chains, and contact chain;
14. the rooted \(q_4\), insertion, scalar-source, entry-counit, endpoint-incidence, and normal
    orientation signs.

Certificate SHA-256:

    be5085dfdf73143972f3ffb23f50add3c80a59f23530164d776f349803cf222d

## Epistemic boundary

Established:

1. the complete occurrence-resolved eight-point PC polarity primitive in the generic
   nonresonant normal-cone/Cousin model;
2. exhaustive coefficient support with no omitted sector;
3. the exact full boundary and complete physical cut table;
4. vanishing of compatible nested, crossing, contact, and all double physical residues;
5. exact normalization, normal orientation, and deck/dihedral covariance.

Not established or claimed:

1. a privileged smooth twisted form or tubular-current representative;
2. extension through resonance after forgetting nearby-cycle filtration;
3. a canonical inverse global scalar intersection pairing;
4. the separate atlas problem of gluing local primitive half-lines by invertible transitions;
5. identification of a global Jordan higher-coherence cell.

The last two items remain distinct from the polarity comparison proved here.  Their possible
Möbius or Jordan obstruction is not an omitted amplitude sector.

## Decision

Promote:

> At generic nonresonant loading, the complete occurrence-resolved eight-point PC polarity
> difference is the boundary of the sum of eight side-ordered marked six-point insertions and
> the entry-83 fixed-mark contact primitive.  The \(G/R/K\) decomposition is exhaustive, every
> physical cut has the required lower-point tensor, all nested and forbidden residues vanish,
> all double residues vanish, and the construction is exactly deck/dihedrally covariant.
