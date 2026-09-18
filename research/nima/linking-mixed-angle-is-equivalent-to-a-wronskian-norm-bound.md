# Linking mixed angle is equivalent to a Wronskian norm bound

Let

$$
G_{\rm link}=
\begin{pmatrix}0&K_{\rm link}\\-K_{\rm link}&0\end{pmatrix},
\qquad
K_{\rm link}=-\frac12J_{\rm link}.
$$

For forward and reciprocal vectors `x,y`, the linking cross term obeys

$$
|\langle x,K_{\rm link}y\rangle|
\le\|K_{\rm link}\|\,\|x\|\,\|y\|
=\frac12\|J_{\rm link}\|\,\|x\|\,\|y\|.
$$

Relative to unit diagonal energies in the two output slots, the optimal operator-level mixed-angle constant is

$$
\rho_{\rm link}=\|K_{\rm link}\|
=\frac12\|J_{\rm link}\|.
$$

Therefore strict linking-sector positivity follows from

$$
\|J_{\rm link}\|<2.
$$

Continuity of the Wronskian form proves only that `||J_link||` is finite. It does not imply this strict inequality. The coefficient `-1/2` is source-forced and cannot be reduced to manufacture a margin.

With nonunit diagonal Green weights `B_+` and `B_-`, the invariant condition is

$$
\left\|B_+^{\dagger/2}K_{\rm link}B_-^{\dagger/2}\right\|<1
$$

on the reduced supports, together with annihilation of both radicals. This is the correct form of the mixed-angle test after semidefinite reduction.

Status: linking contribution to the mixed margin reduced to an explicit normalized Wronskian norm; strict source bound remains open.
