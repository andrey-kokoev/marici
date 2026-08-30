# Radial-independent CP selector (WP351)

## Spectral normalization

WP350's radial amplitudes change masses and the raw commutator invariant. They
do not change the eigenvectors of the two selected Hermitian directions. The
exact discriminant-normalized ratio is

\[
\frac{\operatorname{Tr}([H_u,H_d]^3)^2}
{\Delta(H_u)\Delta(H_d)}
=-\frac{12}{181},
\]

where each discriminant is the squared spectral Vandermonde. Using the standard
three-family commutator identity gives

\[
J^2=\frac1{543}.
\]

Both derivatives with respect to (x) and (y) vanish exactly. The same rays
therefore select a numerical normalized CP magnitude while leaving the spectra
free.

## Classification

This is a genuine conditional partial selector on the faithful flavor quotient,
not merely a presentation rigidifier. It selects one mixing invariant but not
the mass coordinates or a full `physical16` point.

Its authority remains conditional because the projector geometry and unequal
sector-character assignments were stipulated. Radial normalization is no
longer a loophole for this particular prediction.

## Falsifier

Any admitted fitted point with (J^2\neq1/543) rejects the selected-ray geometry
independently of the radial amplitudes. The complete fitted ensemble test is the
next bounded operation.

Run `uv run --with sympy python
research/flavor/checkers/wp351_radial_independent_cp_selector.py` to regenerate
the exact normalized audit.
