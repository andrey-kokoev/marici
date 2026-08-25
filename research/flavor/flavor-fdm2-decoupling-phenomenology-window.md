# Decoupling-versus-CP phenomenology window for FDM-2 (WP113)

Agent: `marici.Figueiredo`. Date: 2026-08-25.

Keep the WP90 couplings and singlet vacuum fixed while varying only the real
vectorlike mass `M` in the full `4x4` down-sector block. This is the smallest
repair family after WP112.

Use the Particle Data Group direct first-row result

\[
|V_{ud}|^2+|V_{us}|^2+|V_{ub}|^2=0.9984\pm0.0007.
\]

Because this one-mediator model can only reduce the three-light row norm, a
permissive three-standard-deviation cap on its first-row deficit is

\[
d_1\le1-(0.9984-3\times0.0007)=0.0037.
\]

Source: Particle Data Group, 2025 CKM review,
https://pdg.lbl.gov/2025/reviews/rpp2025-rev-ckm-matrix.pdf .

The bounded full-matrix checker finds the boundary

\[
M_{unit}=14.01121267,qquad |J_{full}|=1.51669724\times10^{-5}.
\]

This is below the complete fitted ensemble minimum
`3.14132882e-5`. Conversely, the mass that just reaches that ensemble minimum
is

\[
M_J=10.88411672,qquad d_1=0.00549011>0.0037.
\]

A dense bounded monotonicity audit on `M in [M_J,1000]` verifies that increasing
mass reduces both the first-row deficit and the CP quartet. Hence this
one-parameter fixed-coupling repair has no overlap between the permissive
three-sigma first-row domain and the complete-ensemble `|J|` floor.

This is not a universal no-go for vectorlike flavor models. It is a falsifier
for the smallest WP90 repair family with fixed `Y0,a,b,z` and varying only
`M`. Changing couplings, adding mediators, or changing the source map defines
a new model and requires new authority and a fresh ensemble test.

Classification: neither selector instrument nor rigidifier in the admitted
one-parameter repair family. Smallest numerical hostile pair is the two
boundary masses above. Remaining gate: a new independently declared mediator
architecture capable of suppressing nonunitarity without suppressing the
source CP margin below the observed floor.

Verification: `uv run --with numpy --with scipy python
research/flavor/checkers/wp113_fdm2_decoupling_phenomenology_window.py`.
