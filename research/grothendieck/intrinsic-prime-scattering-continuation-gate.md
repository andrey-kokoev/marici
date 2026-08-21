# Intrinsic-prime scattering is exact only before the continuation gate

Epistemic-graph event: 1408.

## Prime determinant in its honest operator domain

Let \`P\` be the intrinsic prime set derived from the pointed
\`pi_0\` semiring, and let \`N\` act on \`ell^2(P)\` by

\`N e_p=p e_p\`.

For \`Re(s)>1\`, the diagonal operator \`N^{-s}\` is trace class because
\`sum_p p^{-Re(s)}\` converges. Its Fredholm determinant is therefore

\`D(s)=det(I-N^{-s})=prod_p(1-p^{-s})=1/zeta(s)\`.

This identity is source-derived in the convergence half-plane: the prime
labels come from irreducibles, not from a fitted zero set.

## A unitary boundary phase

Fix \`sigma>1\` and real \`t\`. Define

\`S_sigma(t)=D(sigma+i t)/D(sigma-i t)\`.

Since the diagonal determinant respects conjugation,
\`D(sigma-i t)=conj(D(sigma+i t))\`, and hence

\`|S_sigma(t)|=1\`.

Thus the intrinsic-prime determinant supplies an exact scalar scattering
phase that can be coupled to the Gaussian endpoint corner. Its logarithmic
derivative is

\`(1/i) d/dt log S_sigma(t)=2 Re T(sigma+i t)\`,

where

\`T(s)=D'(s)/D(s)=sum_(p,k>=1) (log p) p^{-k s}\`.

The phase therefore carries the full prime-power trace, unlike the finite
Gaussian endpoint. This is the first noncircular infinite-dimensional
boundary datum in the program.

## The continuation obstruction

The same formula does not define the desired critical-line boundary by
operator theory. Trace class fails at and below \`Re(s)=1\`. At
\`Re(s)=1/2\`, \`N^{-s}\` is not even Hilbert--Schmidt, since

\`sum_p |p^{-s}|^2=sum_p 1/p\`

diverges.

Higher Schatten regularizations do not solve the identification problem.
Although \`N^{-1/2-it}\` lies in every Schatten class \`S_q\` with \`q>2\`,
a regularized determinant deletes finitely many divergent terms from the
Euler logarithm. Restoring exactly the missing prime terms so that the answer
is \`1/zeta(s)\` requires an additional renormalization law. Choosing that law
by analytic continuation of \`zeta\` would insert the target and make the
spectral construction circular.

Moreover, zeros of \`zeta\` are poles of the continued reciprocal determinant
\`D=1/zeta\`, not zeros of the honest prime Fredholm determinant. A
Hilbert--Polya operator still requires a source-derived inversion, extension,
or boundary quantization that converts this resonance datum into a discrete
self-adjoint spectrum.

## Consequence for the combined boundary

The current source-derived factors divide cleanly:

- the Gaussian norm-two corner supplies the metaplectic eighth phase;
- the dual-cutoff \`xp\` geometry supplies the smooth \`T log T\` count; and
- the intrinsic-prime scattering phase supplies prime-power fluctuations for
  \`sigma>1\`.

All three ingredients exist without using the zeros. What is absent is a
source-derived gluing/renormalization law transporting the prime phase through
\`sigma=1\` to the critical line while preserving self-adjointness and turning
the continued poles into determinant zeros.

## Scope

This is an exact trace-class theorem and a continuation falsifier. It does not
deny meromorphic continuation of \`zeta\`; it proves that such continuation is
not furnished by the present prime Fredholm operator and therefore cannot be
silently counted as a source-derived boundary construction.
