# qRB microstep 101: polarized metric signature

For a nonzero skew-adjoint `K_link`, the two-output operator

$$
G_{\rm link}=\begin{pmatrix}0&K_{\rm link}\\-K_{\rm link}&0\end{pmatrix}
$$

is Hermitian self-adjoint but not an ordinary positive metric. Its off-diagonal polarization carries the signed linking orientation; slot exchange reverses its sign.

Thus the correct positivity statement concerns the separately constructed carrier norm, not `G_link` itself. Treating `G_link` as positive would reintroduce the overly strict Weil/GNS requirement.

Status: indefinite polarized metric semantics fixed; relative positive carrier remains the valid target.
