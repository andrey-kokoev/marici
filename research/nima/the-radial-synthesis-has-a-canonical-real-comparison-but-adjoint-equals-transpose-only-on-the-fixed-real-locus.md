# The radial synthesis makes adjoint equal analytic transpose under the same Real-compatible metrics

## Question

Can the analytic-transpose radial return be compared with the Hermitian adjoint independently of G4's missing interface?

## Claim boundary

Yes on the source-derived radial synthesis. Its columns are real completed-theta graph sections, so coefficientwise conjugations define a canonical Real comparison and give the exact formula relating transpose and adjoint. When both pairings are induced from the same Real-compatible Hermitian metrics, the synthesis adjoint is Real and the two returns agree as complex-linear maps. This does not determine whether G4 uses those metrics or that reciprocal Real structure.

## Real source and target carriers

At finite cutoff let

\[
U_X^{\rm rad}:V_X^{\rm shell}\longrightarrow H_X^{\rm rad}
\]

be the labelled radial synthesis. Choose the retained real labelled basis on \(V_X^{\rm shell}\). The target columns consist of the real-valued sections

\[
\rho,
\qquad e,
\qquad w,
\qquad \rho(0),
\]

with the two oriented copies kept separate. Let \(J_V\) and \(J_H\) be coefficientwise complex conjugation on the complexifications of these real source objects. Then

\[
J_HU_X^{\rm rad}=U_X^{\rm rad}J_V.
\]

This is a source theorem: it uses the real completed-theta atoms and real shell endpoints, not a G4 convention.

## Bilinear and Hermitian pairings

Let the Hermitian pairings be \(\langle\cdot,\cdot\rangle_V\) and \(\langle\cdot,\cdot\rangle_H\). Their associated complex-bilinear forms are

\[
b_V(v_1,v_2)=\langle J_Vv_1,v_2\rangle_V,
\qquad
b_H(h_1,h_2)=\langle J_Hh_1,h_2\rangle_H.
\]

Define the analytic transpose by

\[
b_H(Uv,h)=b_V(v,U^\top h).
\]

A direct substitution into the adjoint identity gives

\[
U^\top=J_VU^*J_H.
\]

This relation holds without choosing coordinates beyond the declared Real structures.

## Equality under Real-compatible metrics

Because \(U\) intertwines the conjugations and the Hermitian metrics are Real-compatible, its adjoint also intertwines them:

\[
J_VU^*=U^*J_H.
\]

Consequently

\[
U^\top=U^*
\]

as complex-linear maps on the full complexifications. This equality is conditional on using the same Real-compatible source metrics to define both pairings. It cannot be transported to a different G4 metric, an independently normalized port frame, or a reciprocal exchange/sign structure without a comparison map.

## Oriented feature qualification

The source Real structure above is coefficientwise conjugation. Reciprocal exchange is a separate operation that swaps the two radial orientations and carries the derivative-level sign fixed by

\[
\mathcal R\widehat{\mathsf D}_+\mathcal R
=-\widehat{\mathsf D}_-.
\]

Thus a G4 Real coherencer may need the composite of conjugation, reciprocal exchange, and the odd-level sign. That composite cannot be inferred from the fact that the radial columns are real. Its metric square and compatibility with the six-coordinate feature form must be checked explicitly.

## Finite conformance test

Once G4 exposes a return \(N_X\), the exact alternatives are:

1. Hermitian lane:
   \[
   N_X=(U_X^{\rm rad})^*;
   \]
2. analytic lane:
   \[
   N_X=(U_X^{\rm rad})^\top
   =J_V(U_X^{\rm rad})^*J_H;
   \]
3. reciprocal-Real lane: the same formula with declared exchange/sign coherencers replacing coefficientwise \(J_V,J_H\).

A checker must compare the full matrices in the declared metrics. Agreement of scalar Schur values on real vectors does not distinguish these lanes.

## Direction rescore

- Radial source Real comparison: completed.
- Adjoint/transpose equality in the declared radial Real metrics: completed.
- Unqualified transport of that equality to G4: 0/10.
- G4 Real coherencer and metric comparison: 10/10, interface-blocked.
- Finite hostile distinguishing equal real scalar returns from unequal complex returns: 8/10 and executable without G4 as a generic instrument.

## Disposition

The radial side of the adjoint/transpose gate is closed: \(U^\top=J_VU^*J_H\), and Real compatibility reduces this to \(U^\top=U^*\) in the declared radial metrics. The remaining uncertainty belongs entirely to G4's undeclared metric and reciprocal Real coherencer. No RH conclusion is authorized.
