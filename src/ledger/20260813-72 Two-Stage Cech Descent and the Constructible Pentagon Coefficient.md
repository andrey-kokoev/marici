# Two-Stage Čech Descent and the Constructible Pentagon Coefficient

## Record

Date: 2026-08-13

Status: exact eight-point combinatorial and occurrence-level theorem.  The
nontransverse route pentagons admit a canonical coefficient repair without an
endpoint transport:

\[
\boxed{
\text{common-label incidence span}
+
\text{two-stage Čech descent}.}
\]

Every scalar flip edge carries a rank-four common-label module mapping into
two rank-five endpoint modules.  The exchanged rank-one quotients are absent
from every supported double-Gysin source.  The resulting physical images do
not cover a full rank-eight quadrangulation fiber face by face, but the
pentagon and its companion square glue through two saturated integral Čech
sequences and recover all eight occurrence lines.

This proves the coefficient descent which a loaded Pochhammer/Cousin lift
must realize.  It does not yet construct tangential loading, scalar-facet
tubes, or the forced lower-face terms of that lift.

Entry 73 adds an essential geometric qualification.  These sequences recover
the complete rank-eight vertex module, but the four physical charts form only
the side belt of the fixed-core cube.  They omit two cap squares and the cube
3-cell.  The coefficient theorem here remains exact; it is not by itself a
geometric cover or a route-to-cube Gysin chain map.

## The wrong object and the right object

Entry 71 proves that no intrinsic edge isomorphism

\[
\tau_s:M_0\xrightarrow{\sim}M_1
\]

is selected by the existing scalar data.  The correct scalar-edge diagram is
instead a span

\[
\boxed{
M_0\xleftarrow{\ j_0\ }M_s
\xrightarrow{\ j_1\ }M_1,
}
\]

where

\[
\operatorname{rank}M_0
=
\operatorname{rank}M_1
=5,
\qquad
\operatorname{rank}M_s=4.
\]

For an oriented flip

\[
T=C\sqcup\{x\}
\longrightarrow
T'=C\sqcup\{y\},
\qquad |C|=4,
\]

the common module is

\[
M_s=\mathbf Z\langle C\rangle,
\]

and the endpoint quotients are

\[
M_0/M_s\cong\mathbf Z\langle x\rangle,
\qquad
M_1/M_s\cong\mathbf Z\langle y\rangle.
\]

Thus scalar specialization is constructible: its rank jumps at the two
vertices.  There is no reason for it to be a local system.

## The flip mapping cone and its augmentation

Give a zero-core triangulation its marked scalar weight

\[
w(T)=-\sum_{d\in T}X_d.
\]

Then the oriented flip satisfies

\[
w(T')-w(T)=X_x-X_y.
\]

Occurrence-theoretically, the exchanged endpoint quotients define a
mapping-cone generator \(h_s\).  After scalar-weight augmentation,

\[
\boxed{
d h_s=X_x-X_y.
}
\]

This equation must not be mistaken for a bare degree-one element of the
Laurent ring.  Before augmentation, the actual datum is the rank-four span
and its two rank-one quotient lines.  Only that occurrence-level object can
be composed with physical Gysin maps.

All eight flip differentials form one deck orbit and transport with positive
face-orientation sign.  Around each route pentagon the five formal edge
differences telescope:

\[
\sum_{i=0}^{4}
\bigl(w(T_{i+1})-w(T_i)\bigr)=0.
\]

This is an exact augmented relation, not yet the loaded five-tube Cousin
identity.

## Supported Gysin kills the exchanged quotients

For each route pentagon and each of the two regional polarities, the directed
dual-tree rule selects one scalar source mark.  The exact audit finds:

\[
16/16
\]

supported sources lie in the common-label module \(M_s\).  Neither exchanged
label \(x\) nor \(y\) is ever selected.

Consequently the supported double-Gysin operation factors through the common
span and annihilates the two endpoint quotient directions:

\[
G_{D,E}(M_0/M_s)=0,
\qquad
G_{D,E}(M_1/M_s)=0.
\]

On the supported common source, the two physical orders agree exactly at
occurrence level:

\[
G_EG_D=G_DG_E.
\]

Each source expands to four basis occurrences in the full rank-eight fiber.
The ordered normal lines then supply the already established Koszul sign for
the degree-one Gysin operations.

This explains the earlier \(\pm\operatorname{Id}\) ambiguity.  It arose only
after the noninvertible span was forced into an endomorphism of the complete
rank-eight fiber.  The supported physical functor never requires such an
endomorphism.

## First Čech layer: polarity descent within one face

Let

\[
L_{F,+},L_{F,-}\subset L_Q
\]

be the two polarity-supported occurrence images of a route face \(F\) with
full core \(Q\).  For every relevant pentagon and square,

\[
\operatorname{rank}L_{F,+}
=
\operatorname{rank}L_{F,-}
=4,
\]

\[
\operatorname{rank}(L_{F,+}\cap L_{F,-})=2,
\]

and

\[
\operatorname{rank}(L_{F,+}+L_{F,-})=6.
\]

Writing

\[
L_F=L_{F,+}+L_{F,-},
\]

one has the exact integral sequence

\[
\boxed{
0
\longrightarrow
\mathbf Z^2
\xrightarrow{\ (1,-1)\ }
\mathbf Z^4\oplus\mathbf Z^4
\xrightarrow{\ +\ }
\mathbf Z^6
\longrightarrow0.
}
\]

This holds on all sixteen route faces that have both polarity-supported
images: the eight pentagons and their eight companion squares.  The incidence
maps are saturated; every nonzero Smith invariant is one.

A single face therefore sees only six of the eight full-core basis lines.
That is not a defect.  It is the first Čech chart.

## Second Čech layer: pentagon--square assembly

Every pentagon \(P\) has, at the same full core \(Q\), an opposite-sheet
companion square \(S\).  Their face-support modules satisfy

\[
\operatorname{rank}L_P
=
\operatorname{rank}L_S
=6,
\]

\[
\operatorname{rank}(L_P\cap L_S)=4,
\]

and

\[
L_P+L_S=L_Q,
\qquad
\operatorname{rank}L_Q=8.
\]

Hence a second exact integral sequence reconstructs the complete
quadrangulation fiber:

\[
\boxed{
0
\longrightarrow
\mathbf Z^4
\xrightarrow{\ (1,-1)\ }
\mathbf Z^6\oplus\mathbf Z^6
\xrightarrow{\ +\ }
\mathbf Z^8
\longrightarrow0.
}
\]

Again all nonzero Smith factors equal one.  There is no hidden torsion in
this coefficient gluing.

More finely, if the polarity images are ordered \((+,-)\) on each face, the
pentagon--square intersection matrix is

\[
\begin{pmatrix}
0&2\\
2&0
\end{pmatrix}.
\]

Thus the companion square supplies exactly the two occurrence lines missing
from the pentagon chart, while the crossed polarity sectors provide the
rank-four overlap.  All eight pentagon cores pass this assembly:

\[
L_P+L_S=L_Q
\quad\text{on }8/8\text{ cores}.
\]

## The two geometric axes reappear in coefficients

Entry 69 separated the octagon geometry into

1. vertical polarity descent through full-core roads;
2. horizontal compatibility among quadrangulations.

The coefficient theorem reproduces the same separation:

\[
\begin{array}{c|c}
\text{vertical coefficient descent}
&
0\to\mathbf Z^2\to\mathbf Z^4\oplus\mathbf Z^4\to\mathbf Z^6\to0
\\
\text{horizontal face descent}
&
0\to\mathbf Z^4\to\mathbf Z^6\oplus\mathbf Z^6\to\mathbf Z^8\to0.
\end{array}
\]

The full coefficient fiber is therefore a colimit of supported charts, not a
constant fiber transported around the route graph.  The two-axis phenomenon
is present simultaneously in topology and coefficients.

At six points, polarity roads and full quadrangulations coincide, so these
two descent stages collapse into the single \(K_{2,3}\) suspension.  Eight
points is again the first arity that separates them.

## Categorical interpretation

The appropriate coefficient object is a constructible cosheaf on the
core-filtered associahedral carrier:

- same-core scalar edges carry incidence spans, not isomorphisms;
- vertex-only quotient lines behave as vanishing directions;
- supported physical Gysin is extension by zero on those quotients;
- full-core fibers are recovered by Čech colimits;
- normal orientation lines convert commuting occurrence maps into the
  Koszul-signed Cousin differential.

In this language, the desired pentagon theorem is a Beck--Chevalley statement
for a diagram of spans.  It is not a commutative square of invertible
parallel transports.

This is the first concrete reason to replace the provisional phrase
``operator algebra on amplitudes'' by

\[
\boxed{
\text{a bivariant, constructible, homotopy-coherent incidence calculus}.}
\]

The associahedral pentagon is the first coherence cell of that calculus.

## What remains for the half-object

The coefficient descent substantially narrows the gap reopened in entries
38--39.  It gives the exact occurrence diagram that a complete scalar-derived
Pochhammer chain must carry.  It does not yet tensor that diagram with the
finite-\(\alpha'\) normal-tube complex.

The remaining construction is now:

1. realize the rank-four scalar-edge span as a loaded scalar-facet term;
2. realize the exchanged quotient cone as the forced vertex/lower-face terms;
3. tensor the first Čech sequence with the pentagon face tube;
4. glue it to the companion-square tube through the second Čech sequence;
5. verify the two marked physical residues and their normal Koszul sign;
6. rotate the result through the single eight-pentagon deck orbit.

If this succeeds, the complete pre-pairing scalar chain claimed provisionally
in entry 39 is restored.  If it fails, the exact saturated occurrence diagram
locates the obstruction in loading or nearby-cycle specialization rather than
in scalar factorization.

## Relation to the Möbius index

Both Čech sequences are saturated over \(\mathbf Z\).  Therefore the
coefficient cover itself does not generate the horizontal index-two class of
the Möbius carrier.  That class must lie in the global attachment of
compatibility cells, in an orientation/loading comparison, or in a later
nearby-cycle quotient.

The value \(-2\operatorname{Id}\) produced by the artificial
\(-\operatorname{Id}\) endpoint transport is thus not the intrinsic source
of the Möbius index.  It is an artifact of replacing a saturated span by a
chosen automorphism.

## Reproducible certificate

Run:

```text
rustfmt --check research/nima/check_pentagon_incidence_span.rs
rustc --edition=2021 -D warnings -O research/nima/check_pentagon_incidence_span.rs -o "$env:TEMP\\marici-pentagon-incidence-span.exe"
& "$env:TEMP\\marici-pentagon-incidence-span.exe"
```

Certificate SHA-256:

```text
67aab3b63c1591a45d9bab006b7314323b3e2083d89313279e1eea70e3a29427
```

The executable enumerates the 132 octagon triangulations and all 300
two-faces, derives the twenty-four route faces, constructs every supported
occurrence image, verifies deck covariance and flip telescoping, checks that
the exchanged labels are absent from all sixteen double-Gysin sources, and
proves both Čech sequences by explicit saturated incidence matrices and unit
Smith minors.

## Decision

Reject:

> Nontransverse coefficient coherence requires choosing a scalar-edge
> automorphism.

Promote:

> The octagon coefficient fibers form a constructible two-stage Čech descent
> system.  Physical Gysin factors through common incidence spans and the
> pentagon--square pair reconstructs every rank-eight full-core fiber
> integrally.

## Internal dependencies

- Entries 24, 27, and 32: marked scalar weights, regional occurrence fibers,
  and strict physical coaction.
- Entries 37--39: transverse base change, the corrected Pochhammer lift, and
  the cohomological half-class.
- Entries 69--71: the two-axis carrier, coefficient square audit, and
  endpoint-transport no-go.
- `research/nima/check_pentagon_incidence_span.rs`: exact certificate.
