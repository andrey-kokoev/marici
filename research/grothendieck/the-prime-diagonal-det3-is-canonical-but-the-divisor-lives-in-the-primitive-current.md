# The Prime-Diagonal det3 Is Canonical but the Divisor Lives in the Primitive Current

## Exact source-derived Schatten family

Let $\mathcal H_{\mathbb P}=\ell^2(\mathbb P)$ and define the diagonal prime
operator

$$
K_s e_p=p^{-s}e_p.
$$

Then

$$
\|K_s\|_{\mathcal S_r}^r
=\sum_p p^{-r\operatorname{Re}s}.
$$

Hence

$$
K_s\in\mathcal S_3
\quad\Longleftrightarrow\quad
\operatorname{Re}s>\frac13,
$$

while on the critical seam $K_s$ is not Hilbert--Schmidt because
$\sum_p p^{-1}$ diverges. This is the exact operator-class threshold predicted
by the primitive, square, and connected-tail filtration.

Vertical Mellin transport is source-native:

$$
K_{\sigma+it}=e^{-itQ}K_\sigma,
\qquad
Qe_p=(\log p)e_p.
$$

## Exact determinant decomposition

For $\operatorname{Re}s>1$,

$$
\log\zeta(s)
=\sum_p\sum_{k\ge1}\frac{p^{-ks}}k.
$$

Meanwhile,

$$
\log\det_3(I-K_s)
=-\sum_p\sum_{k\ge3}\frac{p^{-ks}}k.
$$

Writing the prime zeta function as

$$
P(s)=\sum_p p^{-s},
$$

gives the exact Euler-chamber identity

$$
\zeta(s)
=\exp\left(P(s)+\frac12P(2s)\right)
\det_3(I-K_s)^{-1}.
$$

Thus the source-derived triple is explicitly

$$
\left(P(s),\frac12P(2s),\det_3(I-K_s)^{-1}\right).
$$

The three components are exactly the primitive current, square current, and
connected $k\ge3$ determinant tail.

## Location of the divisor

For $\operatorname{Re}s>0$, every eigenvalue satisfies $|p^{-s}|<1$.
Consequently

$$
\det_3(I-K_s)\ne0
$$

throughout the entire right half-plane where the regularized determinant is
defined, in particular for $\operatorname{Re}s>1/3$.

The connected determinant tail therefore carries no Riemann zero divisor.
Nor can the ordinary exponential of a single-valued holomorphic primitive
current vanish. The nontrivial divisor appears when the primitive current is
analytically continued: $P(s)$ develops logarithmic branching governed by
the zeros and pole of zeta. Equivalently,

$$
P(s)=\sum_{m\ge1}\frac{\mu(m)}m\log\zeta(ms)
$$

where the continuation is valid chartwise. A zeta zero is a logarithmic
singularity of the connected primitive coordinate.

This changes the determinant interpretation sharply:

> The regularized tail is a canonical zero-free determinant. The Riemann
> divisor is encoded in the failure of the primitive boundary current to
> exponentiate as one global scalar chart.

The primitive port is therefore not merely the first counterterm needed to
normalize a determinant. It is the divisor-bearing boundary coordinate.

## Consequence for the self-adjoint programme

The prime-diagonal construction solves the source-authority and Schatten
classification gates but is not a Hilbert--Pólya operator:

- $K_s$ depends on the spectral parameter rather than being the resolvent of
  one fixed self-adjoint operator;
- its regularized determinant is zero-free in the RH region;
- all nontrivial divisor information has moved into the analytically
  continued primitive boundary current;
- reciprocal and archimedean sewing must decide how that logarithmic current
  becomes a global entire section.

This explains why deleting $k=1$ destroyed the physical problem: it deleted
the coordinate carrying the divisor. It also explains why a trace-class-tail
determinant alone repeatedly produced zero-free or tautological objects.

## New singular gate

The next theorem must convert the logarithmic primitive current into a
source-derived boundary monodromy or index for a fixed completed operator.
The necessary checks are:

1. construct the primitive current as a boundary trace before taking
   $\log\zeta$;
2. derive its reciprocal and archimedean monodromy from theta/Tate sewing;
3. show how integer winding of that current becomes the divisor of the
   completed section;
4. prove that the winding is supported only on the self-adjoint seam;
5. retain the square current and $\det_3$ tail so that branch choices and
   regularization anomalies are fixed;
6. reject a hostile common divisor because it changes the primitive boundary
   monodromy without a source lift.

The RH-bearing bridge has therefore narrowed again: it is a primitive-current
monodromy-to-self-adjoint-index theorem.
