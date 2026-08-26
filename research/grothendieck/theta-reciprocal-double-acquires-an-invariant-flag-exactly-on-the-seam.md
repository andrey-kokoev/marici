# Theta reciprocal double acquires an invariant flag exactly on the seam

## Bounded question

Does the simplest reciprocal doubling convert the two source-forcing
residuals into one invariant adjoint flag?

## Reciprocal-conjugate tail double

Use the centered parameter

\[
z=s-\frac12.
\]

In the real reflected tail frame, take

\[
G_{+,q}=-zG_+-f(q)c,
\]

and

\[
G_{-,q}=\bar zG_--f(q)c.
\]

After identifying the common constant channel, set

\[
X=
\begin{pmatrix}
G_+\\
G_-\\
c
\end{pmatrix},
\qquad
K_z(q)=
\begin{pmatrix}
-z&0&-f(q)\\
0&\bar z&-f(q)\\
0&0&0
\end{pmatrix}.
\]

This is the smallest reciprocal double retaining both spectral orientations
and the shared source forcing.

## Constant invariant covector equations

Let

\[
\ell=\begin{pmatrix}a&b&d\end{pmatrix}.
\]

Then

\[
\ell K_z(q)
=
\begin{pmatrix}
-az&
b\bar z&
-(a+b)f(q)
\end{pmatrix}.
\]

For \(\ell K_z=\alpha\ell\) with both sheets visible, \(a\ne0\) and \(b\ne0\),
the first two coordinates require

\[
\alpha=-z=\bar z.
\]

Therefore

\[
z+\bar z=0,
\]

which is exactly

\[
\operatorname{Re}z=0
\qquad\Longleftrightarrow\qquad
\operatorname{Re}s=\frac12.
\]

## Forcing cancellation selects the antisymmetric sheet

Because \(f(q)\) is not constant, a constant invariant covector must also
remove its coefficient. Thus

\[
a+b=0.
\]

Away from the spectral center, the remaining equation forces \(d=0\). Up to
scale, the unique two-sheet covector is therefore

\[
\ell_{\mathrm{rel}}
=
\begin{pmatrix}
1&-1&0
\end{pmatrix}.
\]

On the seam it satisfies

\[
\ell_{\mathrm{rel}}K_z
=
-z\ell_{\mathrm{rel}}.
\]

The relative sheet difference cancels the common forcing and evolves
multiplicatively exactly on the critical line.

## Interpretation

The critical seam is not selected by the zeros. It is selected by a
representation-theoretic coincidence:

- the direct and reciprocal spectral weights become equal;
- the antisymmetric sheet coordinate cancels shared forcing;
- a common invariant adjoint line appears;
- the two local descriptions acquire one multiplicative relative readout.

The offset \(1/2\) is the centering required for reciprocal conjugation to take
the weights \(-z\) and \(\bar z\). Their equality is the vertical critical
line.

This is a precise version of the two-sector fold intuition. The line is where
the relative coordinate gains invariant meaning.

## Why this is not RH

The invariant relative flag exists on the seam, not throughout the open
half-planes. It explains why the seam is canonical but does not prove that the
original scalar cannot cross its incidence divisor away from the seam.

For off-seam confinement, the completed source must provide separate
sectorwise flags or additional boundary-current coordinates whose residuals
absorb the mismatch

\[
z+\bar z=2\operatorname{Re}z.
\]

That mismatch is the same coefficient appearing in the doubled Green-energy
identity. The flag and conservation formulations are therefore two shadows of
one reciprocal-weight obstruction.

## Result

The naive reciprocal double does produce a source-derived invariant adjoint
flag, but only on the critical seam. Its unique generic form is the
antisymmetric sheet difference. This gives a direct explanation of why
\(\operatorname{Re}s=1/2\) is the special line:

> It is the locus where reciprocal spectral weights coalesce and shared
> forcing becomes invisible to the relative sheet coordinate.

The remaining RH theorem is sectorwise open-cell confinement away from that
coalescence locus.

## Sharp falsifier

For the declared reciprocal double, any claimed constant common invariant
covector with \(a,b\ne0\) off the seam must satisfy both

\[
\alpha=-z
\]

and

\[
\alpha=\bar z.
\]

Their incompatibility when \(\operatorname{Re}z\ne0\) is the exact finite
falsifier. Extra source channels help only if their independently derived
incidence changes these adjoint-weight equations.
