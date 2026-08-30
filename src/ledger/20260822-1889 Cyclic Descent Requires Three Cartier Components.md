# 1889 — Cyclic Descent Requires Three Cartier Components

## Question

Entry 1888 describes one routing-chart Cartier object with basis
\(\langle1,L\rangle\).  Determine its action under the \(C_3\) stabilizer of

\[
g_{12}\mid g_{34}\mid g_{56}.
\]

## Chart-orbit correction

Rotation by two sites cyclically permutes

\[
x=y_1^2,qquad v=y_3^2,qquad w=y_5^2.
\]

It does not preserve the single ideal \((L^2,M)\).  Instead it produces
three pairwise-disjoint Cartier components

\[
(L_i^2,M_i),qquad i=0,1,2.
\]

Exact affine-rank tests show that every pair of reduced lines is disjoint.
Thus a single routing-chart line has no intrinsic \(C_3\) character and must
not be treated as a descended object.

## Descended coefficient object

The stabilizer acts freely on the three components.  Since each has Cartier
length two, the occurrence-resolved exceptional object has total length six
and character

\[
\boxed{\chi=(6,0,0)}.
\]

Over \(\mathbb Q\),

\[
\mathcal E_{6,\mathrm{orb}}
\cong
2\bigl(\mathbb Q_{\mathrm{triv}}\oplus\mathbb Q(\zeta_3)\bigr)
\]

at the finite Cartier layer.  The nilpotent generators \(L_i\) are
transported with their components; none is selected as a global eigenline.

## Nine source maps

The nine source completions decompose into exactly three free \(C_3\) orbits
of size three.  Transporting labels, completion walls, and Cartier targets
together gives strict descent on the three-component object.

Therefore

\[
\boxed{
\text{cyclic descent holds occurrence-resolved, but fails for one chosen
routing-chart component.}
}
\]

This refines Entry 1888: its length-two object is one chartwise component,
not the complete descended coefficient object.

## Consequence

No new Carrier structure is required.  The Carrier already retains the
three labelled chart occurrences needed for descent.  Forgetting those labels
would manufacture a noncanonical character assignment.

## Next falsifier

Construct the generic full-rank six-site kinematic family in a labelled
routing atlas and require its cover and critical ideal to intertwine these
three chart transitions before elimination.

## Durable verification

- `research/benincasa/marici-gm/src/bin/six_site_disjoint_pair_triple_c3_descent.rs`
- `research/benincasa/results/six-site-disjoint-pair-triple-c3-descent.json`
- allocator claim: `seqclaim-bba5802cd99f5c8cda50c974`
- epistemic event: `ev-000000002251-803366c1-5e57-49c3-b75a-68b0e562c809`
