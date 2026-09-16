# Fourier transport closes an explicit four-trace endpoint-moment port

## Question

Can the actual Fourier sewing be extended from the radial and spectral presentations to a complete four-component trace presentation?

## Claim boundary

Yes on the Schwartz test core, with continuous dual extension. Fourier transport acts by an explicit order-four matrix on value, mass, derivative, and first moment. This is a source-derived trace port; equality with the separately retained history traces \((P,Q,M_a,J_a)\) requires a further history-to-moment comparison.

## Four traces

For \(f\in\mathcal S(\mathbb R)\), define

$$
P(f)=f(0),
\qquad
Q(f)=\int_{\mathbb R}f(x)\,dx,
$$

$$
M(f)=f'(0),
\qquad
J(f)=\int_{\mathbb R}x f(x)\,dx.
$$

These are continuous functionals on Schwartz space and therefore define a four-port trace map

$$
\Gamma_4(f)=(P(f),Q(f),M(f),J(f)).
$$

## Fourier action

Use

$$
(\mathcal Ff)(y)
=\int_{\mathbb R}f(x)e^{-2\pi ixy}\,dx.
$$

Direct evaluation gives

$$
P(\mathcal Ff)=Q(f),
\qquad
Q(\mathcal Ff)=P(f).
$$

Differentiating under the integral gives

$$
M(\mathcal Ff)
=-2\pi iJ(f).
$$

Fourier inversion gives

$$
f'(0)=2\pi i\int_{\mathbb R}y(\mathcal Ff)(y)\,dy,
$$

hence

$$
J(\mathcal Ff)=\frac1{2\pi i}M(f).
$$

Therefore

$$
\Gamma_4(\mathcal Ff)
=T_4\Gamma_4(f),
$$

where

$$
T_4=
\begin{pmatrix}
0&1&0&0\\
1&0&0&0\\
0&0&0&-2\pi i\\
0&0&(2\pi i)^{-1}&0
\end{pmatrix}.
$$

## Order-four law

The first block squares to the identity, while the second block squares to minus the identity. Thus

$$
T_4^2
=\operatorname{diag}(1,1,-1,-1),
\qquad
T_4^4=I.
$$

This is exactly Fourier square as reflection: value and mass are reflection-even, derivative and first moment are reflection-odd.

## Mixed square

The trace map satisfies the exact analytic intertwining equation

$$
\Gamma_4\mathcal F=T_4\Gamma_4
$$

on \(\mathcal S(\mathbb R)\). Transposition extends the equation to the corresponding strong-dual distributions wherever the four pairings are defined.

## Comparison boundary

The retained relative-history four-port uses endpoint limits, seam value, and seam flux. The present port uses origin value, total mass, origin derivative, and first moment. Their matching dimensions and order-four action do not identify them. A valid comparison must derive the history traces from these four source functionals through the Volterra/history map.

## Disposition

Actual Fourier sewing now has an explicit order-four trace realization, including endpoint and moment data. This constructs a nontrivial Fourier-to-trace mixed square. The remaining \(V_4\) interface question is whether the declared history four-port is the Volterra transport of this endpoint-moment port.