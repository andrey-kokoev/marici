# A physical-diagonal pole does not belong to the C34 Hilbert--Schmidt observer domain

## Question

Can the corrected pair be inserted into the existing `C34` observer domain by
allowing its Mellin multiplier to have the diagonal pole

\[
m(t)=\frac{a(t)}{t-t_0}?
\]

## Local obstruction

Let `D` denote the `C34` difference row. For an integral-kernel presentation,

\[
\|DM_m\|_{\mathcal S_2}^2
=
\int w_D(t)|m(t)|^2\,dt,
\qquad
w_D(t)=\int |K_D(s,t)|^2\,ds.
\]

If `a(t_0)` is nonzero and `w_D` has a positive lower bound near `t_0`, then

\[
\int_{|t-t_0|<\varepsilon}
\frac{w_D(t)|a(t)|^2}{|t-t_0|^2}\,dt
=\infty.
\]

Thus a physical-line simple pole is not in the Hilbert--Schmidt observer
domain. Principal value does not repair this norm divergence: it defines a
distributional linear functional, not the square of a multiplication
operator.

The obstruction could disappear only if the difference row has a sufficiently
strong zero at the pole. No current theorem proves such a zero, and imposing
one at Xi parameters would import the desired divisor into the observer.

## Required extension type

A valid rigged extension must split the multiplier before applying the feature:

\[
m=m_{\rm reg}
+a(t_0)\operatorname{pv}\frac1{t-t_0}
+c\,\delta_{t_0}.
\]

The regular component may remain in the existing Hilbert--Schmidt domain. The
principal-value and residue components require separate continuous maps into a
dual or pole--residue carrier. Their cross traces must be defined by a finite
part or boundary pairing, not by declaring `DM_m` Hilbert--Schmidt.

## Finite falsifier

For any proposed extension, compute the truncated norm

\[
N(\epsilon)=
\int_{\epsilon<|t-t_0|<\epsilon_0}
 w_D(t)|m(t)|^2\,dt.
\]

If `w_D(t_0)|a(t_0)|^2` is positive, then `N(epsilon)` grows as
`epsilon^{-1}`. A claimed Hilbert--Schmidt extension is thereby rejected.
Only an explicitly typed subtraction whose residual converges can pass.

## Disposition

The naive inclusion of the corrected pair into the ordinary `C34` observer
space is refuted generically. The next admissible constructor is a three-part
regular/principal-value/residue observer packet with an independently defined
relative boundary pairing.