# The Square Current Is the Kakutani Obstruction Between Prime-Dilation and Haar Vacua

## Local dilation state

For the prime return amplitude

$$
r_p=p^{-1/2},
$$

the minimal unitary dilation has spectral measure

$$
d\mu_{r_p}(\theta)
=P_{r_p}(\theta)\frac{d\theta}{2\pi},
\qquad
P_r(\theta)=\frac{1-r^2}{1-2r\cos\theta+r^2}.
$$

The uncoupled reference circle uses Haar measure $d\theta/(2\pi)$. Their
Hellinger affinity is

$$
a(r)=\int_0^{2\pi}\sqrt{P_r(\theta)}\frac{d\theta}{2\pi}.
$$

Expanding the Poisson kernel at $r=0$ gives

$$
a(r)=1-\frac{r^2}{4}+O(r^4).
$$

Therefore

$$
-\log a(r_p)
=\frac1{4p}+O(p^{-2}).
$$

## Global disjointness

Kakutani's product-measure criterion implies that the arithmetic product
state $\bigotimes_p\mu_{r_p}$ and the Haar product state are equivalent only
if the accumulated Hellinger defect is finite. But

$$
\sum_p(1-a(r_p))
\sim\frac14\sum_p\frac1p
=\infty.
$$

Hence the two infinite product representations are mutually singular. Their
vacuum overlap vanishes, and no ordinary infinite tensor-product unitary
implements the change from the Haar reference to the critical arithmetic
dilation state.

The arithmetic product state still exists on the quasi-local algebra, and its
GNS representation is well defined. What fails is a common Hilbert
realization in which it is a bounded perturbation of the Haar vacuum.

## Exact role of the square current

The leading representation defect is $r_p^2=p^{-1}$. Thus its global
divergence is precisely the prime-square boundary grade. The earlier
filtration now has three simultaneous meanings:

- $k=1$ is the divisor-bearing primitive return current;
- $k=2$ is the Kakutani/Hellinger obstruction to placing arithmetic and Haar
  vacua in one product representation;
- $k\ge3$ is the summable regularized determinant tail.

This explains why the square current could never be discarded after local
unitary dilation. It is the coordinate measuring the inequivalence of the two
global representations that must be compared.

## Consequence for the global trace formula

There cannot be one naïve tensor-product Hilbert space carrying both the
uncoupled Haar reference evolution and the arithmetic prime-loop evolution as
unitarily equivalent vacua. Therefore the desired global trace cannot be an
ordinary difference of traces in a common Fock representation.

The correct object must be relative:

- a correspondence or bimodule between the Haar and arithmetic GNS
  representations;
- a relative modular operator or unbounded spatial derivative;
- an explicit square-current boundary coordinate recording the failure of
  unitary implementability;
- the $k\ge3$ determinant tail as the summable interior;
- the primitive current as the oriented return/divisor channel.

This is the operator-algebraic form of the Ubersector: two disjoint
representations plus an independently typed interface, not two vectors in one
ambient tensor product.

## Sharp next gate

Construct the source-derived correspondence

$$
\mathcal H_{\mathrm{Haar}}
\dashrightarrow
\mathcal H_{\mathrm{arith}}
$$

before taking a scalar relative trace. It must satisfy:

1. finite-prime restrictions recover the ordinary unitary dilations;
2. its Connes cocycle or relative modular generator has the square current as
   its logarithmic anomaly;
3. the primitive return functional remains fixed and continuous;
4. the connected $k\ge3$ tail is determinant class;
5. reciprocal and archimedean sewing act on the correspondence itself;
6. the resulting relative wave trace is defined without a cutoff-dependent
   functional;
7. the completed spectral generator is self-adjoint in the relative standard
   form.

Failure of such a correspondence is a real obstruction to the prime-loop
Hilbert--Pólya programme. Success would explain why a square-grade boundary
channel is exactly what is needed to compare the arithmetic and continuum
worlds.
