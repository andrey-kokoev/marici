# Source-defined nonforward Breit-Wheeler cut

Two copies of the normalized tree kernel have now been glued across the same
on-shell \(e^+e^-\) phase-space fiber:

\[
\operatorname{Im}\mathcal M_{fi}
=\frac12\int d\Phi_2\,A_iA_f^*.
\]

The resulting object is a \(4\times4\) matrix in the ordered incoming photon
helicity pairs

\[
(++,+-,-+,--).
\]

At the forward sample \(s=10m_e^2\), it is Hermitian to
\(4\times10^{-17}\) and positive definite. Its diagonal divided by \(s\)
gives the polarized total cross sections, as required by the optical theorem.

At the nonforward sample

\[
s=10m_e^2,qquad t=-m_e^2,
\]

the matrix remains finite. Reflecting the scattering plane complex-conjugates
the matrix to \(5\times10^{-17}\).

One nontrivial convention was exposed by the gate: the spherical polarization
frame of the fourth photon differs by \(-1\) from the declared incoming frame
at zero scattering angle. Transporting that frame continuously restores the
forward positive pairing. This sign is part of the comparison map, not an
arbitrary post-processing correction.

## Remaining typing gate

The cut matrix is currently expressed as a physical initial/final helicity
pairing. Before taking dispersive moments, its final-state convention must be
crossed into the all-incoming helicity convention defining
\(\Phi_1,\Phi_2,\Phi_5\). In particular, time reversal exchanges the two
back-to-back final momentum labels. That permutation and its polarization
phases must be derived and checked against the forward optical theorem; they
must not be inferred by fitting the known EFT coefficients.

Reproduce with `research/nima/check_nonforward_breit_wheeler_cut.py`.
