# A Rosenbrock determinant needs minimality or a reduced Fitting invariant

## Presentation obstruction

A transfer readout can have many state-space realizations. Adding an internal
mode that is neither reached by the input nor seen by the output leaves the
transfer function unchanged.

The raw Rosenbrock determinant does change.

## Minimal example

Start with

\[
A=0,
\qquad
B=1,
\qquad
C=-a,
\qquad
D=1.
\]

The transfer function is

\[
G(s)=\frac{s-a}{s},
\]

and the Rosenbrock determinant is \(s-a\).

Now adjoin a hidden internal mode with eigenvalue \(h\):

\[
A_h=
\begin{pmatrix}
0&0\\
0&h
\end{pmatrix},
\qquad
B_h=
\begin{pmatrix}
1\\
0
\end{pmatrix},
\qquad
C_h=
\begin{pmatrix}
-a&0
\end{pmatrix}.
\]

The transfer function remains exactly \((s-a)/s\), because the new mode is
uncontrollable and unobservable. But the enlarged Rosenbrock determinant is

\[
(s-h)(s-a).
\]

It contains a spurious zero at \(s=h\) that is absent from the transfer
readout.

## Required gate

An Evans determinant can represent the completed scalar divisor only after one
of the following is proved:

1. the realization is minimal, with no uncontrollable or unobservable modes;
2. hidden factors are divided out by a source-authorized coprime reduction;
3. the divisor is defined through a presentation-invariant Fitting ideal or
   determinant-line construction.

Arbitrary cancellation after inspecting the scalar transfer function is not
source authorization.

## Finite tests

At each cutoff, verify:

- controllability of \((A,B)\);
- observability of \((C,A)\);
- PBH rank at every internal eigenvalue;
- invariance under source-authorized state similarity;
- stability under adding a contractible state pair;
- agreement between the reduced system divisor and the scalar readout.

In the completed setting, finite minimality is not enough. A mode can become
asymptotically uncontrollable or unobservable, so uniform graph-norm versions
of the PBH gates are required.

## Theta/Tate consequence

The tail, seam, primitive, square, endpoint, and archimedean states must be
retained until their reachability and observability are typed. A raw block
determinant cannot be identified with \(\Xi\) merely because its Schur
complement resembles the scalar readout.

The smallest falsifier is an admitted hidden state whose addition changes the
proposed Evans determinant while leaving every source transfer measurement
unchanged.

