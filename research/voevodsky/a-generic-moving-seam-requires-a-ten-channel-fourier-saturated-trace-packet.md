# A generic moving seam requires a ten-channel Fourier-saturated trace packet

## Question

Does the one-channel repair of the fixed-seam history port remain closed when the seam moves to \(a\ne0\)?

## Claim boundary

No. Fourier exchanges translation with modulation and reflection sends \(a\) to \(-a\). For a generic nonzero seam, the orbit closure of the causal seam value and flux contains ten scalar channels. It degenerates to the four-channel packet at \(a=0\).

## Channel definitions

Let

$$
B_b(g)=g(b),
\qquad
Q_b(g)=\int_{\mathbb R}e^{-2\pi ibx}g(x)\,dx,
$$

$$
A_b(g)=\int_{-\infty}^b g(x)\,dx,
\qquad
C_b(g)=\operatorname{pv}\int_{\mathbb R}
\frac{e^{-2\pi ibx}g(x)}x\,dx.
$$

Also write \(B_0=g(0)\) and \(Q_0=\int g\).

For the moving-seam causal history, \(A_a\) is seam value and \(B_a\) is seam flux.

## Fourier orbit of seam flux

Directly,

$$
B_a(\widehat g)=Q_a(g),
\qquad
Q_a(\widehat g)=B_{-a}(g).
$$

Consequently

$$
B_a\to Q_a\to B_{-a}\to Q_{-a}\to B_a.
$$

A nonzero seam therefore forces the reflected seam and both modulated-mass channels.

## Fourier orbit of seam value

Translation of the Heaviside identity gives

$$
A_a(\widehat g)
=
\frac12B_0(g)-\frac1{2\pi i}C_a(g).
$$

Using \(\mathcal F^2g(x)=g(-x)\),

$$
C_a(\widehat g)
=2\pi iA_{-a}(g)-\pi iQ_0(g).
$$

Together with the reflected equations, this closes the six-channel span

$$
(B_0,Q_0,A_a,A_{-a},C_a,C_{-a}).
$$

## Generic saturated packet

For \(a\ne0\) with \(a\ne-a\), the flux orbit and value orbit are independent. The Fourier-saturated moving-seam trace packet is therefore

$$
\Gamma_a^{\rm sat}
=
(B_0,Q_0,A_a,A_{-a},C_a,C_{-a},
 B_a,Q_a,B_{-a},Q_{-a}).
$$

All ten channels are continuous on the Schwartz test space and on its appropriate strong dual by transposition. Their displayed formulas define an exact order-four action.

## Fixed-seam degeneration

At \(a=0\),

$$
B_a=B_{-a}=B_0,
\quad
Q_a=Q_{-a}=Q_0,
\quad
A_a=A_{-a}=A_0,
\quad
C_a=C_{-a}=C_0.
$$

The ten-channel packet collapses to

$$
(B_0,Q_0,A_0,C_0),
$$

recovering the minimal fixed-seam four-port.

## Consequence

Moving-seam covariance and quarter-turn Fourier closure cannot both live in the old four-scalar history target. The target rank jumps generically because translation becomes modulation under Fourier. This is source-forced, not optional detector enlargement.

## Disposition

A generic moving seam requires a ten-channel Fourier-saturated trace packet; the four-channel repair is special to the Fourier-fixed seam at zero. Any global \(V_4\) presentation claiming both moving-seam and quarter-turn naturality must retain these reflected and modulated channels, or retain an equivalent function-valued response.