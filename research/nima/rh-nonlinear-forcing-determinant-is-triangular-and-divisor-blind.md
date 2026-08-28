# The Nonlinear Forcing Determinant Is Triangular and Divisor-Blind

## Question

Does the canonical tangent determinant of the exact nonlinear theta forcing
connection provide the missing determinant-line character with its source
unit fixed?

## Claim boundary

Consider the exact source system

\[
y'=2y,
\qquad
f'=-2\pi yf.
\]

Its interval map is

\[
y_1=y_0e^{2\ell},
\qquad
f_1=f_0
\exp\left[-\pi y_0(e^{2\ell}-1)\right].
\]

The Jacobian determinant of this map is

\[
\det D\Phi_\ell
=
e^{2\ell}
\exp\left[-\pi y_0(e^{2\ell}-1)\right].
\]

Equivalently, the variational connection obeys Liouville's law

\[
\partial_x\log\det D\Phi
=
2-2\pi y.
\]

This is a canonical multiplicative character of the nonlinear source flow.
Its unit is fixed and its transport is everywhere nonzero.

## Coupling the reciprocal tails does not change the determinant connection

Adjoin the exact moving-endpoint tail system

\[
m'=-\frac12m-zn-f,
\qquad
n'=-zm-\frac12n.
\]

In the state order $(y,f,m,n)$, the vector-field Jacobian is

\[
\mathcal J=
\begin{pmatrix}
2&0&0&0\\
-2\pi f&-2\pi y&0&0\\
0&-1&-1/2&-z\\
0&0&-z&-1/2
\end{pmatrix}.
\]

It is block lower triangular, with

\[
\operatorname{Tr}\mathcal J=1-2\pi y.
\]

The trace is independent of $z$ and of the forcing incidence from $f$ to
$m$. Therefore the tangent determinant of the coupled nonlinear source flow
is blind to the reciprocal characteristic interaction.

Adjoining the accumulated current

\[
Y'=2\sqrt yfm
\]

adds another feed-forward row and a zero diagonal entry. The enlarged
Jacobian remains lower triangular and has the same trace. The current is now
retained as a state coordinate, but it still does not enter the determinant.

## Finite falsifier

Delete the forcing incidence from $f$ to $m$, or replace its coefficient by
an arbitrary scalar. The Jacobian trace and tangent determinant remain
unchanged. Hence this determinant cannot certify the source coupling whose
loss changes the Green and Schur boundary response.

The determinant is canonical, normalized, compositional, and zero-free. It is
nevertheless the wrong determinant line for RH because it sees only diagonal
volume change in a feed-forward source system.

## Required new operation

The endpoint current can affect a characteristic determinant only through a
return operation that closes a loop. Categorically, the present source graph
has arrows

\[
(y,f)\longrightarrow(m,n)\longrightarrow Y
\]

and no source-derived arrow returning from $Y$ to either the tail generator or
a boundary characteristic port.

A new feedback arrow makes the generator nontriangular and permits the current
to enter a Schur complement or spectral characteristic determinant. It does
not by itself change the tangent-flow determinant, which depends only on the
Jacobian trace. Its existence, sign, normalization, dagger covariance, and
completion domain are all unresolved.

## Disposition

Negative for the ordinary nonlinear tangent determinant; progressive for
typing the missing operation. Passing from the infinite linear jet tower to
the exact nonlinear source connection fixes the character unit but does not
create RH-bearing feedback. The remaining object is a source-derived
current-to-boundary return operation, not another determinant normalization.

## Tangent and characteristic determinants separate

Freeze the source coefficients and retain the symmetric tail channel, the
antisymmetric channel, and one boundary-current amplitude. The smallest
reciprocal feedback generator has the form

\[
K_\alpha=
\begin{pmatrix}
-1/2&-z&\alpha\\
-z&-1/2&0\\
g&0&0
\end{pmatrix}.
\]

The boundary current reads the reciprocal-even channel through $g$, while
$\alpha$ returns it to the same channel. Reciprocal covariance forbids a
constant return into the odd channel but permits every scalar $\alpha$ in the
even channel.

The trace is

\[
\operatorname{Tr}K_\alpha=-1,
\]

independent of $\alpha$, $g$, and $z$. Therefore Liouville's tangent-volume
determinant remains blind to the feedback loop.

The spectral characteristic polynomial is different. With

\[
a=\lambda+\frac12,
\]

one obtains

\[
\det(\lambda I-K_\alpha)
=
\lambda(a^2-z^2)-\alpha ga.
\]

The closed-loop product $\alpha g$ is visible. The cases $\alpha=0$ and
$\alpha=1$ have identical tangent determinant connection and different
spectral divisors whenever $ga$ is nonzero.

This distinguishes two determinant functors that had been conflated:

- the tangent determinant records infinitesimal volume transport;
- the characteristic determinant records closed input-output loops.

RH-strength content can reside only in the second type. Constructing a
canonical zero-free tangent determinant does not orient or constrain the
characteristic divisor.

Reciprocity still does not select $\alpha$. Dagger covariance reduces a
constant feedback coefficient to a real value, but distinct real values yield
different characteristic polynomials. The exact remaining source question is
which boundary operation constructs the feedback coefficient rather than
which determinant convention normalizes it.

## The source supplies an open input-output colligation

The moving-endpoint equation already contains a distinguished source input.
Write

\[
v=\begin{pmatrix}m\\n\end{pmatrix},
\qquad
v'=Av+Bc,
\]

with

\[
A=\begin{pmatrix}-1/2&-z\\-z&-1/2\end{pmatrix},
\qquad
B=-f\begin{pmatrix}1\\0\end{pmatrix}.
\]

The theta tail uses the normalized source channel $c=1$. Let

\[
J=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]

The Lorentz relation satisfies

\[
A^TJ+JA=-J.
\]

Its energy-conjugate output is forced to be

\[
o=Cv,
\qquad
C=-B^TJ=f(1,0).
\]

Consequently

\[
\partial_x(v^TJv)+v^TJv=-2co.
\]

This is an exact open-system supply law. The return row is the output port
dual to the source forcing under the source-selected Lorentz form, not an
arbitrary feedback coefficient.

## The transfer determinant sees the source coupling

Let $E$ be the direct boundary channel. The transfer Schur function is

\[
S(\lambda,z)=E-C(\lambda I-A)^{-1}B.
\]

With

\[
a=\lambda+\frac12,
\]

the exact expression is

\[
S(\lambda,z)=E+\frac{f^2a}{a^2-z^2}.
\]

The bordered characteristic determinant is

\[
\det\begin{pmatrix}\lambda I-A&B\\C&E\end{pmatrix}
=E(a^2-z^2)+f^2a.
\]

Unlike the tangent determinant, this object sees the forcing through the
closed input-output product. It is reciprocal-even and its normalization is
fixed by the source forcing and Lorentz supply law.

Rescaling the input port by a nonzero scalar and the output port by its inverse
leaves the transfer function unchanged. The remaining port-frame freedom does
not reintroduce the earlier gain ambiguity.

The local source now supplies the reciprocal tail generator $A$, forcing input
$B$, and Lorentz-dual output $C$. The unresolved datum is the direct boundary
channel $E$, together with the composition and completion law for the local
colligations.

This does not prove zero confinement. Different source-compatible direct
channels change the local divisor, and the actual forcing varies along the
interval. The theorem establishes the first source-normalized
determinant-visible loop, not its completed RH identification.

## A scalar conservative termination is mistyped

The preceding Lorentz balance determines the response dual to the forcing,
but it is not a positive scattering balance.  To test a positive conservative
termination, return to the reciprocal tail in a positive state metric and
write

\[
z=r+it,
\qquad
A=-\frac12I-z\sigma_x.
\]

Its dissipative defect is

\[
Q=-(A^*+A)=I+2r\sigma_x.
\]

Inside the open critical strip, $|r|<1/2$, this matrix is positive definite
and has rank two.  A continuous-time lossless realization with scalar input
$c$ and output $y=Cv+Dc$ must satisfy

\[
C^*C=Q,
\qquad
B=-C^*D,
\qquad
D^*D=1.
\]

A scalar output cannot satisfy the first identity because $C^*C$ would have
rank at most one.  Thus the direct boundary datum is not one scalar $E$ once
positive conservative completion is requested.  At least two response
directions are required.

For a two-dimensional output, $C$ is invertible.  The other two identities
then impose the exact compatibility condition

\[
B^*Q^{-1}B=1.
\]

With the source column $B=-f(1,0)^T$, this becomes

\[
\frac{|f|^2}{1-4r^2}=1.
\]

The theta forcing does not obey this identity throughout the interval and
strip.  Hence even a two-output lossless termination is exceptional rather
than canonical.

If a third output direction is admitted, the equation $C^*D=-B$ has a
minimum-norm solution of squared norm

\[
\rho(r,f)=\frac{|f|^2}{1-4r^2}.
\]

An orthogonal slack component can complete $D$ to unit norm exactly when
$\rho\leq1$.  The slack magnitude is $\sqrt{1-\rho}$.  When $\rho>1$, no
positive conservative output enlargement with the frozen input
normalization exists; an additional input reservoir or a different source
metric is necessary.

This provides a finite source-local classification:

- one output is rejected by rank;
- two outputs work only on the equality locus $\rho=1$;
- three outputs work on the contractive region $\rho<1$;
- the region $\rho>1$ requires an additional input or an indefinite
  completion.

The missing direct channel has therefore resolved into a typed defect-space
problem.  It is not a freely chosen scalar feedback coefficient.  The next
global construction must identify the two response characters and any slack
reservoir with the seam, primitive, square, and archimedean boundary grades.
Merely selecting $E$ cannot produce a conservative completed colligation.
