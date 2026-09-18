# Conservative trace candidate is the closed-loop Schur return

For the recovered conservative cone

$$
\mathcal C(s)=
\begin{pmatrix}
A_0(s)&-B(s)^\dagger\\
-B(s)&D_0(s)
\end{pmatrix},
$$

put

$$
G(s)=D_0(s)^{-1}
$$

on an invertible boundary-history chart. The independently source-derived conservative return is

$$
R_{\rm cons}(s)=B(s)^\dagger G(s)B(s).
$$

Thus the conservative trace functional is not an arbitrary readout. On a source observable `A` represented through the incidence graph, its candidate value is the response obtained by applying `B`, propagating by `G`, and returning by `B^dagger`.

The cyclic observable side acts primewise by

$$
R_{\rm cyc}(s)(P_p\otimes\beta)=p^{-2s}\beta.
$$

Therefore the two remaining generator equations become

$$
B^\dagger G B\,[P_p\otimes w_\theta]
=p^{-2s}w_\theta,
$$

$$
B^\dagger G B\,[P_p\otimes j_\theta]
=p^{-2s}j_\theta,
$$

where the brackets denote the admitted incidence realization of the trace observable in the boundary-history graph.

Equivalently, the even and odd source lines must be eigenlines of the closed-loop Schur return with eigenvalue `p^(-2s)`. The even equation is the wall normalization channel; the odd equation is the oriented Wronskian channel with the forced `-1/2` coefficient.

This formulation derives the functional from the recovered conservative pencil rather than defining it by the desired cyclic trace. It is executable once typed locators for `B`, `D_0`, and the observable-to-incidence realization are materialized.

Status: independent conservative functional identified abstractly as the Schur return; entrywise prime-shell evaluation remains blocked by missing constituent locators.
