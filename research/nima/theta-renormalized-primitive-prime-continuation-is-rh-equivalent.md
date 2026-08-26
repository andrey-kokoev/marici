# Renormalized primitive-prime continuation is RH-equivalent

## Möbius inversion

Let

\[
P(s)=\sum_p p^{-s}
\]

in the Euler half-plane. Absolute convergence gives

\[
\log\zeta(s)
=
\sum_{m\ge1}\frac{P(ms)}{m}.
\]

Möbius inversion yields

\[
P(s)
=
\sum_{m\ge1}
\frac{\mu(m)}{m}
\log\zeta(ms).
\]

Separate the first term:

\[
P(s)=\log\zeta(s)+H(s),
\]

where

\[
H(s)
=
\sum_{m\ge2}
\frac{\mu(m)}{m}
\log\zeta(ms).
\]

## Higher terms are already controlled

If

\[
\operatorname{Re}s>\frac12,
\]

then for every (m\ge2),

\[
\operatorname{Re}(ms)>1.
\]

Each higher term is therefore in the absolutely convergent, zero-free Euler
domain. The series defining (H) converges locally uniformly on compact
subsets of the open critical half-plane and defines an analytic function
there.

Hence the only nontrivial continuation in (P) is the (m=1) logarithm of
(zeta).

## Endpoint renormalization

The pole at (s=1) must be removed before asking for a global analytic
logarithm. Define

\[
Z_*(s)=(s-1)\zeta(s).
\]

This function is analytic and nonzero at (s=1). In the Euler domain,

\[
P(s)+\log(s-1)-H(s)
=
\log Z_*(s),
\]

with compatible branches.

The source endpoint current has exactly one legitimate task here: replace the
separate singular terms by the regular endpoint-completed combination. It does
not independently choose a logarithm around any zero.

## Equivalence theorem

The open half-plane

\[
\operatorname{Re}s>\frac12
\]

is simply connected. Therefore (Z_*) has an analytic logarithm there if and
only if (Z_*) is zero-free there.

Since (H) is already analytic, the following are equivalent:

1. the endpoint-renormalized primitive prime current has a single-valued
   analytic continuation to the open critical half-plane;
2. (Z_*(s)) has an analytic logarithm there;
3. (zeta(s)) has no zeros there.

Together with the functional equation, zero-freeness in the right open
critical half-plane is the Riemann-hypothesis zero-confinement statement.

Thus the proposed primitive-current continuation is not merely difficult. It
is RH-equivalent.

## Consequence for the determinant route

The diagonal Schatten-three tail and square current do not reduce this final
gate:

- the regularized tail is already zero-free for
  (operatorname{Re}s>1/3);
- the square current is analytic for (operatorname{Re}s>1/2);
- the endpoint-renormalized primitive current is analytic there exactly when
  the Euler sector is zero-free there.

Therefore a proof that first constructs the primitive continuation from
(log\zeta), (log\Xi), or a chosen scalar branch is circular.

A noncircular advance would require a source operation that constructs the
single-valued primitive continuation independently and whose consistency can
be verified without inspecting the completed scalar divisor. Such an
operation would itself constitute the missing RH mechanism.

## Finite hostile test

At cutoff (X), let

\[
P_X(s)=\sum_{p\le X}p^{-s}.
\]

Every (P_X) is entire, but this gives no continuation theorem. The required
test is locally uniform convergence of the endpoint-renormalized source
sequence on every compact subset of the open critical half-plane.

Reject any candidate whose renormalization:

- uses the zeros of zeta or xi;
- divides by the completed scalar;
- selects a branch of its logarithm after completion;
- converges only pointwise;
- changes under a source-compatible hostile prime perturbation without an
  independently typed correction.

## Lakatos disposition

The diagonal determinant programme has produced a useful decomposition and a
no-go result:

- third-order regularization explains the arithmetic filtration;
- determinant denominators isolate zero-bearing invertibility;
- first and second currents restore exact framing;
- the primitive continuation remains exactly the zero-free logarithm problem.

Unless a genuinely new source constructor for that continuation is found, the
programme should close rather than present the renormalized primitive current
as an independent explanation of RH.
