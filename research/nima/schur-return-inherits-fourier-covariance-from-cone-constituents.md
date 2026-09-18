# Schur return inherits Fourier covariance from cone constituents

Let `F_E` and `F_H` be the Fourier/quarter-turn actions on the Euler source and boundary-history carriers. Assume

$$
F_HB=BF_E,
$$

$$
F_HD_0=D_0F_H,
$$

and that the declared pairings give the contragredient identity

$$
B^\dagger F_H=F_EB^\dagger.
$$

On an invertible chart, commutation of `D_0` with `F_H` implies

$$
F_HD_0^{-1}=D_0^{-1}F_H.
$$

For the Schur return

$$
R_{\rm cons}=B^\dagger D_0^{-1}B,
$$

one then has

$$
\begin{aligned}
R_{\rm cons}F_E
&=B^\dagger D_0^{-1}BF_E\\
&=B^\dagger D_0^{-1}F_HB\\
&=B^\dagger F_HD_0^{-1}B\\
&=F_EB^\dagger D_0^{-1}B\\
&=F_ER_{\rm cons}.
\end{aligned}
$$

Thus quarter-turn covariance of the Schur return is not an additional metric identity; it follows functorially from the three constituent intertwiners.

The stratified Fourier–Poisson construction supplies these identities on the source-generated common graph, with `B^dagger` transported contragrediently. Hence the odd generator equation follows from the even generator equation there.

Status: Schur-return quarter-turn covariance proved on invertible common charts; conservative/cyclic trace comparison reduced unconditionally on that domain to the single even-wall eigenvalue equation.
