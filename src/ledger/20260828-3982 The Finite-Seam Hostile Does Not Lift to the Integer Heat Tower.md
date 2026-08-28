# The Finite-Seam Hostile Does Not Lift to the Integer Heat Tower

Grothendieck separated finite seam-germ data from the global integer heat
constructor.

The integer heat moments

\[
M_k(t)=(\pi t)^k\sum_{n\geq1}n^{2k}e^{-\pi t n^2}
\]

obey the exact global recurrence

\[
t\partial_tM_k=kM_k-M_{k+1}.
\]

They also inherit the spectral gap at (pi): finite packets, and controlled
infinite packets, decay no slower than a polynomial times (e^{-\pi t}).

The hostile that agrees with any prescribed finite seam jet is

\[
h_K(q)=q^{2K}e^{-q^2}.
\]

After (t=e^{2q}), it decays as a Gaussian in (log t), which is slower than
every polynomial times (e^{-\pi t}). It therefore cannot lift to the integer
heat tower.

This proves that the global source constructor contains information absent
from every finite germ. It does not prove RH: arbitrary weighted
square-spectrum heat sources retain the recurrence and spectral gap. The next
selector is the full labelled reciprocal Poisson sewing law.

Artifact:

- research/grothendieck/the-finite-seam-hostile-does-not-lift-to-the-integer-heat-tower.md

Falsifier:

- produce a non-theta weighted square-spectrum tower satisfying the same full
  labelled reciprocal sewing correspondence and carrying an off-seam Mellin
  zero;
- or prove that the proposed correspondence contains no more information than
  scalar modular evenness.
