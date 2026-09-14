# The physical-chamber return is label-preserving and supplies no route swap

## Canonical chamber path

Assume strict physical triangle inequalities and positive \(x,y,z\). The physical parameter chamber is convex. Connect the exchanged point \((y,x,z)\) to \((x,y,z)\) by

\[
x_t=(1-t)y+tx,
\qquad
y_t=(1-t)x+ty,
\qquad z_t=z.
\]

Every point remains in the same strict physical chamber.

For the \(b\)-pencil, set

\[
A_t=y_t+z,
\qquad B_t=2x_t+y_t+z=A_t+2x_t.
\]

Throughout the path,

\[
0<A_t<B_t.
\]

Therefore the four ordered split-fiber locations

\[
A_t,-A_t,B_t,-B_t
\]

remain pairwise distinct. No braid or collision permutes their labels. Keeping the \(W=\pm Q\) component orientation gives label-preserving continuation

\[
d_i(t=0)\longmapsto d_i(t=1).
\]

## Return through the symmetric midpoint

At \(t=\tfrac12\), \(x_t=y_t\). Site exchange fixes the external parameter point and exchanges the \(a\)- and \(b\)-pencils while preserving their ordered split locations and \(W\)-component labels.

Consequently the natural return built from:

1. chamber transport to the symmetric midpoint;
2. site exchange at the midpoint;
3. chamber transport back;

acts as the identity on the tetrahedral vertex labels and hence on the primitive \(A_1^3\) frame.

## Consequence

The physical-chamber return does not swap \(\beta_{12}\) and \(\beta_{13}\), and it does not decide a nontrivial sum-versus-difference kernel. Any return map that does so must wind around an excluded discriminant or include additional marked-relative/Gysin data not present in the split-fiber location local system.

This also exposes a typing issue: the one-wall extension generators \(w_{101},w_{110}\) cannot be identified merely with component-difference routes. Under their natural site exchange they are related by a de Rham orientation sign, whereas the split-fiber Picard labels return identically. The missing comparison must bridge these two local systems, not merely transport the four vertex locations.

## Claim boundary

This proves absence of a permutation in the ordered split-location subsystem along the convex physical path. A full Picard Gauss--Manin statement additionally requires smoothness of the compact surface family along that path. No claim is made for paths winding outside the physical chamber.

Verification:

- `research/voevodsky/checkers/check_physical_chamber_label_return.py`
- `research/voevodsky/results/physical_chamber_label_return.json`
