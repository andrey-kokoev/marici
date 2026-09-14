# C2 is rejected: the corner e6 coordinate has Betti index four

C2 proposed that the coefficient one in

\[
y e_3+x e_5+e_6
\]

was already a primitive integral Betti coefficient.

The freshly available local Betti comparison gives an exact answer. In the ordered sheet basis \((e_+,e_-)\), the physical boundary is

\[
d=e_--e_+=(-1,1).
\]

The primitive dual reduced-cohomology class is represented symmetrically by

\[
\eta=(-1/2,1/2),
\qquad \eta(d)=1.
\]

The source-normalized first-Rees \(e_6\) covector is

\[
\rho_{e_6}=(-1/8,1/8)=\frac14\eta,
\]

so

\[
\rho_{e_6}(d)=\frac14.
\]

Consequently the integral lattice inside the rational \(e_6\)-line is

\[
\mathbb Z\eta=4\mathbb Z\rho_{e_6}.
\]

The Smith calculations agree:

- occurrence-resolved Betti boundary: invariant factor \(1\);
- quarter-enlarged source \(e_6\) frame: invariant factor \(4\).

Thus the displayed coefficient one is primitive in the frozen de Rham master frame and has Betti index four. The earlier direct reduction

\[
[1,0]_{\rm dR}\mapsto[1,0]_{\rm Betti}\pmod2
\]

is withdrawn.

C2 is therefore rejected. The next replay must retain every factor from the Leray discontinuity, occurrence resolution, and first-Rees comparison, then determine whether the complete physical observable contributes

\[
\rho_{e_6},\quad2\rho_{e_6},\quad\text{or}\quad4\rho_{e_6}=\eta.
\]

Certificate:

- `research/voevodsky/checkers/audit_C2_corner_e6_betti_primitivity.py`;
- `research/voevodsky/results/C2_corner_e6_Betti_primitivity_audit.json`.
