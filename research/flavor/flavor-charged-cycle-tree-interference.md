# Charged-cycle tree interference

## Bounded question

Does WP635's unique incidence invariant enter a finite-mass source amplitude,
or is it only a formal coupling label without an executable transition?

## Two matched paths

At the isotropic connector vacuum, consider the charged heavy transition
between an up-type first-stage messenger and a down-type second-stage
messenger, with one external \(\chi\). There are exactly two length-two paths
in the declared grammar:

1. pass through \(B^u\), using \(Y_S^u\), the inverse mass \(M_{B^u}^{-1}\),
   and \(C_B\);
2. cross first through \(C_A\), pass through \(A^d\) with inverse mass
   \(M_{A^d}^{-1}\), and use \(Y_S^d\).

After suppressing their common connector and charged-field factors, the path
amplitudes are

\[
P_B={Y_S^uC_B\over M_{B^u}},
\qquad
P_A={C_AY_S^d\over M_{A^d}}.
\]

Since \(M_{B^u}=Z_B^u\sigma\) and
\(M_{A^d}=Z_A^d\sigma\), their ratio is

\[
{P_B\over P_A}=
{Y_S^uZ_A^dC_B\over Y_S^dZ_B^uC_A}
=\mathcal I_\chi.
\]

Thus the unique WP635 cycle is exactly the relative phase and magnitude of two
finite-mass tree paths with the same external states. Field rephasings multiply
both paths by the same endpoint phase and leave their ratio unchanged.

## Exact interference witness

At unit magnitudes and equal positive masses, the two relative-sign classes
give

\[
|P_A+P_B|^2=4
\]

for \(\mathcal I_\chi=1\), and zero for
\(\mathcal I_\chi=-1\). The transition rate therefore separates the two sign
classes exactly on this conditional source slice. This is a genuine source-
generated probe, not a projector fitted from the desired result.

Electric charge is conserved: the charge difference between the up and down
messengers is one, matching \(Q_\chi=1\).

## Instrument and selector boundary

WP636 upgrades the charged cycle from algebraic distinguishability to a
conditional tree-level threshold response. It still does not select
\(\mathcal I_\chi\); both constructive and destructive interference are legal
source points. Nor is the response yet experimentally calibrated.

An executable instrument requires a kinematically open heavy transition,
mass-eigenstate mixing from the complete charged messenger matrix, finite
widths, all competing decays, production support, detector resolution, and a
common-frame rate likelihood. If the transition is closed, an off-shell or
loop observable must be derived instead. No conclusion may be transported to
`physical16` until the low-energy matching includes the same invariant.

## Reproduction

Run:

    python research/flavor/checkers/wp636_charged_cycle_tree_interference.py

The generated result is
`research/flavor/results/wp636_charged_cycle_tree_interference.json`.

