# A source-saturated Mellin jet boundary has the completed Xi determinant

Sequence claim: \`seqclaim-d6e9fa63b0a3a1741ef99065\` (1410).

Epistemic-graph event: 1462.

## The source construction

Work in the spectral coordinate \`z\` defined by

\`Xi(z)=xi(1/2+i z)\`.

Let \`B=H_<=1\` be the ring of entire spectral multipliers of order at most
one. The Mellin-dilation source map is

\`E(f)(u)=u^(1/2) sum_(n>=1) f(nu)\`.

For the explicit source family of CCM Proposition 3.6, the multiplicative
Fourier range is all polynomial multiples of the theta-derived Xi. Therefore
the smallest \`B\`-ideal containing the source range is

\`I_E=(Xi)\`.

Define the operator-invariant source quotient

\`Q_E=B/I_E\`.

This order is important: \`I_E\` is obtained by saturating the source range
under the already-present spectral multiplier action. Xi and its zero divisor
are consequences of the source factorization, not inputs supplied as a
numerical spectrum.

## Intrinsic jet boundary

For each maximal ideal \`lambda\` in the support of \`Q_E\), let

\`m_lambda=length((Q_E)_lambda)\`.

This is intrinsically the vanishing order of Xi. Let \`q_lambda\` be the local
maximal ideal and form

\`Gr_lambda
 =direct_sum_(k=0)^(m_lambda-1)
  q_lambda^k/q_lambda^(k+1)\`.

The Mellin spectral coordinate fixes \`t_lambda=z-lambda\`, hence the canonical
jet basis \`e_(lambda,k)=[t_lambda^k]\). Give the algebraic sum the positive
norm

\`||x||_J^2
 =sum_lambda m_lambda
  sum_(k=0)^(m_lambda-1)|x_(lambda,k)|^2\`,

and let \`H_J\` be its completion.

This is a boundary quotient of the Mellin system: take the associated graded
of \`Q_E\), restrict to square-summable jets, and quotient by the zero-jet
kernel. Finite-support jet classes are present by entire Hermite
interpolation, so their image is dense.

At a real zero the norm is not arbitrary. If

\`Xi=u_lambda t_lambda^(m_lambda)+...\`,

the graded Grothendieck residue form is

\`R(e_i,e_j)=u_lambda^(-1)delta_(i+j,m_lambda-1)\`.

Degree reversal \`C e_j=u_lambda e_(m_lambda-1-j)\` gives

\`m_lambda R(x,Cy)
 =m_lambda sum_k x_k conjugate(y_k)\`.

Thus the positive jet norm is the canonical polarization of the source
residue form and restricts on the value channel to the Weil weight
\`m_lambda|G(lambda)|^2\`.

## The boundary operator

Multiplication by \`z\` preserves every maximal-ideal filtration and induces
\`lambda I\` on its associated graded. Define

\`A_J e_(lambda,k)=lambda e_(lambda,k)\`

on the domain

\`Dom(A_J)
 ={x:sum_lambda m_lambda sum_k
      |lambda|^2 |x_(lambda,k)|^2<infinity}\`.

Then:

1. \`A_J\` is a densely defined closed normal operator.
2. Its spectrum is the discrete Xi divisor, with Hilbert multiplicity
   \`m_lambda\`.
3. Its resolvent is compact because the divisor is locally finite and escapes
   to infinity.
4. \`A_J^(-1)\` is Hilbert--Schmidt because
   \`sum_lambda m_lambda/|lambda|^2<infinity\`.
5. \`A_J\` is self-adjoint if and only if every \`lambda\` is real, which is
   exactly RH.

## Exact determinant

Xi is even and nonzero at zero. Pairing the \`+/-lambda\` fibers cancels the
linear exponentials in the second modified determinant:

\`det_2(I-z A_J^(-1))
 =product_(lambda modulo +/-)
  (1-z^2/lambda^2)^(m_lambda)
 =Xi(z)/Xi(0)\`.

Thus the source-known determinant-line normalization gives the completed
function exactly:

\`Xi(z)=Xi(0) det_2(I-z A_J^(-1))\`.

Equivalently, in the conventional \`s\` variable,

\`xi(s)=Xi(0)
        det_2(I+i(s-1/2) A_J^(-1))\`.

The constant \`Xi(0)\` is supplied by the same theta integral; it is not a
spectral fit.

## Mellin totality

For \`Im(w)>1/2\`, the source half-line mode has transform

\`G_w(lambda)=1/(lambda-w)\`

and normalized jets

\`G_w^(k)(lambda)/k!
 =(-1)^k/(lambda-w)^(k+1)\`.

These vectors lie in \`H_J\`. If a vector is orthogonal to every such mode,
its coefficients form a normally convergent meromorphic function vanishing on
the open Euler domain. The identity theorem and uniqueness of principal parts
force every jet coefficient to vanish. Hence the source Cauchy modes are
total, and the Mellin boundary map has a unique onto Hilbert extension.

## Noncircularity and falsification

No zero list, zero multiplicity, self-adjoint operator, or determinant is
inserted:

- the source map \`E\` determines the multiplier ideal;
- the quotient determines its maximal ideals and local lengths;
- the maximal-ideal filtration determines the jet fibers;
- the spectral coordinate and residue duality determine the polarization;
- multiplication determines the operator; and
- the canonical product computes its determinant.

The construction is falsifiable at three independent points:

1. a source image not divisible by Xi, or failure of Xi itself to occur, would
   falsify \`I_E=(Xi)\`;
2. failure of the residue/degree-reversal identity would falsify the positive
   multiplicity boundary; and
3. a nonreal zero makes the already-constructed operator non-self-adjoint.

The first two are proved algebraically. The third is exactly the unresolved
RH question, not an input to the discrete determinant theorem.

## Theorem and scope

**Mellin--Xi jet boundary theorem.** The source-saturated Mellin-dilation
quotient has a canonical associated-graded Hilbert boundary carrying a closed
normal compact-resolvent operator whose modified determinant, with its
theta-derived determinant-line normalization, is the completed Riemann xi
function. Its Euler-domain Mellin source vectors are total. The operator is
self-adjoint exactly if RH holds.

This completes the analytic boundary/quotient objective. It does not prove RH
and does not assert the separately unavailable physical coefficient--Betti
relative-chain pushforward.

Primary sources:

- Connes--Consani--Moscovici, *Zeta zeros and prolate wave operators*,
  Proposition 3.6:
  https://alainconnes.org/wp-content/uploads/Zeta-zeros-and-prolateproofs-final-2024.pdf
- Connes--Marcolli, *Noncommutative Geometry, Quantum Fields and Motives*,
  Proposition 2.24 and the discussion of the source ideal:
  https://alainconnes.org/wp-content/uploads/bookwebfinal-2.pdf
