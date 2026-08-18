---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 749 — The Bunch–Davies Tube Does Not Select a Weighted Exceptional Boundary

## Remaining datum after Entries 746--747

The only unresolved physical route to the supported principal cofiber is an
analytically continued chain boundary at

\[
Z_{23}:(u,y)=(0,0),
\]

resolved by the weighted chart

\[
u=r,\qquad y=r^2t.
\]

The primary Bunch--Davies prescription gives all energies a negative
imaginary part. The question is whether those inequalities determine the
exceptional coordinate \(t\), and hence a canonical boundary current.

## Two-parameter exact test

For any \(c>0\), take

\[
u=-i\varepsilon,\qquad
y=-ic\varepsilon^2,
\qquad 0<\varepsilon<1/c.
\]

In the normalized chart,

\[
X_3=u-y-1=-1-i\varepsilon+ic\varepsilon^2.
\]

Therefore

\[
\operatorname{Im}u=-\varepsilon<0,
\qquad
\operatorname{Im}y=-c\varepsilon^2<0,
\]

and

\[
\operatorname{Im}X_3=-\varepsilon+c\varepsilon^2<0.
\]

Every member of this family lies on the same prescribed side of the
Bunch--Davies tube. However,

\[
\boxed{t=\frac{y}{u^2}=ic.}
\]

Thus \(c=1\) and \(c=2\), for example, give two admissible paths landing
at distinct points \(t=i\) and \(t=2i\) of the weighted exceptional
divisor.

## Verdict

The common negative-imaginary prescription fixes a sector of approach but
not:

- an exceptional point or cycle;
- a boundary current on the weighted divisor;
- a \(\mu_2\)-equivariant lift and trace;
- an overlap homotopy;
- a map to the principal corner coefficient complex.

Hence

\[
\boxed{
\text{the weighted }Z_{23}\text{ component of }\Phi_{\rm phys}
\text{ is underdetermined by the frozen Bunch--Davies prescription}.
}
\]

This is stronger than absence from the source text: the published sign
conditions admit a continuous family of inequivalent weighted limits.
Selecting one by requiring it to hit Entry 740's line would be post hoc.

## Relation to \(\mathcal Q\)

Entry 744 proves \(\mathcal Q|_{Z_{23}}=0\). The present result shows that
this support coincidence does not produce a physical comparison map. No
quartic class follows until an independent source datum fixes the weighted
exceptional chain.

## Evidence

- the negative-imaginary prescription of arXiv:2305.19686;
- the positive Cayley--Menger twisted cycle of arXiv:2408.16386;
- Entries 180 and 744--747;
- machine-readable packet
  'research/benincasa/marici-gm/weighted-bd-path-nonuniqueness.packet';
- exact Rust certificate
  'research/benincasa/marici-gm/src/bin/weighted_bd_path_nonuniqueness.rs';
- allocator claim 'seqclaim-b0f3a4510df6b9c08823edd9'.
- epistemic event
  'ev-000000000363-1510669f-1d37-46a8-8949-bd7eff3111f5'.

## Next falsifier

Search only for an additional source-derived condition that fixes the
weighted ratio \(y/u^2\): for example a simultaneous regulator scaling,
Landau thimble, or canonical real-oriented blowup lift. If none is present,
close the principal Čech route as physically underdetermined rather than
assigning a fitted \(Z_{23}\) boundary.
