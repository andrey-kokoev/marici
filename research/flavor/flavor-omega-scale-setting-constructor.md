# Omega scale-setting constructor

## Question

Can the propositional \(P_{\mathrm{scale}}\) interface be replaced by a
physically standard scale-setting operation native to the WP535 lattice
instrument?

## Independently frozen operation

Use the \(\Omega^-\) baryon as an external low-energy QCD reference. On every
ensemble used for the six flavor ports, measure:

- the dimensionless mass \(a m_\Omega\);
- all six dimensionless pole coordinates \(a\mu_i\);
- the chosen gradient-flow quantities, such as \(w_0/a\) or \(t_0/a^2\);
- their full joint covariance with the flavor correlator estimators.

Freeze an independently declared pure-QCD convention for the physical
\(\Omega^-\) mass, including electromagnetic and isospin corrections. Then

\[
a={a m_\Omega\over m_\Omega^{\mathrm{phys}}},
\qquad
\mu_i={a\mu_i\over a}
={a\mu_i\,m_\Omega^{\mathrm{phys}}\over a m_\Omega}.
\]

This is a named physical transfer chain from an experimental hadron scale to
the lattice energy unit. It is not an optical-frequency extrapolation.

Primary lattice calculations demonstrate the architecture. Miller and
collaborators measured \(a m_\Omega\), \(t_0/a^2\), and \(w_0/a\) on each of
22 ensembles and carried out continuum, volume, tuning, and uncertainty
analysis:

- https://arxiv.org/abs/2011.12166

A 2025 update uses nine HISQ ensembles, explicitly defines electromagnetic
corrections for the pure-QCD \(\Omega^-\) input, and reports a 0.40 percent
determination of \(w_0\):

- https://arxiv.org/abs/2509.14367

These sources authorize the operation type. They do not supply measurements
on the future WP542 ensembles.

## Exact six-port map

In log coordinates, order the inputs as the six \(a\mu_i\), followed by
\(a m_\Omega\) and \(m_\Omega^{\mathrm{phys}}\). The physical outputs have
Jacobian rows

\[
e_i-e_\Omega+e_{\Omega,\mathrm{phys}}.
\]

The six-by-eight Jacobian has rank six. A simultaneous rescaling of every
dimensionless lattice mass cancels exactly, while a shift of the external
physical \(\Omega\) input moves all six physical poles together.

## Covariance is part of the interface

For the complete joint input covariance \(C_{\mathrm{joint}}\),

\[
C_{\mathrm{phys}}=J C_{\mathrm{joint}}J^T.
\]

Even in a diagonal witness, the lattice and physical \(\Omega\) uncertainties
produce a common off-diagonal term in every pair of physical pole outputs.
On actual common ensembles, cross-covariances between \(a m_\Omega\), the
gradient-flow observables, and all flavor estimators must also be retained.

Treating the scale uncertainty as six independent error bars would destroy the
common-frame semantics.

## Temporal contract

The successful WP549 calibration event is now typed concretely:

- precondition: \(\Omega\), flow, and flavor estimators come from the same
  frozen ensemble stream and tuning prescription;
- outcome: a joint scale fit with a declared pure-QCD convention and
  covariance;
- post-state: a valid calibrated state for that ensemble and fit revision;
- deletion replay: removing either \(\Omega\) input or its covariance
  invalidates all physical-unit poles, widths, and residues.

## Authority boundary

WP550 supplies a source-authorized physical architecture for
\(P_{\mathrm{scale}}\), not an executed WP535 dataset. Importing a published
\(w_0\) number without measuring the corresponding dimensionless scale
observable on the WP542 ensembles fails the same-unit gate and restores the
WP548 ambiguity.

The operation identifies physical scales. It still does not select
\(g_Ff/v\) or supply

\[
2\ell_a-\ell_w\ne0.
\]

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp550_omega_scale_setting_constructor.py

The generated result is
research/flavor/results/wp550_omega_scale_setting_constructor.json.

The reviewed graph admission is
ev-000000004997-e9f584ba-efd4-4373-b85f-e9152d06f1f6.
