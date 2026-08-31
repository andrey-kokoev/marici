# Quadratic Stokes–Wronskian functoriality reduces to equality with the canonical pullback metric

## Question

Given the completed nuclear comparison \(T=\operatorname{diag}(\lambda_p)\),
what remains to prove for quadratic Green-form transport?

## Claim boundary

The target metric canonically determines a pullback metric under which \(T\) is
isometric onto its range. Therefore quadratic functoriality is not an unknown
operator construction; it is the equality of the independently declared source
metric with this pullback metric. That equality is not currently proved.

## Target metric and pullback

Let \(G_W\) be the frozen positive Wronskian/wall metric on the target labelled
port. Define on the algebraic Stokes source

\[
 G_{\rm pb}=T^*G_WT.
\]

Then, by construction,

\[
 G_{\rm pb}(x,y)=G_W(Tx,Ty).
\]

Thus \(T\) is an isometry from the completion of the algebraic source in
\(G_{\rm pb}\) onto the closure of its target range.

If the target fibers are normalized to unit metric and
\(Te_p=\lambda_pe_p\), then

\[
 G_{\rm pb}(e_p,e_q)=\delta_{pq}|\lambda_p|^2.
\]

No free scalar remains.

## Retained graph

The saturated graph map

\[
 x\longmapsto(x,Tx)
\]

has the positive form

\[
 G_{\rm graph}(x,y)=G_E(x,y)+G_W(Tx,Ty),
\]

where \(G_E\) is the intrinsic Euler/Stokes source metric. Retention of the
first coordinate makes this graph closed even though \(T\) is compact and its
output-only range is nonclosed in the unweighted Hilbert target.

The graph form has zero radical whenever \(G_E\) does. Hence no inverse of
\(T\) is needed for retained-source radical descent.

## Exact source comparison gate

Let \(G_S\) denote the Stokes metric independently selected by the source
history construction. Quadratic functoriality of the Stokes--Wronskian edge is
exactly

\[
 G_S=T^*G_WT
\]

on the common labelled rapid core, including mixed primitive/square pairings
and the ordered orientation.

Primewise scalar agreement checks only

\[
 G_S(e_p,e_p)=|\lambda_p|^2G_W(e_p,e_p).
\]

A two-column cell additionally requires all polarized entries

\[
 G_S(e_{p,\alpha},e_{p,\beta})
 =G_W(Te_{p,\alpha},Te_{p,\beta})
\]

for the retained endpoint/output labels \(\alpha,\beta\). Diagonal energies do
not determine the reciprocal-odd mixed entry.

## Topology mismatch

Because \(\lambda_p\to0\), \(G_{\rm pb}\) is not uniformly equivalent to the
intrinsic Euler half-density metric. Therefore the identity

\[
 (E,G_E)\longrightarrow(E,G_{\rm pb})
\]

has no bounded inverse in general. The following statements must remain
distinct:

1. \(T\) is isometric from its pullback completion;
2. the retained graph \((x,Tx)\) is closed;
3. \(G_S\) equals the pullback metric on the source core;
4. \(G_E\) is equivalent to the pullback metric.

Statements 1 and 2 hold. Statement 3 is the source quadratic comparison.
Statement 4 is false for the unweighted/intrinsic completion unless the source
object is explicitly changed.

## Cutoff completion

Since \(T\) and the source metrics retain prime labels,

\[
 TP_X=P_XT.
\]

If the polarized identity \(G_S=T^*G_WT\) is proved on every finite labelled
packet, continuity extends it to the pullback completion. This extension does
not yield an output-only lower bound in \(G_E\).

## G4 implication

For the ordered linking port, the completed forward map and its canonical
pullback metric are now explicit. The remaining source theorem is finite and
polarized:

- identify the G4 Stokes source form \(G_S\);
- compare every retained two-output block with \(T^*G_WT\);
- preserve reciprocal sign and grade separation;
- retain the source coordinate during completion.

Once this equality is established, the linking contribution to the joint
adjoint is frozen. Until then, using the pullback metric merely because it makes
\(T\) isometric would be circular.

## Disposition

Quadratic Stokes--Wronskian functoriality has been reduced to one exact metric
identity, not an existence problem. The canonical pullback is constructed; its
identification with the independently sourced G4 Stokes metric remains open.
No RH conclusion is authorized.
