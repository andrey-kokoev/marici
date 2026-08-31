# The local primitive-square mate is the source joint graph, not a ratio map

## Common source packet

Fix a prime \(p\) and retain grades \(k=1,2\).  Let

\[
E_{p,12}=\mathbb C e_{p,1}\oplus\mathbb C e_{p,2}
\]

with the frozen orientation

\[
S_{12}=\operatorname{diag}(-1,+1).
\]

There are two source-derived analytic realizations of the same packet:

1. the window/front realization through the comoving kernel and ordered
   primitive;
2. the theta cut-atom realization through the tail--seam incidence and
   half-density/Wronskian trace.

Denote them

\[
A_{p,12}:E_{p,12}\to\mathcal H_{\rm win,wall},
\]

\[
C_{p,12}:E_{p,12}\to\mathcal H_{\rm cut,Wr}.
\]

Both preserve the two grade labels and apply \(S_{12}\) before any scalar
codiagonal.

## Source-authorized joint graph

The selected quadratic architecture is already the joint-graph construction:
retain both typed outputs before codiagonalization.  Therefore the local mate
object is

\[
\boxed{
\Gamma_{p,12}
=
\{(A_{p,12}x,C_{p,12}x):x\in E_{p,12}\}
\subset
\mathcal H_{\rm win,wall}\oplus\mathcal H_{\rm cut,Wr}.
}
\]

No map from one output line to the other has to be defined by dividing their
trace values.  The mate relation is equality of source provenance in the
fiber product.

Because \(E_{p,12}\) is finite dimensional and both realization maps are
linear, \(\Gamma_{p,12}\) is closed.

## Coefficients are realized before traces

The Euler logarithmic source coefficient is

\[
a_{p,k}=\frac1k p^{-k/2}.
\]

The odd boundary derivative contributes \(2kL\), so the common source loading
is

\[
2kL\,a_{p,k}=2Lp^{-k/2}.
\]

On the cut side, normal evaluation gives

\[
2Lp^{-k/2}\Phi'(kL)=\kappa_p^{(k)}.
\]

On the window side, the same source basis vector gives the oriented reciprocal
front and its ordered primitive.  Thus the arithmetic coefficient is realized
inside \(\Gamma_{p,12}\) before applying either the Stokes or Wronskian trace.

The diagonal ratio \(S_{12}D_{p,12}\) is merely the coordinate matrix obtained
if one chooses the two scalar trace frames afterward.  It is not the
constructor itself.

## Joint positive form

Equip the graph with the source-authorized direct-sum form

\[
\|(A_{p,12}x,C_{p,12}x)\|_\Gamma^2
=
\|A_{p,12}x\|_{\rm res,wall}^2
+
\|C_{p,12}x\|_{\rm cut,Wr}^2.
\]

The resolved GNS-plus-wall form is positive and nondegenerate on the window
image.  The cut-atom wall-extended form is positive and nondegenerate on the
cut image.  Therefore the graph form has zero radical.

The ordered linking polarization is bounded on the window wall graph, while
the Wronskian trace is bounded on the cut graph.  Their source coefficients
are the same coordinates of \(x\).  Hence both forms coexist continuously on
\(\Gamma_{p,12}\).

## Local status

For each prime, the following are now closed:

- common primitive/square source carrier;
- source-fixed grade orientation;
- both analytic realization maps;
- closed local joint graph;
- exact Euler sampling on the cut leg;
- resolved positive polarization on the window leg;
- continuous wall/Stokes and Wronskian traces;
- zero positive radical;
- the conditional scalar determinant margin.

Thus no additional local ratio-map existence theorem is required.

## Remaining completion theorem

The unresolved issue is global.  Let

\[
\Gamma_{12}^{\rm alg}
=
\bigoplus_p\Gamma_{p,12}.
\]

The primitive and square legs have different operator-ideal and summability
classes.  One must prove that the completion of this algebraic joint graph in
the already declared projective/rigged source topology is closed in the full
analytic direct sum and that prime cutoffs converge in every required rung.

This cannot be replaced by an unweighted Hilbert direct sum: primitive history
has the known \(\sum_p(\log p)/p\) divergence.  The connected \(k\ge3\) tail
must also be attached as its separate nuclear grade.

The earliest remaining G1.1 implication is therefore global rigged closed
range of the source joint graph, followed by compatibility of its completed
radical quotients.  No RH conclusion is authorized.
