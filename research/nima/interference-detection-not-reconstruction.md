# One Interference Quadrature Detects Holonomy Without Reconstructing It

Entry 2102's controlled-history readout gives

\[
P_\pm=\frac{1\pm\cos\gamma}{2},
\qquad
\gamma=-\frac{16\pi}{9}.
\]

This detects that the loop is nontrivial, but it is invariant under
\(\gamma\mapsto-\gamma\).  Since

\[
e^{i\gamma}\ne e^{-i\gamma},
\]

the single Hadamard quadrature is not faithful on the holonomy circle.

The ordered two-quadrature profile

\[
(\cos\gamma,\sin\gamma)
\]

does reconstruct \(e^{i\gamma}\).  Operationally, this requires a second
phase-shifted control readout.  That port is standard in the abstract quantum
control model, but it has not been derived from the frozen cosmological
equal-time source.

Thus three levels must be kept separate:

1. **Detection:** distinguish the candidate from a declared null case.
2. **Separation:** distinguish every pair in the candidate family.
3. **Reconstruction:** recover the candidate through a faithful coordinate.

Entry 2102 passes detection but not separation or reconstruction with its
displayed readout alone.  The two-quadrature extension would pass all three
only after both ports are source-admitted.
