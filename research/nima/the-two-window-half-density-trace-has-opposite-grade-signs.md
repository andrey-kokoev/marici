# The two-window half-density trace has opposite grade signs

## Gradewise split

The four-front adjacent-window packet splits canonically by displacement:

\[
b_p=b_p^{(2)}+b_p^{(1)},
\]

with

\[
b_p^{(2)}=U_{-2L}f_0-U_{2L}f_0,
\]

and

\[
b_p^{(1)}=-U_{-L}f_0+U_Lf_0.
\]

The superscripts record Adams grades, not powers of the vectors.

For the odd translated Gaussian pair

\[
q_a:=U_{-a}f_0-U_af_0,
\]

the half-density moments are

\[
M_+(q_a)=2e^{1/(16\pi)}\sinh\frac a2,
\]

\[
M_-(q_a)=-2e^{1/(16\pi)}\sinh\frac a2.
\]

Hence

\[
j_{1/2}(q_a)
=2\sqrt2e^{1/(16\pi)}\sinh\frac a2>0.
\]

Applying this to the two grades gives

\[
\boxed{
j_{1/2}(b_p^{(2)})
=2\sqrt2e^{1/(16\pi)}\sinh L>0,
}
\]

but

\[
\boxed{
j_{1/2}(b_p^{(1)})
=-2\sqrt2e^{1/(16\pi)}\sinh\frac L2<0.
}
\]

Their sum is the previously computed positive value

\[
j_{1/2}(b_p)
=2\sqrt2e^{1/(16\pi)}
\left(\sinh L-\sinh\frac L2\right)>0.
\]

## Arithmetic grade signs

The Euler-to-theta components satisfy

\[
\kappa_p^{(1)}
=2Lp^{-1/2}\Phi'(L)<0,
\]

\[
\kappa_p^{(2)}
=2Lp^{-1}\Phi'(2L)<0.
\]

The frozen Wronskian readout therefore gives

\[
-\frac12\kappa_p^{(1)}>0,
\qquad
-\frac12\kappa_p^{(2)}>0.
\]

Thus, with the current common orientation convention, the gradewise sign
profiles are

\[
\text{boundary half-density trace}:\quad(-,+),
\]

\[
\text{arithmetic Wronskian output}:\quad(+,+).
\]

## Obstruction to a common positive mate

There cannot be one positive scalar \(\lambda_p\) satisfying both labelwise
mate identities

\[
\lambda_pj_{1/2}(b_p^{(1)})
=-\frac12\kappa_p^{(1)},
\]

\[
\lambda_pj_{1/2}(b_p^{(2)})
=-\frac12\kappa_p^{(2)}.
\]

The first equation forces \(\lambda_p<0\), while the second forces
\(\lambda_p>0\).

Even allowing separate grade scalars gives opposite signs:

\[
\lambda_{p,1}
=\frac{-\kappa_p^{(1)}}{2j_{1/2}(b_p^{(1)})}<0,
\]

\[
\lambda_{p,2}
=\frac{-\kappa_p^{(2)}}{2j_{1/2}(b_p^{(2)})}>0.
\]

Therefore the positive scalar obtained after summing grades hides a genuine
labelwise orientation mismatch.  Scalar equality after grade erasure cannot
prove the constructor mate square.

## Required repair

A valid source theorem must supply one of the following, and must say which:

1. a grade-one orientation local system contributing an additional minus sign;
2. an arithmetic incidence convention in which the first-grade coefficient
   carries the window boundary sign;
3. a constructor matrix that is diagonal with the forced sign pattern
   \((-1,+1)\), rather than a common scalar;
4. a different source-derived boundary packet whose gradewise signs match the
   Euler/Wronskian outputs.

None of these may be inserted merely to repair the equation.  It must follow
from the frozen first-Adams constructor, reciprocal sheet convention, or
Hadamard/Wronskian transport.

## Revised earliest gate

The earliest local gate is now sharper than “prove the arithmetic mate
square”:

> Identify the source-authorized grade-one orientation twist, or prove that no
> such twist exists.

Until that sign is derived, the summed candidate normalization
\(-\kappa_p^{(\le2)}/(2s_p^{(1/2)})\) is not constructor-faithful.  The
conditional determinant estimates remain algebraically valid for any proposed
linking magnitude, but they do not resolve this gradewise mismatch.

The connected \(k\ge3\) tail, radical descent, and global closed range remain
open.  No RH conclusion is authorized.
