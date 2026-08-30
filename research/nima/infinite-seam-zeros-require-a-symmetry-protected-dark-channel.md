# Infinite seam zeros require a symmetry-protected dark channel

The scalar Feshbach formula exposes a codimension problem.

A full seam zero requires
\[
a(x)=0,
\qquad
b(x)=0,
\]
where \(a\) is the dark reactive phase and \(b\) is the dark-to-radiative coupling.

For a real parameter \(x\), these are generically more than one real condition. An infinite discrete sequence of simultaneous solutions would require unexplained fine tuning unless the source geometry forces
\[
b(x)\equiv0
\]
on the seam.

The natural protection is reciprocal exchange symmetry. Let
\[
R_{\partial}^{2}=I
\]
act on the two-dimensional boundary space, with

- \(+1\) eigenspace equal to the coherent radiative line;
- \(-1\) eigenspace equal to the disagreement dark line.

If both the radiation form and reactive operator commute with \(R_{\partial}\),
\[
[R_{\partial},W(x)]=0,
\qquad
[R_{\partial},F(x)]=0,
\]
then the parity sectors do not mix. In the dark/radiative frame,
\[
b(x)=0
\]
identically.

The Evans determinant then factorizes exactly:
\[
\det A(x)
=
a(x)\bigl(c(x)-iw(x)\bigr).
\]
Since the radiative factor is zero-free, the completed divisor is the single real seam equation
\[
a(x)=0.
\]

This is the robust one-parameter zero mechanism:

- reciprocal parity protects the dark channel;
- the radiative sector remains strictly open;
- the dark reactive phase crosses zero at discrete ordinates;
- crossing multiplicity is the order of \(a(x)\).

The symmetry must hold for the complete source operator, including archimedean and wall attachments. Prime-diagonal propagation alone may commute with sheet exchange while endpoint loading breaks it.

There is also a weaker protected regime. If an antiunitary reciprocal symmetry sends
\[
b(x)\mapsto-b(x),
\]
then at fixed points of the symmetry one may obtain \(b(x)=0\). But the critical seam is a continuum of fixed spectral parameters, so the operator-level parity law is the clean target.

This refines the earlier mixed-cancellation margin. Off seam, coherent and disagreement channels can couple through analytic continuation while remaining contractive. On seam, self-adjoint reciprocal symmetry must block their reactive mixing exactly.

The source theorem should establish:

1. a boundary involution \(R_{\partial}\) derived from reciprocal-sheet exchange;
2. rank-one radiation supported on the coherent eigenspace;
3. seam reactive covariance
   \[
   R_{\partial}F(x)R_{\partial}=F(x);
   \]
4. strict positivity \(w(x)>0\) on the coherent sector;
5. an independently derived dark scalar
   \[
   a(x)=\langle d,F(x)d\rangle;
   \]
6. analytic continuation of the factorization to the Evans section.

The smallest hostile obtains infinitely many common zeros of \(a\) and \(b\) numerically at finite cutoff but has no symmetry forcing \(b=0\). Small completion perturbations destroy the sequence.

A second hostile proves reciprocal covariance for the bulk but not for the archimedean endpoint block. The endpoint produces a small \(b(x)\neq0\), turning every claimed seam zero into a leaky resonance.

A third hostile sets \(b=0\) by choosing the dark basis from \(F(x)\) at each \(x\). This moving diagonalization need not align with \(\ker W(x)\) and has no fixed source parity.

Thus the next exact finite test is a commutator:
\[
[R_{\partial},F_X(x)]
\stackrel{?}{=}0
\]
for the complete cutoff boundary return. If it vanishes source-exactly and survives completion, the RH divisor reduces to one protected scalar dark phase.
