# The correct Weyl bridge is a bordered determinant with two independent completion gates

## Question

A non-affine entire completed section cannot itself be a diagonal Herglotz
resolvent coefficient.  Does that analytic mismatch kill the positive
collocation route, or is there a source-compatible bridge from a diagonal
coefficient to an entire determinant numerator?

There is an exact finite bridge.  It also isolates two independent ways the
bridge can fail under completion.

## Bordered-determinant identity

Let `A=A*` be an `n`-dimensional carrier and let `u,v` be observer and source
ports.  Away from the spectrum of `A`, define

\[
m_{u,v}(z)=u^*(A-zI)^{-1}v.
\]

The Schur determinant identity gives

\[
\det
\begin{pmatrix}
A-zI&v\\
u^*&0
\end{pmatrix}
=
-\det(A-zI)m_{u,v}(z).
\]

Thus a rational transfer coefficient has a polynomial bordered-determinant
numerator.  The numerator can be entire even though the Weyl coefficient is
meromorphic.  This is the correct way around the entire-Herglotz no-go.

## Collocated case

If `u=v`, then

\[
m_v(z)=v^*(A-zI)^{-1}v
\]

has strict Herglotz sign and no nonreal zeros.  Therefore every nonreal zero
of its bordered determinant numerator must come from a zero of
`det(A-zI)` that is not cancelled correctly.  At finite dimension the reduced
numerator is real-rooted and interlaces the carrier spectrum.  Cyclicity makes
the numerator and denominator coprime; without cyclicity they may share real
factors, but no off-real zero appears.

For a positive carrier metric `H`, the same statement holds after replacing
`u=v` by positive collocation `u=Hv` and conjugating to the `H`-orthonormal
frame.

If `u` and `v` are not collocated, the bordered pencil is not self-adjoint in
the required metric and its numerator may have nonreal zeros.  Grothendieck's
three-point cross-resolvent witness is exactly this failure.

## Two-gate factorization

Suppose a finite scalar section has a source-derived factorization

\[
X_N(z)=D_N(z)m_N(z),
\]

where `m_N` is the collocated diagonal Weyl coefficient and `D_N` is the
carrier determinant or another authorized zero-free transition factor in the
off-seam domain.  Then zero confinement follows from two logically
independent statements:

1. **Port gate:** `m_N` has strict Herglotz sign.
2. **Denominator gate:** `D_N` is nonzero and the product identity is exact.

This explains why all finite Euler stages can be coherent and zero-free while
the completed section remains unresolved.  Completion can fail by either:

- loss of positive collocation or closability in the Weyl coefficient; or
- loss of strict invertibility in the determinant/transition factor.

The second is precisely the inverse-norm escape already isolated by
Grothendieck.  Finite invertibility of every Euler transition does not imply
invertibility of the restricted-product limit.

## Completion theorem required

A legitimate infinite bridge must construct compatible triples

\[
(D_N,m_N,X_N)
\]

from one fixed source system and prove all of the following:

1. the bordered determinant identity is natural under cutoff inclusion;
2. the source and endpoint ports remain positively collocated;
3. the Weyl graphs converge in a topology preserving the strict half-plane
   sign;
4. `D_N` converges to an off-seam invertible determinant-line section;
5. common real factors are controlled rather than hidden by cancellation;
6. the limit product is the independently constructed completed theta/Tate
   section.

Uniform lower bounds are not needed merely to show that each already
constructed limit value is nonzero.  They are needed to infer nonvanishing of
the limit from finite stages.  This distinction prevents compactness language
from being smuggled into a pointwise Herglotz theorem.

## Relation to the full two-port Weyl family

The positive Cayley crossing form of a full matrix Weyl family orients
`det W`, not an off-diagonal entry `W_f0`.  The bordered-determinant bridge
avoids that lower-minor mismatch only if the theta scalar is derived as the
numerator of a collocated scalar Weyl coefficient.  If it remains merely a
cross entry, one still needs an exact source law turning that cross entry into
the bordered numerator.

Equivalently, the programme must derive one of these, not conflate them:

- positive port collocation of the actual theta source and endpoint;
- an associate-divisor identity between the theta cross entry and a
  self-adjoint bordered determinant;
- a rank constraint forcing cross cancellation to equal full rank loss.

## Minimal algebraic falsifiers

- `u* v` is not positive real in the frozen frame, so no positive collocating
  metric exists.
- The theta scalar is an off-diagonal Weyl entry with a zero where the full
  Weyl determinant is nonzero.
- The proposed bordered numerator differs from the scalar section by a factor
  having an off-seam zero.
- Every `D_N` is invertible but the least inverse margin tends to zero.
- The Weyl coefficients converge only after scalar compression, while their
  operator graphs do not close.
- A common numerator/denominator factor is cancelled before its boundary type
  is recorded.
- The determinant identity is fitted after completion rather than inherited
  naturally from finite source incidence.

## Verdict

The analytic-type obstruction does not kill the colligation route.  It tells
us its exact form.  The completed entire section must arise as a bordered
determinant numerator or equivalent characteristic object behind a positive
Weyl coefficient, not as the coefficient itself.

The remaining Deutschian explanation now factorizes cleanly:

> What source law collocates the theta forcing and endpoint ports, and what
> completion law preserves strict invertibility of the accompanying carrier
> determinant so that their bordered numerator is the completed section?

These are independent obligations.  Solving only the first leaves
finite-to-infinite disappearance; solving only the second leaves cross-port
cancellation.
