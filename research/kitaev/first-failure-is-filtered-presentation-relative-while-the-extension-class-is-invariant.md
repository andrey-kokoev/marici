# First failure is filtered-presentation-relative

Owner: \`marici.Kitaev\`

## Question

Which part of a failed constructor relation is structural, and which part
depends on the chosen generators and cost convention?

## Claim boundary

This is a finite algebraic result for a frozen constructor extension. It does
not derive physical constructors, laboratory costs, or completion stability.

## Structural invariant

Let

\[
1\longrightarrow K\longrightarrow E
\overset{q}{\longrightarrow}G\longrightarrow1
\]

be a constructor extension. For central \(K\), a section determines a cocycle
\(\kappa\), and changing the section changes it by a coboundary. Hence

\[
[\kappa]\in H^2(G,K)
\]

is independent of representative choices. The extension splits exactly when
this class vanishes. For noncentral \(K\), the corresponding structural object
is the equivalence class of the extension with its outer action.

## Filtered first failure

Fix a generating alphabet \(\Sigma\), chosen physical lifts, and positive
letter cost \(c\). Define

\[
d_{\Sigma,c}
=
\inf\{c(r):r=1\text{ in }G,\ \widetilde r\ne1\text{ in }E\}.
\]

This number depends on the alphabet, lift frame, and filtration.

If two presentations are related by an isomorphism preserving target
evaluation, physical lifts, source and target typing, and letter costs, then
their first-failure costs agree. This is filtered constructor invariance.

Arbitrary presentation equivalence is insufficient. A Tietze enlargement can
name a long failed relation by a new primitive letter and assign that letter
unit cost. The underlying extension is unchanged while the first-failure cost
shrinks.

## Pauli hostile witness

For \(G=C_2\times C_2\), lift commuting logical generators \(x,z\) by Pauli
operators \(X,Z\). The target relation

\[
xzx^{-1}z^{-1}=1
\]

has physical residual

\[
XZX^{-1}Z^{-1}=-I.
\]

With unit generator cost this is a four-letter witness. Exposing the same
kernel residual as a primitive port makes a one-letter witness without changing
the nonsplitting extension.

## Affine Clifford consequence

A Clifford change preserves first-failure cost only when it preserves the
authorized generator alphabet, chosen lifts, source and target sectors, and
support or cost filtration. Preserving Pauli commutation alone is insufficient.

Thus the valid statement is not unrestricted Clifford invariance. It is
invariance under source-authorized, lift-compatible, filtration-preserving
Clifford automorphisms.

## Deutschian explanation

The hard-to-vary explanation is the nonsplitting extension: closed target
relations can retain kernel content for every strict compiler attempt. The
shortest failed word is the cheapest experiment exposing that explanation
inside a frozen interface. It is diagnostic economy, not the structural law.

## Falsifiers

- First-failure cost changes under a verified filtered constructor isomorphism.
- A presentation change alters primitive ports or cost and is still called
  invariant.
- One failed section is treated as proof that the extension does not split.
- A Clifford relabeling preserves commutation but not locality or authorization.
- Finite failure is promoted to completion-stable detection without a uniform
  margin.

## Disposition

The extension class is presentation-invariant. First-failure cost is invariant
only under filtered constructor isomorphism. Arbitrary presentation changes can
alter the latter without changing the former.

No checker, build, or Git operation was run for this research-only packet.
