# Theta Tate-current grades unify before completion as one log-Euler measure

## One source measure, three completion grades

The atomic incidence currents of every connected Fock grade combine as

\[
 \boxed{
 \mu_{\log}
 =\sum_p\sum_{k\ge1}
 \frac1k p^{-k/2}\delta_{k\log p}.}
\]

Using `n=p^k` and

\[
 \frac{\Lambda(p^k)}{\log(p^k)}=\frac1k,
\]

this is equivalently

\[
 \mu_{\log}
 =\sum_{n=p^k}
 \frac{\Lambda(n)}{\log n}n^{-1/2}\delta_{\log n}.
\]

Thus `P`, `Q`, and the `k>=3` tail are three regularity strata of one
source-defined prime-power current.  They should be split for typing, then
reassembled before scalar completion.

## Euler-half-plane transform

For `Re(z)>1/2`, absolute convergence gives

\[
 \begin{aligned}
 \int_0^\infty e^{-zq}\,d\mu_{\log}(q)
 &=\sum_{p,k}\frac1k p^{-k(1/2+z)}\\
 &=\log\zeta(1/2+z).
 \end{aligned}
\]

The odd boundary readout is the imaginary difference of this Laplace
transform across conjugate spectral characters.  The three-stage Tate
factorization is therefore the typed decomposition of the logarithm of the
finite Euler determinant.

## Derivative current

Multiplying each atom by its scale removes the `1/k` factor:

\[
 q\,d\mu_{\log}(q)
 =\sum_{n=p^k}\Lambda(n)n^{-1/2}\delta_{\log n}.
\]

This is the von Mangoldt current.  Spectral differentiation of the connected
phase therefore produces the arithmetic distribution used by the explicit
formula.  The appearance of prime powers is forced by differentiation of one
log-Euler object, not added as a separate correction.

## Scalar-log continuation is forbidden as a proof primitive

The identity with `log zeta` is source-valid in the zero-free Euler
half-plane.  Continuing a scalar logarithm through the critical strip requires
branch choices around the zeros of `zeta`.  Equivalently,

\[
 \partial_z\log\zeta=\frac{\zeta'}{\zeta}
\]

is meromorphic with poles precisely at the divisor under investigation.

Therefore a compiler that defines its completed boundary current by a global
scalar `log zeta` or `zeta'/zeta` has imported the zero set.  It cannot then
use that current noncircularly to exclude zeros.

## Correct global value type

Before continuation, the joint arithmetic operation must remain
determinant-valued or line-valued:

\[
 \boxed{
 \text{typed log-current}
 \xrightarrow{\exp/\det_3}
 \text{nonzero finite-cutoff transition in a determinant line}.}
\]

The primitive and square fields specify the relative trivialization of that
line; they are not separately completed scalar functions.  Modular and
archimedean sewing must act on the full determinant-line object, with scalar
logs available only locally in charts known to avoid the divisor.

## Compiler consequence

The operations `P`, `Q`, and connected-tail formation precede one joint
reassembly `E`.  Scalar archimedean completion `A` does not braid independently
with each grade:

\[
 \boxed{(P,Q,T_{\ge3})\prec E\prec A_{\det}.}
\]

Here `A_det` must be a determinant-line correspondence, not addition of a
fixed scalar countercurrent.  This explains the no-go in packet 169.

## Remaining obstruction

The finite determinant transition is explicit, but its source-derived
archimedean/modular determinant-line correspondence is not.  Constructing
that correspondence without using `xi`, its zeros, or a global logarithm is
the next gate.  Only afterward can it define the seam incidence maps `B,C`
in the return operator of packet 166.
