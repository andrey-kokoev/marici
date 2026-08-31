# Shifted-flux to Chern–Simons interface no-go: WP1071

## Question

Can WP793's shifted \(G_4\) quantization law directly source WP1070's
required seven-channel Chern–Simons coset?

## Candidate source

WP793 supplies shifted quantization

\[
G_4+\frac{c_2(X)}2\in H^4(X,\mathbb Z),
\]

vertical-flux consistency gates, D3-tadpole capacity, a finite-scan lower
bound on chiral multiplicity, and the exact mirror theorem \(G_4\mapsto -G_4\).

## Required interface

To source WP1070's coset, the same packet must also provide:

1. an embedding from the admitted fourfold construction to the interval or
   orbifold fixed-point theory;
2. an \(SU(6)\to SU(4)\times SU(2)\times U(1)\) branch embedding;
3. a projector to the seven anomaly/Chern–Simons channels;
4. a localized Green–Schwarz endpoint action;
5. an orientation-selection law.

WP793 provides none of these five components.

## Consequence

The required WP1070 coset is a seven-component residue vector

\[
\left(\frac12,\frac14,0,0,0,\frac34,0\right)
\pmod{\mathbb Z^7},
\]

whereas WP793's shift is a scalar four-form class. The WP793 mirror theorem
also preserves the admitted source gates while reversing chirality, so it
cannot select the endpoint orientation.

## Boundary

This is an interface no-go, not a rejection of all future shifted-flux
constructions. A positive successor must supply all five map components and
verify that their image is exactly the WP1070 coset.

## Classification

Shifted-flux-to-Chern–Simons interface no-go. The localization branch is
blocked pending a UV boundary-action packet.

Checker: `research/flavor/checkers/wp1071_shifted_flux_cs_interface_no_go.py`

Result: `results/wp1071_shifted_flux_cs_interface_no_go.json`
