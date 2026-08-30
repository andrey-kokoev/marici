# The staircase Green identity does not turn a zero into an adjoint state

## Bounded question

Does the independent prime-power staircase readout provide a Green identity
that forces every summability-upgraded zero state to satisfy the reciprocal
adjoint boundary law?

## Staircase current

Let (W) be a right-continuous prime-power staircase with positive jumps
(a_j) at (ell_j>0):

\[
dW=\sum_j a_j\delta_{\ell_j}.
\]

For a positive rapidly decaying half-line source (A), define

\[
I_W(z)
=
-\int_0^\infty W(v)A(v)e^{izv}\,dv.
\]

Assume (W(0)=0). The decay of (A) removes the endpoint at infinity.
Stieltjes integration by parts gives

\[
\int_0^\infty W(v)A'(v)e^{izv}\,dv
=
-\sum_j a_jA(\ell_j)e^{iz\ell_j}
+izI_W(z).
\]

Equivalently,

\[
izI_W(z)
=
\int_0^\infty W(v)A'(v)e^{izv}\,dv
+\sum_j a_jA(\ell_j)e^{iz\ell_j}.
\]

This is the exact Green identity for the centered staircase port. The jump
term is the labelled prime-power boundary current.

## The scalar zero is absent

The completed scalar readout is

\[
X(z)
=
\int_0^\infty A(v)
\left[e^{izv}+e^{-izv}\right],dv.
\]

Neither the staircase Green identity nor its reciprocal copy contains a factor
forcing (I_W) to vanish when (X) vanishes. The two functionals have
different source multipliers, (1) and (W), and are linearly independent
whenever (W) is nonconstant.

## Exact positive off-seam witness

Take the positive even two-shell measure with half-line atoms at (v=1,2):

\[
A=a\delta_1+b\delta_2,
\qquad
a,b>0.
\]

Choose

\[
z=\pi+iy,
\qquad
y\ne0,
\]

and

\[
b=a\frac{\cosh y}{\cosh 2y}.
\]

Then

\[
X(z)
=
2\left[-a\cosh y+b\cosh 2y\right]
=0.
\]

The point is off the real (z)-axis and hence off the critical seam. For a
nonconstant staircase,

\[
I_W(z)
=
-aW(1)e^{iz}-bW(2)e^{2iz}
\]

is generically nonzero. Its reciprocal value uses (-z), while its adjoint
uses (-\overline z); these differ because (y\ne0).

The atoms may be replaced by sufficiently narrow positive even bumps. The
zero and the failure of adjointness persist after a small parameter adjustment,
so the obstruction is not an artifact of distributions.

## Result

Positivity, a scalar zero, completion-safe staircase incidence, and the exact
Green identity do not imply reciprocal adjointness. The proposed extension
theorem cannot be derived from those ingredients alone.

This closes a possible circular shortcut. Declaring that every zero-induced
state is star-compatible would already exclude the hostile witness for the
same reason it would imply RH. Source authority must supply an additional
theta-specific coupling before the zero is inspected.

## Remaining target

The next admissible question is narrower:

> Which exact relation between the Gaussian heat flow and the arithmetic
> staircase holds for the theta source but fails for the positive two-shell
> witness?

The relation must involve both (A) and the jumps of (W), not merely their
separate positivity or transforms. It must also imply star-compatible
extension at a zero rather than assume it.
