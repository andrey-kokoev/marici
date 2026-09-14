# The radial combined response specifies the conditional diagonal cancellation target

Date: 2026-09-08

## Source identity

For one diagonal theta-label shell, the radial graph provides the entire
sections `R,E,W` and

\[
zR-\rho(0)=E-\frac12W.
\]

Prior shell conventions fix

\[
I^{(0)}=-R,
\qquad
I^{({\rm end})}=-2E.
\]

The reciprocal-plus-linking response required by radial Stokes is not a fitted
value at Xi zeros.  It is the source section

\[
I^{({\rm resp})}
:=I^{({\rm recip})}+I^{({\rm link})}
=R+2E
=\frac{\rho(0)+E-\frac12W}{z}+2E,
\]

with the apparent singularity removable by the graph identity.

Consequently, **if** the conservative G4 constructor independently realizes this response,

\[
I^{(0)}+I^{({\rm end})}+I^{({\rm resp})}=0
\]

for every spectral parameter.  Differentiating gives zero for every parameter
jet.  Thus the diagonal shell family preserves every Xi-adic filtration level
without using Xi or restricting to its divisor.

## Why the enlarged radial port matters

The old five-port presentation demanded a source-authorized split of
`R+2E` between two scalar reciprocal and linking coordinates.  The radial
history graph canonically retains the combined function-valued response before
that split.  The arithmetic adjoint cancellation depends only on their
codiagonal sum, so no split is needed to prove the diagonal lower equation.

This does not authorize erasing the separate reciprocal/linking outputs in the
full polarized observer.  They can remain diagnostic boundary coordinates,
while the conservative lower equation receives the source-derived radial
combined-response codiagonal.

## Multiplicity consequence

For every shell and every `j>=0`,

\[
\partial_z^j
\left(I^{(0)}+I^{({\rm end})}+I^{({\rm resp})}\right)=0.
\]

Hence the diagonal contribution to the Evans residual is divisible by `tau`
trivially (indeed it is identically zero).  This is the kind of parameterwise
source cancellation required by the Mellin-to-Evans filtration gate.

## Remaining pair sector

The result is diagonal in the ordered theta-label pair.  Off-diagonal pairs
carry the separately constructed ratio/separation cocycle.  A complete
prime-shell theorem still must:

1. assemble diagonal and off-diagonal pair responses with their exact product
   and ratio labels;
2. prove the off-diagonal codiagonal cancels its ordinary and endpoint terms;
3. transport that pairwise identity through theta-label summation and the
   centered prime-shell adjoint;
4. retain the common mode and prime/grade cutoff naturality.

Thus the dominant diagonal response target is completely specified by the radial enlargement,
but its source-authorized placement in G4 and the full prime-shell residual family remain open.

## Evidence

- `research/nima/the-radial-stokes-identity-fixes-the-exact-combined-diagonal-reciprocal-linking-section.md`
- `research/nima/the-minimal-diagonal-response-is-a-first-order-radial-history-graph-with-wall-trace-and-wronskian-incidence.md`
- `research/voevodsky/radial_laplace_jet_probe_is_a_faithful_shell_natural_g4_enlargement_20260908.md`
