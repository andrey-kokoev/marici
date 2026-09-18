# Many-many Hadamard odd-interface integration

For each pair-labelled endpoint plane, apply the canonical frame

$$
H=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
$$

The even wall coordinate and odd jump coordinate are

$$
(e_{\rm wall},e_{\rm jump})=H(\epsilon,\mu).
$$

The source normalization identifies the relative constant wall with the theta wall by

$$
(-1,-1)=-2w_\theta,
\qquad
w_\theta=\left(\frac12,\frac12\right)^T.
$$
Thus the even wall channel carries amplitude factor `-2` in the theta comparison.

The odd pair-to-window map is the normalized rank-one compression

$$
K^{\rm odd}_{nm}=d_{nm}\otimes\ell_{\rm jump},
\qquad
\ell_{\rm jump}(y)=2\sqrt2\langle e_{\rm jump},y\rangle.
$$

Apply this map to the ordered four-block family before scalar codiagonalization. The `P,N` blocks feed the even wall channel with the source factor `-2`; the `Q,R` blocks feed the odd jump channel and reconstruct the ordered cross block by

$$
C=\frac12(P-N-Q+R).
$$

This supplies the normalized source-derived theta-to-wall interface for the finite many-many carrier. Refinement compatibility follows from applying the same `H` and `ell_jump` on every labelled pair coordinate.

Status: canonical Hadamard/odd interface integrated; full analytic–arithmetic source equality remains the final local verification.
