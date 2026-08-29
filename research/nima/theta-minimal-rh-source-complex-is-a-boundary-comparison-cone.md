# The minimal RH source complex is a boundary-comparison cone

## Type audit of existing components

The existing theta/Tate pieces do not all have the same categorical role.

The doubled tail operators are genuine two-term differentials:

\[
D_z^\pm:E_\pm^0\to E_\pm^1.
\]

The endpoint dilation module is another finite two-term complex:

\[
D_s^\partial:V_\partial^0\to V_\partial^1.
\]

The seam is an independent state component and boundary trace. It is not a bounded function of the tail and cannot be inserted as a derived tail coordinate.

The primitive and square currents are source incidence maps:

\[
I_1:A_{\mathrm{cyc}}^{(1)}\to Y_1,
\qquad
I_2:A_{\mathrm{cyc}}^{(2)}\to Y_2.
\]

They are determinant-chart coordinates at different cyclic arities. They are not new bulk differentials and must not be appended as independent positive ports.

The archimedean term appears both in the tail forcing and in the completed boundary current. Its two appearances require a declared comparison, not duplication.

## Why direct sum is wrong

A direct sum of the analytic and arithmetic complexes would have a determinant equal to the product of their determinants. It would not require their boundary values to agree.

Thus

\[
\mathcal C_{\mathrm{an}}\oplus\mathcal C_{\mathrm{arith}}
\]

preserves two valid presentations while adding no coherence between them. Equal scalar readouts after projection would still permit unrelated source states.

The desired object must impose a shared boundary relation before determinant formation.

## Boundary-comparison cone

Let

\[
B_{\mathrm{an}}:
E_{\mathrm{tail}}\oplus E_{\mathrm{seam}}\oplus V_\partial
\longrightarrow
\mathcal B
\]

be the complete analytic boundary trace, including the doubled endpoint flux and archimedean reservoir.

Let

\[
B_{\mathrm{arith}}:
\widehat{\operatorname{Cyc}}(A_+)
\oplus
\widehat{\operatorname{Cyc}}(A_-)
\longrightarrow
\mathcal B
\]

be the typed arithmetic incidence, including primitive, square, connected, and reciprocal orientations.

If both maps land in one source-authorized boundary carrier \(\mathcal B\), form the comparison differential

\[
\delta_s(x,a)
=
B_{\mathrm{an},s}(x)-B_{\mathrm{arith},s}(a).
\]

The minimal comparison complex is the homotopy fiber or mapping cone of this difference:

\[
\mathcal C_s
=
\operatorname{Cone}
\left(
B_{\mathrm{an},s}-B_{\mathrm{arith},s}
\right)[-1].
\]

Its degree-zero kernel consists of analytically and arithmetically coherent states. Its cokernel records boundary distinctions that neither presentation reconciles.

The bulk differentials \(D_z^\pm\) and \(D_s^\partial\) must be included in the analytic leg before the cone is taken. The cyclic arity tower and its atomic incidence must be included in the arithmetic leg before the cone is taken.

## Source support

The boundary carrier must retain typed support:

\[
\mathcal B
=
\mathcal B_{\mathrm{seam}}
\oplus
\mathcal B_{\mathrm{right}}
\oplus
\mathcal B_{\mathrm{left}}
\oplus
\mathcal B_{\mathrm{endpoint}},
\]

with the primitive exponential, square tempered/Hilbert, connected trace-class, and archimedean grades preserved inside the relevant supported pieces.

Only seam-supported classes may be quotiented by seam incidence. Reciprocal open-sector classes must remain distinct even when their integrated indices cancel.

## The actual missing map

The analytic boundary data currently live in tail–seam graph or direct-sum spaces. The arithmetic data live as atomic currents on logarithmic scale and as relative determinant coordinates.

No source-derived comparison currently identifies these as maps into one completed carrier. Therefore the first missing constructor is not another differential or another current. It is a typed comparison correspondence

\[
\kappa:
\mathcal B_{\mathrm{an}}
\rightharpoonup
\mathcal B_{\mathrm{arith}}
\]

or, equivalently, two incidence maps into a third carrier \(\mathcal B\).

It must preserve:

- scale labels;
- seam versus bulk support;
- cyclic arity;
- Fourier reversal;
- endpoint orientation;
- the different primitive and square topologies;
- cutoff transition coherence.

## Relation to the determinant section

Once the cone is a Fredholm family, its determinant line and canonical section are derived functorially. A zero then means cohomology of the comparison complex rather than a scalar cancellation between unrelated presentations.

This still does not prove RH. The required open-sector contraction must be constructed on the cone and shown to survive completion. But the contraction now has a correctly typed target.

## Finite hostile

Take two scalar source spaces with readouts \(T(a)=a\) and \(I(r)=r\).

Their direct sum map

\[
(a,r)\mapsto(a,r)
\]

has no coherent-state kernel. It treats the two observations independently.

The comparison map

\[
(a,r)\mapsto a-r
\]

has kernel \(\{(a,a)\}\), exactly the reconciled diagonal. Replacing it by \(a+r\), or comparing only after separate scalar determinants are formed, changes the coherence relation.

Thus the sign and common codomain of the cone are source data.

## DPC

A proposed source complex passes only if:

1. every component is assigned its actual degree and variance;
2. seam state is retained independently;
3. primitive and square incidences remain arity-typed;
4. analytic and arithmetic legs meet in a source-authorized common carrier;
5. their comparison is formed before scalar determinant projection;
6. support and topology survive the comparison;
7. the determinant section is derived from the resulting Fredholm cone;
8. open-sector contractions are constructed on the cone rather than on a manufactured scalar differential.

## Outcome

The existing pieces determine the architecture but not the completed complex. The RH source complex must be a boundary-comparison cone. Its first missing datum is the common boundary carrier and the comparison correspondence joining analytic tail–seam traces to cyclic arithmetic scale currents. That is the exact place where the two source presentations must genuinely interact.
