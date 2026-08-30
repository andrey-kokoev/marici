# Omega transfer to poles, widths, and residues

Work package: WP551  
Owner: marici.Figueiredo

## Question

Which parts of WP534 inherit WP550's same-ensemble Omega calibration, and
which parts remain independent of the lattice energy unit?

## Typed quantities

WP534 uses a mass-squared resolvent. Its six simple pole packets contain:

- complex pole squares \(\mu_i^2=M_i^2-iM_i\Gamma_i\), of mass dimension two;
- widths \(\Gamma_i\), of mass dimension one;
- signed resolvent residues \(r_i=N(m_i^2)/D'(m_i^2)\), of mass dimension zero.

The last statement is also forced by the exact reconstruction

\[
K(0)=\sum_i {r_i\over-m_i^2}.
\]

The kernel has mass dimension minus two, so the signed residues are
dimensionless. Positive current-trace residues are projector weights and are
dimensionless for the same reason.

## Exact transfer law

Let \(\widehat q\) be the dimensionless lattice representation of a quantity
with declared mass dimension \(d\). The Omega constructor gives

\[
q_{\mathrm{phys}}
=\widehat q\left({m_\Omega^{\mathrm{phys}}\over a m_\Omega}\right)^d.
\]

In log coordinates its row is

\[
e_{\widehat q}-d e_{a m_\Omega}+d e_{m_\Omega^{\mathrm{phys}}}.
\]

For the six pole squares, six widths, and six residues, the resulting
eighteen-by-twenty Jacobian has rank eighteen. A common change of lattice unit
cancels exactly.

The common scale covariance is proportional to the outer product of the
dimension vector

\[
d=(2,2,2,2,2,2,1,1,1,1,1,1,0,0,0,0,0,0)^T.
\]

It correlates every pole-square and width readout. It contributes nothing to
the dimensionless residue block.

## Deletion replay and correction to WP550

Deleting the same-ensemble Omega measurement or its physical convention
invalidates all twelve dimensionful pole-square and width readouts together.
It does not invalidate a dimensionless residue merely by removing the scale.
Residues still require the independent WP535 current renormalization,
operator-mixing, subtraction, and covariance contract.

This refines WP550's overly broad phrase that scale deletion invalidates
residues. Scale authority and current-normalization authority are distinct.

## Status

This is an exact unit and covariance transfer theorem on the WP534 benchmark,
not an executed calibration. It neither supplies WP542 joint data nor selects
\(g_Ff/v\). A successful transfer identifies the physical units of a realized
packet; it does not create a source law.

The smallest exact falsifier is to assign a nonzero Omega-scale covariance to
a dimensionless residue, or to delete the common Omega latent variable while
leaving any dimensionful pole or width marked calibrated.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp551_omega_pole_width_residue_transfer.py

The generated result is
research/flavor/results/wp551_omega_pole_width_residue_transfer.json.
