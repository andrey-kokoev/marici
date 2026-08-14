# Resolved Overlap Ideals and Effective Belt Descent

## Record

Date: 2026-08-13

Status: exact eight-point polynomial support-hyper-Čech and carrier-kernel
theorem.  The four interval bridges isolated in entry 78 are canonical in
the support-selected algebraic carrier.  They are simultaneously the minimal
resolutions of the adjacent overlap ideals and the residual relation complex
of the actual polygon-to-belt map.  Entry 80 proves their universal formal
monodromy base change and shows that this does not by itself supply their
finite-\(\alpha'\) scalar-geometric realization, which remains conditional.
Entry 81 fixes their homological type: each bridge is the top determinant of
a rank-two endpoint Koszul complex, not a rank-one
\(\operatorname{Tor}_1\) excess class.
Entry 82 then applies the required operation order: this scalar descent is
formed first and the facewise PC functor is applied once to the actual
regional target.  The resulting target-first local loaded symbol is exact.

The result has two independent parts:

1. resolve the coefficient intersections selected by the physical support
   poset;
2. compute the complete kernel of the already established raw-weighted maps
   from the two pentagons and two squares to the regional belt.

They produce the same four interval complexes.  Thus the bridges are not
free cells added to repair a failed map.

## Epistemic-graph relation

Entry 78 was admitted to the Marīci epistemic graph as the conjecture that
the four overlap bridges are rank-one excess-intersection classes:

    ev-000000000017-5518d0c0-db1f-40be-9edb-59b546ad49ab

The present result partially resolves that node.  Rank one, the primitive
\((X_{11},-X_{10})\) weights, saturated cycle gluing, and occurrence in the
actual carrier kernel are now proved algebraically.  Scalar/Cousin provenance
at finite loading remains conjectural.  Here "rank one" means the unique
syzygy module.  Entry 81 proves that \(\operatorname{Tor}_1\) has rank two,
that the rank-one class is the degree-two determinant, and that the documented
scalar \(t\)-square has zero excess.  The graph should therefore retain the
original admission and its later falsifying successor rather than identify
the algebraic bridge with an excess line.  The original split was:

1. an evidence-backed algebraic theorem;
2. a narrowed geometric-provenance conjecture.

Admission of the original node certified graph validity, not truth; this
split preserves that distinction.

## The four facet ideals

Work over

\[
A=\mathbf Z[X_{00},X_{01},X_{10},X_{11},X_{20},X_{21}]
\]

and set

\[
\mathfrak p_r=(X_{r0},X_{r1}),
\qquad
I_Q=\mathfrak p_0\mathfrak p_1\mathfrak p_2.
\]

For \(Q=\{03,05\}\), the four physical support facets are

\[
P_+:x_2=1,
\qquad
P_-:x_0=1,
\qquad
S_+:x_2=0,
\qquad
S_-:x_0=0.
\]

Restricting the opposite labels of entry 77 gives the facet ideals

\[
\begin{aligned}
M_{P_+}&=X_{20}\mathfrak p_0\mathfrak p_1,\\
M_{P_-}&=X_{00}\mathfrak p_1\mathfrak p_2,\\
M_{S_+}&=X_{21}\mathfrak p_0\mathfrak p_1,\\
M_{S_-}&=X_{01}\mathfrak p_1\mathfrak p_2.
\end{aligned}
\]

Each is minimally resolved by its lcm-labelled square facet in
\(K_Q^{\rm w}\).

## Support-adjacent intersections

The nonempty intersections in the physical belt support poset are

\[
(P_+,P_-),
\qquad
(P_+,S_-),
\qquad
(P_-,S_+),
\qquad
(S_+,S_-).
\]

Their module intersections inside \(I_Q\) are

\[
\begin{aligned}
J_{P_+P_-}&=X_{20}X_{00}\mathfrak p_1,\\
J_{P_+S_-}&=X_{20}X_{01}\mathfrak p_1,\\
J_{P_-S_+}&=X_{00}X_{21}\mathfrak p_1,\\
J_{S_+S_-}&=X_{21}X_{01}\mathfrak p_1.
\end{aligned}
\]

Thus every adjacent overlap has the uniform form

\[
\boxed{
J_e=C_e(X_{10},X_{11}).
}
\]

It has two minimal generators.  If

\[
v^0=(v_0,0,v_2),
\qquad
v^1=(v_0,1,v_2),
\]

then

\[
m_{v^0}=C_eX_{11},
\qquad
m_{v^1}=C_eX_{10}.
\]

Since \(X_{10}\) and \(X_{11}\) are coprime, the first syzygy module is
generated primitively by

\[
\boxed{
X_{11}m_{v^1}-X_{10}m_{v^0}=0.
}
\]

The minimal free resolution is exactly the weighted middle interval

\[
K_e^{\rm w}
=
\left[
A h_e
\xrightarrow{\ d\ }
A e_{v^0}\oplus A e_{v^1}
\right],
\]

with

\[
d h_e
=
X_{11}e_{v^1}-X_{10}e_{v^0}.
\]

Both maps from \(K_e^{\rm w}\) into its two facet resolutions are literal
labelled-cell inclusions.  The bridge of entry 78 is therefore forced once
the adjacent coefficient overlap is resolved rather than truncated to its
two generators.

## Why the support poset cannot be forgotten

The two opposite facet pairs are disjoint as faces of the belt, but their
ideals also have nonzero algebraic intersections:

\[
M_{P_+}\cap M_{S_+}
=
X_{20}X_{21}\mathfrak p_0\mathfrak p_1,
\]

\[
M_{P_-}\cap M_{S_-}
=
X_{00}X_{01}\mathfrak p_1\mathfrak p_2.
\]

Each has four minimal generators.  Including them would create false
overlaps between disjoint facets.

Consequently

\[
\boxed{
\text{module intersection alone is not the physical Čech nerve.}
}
\]

The correct object is the monomial coefficient system on the scalar
face-support poset.  The poset first decides which intersections exist; the
module intersection then supplies the coefficient object and its derived
resolution.

This is the precise role of the filtration whose loss was diagnosed in entry
78.

## The resolved support hyper-Čech sequence

Let \(K_{F_i}^{\rm w}\) be the four weighted square-facet resolutions and
let \(K_e^{\rm w}\) be the four adjacent interval resolutions.  There are no
triple support intersections.  The augmented sequence

\[
\boxed{
0
\longrightarrow
\bigoplus_{e\in C_4}K_e^{\rm w}
\xrightarrow{\ \delta\ }
\bigoplus_{i=0}^{3}K_{F_i}^{\rm w}
\xrightarrow{\ q\ }
B_Q^{\rm w}
\longrightarrow0
}
\]

is a strict sequence of polynomial chain complexes.  Its degreewise ranks
are

\[
\begin{array}{c|ccc}
\text{cell degree}
&\bigoplus K_e^{\rm w}
&\bigoplus K_{F_i}^{\rm w}
&B_Q^{\rm w}\\ \hline
0&8&16&8\\
1&4&16&12\\
2&0&4&4.
\end{array}
\]

For each belt cell, either one chart contains it or two adjacent charts do.
The local augmented Čech sequence is correspondingly either

\[
0\to0\to A\xrightarrow{1}A\to0
\]

or

\[
0\to A
\xrightarrow{(1,-1)}
A^2
\xrightarrow{(1,1)}
A\to0.
\]

It is split exact cell by cell.  The monomial labels commute with these
incidences, so exactness holds over \(A\), not only after setting the
variables to one.

Equivalently, the mapping-cone totalization has free ranks

\[
(16,24,8)
\]

and its comparison with \(B_Q^{\rm w}\) is a strict polynomial
quasi-isomorphism.  At unit specialization both have

\[
(H_0,H_1,H_2)=(\mathbf Z,\mathbf Z,0)
\]

with only unit Smith factors.

Thus the support-filtered algebraic belt descent exists canonically.

## The actual polygon carrier has the same relation complex

Now use the actual route carriers, not copied target facets.  Form

\[
\mathcal R_Q
=
C_*(P_+)\oplus C_*(P_-)
\oplus C_*(S_+)\oplus C_*(S_-),
\]

where \(P_\pm\) are pentagons and \(S_\pm\) are squares, and let

\[
\Phi_Q^{\rm raw}:
\mathcal R_Q
\longrightarrow
B_Q^{\rm w}
\]

be the raw-weighted polynomial carrier map certified in entry 78.  Its source
cell ranks are

\[
(18,18,4),
\]

while the belt ranks are

\[
(8,12,4).
\]

The complete degreewise relation lattice

\[
\mathcal K_Q
=
\ker\Phi_Q^{\rm raw}
\]

has ranks

\[
\boxed{
(\operatorname{rank}K_0,
\operatorname{rank}K_1,
\operatorname{rank}K_2)
=(10,6,0).
}
\]

These are saturated integral kernels.  Appending one anchor for every
nonzero target fiber gives unimodular bases in degrees zero and one.

Restricting the polygon boundary to \(\mathcal K_Q\) separates two unit
interval summands.  They are exactly the collapsed scalar edges in the two
pentagons:

\[
H_{s,+}\oplus H_{s,-}.
\]

Quotienting them leaves the matrix

\[
d_{\rm rel}:\mathbf Z^4\longrightarrow\mathbf Z^8.
\]

Every column has two entries \(\pm1\), every row occurs in exactly one
column, and its Smith rank is four with all nonzero factors equal to one.
Hence

\[
\boxed{
\mathcal K_Q/
(H_{s,+}\oplus H_{s,-})
\cong
\bigoplus_{e\in C_4}
[\mathbf Z\to\mathbf Z^2],
}
\]

the direct sum of four primitive interval relation complexes.

After restoring the opposite-monomial decoration, these are precisely the
four \(K_e^{\rm w}\) above.  The bridges are therefore also the residual
kernel of the actual scalar route-chart map.

This provides a second construction independent of merely declaring the
target facet intersections.

## The two Čech layers are now separated exactly

The carrier kernel gives a canonical two-stage descent:

\[
\begin{array}{ccl}
\text{internal pentagon layer}
&:&H_{s,+}\oplus H_{s,-},\\
\text{inter-chart belt layer}
&:&\displaystyle\bigoplus_{e\in C_4}K_e^{\rm w}.
\end{array}
\]

The first removes the two collapsed scalar-edge redundancies.  The second
identifies the four pairs of route edges having the same physical middle-edge
image.  Conflating these layers was the source of the earlier rank-six and
missing-bridge puzzles.

The decomposition is intrinsic to the established polynomial chart map:
the relation lattice is its complete kernel, not a selected sublattice.

## No division by two or eight

Every kernel completion, overlap incidence, and four-cycle normalization is
unimodular.  Therefore the descended primitive class is obtained by integral
identification of occurrence representatives, not by averaging their sum.

At one regional interval the two endpoints represent the same primitive
class \(g_r\), whereas their polarization is \(2g_r\).  At eight points the
eight occurrence representatives descend to \(g_Q\), whereas the full
polarized sum is \(8g_Q\).  The resolved Čech quotient selects the common
class without dividing by \(8\).

This is the chain-level explanation of the index computed in entries 75 and
77.

## Relation-groupoid interpretation

The route pentagon and companion square remain disjoint scalar faces.  The
new theorem does not turn their ordinary intersection into an interval.
Instead it identifies the correct derived relation object of their common
image:

\[
\mathcal K_Q
\rightrightarrows
\mathcal R_Q
\longrightarrow
B_Q^{\rm w}.
\]

After the internal scalar-edge quotient, the four interval components of
\(\mathcal K_Q\) are the arrows of the effective support descent groupoid.
The belt is its polynomial homotopy colimit.

This is the precise local model for the emerging statement:

> The scalar half-object is assembled as a derived image with descent, not as
> an ordinary common-face subobject of the scalar associahedron.

The distinction matters.  The algebraic relation groupoid is canonical once
the chart map and support poset are given, but a scalar-geometric theorem must
still construct that chart map and its relation object before taking the
field-theory associated grade.

## Epistemic boundary

Established:

1. every support-adjacent facet-ideal intersection is
   \(C_e(X_{10},X_{11})\);
2. its unique primitive first syzygy is the middle weighted interval;
3. the support-selected hyper-Čech sequence is split exact over \(A\);
4. its cone is strictly polynomially quasi-isomorphic to the weighted belt;
5. the actual route-polygon carrier has saturated kernel ranks \((10,6,0)\);
6. two kernel intervals are exactly the two \(H_s\) cones;
7. quotienting them leaves exactly four primitive interval complexes;
8. every normalization is unimodular, with no division by \(2\) or \(8\);
9. the construction respects the outer-square deck action and the ordered
   normal Koszul sign.

Not established:

1. a physical finite-\(\alpha'\) loaded Pochhammer/Cousin relation groupoid
   whose associated grade is the certified polynomial kernel; entry 80 proves
   the formal \(X\mapsto q-1\) base change but also proves that it cannot be
   substituted for this geometric comparison without double loading;
2. a correctly typed endpoint-determinant kernel implementing the physical
   double-Gysin comparison; entry 81 falsifies the previously proposed
   rank-one excess-line typing;
3. the five-term loaded pentagon naturality identity;
4. assembly of all quadrangulation charts and computation of the residual
   octagon/Jordan holonomy;
5. the resulting global identification with \((\operatorname{Pf}'A)^2\).

Reject:

> The four bridges are independent filler data which can be normalized only
> after dividing by the number of occurrence representatives.

Also reject:

> The unrestricted nerve of the four facet ideals is the physical belt
> nerve.

Also reject:

> Polynomial effective descent by itself proves finite-\(\alpha'\) scalar
> Pochhammer/Cousin naturality.

## Next formula objective

Construct the loaded relation complex as a genuine homotopy fiber

\[
\boxed{
\mathcal K_Q^{\alpha'}
=
\operatorname{hofib}\!\left[
\bigoplus_{i=0}^{3}
\operatorname{PC}_{\alpha'}(\mathcal U_i;\mathcal L_i)
\longrightarrow
\operatorname{PC}_{\alpha'}(B_Q;I_Q)
\right].
}
\]

Prove that it carries a canonical filtration with

\[
\operatorname{gr}\mathcal K_Q^{\alpha'}
\simeq
(H_{s,+}\oplus H_{s,-})
\oplus
\bigoplus_{e\in C_4}K_e^{\rm w}.
\]

For one representative route pentagon, verify that the loaded boundary of
the relation object gives the five-term Cousin identity, then rotate through
the eight deck images.  Only after this finite-loading theorem should the
eight local kernels be assembled around the residual compatibility octagon
and compared with the Jordan defect.

## Reproducible certificate

Run:

    rustfmt --check research/nima/check_resolved_overlap_hypercech.rs
    rustc --edition=2021 -D warnings -O research/nima/check_resolved_overlap_hypercech.rs -o "$env:TEMP\\marici-resolved-overlap-hypercech.exe"
    & "$env:TEMP\\marici-resolved-overlap-hypercech.exe"

Certificate SHA-256:

    54294778b90b634c4bc542d93a1bc7273e52008a34da37ea06becd65ab554acf

## Decision

Promote:

> The four missing bridges are canonical in the polynomial support-selected
> scalar carrier.  They are the minimally resolved adjacent overlap ideals
> and, independently, the residual saturated kernel of the actual
> polygon-to-belt map after removing the two internal pentagon cones.

Retain as the immediate frontier:

> Realize this effective relation groupoid as a loaded finite-\(\alpha'\)
> scalar specialization and prove its pentagon naturality.  The subsequent
> global obstruction is the residual octagon/Jordan holonomy, not another
> local coefficient choice.

## Internal dependencies

- Entry 38: facewise Pochhammer/Cousin symbols and finite-loading gap.
- Entries 72--75: constructible charts, belt, and derived route carrier.
- Entry 76: actual regional cube, caps, and lcm resolution.
- Entry 77: primitive boundary half-line.
- Entry 78: unfiltered comparison and four-bridge support obstruction.
- Entries 80--81: formal monodromy base change, double-loading no-go, and
  exact replacement of rank-one excess by the rank-two Koszul determinant.
- research/nima/check_resolved_overlap_hypercech.rs.
