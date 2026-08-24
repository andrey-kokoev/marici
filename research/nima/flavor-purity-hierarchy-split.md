# Flavor purity splits into hierarchy and alignment

This independent continuation of Figueiredo WP49--WP51 preserves her
artifacts and tests the remaining near-unity question from the physical
purity functions.

Along the strict small-angle ray

\[
s_{13}=r s_{23},\qquad r=s_{13}^{\rm obs}/s_{23}^{\rm obs},
\]

the first two anchors approach

\[
F_u\longrightarrow 1-\frac{y_c^2}{y_t^2},
\qquad
F_c\longrightarrow 1.
\]

Their near-unity is therefore hierarchy-forced. The third anchor behaves
differently. Its strict-limit function of \(r\) has a tested maximum

\[
F_t\simeq0.9915244
\quad\text{at}\quad r\simeq0.08825,
\]

while the observed ratio is \(0.0898305\). Hostile legal rays give
\(F_t(0.03)\simeq0.9564\) and \(F_t(0.18)\simeq0.9085\).

Thus the joint claim that all three purities are universally driven to one
is false. The source hierarchy explains \(u,c\); the \(t\) value is a
ratio-alignment effect, close to the top of a valley but neither exactly one
nor universal.

This does not explain why the measured CKM ratio lies near that valley
maximum. It types the remaining question correctly: a numerical point
selector is missing, not another algebraic inversion.

Verification:

    python research/nima/checkers/check_flavor_purity_hierarchy_split.py

The dependency-free checker passes 6/6.
