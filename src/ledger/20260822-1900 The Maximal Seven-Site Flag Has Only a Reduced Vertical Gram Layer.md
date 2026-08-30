# Entry 1900 — The Maximal Seven-Site Flag Has Only a Reduced Vertical Gram Layer

## Hard-to-vary claim

For the source-admitted maximal seven-site flag selected before inspecting its
coefficient geometry, the generic critical projection is empty after routing-
Gram saturation. Its two Gram-boundary components yield reduced lines of
Cartier length one: one is source-visible, while the other lies entirely in the
inherited all-soft locus. Hence this orbit carries neither a horizontal
physical divisor nor a vertical Cartier excess.

## Frozen source orbit

Entry 1898 selected the neutral representative

\[
G-e_{12}\mid g_{134567}\mid g_{14567}\mid g_{1567}\mid g_{167}\mid g_{17},
\]

from the 88 orbits tied at the predeclared maximal score \((6,5,0,7)\). It has
affine face rank seven, denominator rank fourteen, trivial stabilizer, and a
free labelled \(C_7\)-orbit. No discriminant information entered its selection.

## Generic cover and wall pullback

Use the \(C_7\)-invariant increment pairing with distance classes

\[
2,\qquad \frac32,\qquad \frac12,\qquad k.
\]

The routing Gram determinant is

\[
\det G_{\rm route}=-\frac14 k(6+7k).
\]

On the homogeneous site-energy slice \(X_i=t\), the six walls solve as

\[
(y_1,\ldots,y_6)=\frac t2(-7,-5,-3,-1,1,3),
\]

with \(y_7\) free. Set \(z=t^2\) and \(x=y_7^2\). The complete labelled
routing atlas contains seven charts and passes all 49 labelled squared-distance
pullback identities. Unrestricted normal Gram data remain explicit.

## Generic critical ideal

Let \(F,G,H\) be the pulled-back cover equations. Only \(H\) depends on the
free loop square \(x\), and

\[
\boxed{\partial_xH=4k(6+7k).}
\]

This is a unit away from the frozen routing-Gram divisor. Therefore

\[
(F,G,H,\partial_xH):\bigl(k(6+7k)\bigr)^\infty=(1).
\]

There is no generic critical locus and hence no horizontal Landau divisor,
real critical sheet, multiplier, or Bunch--Davies pinch to activate. Ordinary
solutions of \(F=G=H=0\) away from the Gram divisor are transverse in \(x\)
and are not critical support.

## Gram specializations

At \(k=0\), the critical equations reduce to

\[
F=-12(z-1)^2,\qquad G=6(z-1),\qquad H=12(z-1),\qquad \partial_xH=0.
\]

Thus the scheme-theoretic ideal is \(\boxed{(z-1)}\), with \(x\) free. The
simple factors in \(G\) and \(H\) kill the apparent square in \(F\), so the
vertical object is reduced and has Cartier length \(\boxed{1}\).

On the source slice \(t=1\), with signed free loop energy \(r=y_7\), the seven
singleton residue factors are

\[
r-\frac52,\ -5,\ -3,\ -1,\ 1,\ 3,\ r+\frac52.
\]

Their product is generically nonzero away from the inherited soft points
\(r=\pm5/2\). The vertical Gram line is source-visible, but it is not the
specialization of a generic vanishing cycle.

The second routing-Gram component is \(6+7k=0\). At \(k=-6/7\),

\[
F=-\frac{972}{49}z^2,
\qquad
G=-\frac{4482}{343}z,
\qquad
H=-\frac{29916}{343}z.
\]

Its critical scheme is therefore the reduced line \((z)\), again with \(x\)
free and Cartier length one. But \(z=t^2=0\) forces

\[
t=y_1=\cdots=y_6=0
\]

under the frozen wall solution. The universal and singleton source factors
vanish there. This entire second line is inherited all-soft support and is not
a new source-visible vertical sector.

## Classification

The selected highest-priority source orbit realizes

\[
\boxed{
\begin{gathered}
\text{one source-visible reduced vertical Gram line}\\
+\ \text{one inherited all-soft reduced line}.
\end{gathered}
}
\]

It has no horizontal physical support, vertical Cartier excess, new carrier
incidence, or Carrier failure. This refutes direct inheritance of the six-site
horizontal-physical-plus-vertical-Cartier architecture for this orbit while
supporting the narrower H2 architecture: the existing Carrier remains
sufficient and the survivor is coefficient data on an existing Gram boundary.

## Next falsifier

Select, from the same frozen inventory, a maximal orbit with a different
compatibility type and test whether more than one free loop square survives its
wall pullback. A horizontal divisor can occur only when the critical Jacobian
is not forced to be a routing-Gram unit as it is here.

## Durable verification

- `research/benincasa/marici-gm/src/bin/seven_site_full_source_inventory.rs`
- `research/benincasa/marici-gm/src/bin/seven_site_maximal_flag_cover.rs`
- `research/benincasa/marici-gm/src/bin/seven_site_maximal_flag_atlas.rs`
- `research/benincasa/marici-gm/src/bin/seven_site_maximal_flag_critical.rs`
- `research/benincasa/results/seven-site-full-source-inventory.json`
- `research/benincasa/results/seven-site-maximal-flag-cover.json`
- `research/benincasa/results/seven-site-maximal-flag-atlas.json`
- `research/benincasa/results/seven-site-maximal-flag-critical.json`
- allocator claim: `seqclaim-552be547b41d75c710116118`
- epistemic events:
  `ev-000000002267-834c1894-79cf-45fb-aa03-3ebefc5ea9ec`,
  `ev-000000002268-8e3b39d3-6fd8-4ac7-ab92-a7567c0a6d84`
