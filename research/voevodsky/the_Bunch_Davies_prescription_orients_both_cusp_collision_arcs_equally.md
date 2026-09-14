# The Bunch--Davies prescription orients both cusp collision arcs equally

Write the even infinity quartic as a quadratic in \(r=t^2\):

\[
x^2r^2-Ar+y^2,
\qquad
A=x^2+y^2-(E-x-y)^2.
\]

Its discriminant is

\[
\Delta_r=A^2-4x^2y^2
=-8xy(x+y)E+O(E^2).
\]

At \(E=0\), the two doubled nodes are

\[
t_\pm=\pm i\sqrt{y/x}.
\]

Take the Bunch--Davies approach through the lower half-plane,

\[
E=-i\varepsilon,
\qquad \varepsilon>0.
\]

For positive \(x,y\), the leading discriminant has phase \(\pi/2\), and its principal square root has phase \(\pi/4\). Passing from the displacement in \(r\) to the displacement in \(t\) divides by \(2t_\pm\). Hence the local collision arcs have phases

\[
\arg\delta t_+=-\frac\pi4,
\qquad
\arg\delta t_-=\frac{3\pi}4.
\]

These differ by \(\pi\): the two arcs lie on the same unoriented diagonal and are exchanged by \(t\mapsto-t\).

Therefore a positive loop around \(E=0\) produces the same-sense half-twist at both nodes. Their Picard--Lefschetz contributions are equal, with no hidden relative sign introduced by the physical \(i\varepsilon\) prescription.

This supplies genuine based-path information beyond the permutation shadow. It fixes the relative orientation of the paired local thimbles. It still does not provide their integral image in the algebraic Gysin kernel; that final transport is the missing specialization map.

Certificate:

- `research/voevodsky/checkers/bunch_davies_quartic_collision_arcs.py`;
- `research/voevodsky/results/BD_quartic_collision_arcs.json`.
