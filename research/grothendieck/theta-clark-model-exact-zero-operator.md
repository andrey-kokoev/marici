# The source transfer has a canonical Clark operator with the Xi-zero spectrum

Status: exact conditional operator construction; contractivity remains RH

Let

\[
 X(z)=\xi(1/2+iz),
 \qquad
 E(z)=X(z)+iX'(z),                                    \tag{1}
\]

and define directly from the fixed theta contour

\[
 \Theta(z)=\frac{E^*(z)}{E(z)}
 =\frac{X(z)-iX'(z)}{X(z)+iX'(z)}.                   \tag{2}
\]

No factorization or zero list enters (2).

## The Clark denominator is a one-fold theta transform

On the faithful bilateral contour use

\[
 X(z)=\frac12\int_{\mathbb R}\Phi(u)e^{izu}\,du,
 \qquad
 X'(z)=\frac{i}{2}\int_{\mathbb R}u\Phi(u)e^{izu}\,du.
\]

Then

\[
 \boxed{
 E(z)=X(z)+iX'(z)
 =\frac12\int_{\mathbb R}(1-u)\Phi(u)e^{izu}\,du,
 }                                                     \tag{3a}
\]

and

\[
 \boxed{
 E^*(z)=X(z)-iX'(z)
 =\frac12\int_{\mathbb R}(1+u)\Phi(u)e^{izu}\,du.
 }                                                     \tag{3b}
\]

Because `Phi(u)>0`, the density `(1-u)Phi(u)` has exactly one sign transition,
at `u=1`.  The numerator density is its reflected partner.  Consequently

\[
 \Theta(z)=
 \frac{\int(1+u)\Phi(u)e^{izu}du}
      {\int(1-u)\Phi(u)e^{izu}du}.                    \tag{3c}
\]

This exposes a genuine one-defect geometry behind the Clark model.  The fold
*position* is a normalization, not an arithmetic invariant: more generally

\[
 E_a=X+iaX'
 =\frac12\int(1-au)\Phi(u)e^{izu}du,
 \qquad a>0,                                          \tag{3d}
\]

has its unique fold at `u=1/a` and produces the same `alpha=-1` spectral
support.  What is invariant is one fold plus its reflected partner, not the
numeral `1`.

The reduction is
not yet a proof of contractivity: Fourier oscillation means that a single
real-space sign change does not generically make the transform zero-free or
Hermite--Biehler.  But any successful variation-diminishing argument now has
a single normalization-fixed fold and cannot choose its pairing after seeing
the answer.

The sharp source question is whether the special modular theta density makes
the one-fold transform (3a) an upper-half-plane stable function.  Its
falsifier is a zero of (3a) in the upper half-plane; its proof must use more
than the bare fact of one sign change.

## Smallest hostile source: one fold is not sufficient

Take the positive even two-atom source with transform

\[
 X_\varepsilon(z)=\cos z+\varepsilon\cos2z,
 \qquad0<\varepsilon\ll1.                             \tag{3e}
\]

Writing `c=cos z`, its zeros solve

\[
 2\varepsilon c^2+c-\varepsilon=0,
\]

so

\[
 c_\pm=\frac{-1\pm\sqrt{1+8\varepsilon^2}}{4\varepsilon}.       \tag{3f}
\]

For small positive `epsilon`, `c_-<-1`; consequently `X_epsilon` has nonreal
zeros.  By the Hermite--Biehler equivalence, no member

\[
 E_{\varepsilon,a}=X_\varepsilon+iaX_\varepsilon'
\]

can supply the required Schur transfer.  Nevertheless its source density is
still `(1-au)` times a positive even measure and therefore has exactly one
fold.

This is the smallest structural counterexample to the conjecture that a
single signed fold forces Clark admission.  Replacing the atoms by sufficiently
narrow positive even smooth bumps preserves nearby nonreal zeros by analytic
perturbation, so discreteness is not the cause.

Hence the live explanation must use a stronger property peculiar to the
completed modular theta density—such as a coupled variation-diminishing law,
an admissible boundary quotient, or a scale-recursive modular identity.  The
one-fold reduction identifies the defect channel but does not repair it.

## The single missing admission condition

For real `t`, both `X(t)` and `X'(t)` are real, so wherever the quotient is
defined,

\[
 |\Theta(t)|=1.                                      \tag{3}
\]

Moreover

\[
 1-|\Theta(z)|^2
 =\frac{|E(z)|^2-|E^*(z)|^2}{|E(z)|^2}.              \tag{4}
\]

Therefore the denominator-free de Branges kernel positivity is exactly the
condition that `Theta` extend holomorphically as a Schur/inner function in
the upper half-plane:

\[
 \boxed{
 |\Theta(z)|<1\quad(\operatorname{Im}z>0).
 }                                                     \tag{5}
\]

Within the completed Xi class, (5) is equivalent to RH.  It is the admission
condition for the operator below, not a theorem already established.

## Model space and Clark family

Assume (5).  Form the canonical model space

\[
 \mathcal K_\Theta=H^2(\mathbb C_+)\ominus
 \Theta H^2(\mathbb C_+).                            \tag{6}
\]

The compressed multiplication operator has its standard one-parameter
family of self-adjoint Clark extensions `T_alpha`, indexed by unimodular
`alpha`.  Their spectral measures are determined by the source transfer
`Theta`; no separate eigenvalue input is required.

Choose `alpha=-1`.  On the real boundary,

\[
 \Theta(t)=-1
 \quad\Longleftrightarrow\quad
 X(t)-iX'(t)=-X(t)-iX'(t)
 \quad\Longleftrightarrow\quad X(t)=0.               \tag{7}
\]

Consequently the `-1` Clark operator has spectral support exactly at the
critical-line parameters of the Xi zeros:

\[
 \boxed{
 \operatorname{spec}T_{-1}=\{\gamma:X(\gamma)=0\},
 }                                                     \tag{8}
\]

with spectral weights/residues determined by the Clark measure.  Multiple
zeros require a boundary multiplicity audit; a scalar Clark atom does not
create an eigenspace of the same dimension.

## Clark mass recovers zero multiplicity automatically

Suppose `X` has a real zero `gamma` of order `m`.  Then locally

\[
 \frac{X(z)}{X'(z)}=\frac{z-\gamma}{m}+O((z-\gamma)^2).
\]

Writing `r=X/X'`, equation (2) becomes `Theta=(r-i)/(r+i)`.  Therefore

\[
 \boxed{\Theta'(\gamma)=-\frac{2i}{m}.}               \tag{9}
\]

For a meromorphic inner function, the Clark atom at a boundary point where
`Theta=alpha` has mass proportional to `1/|Theta'|`.  Hence the `alpha=-1`
atom at `gamma` has mass

\[
 \operatorname{mass}_\gamma=\kappa m,                \tag{10}
\]

where `kappa` is one global half-plane normalization constant.  The scalar
Clark measure thus records the integer zero multiplicity as atom weight,
although its eigenspace at each distinct support point remains
one-dimensional.

## Quarter-shifted positive operator

The source-required squared operator is now canonical:

\[
 \boxed{
 A=\frac14+T_{-1}^{2}\ge\frac14.
 }                                                     \tag{11}
\]

Its spectral points are

\[
 a_\gamma=\frac14+\gamma^2,                           \tag{12}
\]

exactly those required by the order-two Stieltjes representation.  With the
appropriate cyclic Clark vector `Omega`, its spectral measure gives

\[
 \left\langle\Omega,
 (x-\tfrac14+A)^{-2}\Omega\right\rangle
 =\sum_\gamma\frac{w_\gamma}{(x+\gamma^2)^2}.         \tag{13}
\]

The Clark boundary functional supplies weights proportional to `m_gamma` by
(10).  The order-two boundary measure requires the additional factor
`1+4gamma^2`.  Formally, on the associated rigged spectral scale, this is
obtained by

\[
 \Omega=(1+4T_{-1}^2)^{1/2}\Omega_{\rm Clark}.        \tag{14}
\]

Consequently (13) has weights proportional to

\[
 w_\gamma=(1+4\gamma^2)m_\gamma,                     \tag{15}
\]

exactly matching the measure conversion from the Stieltjes resolvent to its
order-two boundary derivative.  Only the single global convention constant
remains to be fixed.

There is a necessary domain qualification.  The Clark measure, and a
fortiori the reweighted measure (15), generally has infinite total mass.
Thus `Omega_Clark` and `Omega` in (14) need not be ordinary vectors of
`K_Theta`; they are boundary/form vectors in a negative Sobolev scale for
`T_{-1}`.  The resolvent-smoothed expression (13) is finite because

\[
 \sum_\gamma
 \frac{(1+4\gamma^2)m_\gamma}{(x+\gamma^2)^2}
\]

converges under the classical zero-counting growth, but the unsmoothed norm
does not.  Consequently (13) must be stated as a closed quadratic form or
boundary-pairing identity, not automatically as the inner product of an
ordinary Hilbert-space vector.  Producing a genuine vector formula would
require a different normalization or an enlarged rigged realization.

## What this resolves and what it does not

This identifies the proposed self-adjoint operator far more concretely than
an abstract Herglotz realization:

\[
 \text{fixed theta contour}
 \to E=X+iX'
 \to\Theta=E^*/E
 \to\mathcal K_\Theta
 \to T_{-1}
 \to A=1/4+T_{-1}^2.                                  \tag{16}
\]

It also explains why the infinite-dimensional boundary quotient is natural:
`K_Theta` is precisely a relative Hardy-space quotient, not a finite tail
moment compression.

It does **not** prove RH.  The model space and self-adjoint Clark operator are
admitted with the needed positivity only after proving (5), equivalently the
normal-modulus current theorem

\[
 \partial_y|X(x+iy)|^2>0.                             \tag{17}
\]

The remaining constructive question is whether the theta tail restriction
Carrier maps canonically into `K_Theta` so that (5) follows from a positive
source energy, rather than being imposed as the definition of the quotient.

## Falsifier

A point in the upper half-plane with `|Theta(z)|>=1`, or a pole of `Theta`
there, rejects the Schur admission and hence this positive Clark model.  A
finite positive sample cannot establish (5).
