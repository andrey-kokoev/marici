---
id: 467
authors:
  - marici.Benincasa
date: 2026-08-18
---
# Doubled Carrier Reduction Does Not Lift as an Ordinary Cokernel Map

## Record

Status: obstruction to lifting Entry 466's frozen carrier-reduction sequence
as an ordinary module map.

Entry 466 identifies the soft-fiber resonance plane as the kernel of reduction
from the complete exact cokernel to the quartic carrier quotient. To lift that
map over the weighted Rees family by ambient reduction modulo the doubled
carrier would require

\[
\operatorname{im}d_{\rm ex}\subseteq(K)
=
(u^2z^2).
\]

After removing the common weighted exceptional factor, the local condition is

\[
\operatorname{im}d_{\rm ex}\subseteq(z^2).
\]

Entries 462 and 464 instead establish

\[
\operatorname{im}d_{\rm ex}\subseteq(z),
\qquad
\operatorname{im}d_{\rm ex}\nsubseteq(z^2).
\]

The strict failure is witnessed on the odd resonance by the normalized unit
symbol

\[
\bar\sigma_z(q)=-6\eta_-.
\]

Therefore ambient reduction modulo the doubled carrier does not descend from
the complete exact cokernel. The proposed ordinary exact sequence

\[
0\to\mathcal R_{\rm res}
\to C_{\rm exact}
\to\mathcal M_{\rm CM}
\]

does not exist over the full weighted Rees family in that form.

Reduction modulo the reduced carrier \((z)\) does descend, because all exact
images contain one factor of \(z\). Retaining the doubled Cartier structure
requires replacing the ordinary carrier quotient by its two-term resolution
and taking a homotopy fiber. The first-Cartier symbol is then the connecting
differential: rank zero on the even resonance and rank one on the odd
resonance.

This obstruction is coefficient-complex data. It does not require a new
carrier stratum.

## Classification

- doubled carrier: existing \(z^2=0\) structure;
- obstruction: conormal/first-Cartier exact symbol;
- ordinary reduced-carrier map: well-defined;
- ordinary doubled-carrier map: refuted;
- required machinery: derived two-term carrier resolution and homotopy fiber;
- new carrier datum: none.

## Next falsifier

Construct the homotopy fiber of the chain map to the two-term carrier
resolution

\[
[\mathcal O\xrightarrow{z^2}\mathcal O]
\]

with the first-Cartier null-homotopy supplied by the normalized exact symbols.
Compute its cohomology on all Rees degrees and verify that the resonant part is
exactly the length-three object from Entries 464--465, with no additional
kernel or cokernel from the quartic tail.

## Evidence

- research/benincasa/marici-gm/src/bin/soft_axis_carrier_reduction_lift.rs;
- Entries 462 and 464--466.
