# qRB microstep 145: Hermitian branch symmetry

A translation-Gram kernel must satisfy

$$
K_t(-d)=\overline{K_t(d)}.
$$

For the real source and symmetric pole prescription, this requires the upward and downward gamma-contour continuations to be paired by complex conjugation. Residue corrections must therefore obey

$$
R_k(-d)=\overline{R_k(d)}.
$$

At real `d`, the resulting completed kernel is real and even after the reflected branches are combined.

This is a necessary consistency check before any Toeplitz positivity test. A failure indicates a contour-orientation or endpoint-normalization error, not necessarily a positivity failure.

Status: Hermitian branch-symmetry criterion isolated; full residue-corrected verification remains open.
