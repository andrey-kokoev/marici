# Green--Real boundary systems form a graded category of comparison cells

## Question

What categorical object simultaneously types closed differential domains, boundary Green forms, reciprocal reversal, and Real comparison?

## Claim boundary

A concrete category can be defined whose objects are Green--Real boundary systems and whose morphisms are unitary comparison cells graded by differential and Green orientation signs. Composition multiplies the signs and preserves all domains and Real structures. The radial phase gauges are degree \((+,+)\) equivalences; reciprocal swaps are degree \((-,-)\) automorphisms. This is a definition and verification for the declared operator class, not a universality theorem.

## Problem

Ordinary representation intertwiners do not record:

- the domain of an unbounded first-order operator;
- its boundary trace;
- the Green form;
- whether a map preserves or reverses differential and boundary orientation;
- the antiunitary Real structure.

These cells must compose coherently if constructor-role typing is to extend beyond bounded Hilbert observers.

## Bold conjecture

Ungraded unitary intertwiners suffice; differential reversal and Green anti-isometry can be treated as harmless signs outside the morphism type.

## Named rivals

1. The two signs are compositional degrees and must be retained.
2. Domain transport alone determines the boundary sign.
3. Real compatibility follows automatically from complex unitary equivalence.
4. The radial reciprocal swap supplies a nontrivial graded automorphism.

## Objects

A Green--Real boundary system is a tuple

\[
\mathfrak X
=(H,\mathcal E,D,B,\gamma,J_B,\Lambda,J_H),
\]

where:

- \(H\) is a complex Hilbert carrier;
- \(\mathcal E\subset H\) is a dense graph-norm domain;
- \(D:\mathcal E\to H\) is closed;
- \(B\) is a finite- or Hilbert-dimensional boundary carrier;
- \(\gamma:\mathcal E\to B\) is continuous in the graph norm;
- \(J_B=J_B^*\) defines the boundary Green form;
- \(\Lambda\subset B\) is a declared maximal-isotropic domain relation;
- \(J_H\) is an antiunitary involution preserving \(\mathcal E\), commuting with \(D\), and inducing a compatible boundary Real structure.

The Green identity is part of the object data:

\[
\langle Dx,y\rangle_H+
\langle x,Dy\rangle_H
=
\langle\gamma x,J_B\gamma y\rangle_B
\]

with the sign convention fixed by the object.

## Graded morphisms

A morphism

\[
(C,C_B;\sigma,\varepsilon):
\mathfrak X\to\mathfrak Y
\]

consists of unitary maps

\[
C:H_X\to H_Y,
\qquad
C_B:B_X\to B_Y,
\]

and signs

\[
(\sigma,\varepsilon)\in\{\pm1\}^2
\]

such that:

\[
C\mathcal E_X=\mathcal E_Y,
\]

\[
CD_X=\sigma D_YC,
\]

\[
C_B\gamma_X=\gamma_YC,
\]

\[
C_B\Lambda_X=\Lambda_Y,
\]

\[
C_B^*J_{B,Y}C_B=\varepsilon J_{B,X},
\]

and

\[
CJ_{H,X}=J_{H,Y}C.
\]

The sign \(\sigma\) records differential orientation; \(\varepsilon\) records Green orientation. Neither is suppressed.

## Compatibility constraint

If the same Green identity convention is used on source and target and the boundary trace square is ungraded, substituting the differential intertwining into the Green identities forces

\[
\sigma=\varepsilon.
\]

Indeed differential reversal changes the left side by \(\sigma\), while the boundary comparison changes the right side by \(\varepsilon\).

The larger \(\mathbb Z_2\times\mathbb Z_2\) grading remains useful when trace orientation, inward/outward normal conventions, or an additional boundary sign is separately included. For the present normalized radial category, admitted morphisms lie in the diagonal subgroup

\[
\{(+,+),(-,-)\}.
\]

This rejects rival 2 only in its overstrong form: the signs coincide after conventions are fixed, but both must be recorded to verify that fact.

## Composition theorem

Let

\[
(C_1,C_{B,1};\sigma_1,\varepsilon_1):
\mathfrak X\to\mathfrak Y
\]

and

\[
(C_2,C_{B,2};\sigma_2,\varepsilon_2):
\mathfrak Y\to\mathfrak Z.
\]

Then

\[
(C_2C_1,C_{B,2}C_{B,1};
\sigma_2\sigma_1,
\varepsilon_2\varepsilon_1)
\]

is a morphism \(\mathfrak X\to\mathfrak Z\).

### Verification

Domain and wall transport compose directly. For the differential,

\[
C_2C_1D_X
=
\sigma_1C_2D_YC_1
=
\sigma_1\sigma_2D_ZC_2C_1.
\]

For the Green matrix,

\[
(C_{B,2}C_{B,1})^*J_{B,Z}(C_{B,2}C_{B,1})
=
\varepsilon_2\varepsilon_1J_{B,X}.
\]

Real intertwiners compose. Therefore the morphism axioms are closed under composition.

Identity maps have degree \((+,+)\), and associativity is inherited from operator composition. Hence these objects and morphisms form a graded category.

## Inverses

Every morphism is unitary and has inverse

\[
(C^{-1},C_B^{-1};\sigma,\varepsilon).
\]

Thus the unitary comparison subcategory is a graded groupoid. Nonunitary bounded comparison maps may be added later, but their domain and Green pullback conditions require separate analysis.

## Radial phase-gauge morphisms

For the systems at phases \(u,v\),

\[
G_{v,u}=\operatorname{diag}(1,v/u)
\]

maps fold, domain, wall, reciprocal parity, Green form, and Real structure at \(u\) to those at \(v\). It commutes with the radial differential and preserves the Green form, so

\[
(G_{v,u},G_{v,u}|_B;+,+)
\]

is a degree-\((+,+)\) equivalence.

The groupoid law

\[
G_{w,v}G_{v,u}=G_{w,u}
\]

is exactly categorical composition.

## Reciprocal graded automorphism

For one phase \(u\), the reciprocal swap satisfies

\[
W_uD=-DW_u
\]

and

\[
W_u^*J_\partial W_u=-J_\partial.
\]

It preserves the twisted Real structure:

\[
W_uJ_u=J_uW_u.
\]

With the boundary swap induced by \(W_u\), it is a degree-\((-,-)\) automorphism of the underlying unrestricted boundary system. Its square has degree \((+,+)\):

\[
W_u^2=I.
\]

For a fixed maximal-isotropic wall \(\Lambda_u=X_+(u)|_B\), \(W_u\) preserves \(\Lambda_u\) pointwise. Thus it is also an automorphism of the wall-domain object.

This verifies rival 4.

## Fold comparison

The canonical fold

\[
C_u:L^2(\mathbb R)\to
L^2(\mathbb R_+)\oplus L^2(\mathbb R_+)
\]

is degree \((+,+)\) when the whole-line cut system is given the transported boundary orientation. It satisfies

\[
C_u\partial_t=DC_u,
\qquad
C_uK=J_uC_u.
\]

The Fourier half-turn/reflection is degree \((-,-)\), and the square

\[
C_uF^2=W_uC_u
\]

is equality of graded morphisms.

## Real independence

Rival 3 fails. If \(C\) is a complex unitary comparison, then

\[
J_{H,Y}'=CJ_{H,X}C^{-1}
\]

is one compatible target Real structure, but a pre-existing \(J_{H,Y}\) need not equal it. Real compatibility is an additional cell, as the phase-twisted construction demonstrates.

## Observer functor

A bounded observer \(A:H\to Y\) can be attached to an object. A degree-\((+,+)\) unitary comparison transports it by

\[
A\longmapsto VAC^{-1}
\]

for a target unitary \(V\). Its Gramian transforms by

\[
A^*A\longmapsto C A^*A C^{-1}.
\]

Therefore lower modulus, compactness, essential spectrum, and Calkin invertibility are invariant under enriched equivalence.

This is the first observer invariant functor from the comparison groupoid to positive-operator data.

## Constructor-role signatures

The new roles are:

- `green_real_boundary_object`;
- `orientation_preserving_comparison`, degree \((+,+)\);
- `orientation_reversing_comparison`, degree \((-,-)\);
- `boundary_domain_transport`;
- `real_intertwiner`;
- `observer_gramian_transport`.

A candidate comparison is admitted only if every domain, wall, Green, Real, and degree field is supplied. Hilbert unitarity alone is insufficient.

## Strongest falsification attempt

The two signs initially appear independent. The Green identity forces their equality under the normalized trace convention, reducing the realized grading from \(\mathbb Z_2\times\mathbb Z_2\) to its diagonal. This is not a defect in the category: it identifies the admissible subcategory for the chosen convention. Other trace-orientation conventions must expose the additional sign rather than silently violating the identity.

## Disposition

Green--Real boundary systems with unitary graded comparison cells form a well-defined groupoid. The principal radial fold, phase gauges, and reciprocal swap are explicit morphisms. Stable-observer data descend to unitary-equivalence invariants through Gramian conjugation. The next frontier is extension from bounded observers on \(H\) to boundary traces and closed operators on graph-norm domains.
