# Retaining the full radial state collapses the composite kernel to interval cycles

## Question

When does the exact kernel extension acquire no additional realized endpoint–Wronskian balance beyond interval cycles?

## Claim boundary

If the unlabelled full-feature synthesis retains the complete radial state and has the same kernel as that state coordinate, then its range intersects the internal balanced channel only at zero. The composite codiagonal kernel is then exactly the interval-cycle space. This criterion fails if only endpoint and transform readouts are retained without the radial state or a proved recovery map.

## State-retaining synthesis

Let

\[
U:C\longrightarrow X
\]

be a common unlabelled synthesis into the full radial graph. Let

\[
P_\rho:X\longrightarrow\mathcal R
\]

retain both complete oriented radial states \(\rho_\pm\). Assume

\[
\ker(P_\rho U)=\ker U=Z_1(G).
\]

The first equality says that every remaining endpoint and Wronskian feature is functorially determined on the common-history quotient: no source packet can have zero radial state but a nonzero hidden full feature.

## Balanced-range intersection

Take

\[
x=Uc
\in
\operatorname{ran}U\cap N_{\rm bal}.
\]

Every element of the minimal balanced channel satisfies

\[
P_\rho x=0.
\]

Therefore

\[
P_\rho Uc=0,
\]

so the kernel hypothesis gives

\[
c\in Z_1(G)=\ker U.
\]

Hence \(x=Uc=0\). Thus

\[
\operatorname{ran}U\cap N_{\rm bal}
=\{0\}.
\]

Substitution into the composite-kernel exact sequence yields

\[
\ker(DU)=Z_1(G).
\]

No additional endpoint–Wronskian null direction is realized after the interval-cycle quotient.

## Equivalent recovery criterion

The kernel equality follows if there is a continuous recovery map on the source-generated range,

\[
\mathcal Q:
P_\rho(\operatorname{ran}U)
\longrightarrow

\operatorname{ran}U,
\]

such that

\[
\mathcal QP_\rho x=x
\]

for every \(x\in\operatorname{ran}U\). Full radial-state recovery is enough; ambient recovery outside the source range is unnecessary.

## Why the six readouts alone do not suffice

The displayed packet

\[
(-\rho(0),E_+,W_+;+\rho(0),E_-,W_-)
\]

retains only the wall value and transform families unless its carrier also includes \(\rho_\pm\) or proves graph recovery from \(E_\pm,W_\pm\). On the rapid graph, complete transforms do recover the derivative sources and rapid boundary conditions recover \(\rho_\pm\), but G4 must expose that topology and recovery law.

A witness listing only endpoint and transform field names does not establish the kernel equality.

## Architecture split

Two common-history architectures now have different radicals.

### State-retaining common history

If \(P_\rho\) and range recovery are declared, then

\[
\ker(DU)=Z_1(G).
\]

The only source loss before a downstream Green metric is interval-cycle provenance.

### Readout-only common history

If the carrier keeps only scalarized or incomplete readouts, then

\[
\operatorname{ran}U\cap N_{\rm bal}
\]

remains open and the composite kernel may be larger.

## Source-ray consequence

The source-fixed completed-theta ray already misses \(Z_1(G)\). Under the state-retaining hypothesis it therefore survives the complete common-history codiagonal injectively. This is a source-recovery statement, not five-port cancellation, Xi-divisor cancellation, or Green-form nondegeneracy.

## G4 conformance requirement

To use the collapsed-kernel theorem, G4 must expose:

1. complete radial states \(\rho_\pm\), or a range recovery map from its retained features;
2. the rapid graph topology supporting transform injectivity and boundary recovery;
3. equality of the state-coordinate kernel with the interval-cycle space;
4. placement of any later Green metric.

The current SCC interface exposes none of these witnesses.

## Disposition

The remaining balanced-range ambiguity is eliminated for a state-retaining common-history architecture: the composite kernel is exactly the reciprocal-invariant interval-cycle space. For the current G4 witness, application is blocked by missing carrier and recovery data. No RH conclusion is authorized.
