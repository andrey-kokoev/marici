# The quarter shift ratio reduces to adjacent LU quotients

## Question

What parameter-uniform asymptotic would prove

\[
\frac{S_m(\mathbf s_0+1)^2}
{m^2S_m(\mathbf s_0)S_m(\mathbf s_0+2)}
\to\frac{104}{1575}?
\]

Define the adjacent common-shift quotient

\[
H_m(t)=rac{S_m(\mathbf s_0+t+1)}{S_m(\mathbf s_0+t)}.
\]

Then the required ratio factors exactly as

\[
rac{S_m(\mathbf s_0+1)^2}
{S_m(\mathbf s_0)S_m(\mathbf s_0+2)}
=rac{H_m(0)}{H_m(1)}.
\]

Therefore it is enough to prove parameter-uniform asymptotics

\[
H_m(t)=h(t)m^{\lambda(t)}(1+o(1))
\]

at \(t=0,1\), with

\[
\lambda(0)-\lambda(1)=2,
\qquad
\frac{h(0)}{h(1)}=rac{104}{1575}.
\]

Because \(S_m\) is a determinant, \(H_m(t)\) is also the product of adjacent-parameter ratios of its LU pivots. This replaces a difference of four large free energies by a single family of local pivot quotients.

## Disposition

Resolve the shift-ratio proof target to exponent difference two and amplitude ratio \(104/1575\) for adjacent LU quotients. The next leaf is `quarter-staircase-lu-pivot-shift`: derive a recurrence or product representation for those pivot quotients.

## Claim boundary

The factorization is exact but supplies neither asymptotic. Reusing the degree-eighteen fit that proposed \(13/60\) would be circular; the pivot asymptotic must be derived independently.
