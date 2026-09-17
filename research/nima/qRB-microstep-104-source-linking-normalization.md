# qRB microstep 104: source linking normalization

The source record fixes the linking coefficient, rather than leaving a free stabilization parameter:

$$
K_{\rm link}=-\frac12J_{\rm link}.
$$

Consequently the polarized two-output operator is

$$
G_{\rm link}
=\begin{pmatrix}0&-J_{\rm link}/2\\J_{\rm link}/2&0\end{pmatrix},
$$

and its norm is controlled by

$$
\|G_{\rm link}\|\le\frac12\|J_{\rm link}\|.
$$

Any additional positive carrier stabilization must use this fixed normalization; it is not allowed to retune the linking coefficient to force positivity.

Status: source coefficient fixed; optional carrier stabilization remains a separate presentation choice.
