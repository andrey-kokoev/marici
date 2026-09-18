# The minimal theta ordered-flux instrument is an explicit three-moment signed matrix

The direct positive-exponential bridge is impossible: modular evenness gives `Phi'(0)=0`, while every nonconstant positive exponential mixture has strictly negative seam derivative. The ordered-flux construction must retain the signed theta moment grades.

Write

$$
\Phi=4M_2-6M_1
$$

and use the exact raising law

$$
M_k'=\left(2k+\frac12\right)M_k-2M_{k+1}.
$$

In the ordered basis

$$
\mathbf M=(M_1,M_2,M_3)^T,
$$

the source and first derivative coefficient vectors are

$$
c=(-6,4,0)^T,
$$

$$
d=(-15,30,-8)^T,
$$

because

$$
\Phi'= -15M_1+30M_2-8M_3.
$$

Thus the ordered bulk cross current is carried by the rank-two coefficient tensor

$$
dc^T.
$$

Its reflection-even Hermitian polarization has coefficient matrix

$$
\boxed{
S_\theta=dc^T+cd^T
=
\begin{pmatrix}
180&-240&48\\
-240&240&-32\\
48&-32&0
\end{pmatrix}.
}
$$

Its oriented skew polarization has coefficient matrix

$$
\boxed{
A_\theta=dc^T-cd^T
=
\begin{pmatrix}
0&120&-48\\
-120&0&32\\
48&-32&0
\end{pmatrix}.
}
$$

For a spectral parameter `z=a+it`, the ordered face current splits into the `a`-weighted symmetric moment pairing and the `t`-weighted oriented pairing represented by `A_theta`, after inserting the actual moment Gram kernel in the declared Hermitian lane.

This is the smallest source module capable of representing the theta flux: `M_3` is forced by differentiating `Phi`, even though `Phi` itself uses only `M_1,M_2`. The scalar positive-mode theorem erases exactly this raising channel.

The next finite source test is no longer cone membership. It is whether the arithmetic primitive/square/connected incidence transports its three retained grades to these two matrices, with the external flux block already cancelled. In particular, any proposed comparison omitting the `M_2--M_3` coefficient `32` or reversing `A_theta` fails before Xi specialization.

Status: direct positive-mode bridge rejected; exact minimal signed three-moment ordered-flux instrument constructed; arithmetic transport and positivity/dilation of this signed instrument remain open.
