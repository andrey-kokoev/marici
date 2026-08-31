# RH G1.3 reduces to the separate connected-tail return

## Question

Which part of typed coefficient polarization and endpoint loading remains open
after the source joint-graph and oriented-margin results?

## Primitive-square source typing

For each prime, retain

\[
E_{p,12}=\mathbb Ce_{p,1}\oplus\mathbb Ce_{p,2}
\]

with source orientation

\[
S_{12}=\operatorname{diag}(-1,+1).
\]

The window and cut-atom realizations

\[
A_{p,12}:E_{p,12}\to\mathcal H_{\rm win,wall},
\qquad
C_{p,12}:E_{p,12}\to\mathcal H_{\rm cut,Wr}
\]

retain both grade labels.  Their common source loading is

\[
2k(\log p)\frac1k p^{-k/2}
=2(\log p)p^{-k/2},
\qquad k=1,2.
\]

Normal evaluation on the cut leg gives

\[
\kappa_p^{(k)}
=2(\log p)p^{-k/2}\Phi'(k\log p).
\]

Thus coefficient loading is defined before either scalar trace and is not a
fitted Stokes/Wronskian ratio.

## Polarized carrier

The local mate is the source joint graph

\[
\Gamma_{p,12}
=\{(A_{p,12}x,C_{p,12}x):x\in E_{p,12}\}.
\]

Its direct-sum positive form has zero radical.  The resolved window
polarization, explicit wall coordinate, ordered Stokes linking form, cut-atom
Green form, and Wronskian trace are all continuous on their typed factors.
The global retained map

\[
x\longmapsto(x,Ax,Cx)
\]

is closed in the declared labelled rigged topology and commutes with finite
prime/grade cutoffs.

Therefore typed polarization and loading are closed on the strict
primitive-square cell.

## Uniform loading margin

The ordinary two-window determinant has a uniform lower bound exceeding
\(0.25\).  The Euler-theta incidence satisfies

\[
|\kappa_p|<0.142.
\]

Consequently the conservative oriented scalar margin obeys

\[
\Delta_p^{\rm res}-\frac{\kappa_p^2}{4}>0.244.
\]

This bound is stronger than needed for the truncated incidence
\(\kappa_p^{(\le2)}\), because

\[
0<-\kappa_p^{(\le2)}<-\kappa_p.
\]

Hence the strict primitive-square endpoint loading cannot exhaust the positive
window area.  Both saturated and codiagonal finite assemblies satisfy the same
conservative margin.

## Why the connected tail cannot be absorbed

The two-endpoint packet contains only \(L\) and \(2L\).  Its arithmetic
incidence is therefore

\[
\kappa_p^{(\le2)}
=\kappa_p^{(1)}+\kappa_p^{(2)}.
\]

The remainder

\[
\kappa_p^{(\ge3)}
=\sum_{k\ge3}\kappa_p^{(k)}
\]

has no source basis vector in \(E_{p,12}\).  Adding it to the local scalar
coefficient would erase the grade label and falsely represent a connected tail
as a strict primitive-square endpoint.

It must enter through a separate completed nuclear source summand
\(E_{p,\ge3}\) and its own return map before any allowed codiagonal.

## Disposition

G1.3 is closed on the strict primitive-square summand:

- coefficient types and grade orientation are fixed;
- positive and linking polarizations coexist on a common source graph;
- endpoint loading is source-derived;
- radical compatibility and cutoff naturality hold on the retained graph;
- the loading margin is uniformly positive.

The successor packet
`the-connected-prime-power-tail-has-a-separate-nuclear-wronskian-return.md`
constructs this missing summand. It defines

\[
R_{\ge3}e_{p,k}=\kappa_p^{(k)}j_p
\]

through continuous normal evaluation of the labelled cut atom, proves nuclear
completed synthesis and cutoff naturality, and attaches it as the closed
zero-radical retained graph \(\Gamma_{\ge3}\). The full typed carrier is
therefore

\[
\Gamma_{12}\oplus\Gamma_{\ge3}.
\]

Accordingly G1.3 is now a closure candidate on the retained saturated
architecture. It remains open only if the authoritative constructor requires
closed range after an output-only codiagonal that forgets source grades.

No ledger status is changed, and no RH conclusion is authorized.
