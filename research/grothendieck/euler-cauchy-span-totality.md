# Pick positivity makes the Euler Cauchy span automatically total

Epistemic-graph event: 1441.

## Conditional analytic Hilbert space

Assume the equivalent positivity conditions of Ledgers 1382--1385. Then
\`K_Xi\` is a positive analytic kernel on the upper half-plane and defines a
reproducing-kernel Hilbert space \`H_Xi\`. Its kernel vectors satisfy

\`<f,k_z>=f(z)\`.

Ledger 1396 constructs source Mellin modes mapping to \`k_z\` for every
\`z\` in the open Euler domain

\`Omega_E={z:Im(z)>1/2}\`.

## Totality theorem

Let \`f in H_Xi\` be orthogonal to every \`k_z\` with \`z in Omega_E\`.
Then

\`f(z)=0\` for all \`z in Omega_E\`.

Functions in \`H_Xi\` are analytic on the upper half-plane. Since
\`Omega_E\` is nonempty and open, the identity theorem gives \`f=0\`
everywhere. Therefore

\`closure span{k_z:z in Omega_E}=H_Xi\`.

Thus the one-sided Mellin modes in the honest Euler half-plane are already a
total source family after positivity.

## Consequences

No separate choice of analytic continuation on boundary vectors remains:

- the Euler-domain Weil-to-Pick isometry has at most one Hilbert extension;
- its extension is automatically onto \`H_Xi\`;
- the full upper-half-plane kernel is determined by the source subdomain; and
- the Herglotz multiplication model and compact-resolvent operator of Ledger
  1382 follow from standard realization once positivity holds.

This removes density and Cauchy-span closure as independent conjectural gates.
It does not prove positivity. Before RH, the Pick form is indefinite and the
RKHS/orthogonality argument is unavailable; an indefinite topology is not
canonically selected.

## Remaining provenance distinction

Analytically, the source comparison is now complete conditional on positivity:

\`Mellin half-line modes -> Weil quotient -> H_Xi -> A\`.

The physical/Carrier provenance remains weaker. No relative-chain boundary
map realizes the logarithmic test functions or their Weil pairing. Therefore
the result is a source-derived analytic Mellin boundary, not a demonstrated
physical coefficient--Betti pushforward.

## Scope

This is a conditional totality and uniqueness theorem. It assumes Pick
positivity/RH and does not establish the physical relative-chain map.
