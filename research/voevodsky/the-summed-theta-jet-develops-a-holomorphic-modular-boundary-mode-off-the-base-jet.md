# The summed theta jet develops a holomorphic modular boundary mode off the base jet

Let

\[
\Phi_x(t)=e^{x/2}\sum_{n\ge1}e^{-cX_n}(4X_n^2-6X_n),
\qquad X_n=\pi n^2e^{2x},\quad c=1-t.
\]

On every strict disc around zero, `Re(c)>0`.  As `x -> -infinity`, the zero
Poisson mode gives

\[
\sum_{n\ge1}X_ne^{-cX_n}
\sim \frac14c^{-3/2}e^{-x},
\]

and

\[
\sum_{n\ge1}X_n^2e^{-cX_n}
\sim \frac38c^{-5/2}e^{-x}.
\]

Therefore

\[
\Phi_x(t)
\sim
\frac32\left(c^{-5/2}-c^{-3/2}\right)e^{-x/2}
=
\frac32\,t(1-t)^{-5/2}e^{-x/2}.
\]

At `t=0` the coefficient vanishes, which is the familiar modular cancellation
making the completed forcing rapidly decreasing.  For every nonzero nearby
`t`, however, the summed jet has a non-L2 boundary mode.  Consequently no
holomorphic disc of the unrenormalized generating section takes values in
`L2(R_x)` or `H1(R_x)`.

The required boundary subtraction is holomorphic and forced:

\[
E_x(t)=\frac32\,t(1-t)^{-5/2}e^{-x/2}.
\]

After retaining `E` as a separate modular endpoint coordinate, Poisson
summation leaves only nonzero dual modes, which are exponentially decreasing
as `x -> -infinity`; the original Gaussian estimate controls `x -> +infinity`.
Thus the renormalized bulk candidate is

\[
\Phi_x^{\rm bulk}(t)=\Phi_x(t)-E_x(t).
\]

A complete graph theorem still requires directed bounds for the Poisson
remainder and its `x,t` derivatives, but the obstruction and the unique leading
counterterm are explicit.

This corrects the earlier expectation that subtracting only the base value at
`t=0` could produce a whole-line history-valued jet.  The completed sum needs a
`t`-dependent modular boundary line.
