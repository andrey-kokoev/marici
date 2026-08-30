# 2830 — Equal-Rank Supports Have Inequivalent Soft-Axis Gysin Behavior

## Derived restriction model

Let

\[
Z=V(x,y)
\]

be the coordinate-soft \(z\)-axis. For a hypersurface \(D=V(L)\), its derived restriction to \(Z\) is represented by

\[
\mathcal O_D\otimes_R^{\mathbb L}\mathcal O_Z
\simeq
[\mathcal O_Z\xrightarrow{L|_Z}\mathcal O_Z].
\]

On the generic axis, localize at \(z\neq0\).

## Vertex relation

For

\[
L_V=x+y+3z,
\]

one has

\[
L_V|_Z=3z.
\]

This is a unit on \(\mathbb F[z,z^{-1}]\). Hence the generic derived restriction is acyclic:

\[
H^0=0,
\qquad
\operatorname{Tor}_1=0.
\]

At the origin it has an ordinary transverse intersection class but no excess Tor class.

## Complementary relation

For

\[
L_C=x+y,
\]

one has

\[
L_C|_Z=0.
\]

The derived differential vanishes. Therefore the generic soft axis carries

\[
H^0\simeq\mathcal O_Z,
\qquad
\operatorname{Tor}_1\simeq\mathcal O_Z.
\]

The second line is the excess intersection/Gysin direction produced by containment of the soft axis.

## Consequence

The two packets have identical abstract Koszul count, rank, nullity, and kernel coordinates, but their supported comparison objects are inequivalent:

\[
\text{vertex packet: generic soft restriction }0,
\]

\[
\text{complementary packet: ordinary line plus excess Gysin line}.
\]

Thus occurrence-labelled affine support predicts a derived-calculus consequence that bare Koszul rank cannot predict.

This remains an algebraic support theorem. It does not show that the excess line pairs nontrivially with the physical Bunch–Davies chain.

## Next falsifier

Transport the complementary excess line through the actual coefficient connection and test its physical-cycle incidence. If connection transport kills it or the source cycle misses \(Z\), the algebraic distinction is physically silent. No new Carrier stratum may be added to activate it.

## Durable artifacts

- `research/benincasa/check_equal_rank_soft_axis_derived_restriction.py`
- `research/benincasa/equal-rank-soft-axis-derived-restriction.json`
