# Many-many corrected four-block reconstruction

Let the unscaled ordered endpoint Gram be

$$
K=\begin{pmatrix}T&C\\C^*&O\end{pmatrix}.
$$

The corrected wall-frame transport is

$$
K_\theta=T_\theta K T_\theta^*.
$$

The Hadamard blocks are formed after the source factor is inserted. The ordered cross block is recovered by applying the inverse frame transport:

$$
K=T_\theta^{-1}K_\theta(T_\theta^{-1})^*.
$$

Equivalently, the four-block reconstruction remains

$$
C=\frac12(P-N-Q+R),
$$

provided `P,Q,R,N` are the corrected transported blocks. Using uncorrected blocks would rescale the even/odd cross terms incorrectly.

For refinement maps `R_beta,alpha`, the corrected transport is natural when

$$
T_\theta R_{\beta\alpha}=R^{\rm wall}_{\beta\alpha}T_\theta.
$$

Status: corrected reconstruction formula fixed; numerical source block comparison remains open.
