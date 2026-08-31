# The correct completed-theta pair shell density is an explicit incomplete-gamma kernel

## Question

What is the exact ordered-pair shell correlation for the completed theta atoms
in the logarithmic Evans coordinate?

## Claim boundary

It is a three-term incomplete-gamma expression. This replaces the retracted erf
kernel and constructs the correct labelled density before summation over theta
labels. It does not construct the reciprocal/linking response that must cancel
its Laplace transform.

## Completed labelled atoms

Use the fixed single-label normalization

\[
 \Phi_n(u)
 =e^{u/2}
 \left(2a_n^2e^{4u}-3a_ne^{2u}\right)e^{-a_ne^{2u}},
 \qquad
 a_n=\pi n^2.
\]

Any global theta-series multiplicity is applied after this basis calculation.

For an ordered pair \((n,m)\), shell \([a,b]\), and separation \(t\ge0\),
define

\[
 \rho_{nm}^{[a,b]}(t)
 =\int_a^b\Phi_n(u)\Phi_m(u+t)\,du.
\]

Set

\[
 A=\pi n^2,
 \qquad
 C=\pi m^2e^{2t},
 \qquad
 \lambda=A+C,
\]

and

\[
 Y_-=e^{2a},
 \qquad
 Y_+=e^{2b}.
\]

## Polynomial reduction

With \(Y=e^{2u}\),

\[
 du=\frac{dY}{2Y}
\]

and

\[
 e^{u/2}e^{(u+t)/2}=e^{t/2}Y^{1/2}.
\]

The completed polynomial factors obey

\[
 (2A^2Y^2-3AY)(2C^2Y^2-3CY)
 =4A^2C^2Y^4-6AC(A+C)Y^3+9ACY^2.
\]

Therefore

\[
 \Phi_n(u)\Phi_m(u+t)\,du
 =\frac{e^{t/2}}2
 \left[
 4A^2C^2Y^{7/2}
 -6AC\lambda Y^{5/2}
 +9ACY^{3/2}
 \right]e^{-\lambda Y}\,dY.
\]

## Incomplete-gamma notation

Define

\[
 \Delta\gamma_s(\lambda;Y_-,Y_+)
 =\gamma(s,\lambda Y_+)-\gamma(s,\lambda Y_-),
\]

where \(\gamma\) is the lower incomplete gamma function. Then

\[
 \int_{Y_-}^{Y_+}Y^{s-1}e^{-\lambda Y}\,dY
 =\lambda^{-s}\Delta\gamma_s(\lambda;Y_-,Y_+).
\]

## Exact ordered-pair kernel

The shell density is

\[
 \rho_{nm}^{[a,b]}(t)
 =\frac{e^{t/2}}2
 \left[
 \frac{4A^2C^2}{\lambda^{9/2}}
 \Delta\gamma_{9/2}
 -\frac{6AC}{\lambda^{5/2}}
 \Delta\gamma_{7/2}
 +\frac{9AC}{\lambda^{5/2}}
 \Delta\gamma_{5/2}
 \right],
\]

where every incomplete-gamma difference has arguments
\((\lambda;Y_-,Y_+)\).

The second coefficient follows from
\(-6AC\lambda\lambda^{-7/2}=-6AC\lambda^{-5/2}\).

## Ordered orientation

Swapping \(n\) and \(m\) sends

\[
 (A,C)=(\pi n^2,\pi m^2e^{2t})
\]

to

\[
 (\pi m^2,\pi n^2e^{2t}).
\]

At \(t=0\), the kernel is symmetric. For \(t>0\), the separation dilation is
attached to the second label, so the ordered kernels generally differ. Ratio
orientation is retained without adding a fitted phase.

## Shell concatenation

For \(a<b<c\), incomplete-gamma endpoint differences telescope, giving

\[
 \rho_{nm}^{[a,c]}
 =\rho_{nm}^{[a,b]}+\rho_{nm}^{[b,c]}.
\]

Thus the formula is natural under consecutive-prime shell composition.

## Completed forcing

If

\[
 \Phi=\sum_{n\ge1}d_n\Phi_n
\]

with the source-fixed theta coefficients and multiplicities, then on the
admitted rapidly convergent core

\[
 \rho_{a,b}(t)
 =\sum_{n,m}d_nd_m\rho_{nm}^{[a,b]}(t).
\]

No codiagonalization occurs before the ordered-pair kernel is formed.

## Candidate-one readout

The ordinary analytic shell remains

\[
 I_{a,b}^{(0)}(z)
 =-\int_0^\infty e^{-zt}\rho_{a,b}(t)\,dt.
\]

The density is now explicit label by label. A proposed reciprocal/linking law
must reproduce its negative after the separately typed endpoint-flux term is
removed.

## Disposition

The correct first arrow for candidate one is constructed as an
incomplete-gamma ordered-pair kernel in the logarithmic half-density
coordinate. The response-current comparison and full multiplicity cancellation
remain open. No RH conclusion is authorized.
