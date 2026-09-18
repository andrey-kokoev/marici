# Many-many corrected Hadamard wall frame

The source-normalized endpoint frame is

$$
T_\theta
=\begin{pmatrix}-2&0\\0&1\end{pmatrix}H
=\frac1{\sqrt2}
\begin{pmatrix}-2&-2\\1&-1\end{pmatrix}.
$$

The first row maps to the relative constant wall and the second row maps to the oriented odd jump. The inverse frame is used on the target side, with the source metric retained explicitly.

For a four-block family, apply `T_theta` to the endpoint indices before forming the wall blocks. The ordered cross block is then reconstructed from the transformed four blocks using the same Hadamard linear combination, with the even-channel factor carried in each occurrence of the first row.

This prevents the relative wall vector from being identified with the theta wall vector at the wrong amplitude.

Status: corrected frame matrix fixed; transformed four-block source equality remains to be checked.
