---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2216 — The Contact Packet Has a Fixed-State Mixed Readout

## From family derivative to same-state estimator

Entry 2212 expressed the contact class as a derivative across nearby Gaussian
boundary states. Entry 2215 supplies the equivalent estimator in the original
state:

\[
\boxed{
R_e
=\langle O_{\rm ct}S_{K_e}\rangle_c
=-8C_e.
}

Thus preparing and subtracting a second nearby state is not required in
principle. The response can be obtained from a mixed correlator containing
the centered quadratic score insertion.

## Precise observability statement

The ordinary scalar correlator remains blind:

\[
\langle O_{\rm ct}\rangle=0.
\]

The source-defined mixed port is not:

\[
(\langle O_{\rm ct}S_{K_{12}}\rangle_c,
  \langle O_{\rm ct}S_{K_{23}}\rangle_c,
  \langle O_{\rm ct}S_{K_{31}}\rangle_c)
=-8(C_{12},C_{23},C_{31}).
\]

This is the cosmological instance of the cross-sector rule that information
annihilated by a coarse scalar readout can survive in a relational or mixed
port.

## Remaining qualifications

- The insertion is a boundary-state score observable, not a new Carrier cell.
- Generic momentum evaluation gives rank three; coincident energies reduce it
  as in Entry 2213.
- Whether a concrete late-time experiment can access this mixed correlator is
  an operational question beyond the universal integrand theorem.

## Evidence

- Entries 2199, 2212–2215
- `research/benincasa/checkers/fixed_state_score_port.rs`

