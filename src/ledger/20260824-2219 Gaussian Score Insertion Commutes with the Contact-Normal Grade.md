---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2219 — Gaussian Score Insertion Commutes with the Contact-Normal Grade

## Typed projector

Let \(\operatorname{gr}_{\rm ct}\) denote the contact-normal associated-grade
map already used to define the three channels of Entry 2174. The Gaussian
kernel coordinate \(K_e\) and the contact normal are independent source
coordinates on the generic locus. Hence coefficient extraction in the
contact normal commutes with logarithmic differentiation in \(K_e\):

\[
\boxed{
\left[\operatorname{gr}_{\rm ct},
K_e\partial_{K_e}\right]=0.
}
\]

On the projected route pair,

\[
\operatorname{gr}_{\rm ct}F_e(K_e)
=8C_e-8C_eK_e.
\]

At \(K_e=1\),

\[
\operatorname{gr}_{\rm ct}F_e=0,
\qquad
K_e\partial_{K_e}\operatorname{gr}_{\rm ct}F_e=-8C_e.
\]

## Extracted observable

The source-normalized mixed contact readout is therefore

\[
\boxed{
\operatorname{gr}_{\rm ct}
\langle O S_{K_e}\rangle_c=-8C_e.
}
\]

The contact grade removes the backgrounds identified in Entry 2218 without
being chosen to fit the answer. It predates the Gaussian-score construction
and is defined by the source's normal channel.

## Scope

The commutation is established on the generic transverse locus. At soft or
nontransverse intersections, a Rees/nearby-cycle comparison may be required;
the generic result must not be extended there silently.

## Evidence

- Entries 2158–2159, 2174, and 2217–2218
- `research/benincasa/checkers/contact_grade_score_commutation.rs`
