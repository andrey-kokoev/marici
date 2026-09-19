# The ordered skew pole anomaly is a residue row, not a Riemann--Lebesgue zero

## Question

What is the qualitative boundary value of the ordered commutator when one
observer contains a physical-line principal-value pole?

## Universal distributional asymptotic

The regular-source vanishing proof reduces the moving-cutoff term to an
oscillatory integral. Near the pole, its singular contribution has the model

\[
I_L=
\operatorname{pv}\!\int
 e^{iL(t-t_0)}
\frac{f(t)}{t-t_0}\,dt,
\]

with `f` smooth and rapidly decreasing. The Fourier transform of the
principal-value distribution gives

\[
\lim_{L\to\pm\infty}I_L
=
\pm i\pi f(t_0),
\]

up to the fixed Fourier convention. Thus the singular term does not obey the
ordinary Riemann--Lebesgue limit. Its boundary value is a residue evaluation.

Applying this to the polarized ordered relative kernel shows that

\[
\mathcal A_{\rm skew}(\Phi,u_z)
=c_{\rm ord}
\operatorname{Res}_{t=t_0}
\left[
\overline{m_\Phi(t)}
\partial_t\log\gamma(t)
m_{u_z}(t)
\right],
\]

where `c_ord` is fixed by the declared Fourier and commutator conventions. It
is not an adjustable Green coefficient.

## Packet consequence

The pole-domain extension adds no new independent channel. Its nonvanishing
skew boundary value is the same residue coordinate already present as the
Sokhotski jump. Therefore the ordered `C34` packet has:

- Hermitian wall coordinate from principal value;
- skew jump coordinate from residue;
- finite endpoint rows.

The retained Wronskian packet has the same wall/jump decomposition. Sewing now
requires only verification of the sign and normalization of `c_ord` against
the fixed Wronskian quarter-column. It does not require forcing the skew limit
to zero.

## Finite falsifier

Choose a test numerator with `f(t0)=1`. Any proposed extension predicting zero
skew boundary value fails the model distribution identity above. A proposed
normalization passes only if its ordered upper/lower difference reproduces the
Sokhotski jump with the same orientation.

## Disposition

The regular Riemann--Lebesgue theorem cannot be promoted to the pole observer.
The ordered skew anomaly is canonically residue-valued. The remaining local
packet test is the exact sign and factor comparison with the retained
Wronskian jump.