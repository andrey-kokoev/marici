# Common radial history has a cutoffwise half-line L2 bound

## Question

Does the source-defined common history map continuously into the half-line Hilbert carrier already used by the radial interface?

## Claim boundary

At every finite interval-graph cutoff, yes, conditional only on the completed atom \(\Phi_1\) belonging to \(L^2(\mathbb R)\cap L^\infty(\mathbb R)\), which follows from its recorded Gaussian-tail formula. The bound depends explicitly on cutoff support and total edge length. No cutoff-uniform bound or completed source map is claimed.

The variable below is the separation coordinate, not physical time.

## Source map

For fixed ratio label \(D\), let

\[
J_Dc(v)=\sum_{e\in E_D}c_e\mathbf 1_{[A_e,B_e]}(v)
\]

and

\[
B_Dc(s)=\int_{\mathbb R}J_Dc(v)\Phi_1(v)\Phi_1(v+s+D)\,dv,
\qquad s\geq0.
\]

Let \([a_D,b_D]\) contain the support of every interval and put

\[
L_D=b_D-a_D,
\qquad
S_D=\sum_{e\in E_D}|B_e-A_e|.
\]

## Half-line estimate

Cauchy--Schwarz in \(v\) gives

\[
|B_Dc(s)|^2
\leq
\|J_Dc\,\Phi_1\|_2^2
\int_{a_D}^{b_D}|\Phi_1(v+s+D)|^2\,dv.
\]

Integrating over \(s\geq0\) and changing variables yields

\[
\int_0^\infty\int_{a_D}^{b_D}
|\Phi_1(v+s+D)|^2\,dv\,ds
\leq
L_D\|\Phi_1\|_2^2.
\]

Therefore

\[
\|B_Dc\|_{L^2(\mathbb R_+)}
\leq
\sqrt{L_D}\,\|\Phi_1\|_2
\|J_Dc\Phi_1\|_2.
\]

Using \(\|J_Dc\Phi_1\|_2\leq\|\Phi_1\|_\infty\|J_Dc\|_2\) and the interval Gram matrix \(G_D\),

\[
\|J_Dc\|_2^2=c^*G_Dc,
\qquad
(G_D)_{ef}=|[A_e,B_e]\cap[A_f,B_f]|.
\]

Since \(G_D\) is positive semidefinite and

\[
\lambda_{\max}(G_D)\leq\operatorname{tr}G_D=S_D,
\]

we obtain

\[
\|B_Dc\|_{L^2(\mathbb R_+)}
\leq
C_D\|c\|_2,
\qquad
C_D=
\sqrt{L_DS_D}\,
\|\Phi_1\|_\infty\|\Phi_1\|_2.
\]

This constructs a bounded cutoffwise map

\[
B_D:\mathbb C^{E_D}\longrightarrow L^2(\mathbb R_+).
\]

Applying the same estimate to the reciprocal half gives the doubled half-line target, with norm bound at most \(\sqrt2 C_D\) when both components use the same estimate.

## Compatibility with the cycle port

The prior spanning-forest theorem identifies \(\ker B_D=Z_1(G_D)\). Hence the bounded history map alone is not faithful. The augmented map \((B_D,Z_D)\) is faithful at each finite cutoff; its Hilbert target is

\[
L^2(\mathbb R_+)\oplus\mathbb C^{\beta_1(G_D)}.
\]

The finite-dimensional cycle factor requires its own declared covariance or norm before joining the calibrated metric.

## Residual

The estimate depends on \(L_D\) and \(S_D\). Prior research does not bound their growth over the cutoff system, nor specify transition maps between the chosen spanning forests. Therefore this establishes the missing half-line map cutoffwise but does not construct a bounded map from an unbounded completion.

## Disposition

The source common history does enter the existing half-line Hilbert carrier at every finite cutoff. The next obstruction is uniform cutoff control and compatible cycle-port transitions, not existence of the individual Hilbert maps.
