# Self-adjoint linearization is equivalent to real-rootedness unless source-derived

## Bounded question

Does the existence of a divisor-preserving self-adjoint linearization add
independent force to the theta cross-transfer problem?

## Finite bordered numerator

Let \(A=A^*\) be an \(n\)-dimensional carrier and let \(b_0,b_f\) be the
endpoint and source ports. Define

\[
F(z)=b_f^*(A-zI)^{-1}b_0
\]

and its polynomial numerator

\[
p(z)=-\det(A-zI)F(z).
\]

The bordered determinant identity gives

\[
p(z)=
\det
\begin{pmatrix}
0&b_f^*\\
b_0&A-zI
\end{pmatrix}.
\]

After cancellation of common carrier factors, \(p\) is precisely the finite
cross-transfer divisor.

## Arbitrary self-adjoint realization criterion

Suppose there are a finite self-adjoint matrix \(H\) and a nowhere-zero entire
function \(u\) such that

\[
p(z)=u(z)\det(H-zI).
\]

Every zero of \(\det(H-zI)\) is real. Since \(u\) has no zeros, every zero of
\(p\) is real.

Conversely, if \(p\) has only real zeros, then after removing its nonzero
constant factor one can place those zeros, with multiplicity, on the diagonal
of a self-adjoint matrix \(H_p\). A constant unit then gives

\[
p(z)=u\det(H_p-zI).
\]

Therefore a divisor-preserving self-adjoint linearization exists if and only
if \(p\) is real-rooted, when the linearization may be manufactured after
\(p\) is known.

This equivalence is the finite analogue of the Hilbert--Polya circularity
test. Existence alone supplies no explanation of real-rootedness. The operator
must be derived from source constructors before the divisor is inspected.

## The noncircular collocated case

If the two ports are positively collocated,

\[
b_f=c\,b_0,
\qquad
c>0,
\]

then

\[
F(z)=c\,b_0^*(A-zI)^{-1}b_0
\]

is a scalar Herglotz or anti-Herglotz function, depending on the resolvent
convention. Its poles are real, its residues have one sign, and its finite
zeros are real and interlace the carrier poles after removal of invisible
eigenspaces.

Here real-rootedness follows from an independently typed positive spectral
measure. It is not imported by constructing \(H_p\) from the zeros.

The theta ports are not collocated:

\[
b_0=\delta_0,
\qquad
b_f=f.
\]

The previously established local-metric obstruction shows that a positive
local \(L^2\) weight cannot identify source forcing with endpoint evaluation.
Thus the shortest Herglotz proof is unavailable in the native carrier metric.

## Positive-metric symmetrization gate

A broader noncircular route would derive a positive metric operator \(G\)
before zero inspection such that

\[
GA=A^*G
\]

and the two ports become adjoint in the \(G\)-metric. This would turn the cross
transfer into a diagonal matrix coefficient of a source-derived self-adjoint
system.

But choosing \(G\) from \(p\), from its zeros, or from a desired Bezoutian is
the same circularity in another coordinate. Source authority must come from
theta/Tate transport, seam incidence, or a completed graph energy.

## Relation to the resistance route

Effective resistance can optimally control an anchored normalization unit once
the source supplies:

1. the incidence graph;
2. positive conductances;
3. the anchored field;
4. the Green or Clark energy represented by that graph.

It cannot by itself identify the source port with the endpoint port or create
the required metric. Hence the resistance estimate is a downstream closure
certificate, not the missing linearization constructor.

## Result

The phrase “construct a self-adjoint operator with the theta-zero spectrum” is
not yet a research mechanism. At finite cutoff it is equivalent to proving
that the bordered numerator is real-rooted, unless the operator and its metric
are derived independently from the labelled source.

The live source theorem is now narrower:

> Derive a positive theta/Tate metric or boundary correspondence that
> collocates the source and endpoint ports before scalar compression.

If no such correspondence exists, the bordered determinant remains the
faithful non-self-adjoint transmission section.

## Sharp falsifiers

A proposed linearization fails source authority if any of the following is
true:

- its matrix entries depend on zeros of \(p\);
- its metric is solved backward from the desired Bezoutian;
- it replaces \(b_f\) by \(b_0\) without a source correspondence;
- it uses effective resistance before deriving the graph energy;
- its determinant agrees only after multiplication by an unproved
  zero-free unit.
