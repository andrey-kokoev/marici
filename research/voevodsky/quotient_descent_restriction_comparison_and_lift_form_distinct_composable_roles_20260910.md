# Quotient descent, restriction, comparison, and lift form distinct composable roles

## Question

How should symmetry operations be typed so that quotient descent, subgroup restriction, comparison, and presentation lift compose without the contradiction found in the Fourier/radial example?

## Claim boundary

The four roles have different domains in the category of group representations. Restriction and comparison compose canonically. Quotient descent composes along quotient homomorphisms. A presentation lift is extra extension data and need not exist or be unique. The Fourier/radial sewing square is restriction followed by comparison, not quotient descent.

## Problem

The equation

\[
C_uF^2=W_uC_u
\]

was informally described as descent from \(C_4\) to \(C_2\). But the quotient homomorphism

\[
q:C_4\to C_2
\]

sends the square of a generator to the identity. It cannot send \(F^2\) to the nontrivial radial involution \(W_u\).

## Bold conjecture

Restriction, quotient descent, and lifting are interchangeable presentations of the same symmetry transfer.

## Named rivals

1. Each operation has a different variance in the group variable.
2. Restriction plus comparison explains the radial square without quotienting.
3. A lift exists automatically once a subgroup comparison exists.
4. Projective or metaplectic data can replace an absent ordinary extension.

## Ambient category

For a group \(G\), let \(\operatorname{Rep}(G)\) denote a declared category of continuous unitary representations on the chosen Hilbert or rigged carriers. A homomorphism

\[
f:K\to G
\]

induces restriction

\[
f^*:\operatorname{Rep}(G)\to\operatorname{Rep}(K).
\]

This contravariance in the group is the first type constraint.

## Role 1: subgroup restriction

Given an inclusion

\[
i:K\hookrightarrow G
\]

and \((X,\rho)\in\operatorname{Rep}(G)\), restriction produces

\[
i^*X=(X,\rho\circ i)\in\operatorname{Rep}(K).
\]

No information is removed from the carrier. Only the family of symmetry operators being used is narrowed.

Restriction is canonical and composes:

\[
(j\circ i)^*=i^*j^*.
\]

## Role 2: comparison cell

For two \(K\)-representations \(X,Y\), a comparison is an intertwiner

\[
C:X\to Y,
\qquad
C\rho_X(k)=\rho_Y(k)C.
\]

If \(C\) is unitary, it is an equivalence in \(\operatorname{Rep}(K)\). Comparisons compose covariantly:

\[
C_2C_1:X\to Z.
\]

A comparison changes carriers but not the acting group.

## Role 3: quotient descent

Let

\[
q:G\twoheadrightarrow H,
\qquad
K=\ker q.
\]

An object \(X\in\operatorname{Rep}(G)\) descends to an \(H\)-representation on the same carrier exactly when \(K\) acts trivially:

\[
\rho_X(k)=I
\qquad(k\in K).
\]

Then there is a unique \(\bar\rho:H\to U(X)\) with

\[
\rho_X=\bar\rho\circ q.
\]

If \(K\) acts nontrivially, one may instead pass to invariants, coinvariants, or a quotient carrier, but each requires a separate constructor and may discard information.

Quotient descents compose only when their kernel-triviality conditions hold at each stage.

## Role 4: presentation lift

Given \(i:K\hookrightarrow G\) and a \(K\)-representation \(Y\), a presentation lift is a \(G\)-representation \(\widetilde Y\) together with a comparison

\[
i^*\widetilde Y\simeq Y.
\]

Existence is an extension problem. Uniqueness is an additional rigidity problem. A projective lift or representation of a central extension is not an ordinary lift in \(\operatorname{Rep}(G)\); its phase line and cocycle must remain explicit.

## Composition table

The admitted composites are:

1. restriction followed by restriction;
2. comparison followed by comparison within the same representation category;
3. restriction followed by comparison;
4. quotient descent followed by quotient descent when kernel conditions hold;
5. lift followed by restriction, producing the declared comparison back to the original subgroup action.

The following composites are undefined without extra data:

1. comparison across different acting groups without a specified homomorphism;
2. quotient descent when the kernel action is nontrivial;
3. promotion of a projective lift to an ordinary representation;
4. use of a lift as an observer capable of reconstructing carrier information;
5. treating subgroup restriction as carrier quotienting.

## Principal worked example

Let \(G=C_4=\langle F\mid F^4=I\rangle\) and

\[
K=\langle F^2\rangle\cong C_2.
\]

Restrict the whole-line presentation representation along

\[
i:K\hookrightarrow C_4.
\]

Let the radial reciprocal group be

\[
K_{\rm rad}=\langle W_u\mid W_u^2=I\rangle.
\]

The group isomorphism

\[
\alpha:K\to K_{\rm rad},
\qquad
\alpha(F^2)=W_u
\]

and canonical fold \(C_u\) give the comparison

\[
C_u\rho_X(F^2)=\rho_{\rm rad}(W_u)C_u.
\]

Thus the exact role chain is

\[
\operatorname{Rep}(C_4)
\xrightarrow{i^*}
\operatorname{Rep}(K)
\xrightarrow[\alpha]{C_u}
\operatorname{Rep}(K_{\rm rad}).
\]

No quotient of \(C_4\) is used.

## Metaplectic qualification

A metaplectic phase line may lift the quarter-turn presentation into a central extension. This records extension data above the restricted half-turn representation. It neither changes the established comparison \(C_u\) nor supplies a stable complementary observer. Its constructor role is `projective_presentation_lift`, not `quotient_descent` or `comparison_cell`.

## Real and Green enrichment

The representation categories in the worked example carry additional structure:

- Green form \(J_\partial\);
- Real conjugations \(J_V,J_H\);
- domain and wall relation \(\Lambda_u\);
- transpose and adjoint.

An enriched comparison must preserve or explicitly reverse each structure:

\[
W_u^*J_\partial W_u=-J_\partial,
\qquad
C_uF^2=W_uC_u,
\qquad
U^\top=J_VU^*J_H.
\]

Equivariance alone does not imply these cells.

## Strongest falsification attempt

The bold conjecture fails on the smallest cyclic example. For the quotient \(q:C_4\to C_2\),

\[
q(F^2)=q(F)^2=e.
\]

But radial sewing requires \(F^2\) to correspond to \(W_u\ne I\). Therefore no relabelling makes the radial square a quotient descent. Restriction plus comparison satisfies all group laws without alteration.

Rival 3 also fails in general: a \(K\)-representation need not extend to \(G\), and extensions may be inequivalent. Rival 4 survives only as explicitly projective data, not as an ordinary lift.

## Constructor-role signatures

The role signatures are:

- `subgroup_restriction`: contravariant group input, unchanged carrier;
- `comparison_cell`: same acting group, carrier morphism;
- `quotient_descent`: covariant factorization of an action, kernel-triviality obligation;
- `presentation_lift`: extension problem with existence and uniqueness residuals;
- `projective_presentation_lift`: central-extension action with explicit cocycle.

These signatures prevent the earlier terminology collapse.

## Disposition

The corrected symmetry spine is a calculus of restriction, genuine quotient descent, comparison, and lift—not an undifferentiated notion of descent. The radial Green/Real system realizes subgroup restriction plus enriched comparison. The next frontier is to combine this calculus with complementary-observer stability: determine which observer roles commute with restriction and which must retain extension data absent from the operational subgroup carrier.
