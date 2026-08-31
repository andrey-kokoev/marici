# G3 margins must be tested after the retained constructor, not trivialized by its source coordinate

## Question

Does retaining the source coordinate close the five uniform Green margins
automatically?

No.  The retained coordinate closes the constructor graph and protects radical
descent.  It must not be counted again as an output observer when testing G3.
Otherwise every margin would become positive by adjoining an identity summand,
independently of the analytic and arithmetic coupling that G3 is meant to test.

## Constructor norm versus observer norm

The selected G1/G2 carrier has graph norm

\[
\|x\|_\Gamma^2
=\|x\|_E^2+\|Ax\|^2+\|Cx\|^2.
\]

The first term makes

\[
x\mapsto(x,Ax,Cx)
\]

a closed embedding.  G3 instead concerns the reduced observer assembled from
\(A\), \(C\), seam differences, common-mode forms, and mixed couplings.  Its
lower bounds must be proved after declaring which source coordinate is gauge,
which is retained provenance, and which components are physically evaluated.

A bound obtained solely from \(\|x\|_E^2\) certifies constructor faithfulness,
not any of the five G3 margins.

## Updated margin status

### Arithmetic margin

The strict primitive-square Pauli observer satisfies

\[
2m_\nu^2I\le\mathcal O_p^*\mathcal O_p\le2I
\]

uniformly in \(p\), and G1.4 makes its completed sum prime diagonal. The
successor packet
`the-retained-pauli-pair-closes-the-arithmetic-margin-before-terminal-scalarization.md`
identifies the G3 arithmetic observer with this retained pair and therefore
closes

\[
\delta_P=2m_\nu^2
\]

in squared-norm normalization. The connected grades remain a separate nuclear
labelled return and cannot reduce the direct-sum low-grade margin. A later
scalar row does not inherit this bound.

### Analytic margin

The wall-jump endpoint frame has exact Gram

\[
\begin{pmatrix}1/2&0\\0&1/8\end{pmatrix},
\]

and each retained history sheet has lower bound \(1/8\). The successor packet
`the-doubled-quarter-turn-history-observer-closes-the-full-analytic-margin.md`
retains both sheets and proves the exact graph-norm identity

\[
\|Q_+x\|^2+\|Q_-x\|^2
=\|x\|^2+\|Hx\|^2.
\]

Thus the complete doubled history observer sees the zero-trace bulk as well as
the endpoint directions and has analytic margin one in the history graph norm.
The analytic margin remains conditional only for any additional analytic
summand not contained in this closed history graph.

### Glue margin

The corrected scalar codiagonal has dense nonclosed range and zero glue margin.
The successor packet
`the-full-labelled-front-cut-seam-repairs-the-zero-scalar-glue-margin.md`
retains the full differentiated-front and cut-atom vectors instead. Their
source comparison \(J\) is bi-bounded in the resolved and wall-extended Green
norms. For

\[
D(x,y)=Jx-y,
\]

one has \(DD^*=JJ^*+I\ge I\), hence

\[
\delta_{\rm glue}\ge1.
\]

This closes the boundary-incidence glue margin before scalar Wronskian
projection. An undifferentiated primitive-window seam would still require its
own polarized two-column comparison.

### Coherent diagonal margin

Primewise coherent endpoint forms are positive, and source idempotents make the
completed G1 block prime diagonal. The successor packet
`the-coherent-joint-graph-inherits-a-uniform-diagonal-margin-from-the-vector-seam.md`
uses the bi-bounded seam comparison and doubled analytic observer, not the
provenance identity. If \(m_J\) is the seam lower bound and \(c_A\) the analytic
squared-norm margin, then

\[
\delta_{\rm diag}^2
\ge c_A\frac{m_J^2}{1+m_J^2}>0.
\]

Thus the coherent common-mode margin is closed on the reduced full-vector
joint graph before scalar projection.

### Mixed margin

On the strict primitive-square block,

\[
\Delta_p^{\rm res}-\frac{\kappa_p^2}{4}>0.244.
\]

This prevents the local oriented loading from exhausting the window area. The
successor packet
`the-vector-seam-and-doubled-analytic-observer-force-a-global-mixed-margin.md`
uses the full vector seam to obtain direct assembled coercivity

\[
B\ge g_0I,
\qquad
g_0=
\left[
\max\left\{
\frac2{m_J^2},
\frac{1+2/m_J^2}{c_A}
\right\}
\right]^{-1}.
\]

If \(M_B\) bounds the coherent and disagreement diagonal blocks, congruence of
the normalized block gives

\[
\|B_{cc}^{-1/2}B_{cd}B_{dd}^{-1/2}\|
\le1-\frac{g_0}{M_B}<1.
\]

Thus \(\delta_{\rm mix}=g_0/M_B>0\) on the completed full-vector boundary
architecture, including the connected grades.

## Exact anti-shortcut

Let \(T:E\to Y\) be any compact output incidence with minimum modulus zero.
The augmented graph observer

\[
x\mapsto(x,Tx)
\]

has lower bound one, while \(T\) still has no positive lower bound.  Therefore
constructor closedness and output observability are logically independent.
This is precisely the distinction between G1/G2 and G3.

## Revised G3 frontier

All five margins are closure candidates on the declared full-vector boundary
architecture before terminal scalarization. Remaining scope checks are:

1. identify any analytic summand outside the doubled closed history/cut graph;
2. confirm that the authoritative seam is the differentiated boundary-front
   seam rather than an undifferentiated primitive-window seam;
3. preserve the full Pauli, reciprocal-history, and vector-seam outputs until
   the G3 Green form is completed.

If these constructor-scope checks pass, the five-margin theorem has uniform
positive constants. A scalar Wronskian or terminal arithmetic projection does
not inherit them. G4 and RH remain open regardless of G3 closure.
