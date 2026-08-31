# Retaining the source coordinate closes the global rigged joint graph

## Declared source object

Let \(\mathcal E\) be the complete projective arithmetic source carrying the
prime-power grading, for example the declared exponential Köthe test space
with primitive, square, and connected rungs retained separately.

Let

\[
A:\mathcal E\to\mathcal Y_{\rm win}
\]

be the completed window/history realization in its typed rigged codomain, and
let

\[
C:\mathcal E\to\mathcal Y_{\rm cut}
\]

be the completed theta cut-atom realization.  The existing source packets
prove continuity grade by grade:

- primitive: continuous into its distributional/history rung;
- square: Hilbert--Schmidt on the Hilbert rung;
- connected tail: nuclear;
- all grades: prime/grade diagonal and cutoff-natural.

The source-authorized joint-graph order retains the faithful source coordinate
before all output codiagonals.

## Full graph embedding

Define

\[
\mathcal J:\mathcal E
\longrightarrow
\mathcal E\times\mathcal Y_{\rm win}\times\mathcal Y_{\rm cut},
\qquad
\mathcal Jx=(x,Ax,Cx).
\]

This map is continuous.  Its inverse on its range is the first-coordinate
projection

\[
\pi_0(x,y,z)=x,
\]

which is continuous.  Thus \(\mathcal J\) is a topological embedding.

## Closed range

Suppose a net

\[
(x_\alpha,Ax_\alpha,Cx_\alpha)
\]

converges in the product to \((x,y,z)\).  The first coordinate gives

\[
x_\alpha\to x
\quad\text{in }\mathcal E.
\]

Continuity of \(A\) and \(C\) then gives

\[
Ax_\alpha\to Ax,
\qquad
Cx_\alpha\to Cx.
\]

Uniqueness of limits in the Hausdorff codomains implies

\[
y=Ax,
\qquad
z=Cx.
\]

Hence

\[
\operatorname{ran}\mathcal J
=\{(x,Ax,Cx):x\in\mathcal E\}
\]

is closed.

No Hilbert lower bound and no uniform singular-value estimate are needed.  The
closed-range mechanism is retention of the source coordinate.

## Cutoff completion

Let \(P_X\) be the finite prime/grade cutoff.  Since all realization maps are
label diagonal,

\[
\mathcal JP_X
=(P_X\oplus P_X\oplus P_X)\mathcal J.
\]

Finite packets are dense in every declared source seminorm, so

\[
\mathcal JP_Xx\to\mathcal Jx
\]

in the product rigged topology.  Thus the algebraic local joint graphs complete
to the closed global graph above.

## Radical

The positive joint form contains the source coordinate norm or seminorm family
as a direct summand.  Therefore an element in its common radical must have

\[
x=0.
\]

Then \(Ax=Cx=0\) automatically.  Hence the retained joint graph has zero
radical before any quotient or codiagonal.

Bounded wall/Stokes and Wronskian linking forms vanish on this zero radical and
therefore descend trivially on the joint graph.

## Why compact incidence is not a contradiction

The theta sampling leg by itself can be compact with dense nonclosed range in
an unweighted Hilbert realization.  The full map

\[
x\mapsto(x,Cx)
\]

still has closed graph and closed range in \(\mathcal E\times\mathcal Y\)
because the source coordinate is retained.

Thus compactness obstructs inverse recovery after forgetting \(x\); it does
not obstruct the source-authorized saturated joint graph.

## Exact remaining distinction

This theorem closes global rigged closed range for the **retained graph**.  It
does not prove closed range after applying an output-only pushforward such as

\[
(x,Ax,Cx)\longmapsto Ax+TCx
\]

or after forgetting the source coordinate.  Such a codiagonal can recover the
compact/nonclosed-range obstruction.

Accordingly, the remaining global question is no longer closedness of the
saturated source graph.  It is whether G1.1 requires only that retained graph,
or requires a later analytic--arithmetic codiagonal/pushout with the source
coordinate removed.  If the latter, closed range must be proved separately in
the declared quotient topology.

No RH conclusion is authorized.
