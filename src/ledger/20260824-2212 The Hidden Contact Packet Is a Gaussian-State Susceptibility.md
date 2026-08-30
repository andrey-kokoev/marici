---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2212 — The Hidden Contact Packet Is a Gaussian-State Susceptibility

## Exact response

For the channel labelled by edge \(e\), the cancelling contact routes are

\[
(A_e,B_e)=(8C_e,-8C_e).
\]

The grade-two route does not erase the final edge \(e\), while the
grade-three route does. Therefore

\[
\frac{\partial}{\partial\log K_e}(A_e+B_e)
=B_e=-8C_e.

Since \(K_e=(2\operatorname{Re}\psi_2(y_e))^{-1}\),

\[
\boxed{
\frac{\partial}{\partial\log\operatorname{Re}\psi_2(y_e)}
(A_e+B_e)=+8C_e.
}

The shared erased edges contribute equally to both routes and cancel from
the edge-specific response.

## Upgrade in status

The contact packet is invisible in the correlator value but visible in its
first response to the Gaussian boundary kernel. It is therefore a genuine
linear susceptibility of the source-defined probability distribution:

\[
\boxed{
\text{zero scalar value}
\quad+\quad
\text{nonzero boundary-state response}.
}

This is physical readout at the level of a controlled family of boundary
states. It does not imply that a single fixed-state measurement reconstructs
the three routes.

## Evidence

- Entries 2195, 2201, and 2211
- `research/benincasa/checkers/gaussian_contact_susceptibility.rs`

