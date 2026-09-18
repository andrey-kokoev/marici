# Many-many relative-trace / determinant comparison square

Let `A_trans` be the pointed labelled translation algebra and let `S_3` be the connected determinant-ideal carrier. The missing source morphism is

$$
\Theta_{\rm tr}:\mathcal A_{\rm trans}\to\mathcal S_3
$$

such that, for every interval operator `H_X`, the diagram

$$
\begin{CD}
H_X @>{\Theta_{\rm tr}}>> K_X\\
@V{\operatorname{Tr}^{\rm rel}_G}VV
@VV{(\operatorname{Tr},\frac12\operatorname{Tr}(\cdot^2),\det_3)}V\\
(J_X^{(1)},J_X^{(2)},J_X^{(\ge3)})
@>>{\text{line totalization}}>
\mathcal L_{\rm prim}\otimes\mathcal L_{\rm sq}\otimes\mathcal L_{\det_3}
\end{CD}
$$

commutes in the relative determinant line.

The first two coordinates require

$$
\operatorname{Tr}K_X=J_X^{(1)},
\qquad
\frac12\operatorname{Tr}(K_X^2)=J_X^{(2)}.
$$

The connected coordinate requires the `det_3` tail of the same `K_X`. The map must also commute with interval concatenation, reciprocal transport, and the Tate line character.

Status: exact relative-trace/determinant comparison square fixed; source morphism `Theta_tr` remains open.
