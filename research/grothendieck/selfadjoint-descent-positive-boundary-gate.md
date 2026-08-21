# Self-adjoint descent requires a new positive boundary, not the Xi determinant

Long-horizon intent and falsification policy are recorded in
`deutschian-prime-spectral-explanation-charter.md`. This packet supplies the
functional-analytic no-go and exact positivity gate used by that charter.

## Question

Why should the source-derived Mellin--Xi boundary operator be self-adjoint?

The determinant identity does not answer this.  The source quotient constructs
a closed normal operator whose eigenvalues are the Xi divisor.  A positive
change of metric cannot make a nonreal scalar eigenvalue self-adjoint.  Thus
self-adjointness must be forced before the quotient is decomposed into zero
fibres.

## Native Hilbert-quotient no-go

Put the logarithmic Mellin variable on `H=L^2(R,dt)`.  The self-adjoint
dilation generator becomes multiplication by the real variable,

`D=M_t`.

Theta completion gives the bounded self-adjoint multiplier

`C_Xi=Xi(D)=M_Xi`.

Since Xi is a nonzero entire function, its real zero set has Lebesgue measure
zero.  Hence

`ker C_Xi=L^2({t:Xi(t)=0})=0`.

For every bounded operator,

`closure(Ran C_Xi)=(ker C_Xi^*)^perp`.

Consequently

`closure(Ran C_Xi)=H`

and the ordinary Hilbert cokernel is zero.  The same conclusion holds for a
closed translation-reducing quotient: in the Fourier representation it is
supported on a measurable set, while the discrete Xi divisor has measure
zero.

**No-go theorem.** The nontrivial Xi jet boundary is not a continuous Hilbert
quotient of the native unitary dilation representation by the closed theta
source range.  Therefore it cannot inherit self-adjointness from the dilation
generator by ordinary reducing-subspace descent.

This does not invalidate the analytic entire-function quotient.  It shows
that passing from the source to jets changes topology: generalized evaluation
states become normalizable only after supplying an additional boundary form.

## Exact positive-descent gate

Let `T` be the admissible logarithmic Mellin test algebra and let `W` be the
centered prime--gamma Weil functional derived from the explicit formula.  Set

`<f,g>_W=W(f*g^*)`.

Multiplication by the Mellin spectral coordinate defines a formal boundary
relation `Z`.  The desired source-side construction would have to prove,
without using a zero list,

1. `W(f*f^*)>=0` for every `f in T`;
2. the null space of this form is invariant under `Z`;
3. `Z` is closable on the positive completion; and
4. its closure is self-adjoint (or has a source-canonical self-adjoint
   realization) with compact resolvent.

The first condition is already Weil's positivity criterion and is equivalent
to RH.  On the spectral side this is transparent:

`W(f*f^*)=sum_rho |F((rho-1/2)/i)|^2`

is a positive evaluation norm precisely when all spectral parameters are
real.  Conditions 2--4 cannot manufacture reality after condition 1 fails.

Hence the honest answer is:

**the present boundary operator should be self-adjoint exactly if the
prime--gamma source functional is positive; the determinant alone supplies no
reason for that positivity.**

## Source-positive factorization conjecture

The strongest noncircular attack target is the following.

**Conjecture (source-positive Weil factorization).** There exists a Hilbert
space `K` and a closable transform `R:T->K`, constructed directly from the
theta endpoint and prime-power source distributions, such that

`W(f*g^*)=<Rf,Rg>_K`

for all admissible `f,g`, and such that Mellin multiplication intertwines with
a self-adjoint boundary relation on `K`.

This statement implies Weil positivity and therefore RH.  Conversely, RH
provides the abstract spectral factorization, so the mathematical novelty
must be that `R` is given on the arithmetic/source side without first using
the zeros.

The factorization cannot be termwise in the naive prime expansion: every
prime mode contributes with the wrong sign before the archimedean and endpoint
terms are combined.  A viable construction must therefore be global and
nonlocal--for example a reflection-positive theta/prime correspondence,
canonical-system energy, or an arithmetic scattering defect whose norm
already includes the gamma counterterm.

## Smallest hostile tests

There are two independent falsifiers.

1. **One nonreal fibre.** On a one-dimensional positive space, `Z=lambda I`
   is self-adjoint only when `lambda` is real.  No polarization repairs a
   nonreal `lambda`.
2. **Finite source Gram test.** For any proposed explicit transform `R`, choose
   finitely many compactly supported Mellin tests `f_i` and compare
   `W(f_i*f_j^*)` with `<Rf_i,Rf_j>`.  A negative eigenvalue or a failed null
   invariance falsifies the proposal before any operator-domain analysis.

The finite Gram test is the preferred experimental attack because a single
negative minor kills an entire proposed factorization, while persistent
positive minors identify where the archimedean term dominates the negative
prime directions.

## Consequence for the Xi jet theorem

The existing theorem remains unconditional with “normal” in place of
“self-adjoint.”  Its degree-reversal polarization correctly records
multiplicity, but it does not prove spectral reality: it is defined fibrewise
after the divisor is known.  The long-horizon problem is now isolated to one
source-side statement--positive factorization of the Weil form--rather than a
search for a better metric on the already diagonalized jet operator.

## Scope

This is a functional-analytic no-go and a reformulation of the remaining
self-adjointness gate.  It does not prove the source-positive factorization,
RH, or the unavailable physical coefficient--Betti relative-chain
pushforward.
