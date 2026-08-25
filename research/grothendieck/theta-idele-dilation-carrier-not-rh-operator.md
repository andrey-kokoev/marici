# The idele dilation generator is canonical but is not the RH operator

## 1. Source-derived generator

The adelic Schrödinger representation carries a canonical multiplicative
action. For an idele \(a\in\mathbb A^\times\), set

\[
  (R_af)(x)=|a|_{\mathbb A}^{1/2}f(ax).
\]

With Haar measure fixed, \(R_a\) is unitary and

\[
  R_aR_b=R_{ab}.
\]

Restricting to the positive archimedean one-parameter subgroup
\(a_\tau=(e^\tau,1,1,\ldots)\) gives a strongly continuous unitary group.
Stone's theorem therefore supplies a canonical self-adjoint generator
\(K\):

\[
  R_{a_\tau}=e^{-i\tau K}.
\]

In the real Schrödinger chart its formal differential expression is the
logarithmic dilation operator

\[
  K=-i\left(x\partial_x+\tfrac12\right),
\]

or \(-i\partial_u\) after \(u=\log|x|\). Thus the generator is derived from
source transport rather than manufactured from \(\xi\).

## 2. The completed readout

The rational comb and a chosen adelic vacuum \(f\) produce theta through a
distributional matrix coefficient,

\[
  \Theta_f(\tau)
  =
  \langle\Delta_{\mathbb Q},R_{a_\tau}f\rangle.
\]

Mellin transformation and the endpoint completion turn this orbit readout
into the completed zeta scalar. Schematically,

\[
  X(z)
  =
  \mathcal M_\tau
  \langle\Delta_{\mathbb Q},e^{-i\tau K}f\rangle(z)
  +\text{typed endpoint terms}.
\]

This construction explains the functional equation through Fourier rotation
and reciprocal dilation.

## 3. Decisive distinction

Although \(K\) is self-adjoint, \(X(z)\) is not thereby its characteristic
determinant. It is a transformed matrix coefficient involving a
distributional observation boundary and a vacuum.

Self-adjointness controls the spectral support of \(K\), but it does not force
the complex zeros of an arbitrary matrix coefficient or of its Mellin
transform onto the real spectral axis. Even positive-definite real-time
coefficients can have analytic continuations with zeros away from that axis.

\[
\boxed{
K=K^*
\quad\not\Longrightarrow\quad
\text{zeros of }
\mathcal M\langle\Delta,e^{-i\tau K}f\rangle
\text{ are spectral}.}
\]

This closes a potential Hilbert--Pólya shortcut.

## 4. The missing incidence map

To turn a zero of \(X\) into a forbidden nonreal eigenvalue, one needs an
independently derived construction

\[
  X(z)=0
  \quad\Longleftrightarrow\quad
  L_z\cap L_{\mathrm{arith}}\ne0,
\]

where \(L_z\) is the Cauchy-data relation of a symmetric operator and
\(L_{\mathrm{arith}}\) is a maximal self-adjoint boundary relation.

Equivalently, one needs a relative Fredholm determinant

\[
  X(z)=u(z)\det_{\mathrm{rel}}(T_z),
  \qquad u(z)\ne0,
\]

with \(T_z\) derived from the Weyl carrier, comb, vacuum, and dilation action
before \(X\) is evaluated.

The matrix coefficient supplies the scalar numerator; it does not supply
this incidence typing.

## 5. Revised hard-to-vary conjecture

**Overlap-to-incidence conjecture.** The completed theta matrix coefficient
is the boundary pairing of two source-derived Cauchy-data relations, and its
vanishing is exactly their loss of transversality. The rational Weyl fixed
line determines one relation; reciprocal dilation determines the other.
Their Green form is the adelic product character, and the arithmetic relation
is maximal self-adjoint.

The conjecture is stronger than self-adjointness of the carrier and weaker
than inserting the zeros as spectrum. Its decisive construction is the
boundary trace that turns the distributional overlap into a Fredholm
incidence determinant.

## 6. Smallest hostile test

Keep the same self-adjoint dilation generator \(K\), Weyl representation, and
rational comb, but replace the vacuum by another Fourier-stable analytic
state in the common core. If the resulting matrix coefficient acquires
off-line zeros, then carrier self-adjointness and comb rigidity remain intact.
Any proposed overlap-to-incidence functor must reject that vacuum through a
source condition visible before locating its zeros.

This identifies the remaining special datum: not the carrier alone, and not
the arithmetic boundary alone, but their completed theta vacuum coupling.

## 7. Scope

The unitary idele action and its self-adjoint logarithmic generator are
standard consequences of Haar covariance and Stone's theorem. The
matrix-coefficient distinction is exact. No overlap-to-incidence functor,
Fredholm determinant identity, maximal arithmetic boundary, or RH theorem is
constructed here.
