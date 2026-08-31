# The source-authorized joint graph selects the resolved saturated order

## Two different uses of “graph”

The remaining form-selection ambiguity was partly terminological.  The corpus
uses “graph form” for two distinct constructions:

1. the **history graph**
   \[
   f\longmapsto(f,H_\Phi f),
   \]
   whose Gram is \(I+H_\Phi^*H_\Phi\);
2. the **joint comparison graph**
   \[
   y\longmapsto(y,K_py),
   \]
   whose Gram is
   \[
   G_{\Gamma,p}=G_{\theta,p}+K_p^*G_{\mathrm{win},p}K_p.
   \]

The second is explicitly identified in the existing quadratic-functoriality
packet as the source-authorized completed quadratic object.  Its defining
feature is retention of both typed coordinates with the direct-sum metric; it
is not a codiagonalized scalar output.

## Application to wall and derivative tail

The resolved theta history has the typed factorization

\[
R f=(f,Bf,M_\Phi f),
\]

where the components are respectively the retained input wall, derivative
tail, and theta output wall.  Its direct-sum Gram is

\[
R^*R=(1+M_\Phi^2)I+B^*B.
\]

This has exactly the same categorical pattern as the authorized joint
comparison graph: retain the faithful coordinate and add the positive Gram of
each typed shadow.  Consequently the wall/tail restriction of the
source-authorized joint graph selects the resolved, Fourier-saturated order:
quadratic evaluation occurs before any output codiagonal.

By contrast, the history convolution

\[
H_\Phi f=M_\Phi f+Bf
\]

uses the codiagonal of the output-wall and tail coordinates.  Its graph Gram

\[
I+H_\Phi^*H_\Phi
=(1+M_\Phi^2)I+M_\Phi(B+B^*)+B^*B
\]

is the Gram of a downstream analytic synthesis map.  It is a valid graph norm
for causal history, but it is not the direct-sum joint comparison form merely
because both are called graph forms.

## Compatibility with existing source statements

This selection reconciles four earlier facts:

- the output wall is typed separately from the input wall and is connected by
  the arrow \(w\mapsto M_\Phi w\);
- the canonical tensor-unit counit is retained rather than rescaled;
- Fourier saturation makes wall and tail orthogonal in the boundary observer
  topology;
- quadratic functoriality is covariance of a joint graph, not isometric
  identification or scalar codiagonalization of its coordinates.

It also explains why the causal cross term is strictly negative without
contradiction: that term belongs to the downstream history synthesis Gram,
not to the resolved joint boundary Gram.

## What is and is not closed

At the formal finite-cutoff level, the form-selection question is now answered:

\[
G_{\mathrm{joint,res}}
=(1+M_\Phi^2)I+B^*B
\]

on the wall/tail sector, with zero wall–tail cross block.

The Adams-ray part of this completion statement is already available: the
source-weighted incidence commutes with finite cutoffs, has an exact
contractive cocycle, and lifts without loss to the Fourier-saturated pro-Gram.
The wall is transported separately by the split tensor-unit retract.  What is
not yet proved is stability of the remaining comparison cells—beginning with
seam transport composed with endpoint attachment—or closed range of the full
analytic–arithmetic source pushout in the global rigged topology.

Thus the resolved saturated Gram is source-selected not only at finite cutoff
but along the completed Adams grade ray.  Its orthogonality still may not be
transferred to an arbitrary unsaturated causal-history domain or to the full
nine-operation constructor without the remaining comparison-cell theorem.

## Updated earliest obstruction

The earliest unresolved implication is no longer “which form is intended?” or
“does the Adams ray preserve it?”  It is:

> Prove that seam transport composed with endpoint attachment preserves the
> resolved Fourier-saturated comparison graph, carries radicals into radicals,
> and gives a closed-range full source pushout in the declared global rigged
> topology.

After that, the target two-column Gram is

\[
G_{ij}
=(1+M_\Phi^2)\langle q_i,q_j\rangle
 +\langle Bq_i,Bq_j\rangle
 +G_{\mathrm{jump},ij}
 +G_{\mathrm{Wr},ij}
 +G_{\mathrm{window},ij},
\]

with no wall–tail cross term.  The remaining numerical/symbolic work is to
supply the jump, Wronskian, window, and fourth-grade entries on the same closed
domain.

## Status

The source ordering selects the resolved saturated branch, and the completed
Adams grade ray preserves it with cutoff-compatible contractive control.  G1.1
remains open at seam/endpoint comparison-cell stability, full-pushout closed
range, radical compatibility, and the remaining Green entries and uniform
bounds.  No RH conclusion is authorized.
