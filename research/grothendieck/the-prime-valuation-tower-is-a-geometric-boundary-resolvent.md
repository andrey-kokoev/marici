# The Prime-Valuation Tower Is a Geometric Boundary Resolvent

## Valuation channels

Fix a prime \(p\). Decompose the direct comb trace by exact valuation:

\[
B_+f
=
\sum_{r\geq0}B_{p,r}f,
\]

where

\[
B_{p,r}f
=
\sum_{v_p(k)=r}
k^{-1/2}f(\log k).
\]

The primitive channel is

\[
B_{p,0}f
=
\sum_{p\nmid k}
k^{-1/2}f(\log k).
\]

## Exact transport formula

For \(r\geq0\),

\[
B_{p,0}T_{r\log p}f
=
\sum_{p\nmid n}
n^{-1/2}f(\log(p^rn)).
\]

Writing \(k=p^rn\) gives

\[
B_{p,0}T_{r\log p}f
=
p^{r/2}B_{p,r}f.
\]

Therefore

\[
B_{p,r}
=
p^{-r/2}B_{p,0}T_{r\log p}.
\]

The full local comb is the geometric boundary resolvent

\[
B_+
=
B_{p,0}
\sum_{r\geq0}
p^{-r/2}T_{r\log p}.
\]

Formally,

\[
B_+
=
B_{p,0}
\left(
1-p^{-1/2}T_{\log p}
\right)^{-1}.
\]

The order is functional: the translation acts on the test packet before the
primitive trace.

## Convergence in the positive rigging

On

\[
\mathcal H_{+,\varepsilon}
=
H^1\left(
\mathbb R,
e^{(1+\varepsilon)q}\,dq
\right),
\]

translation satisfies

\[
\lVert T_{r\log p}\rVert
=
p^{-(1+\varepsilon)r/2}.
\]

Thus the \(r\)-th valuation contribution has operator bound

\[
p^{-r/2}
\lVert T_{r\log p}\rVert
=
p^{-(1+\varepsilon/2)r}.
\]

For every fixed prime and every \(\varepsilon\geq0\), the valuation tower is
geometrically summable.

## Global prime threshold

The first nontrivial local correction is bounded at scale

\[
p^{-1-\varepsilon/2}.
\]

For \(\varepsilon>0\),

\[
\sum_p p^{-1-\varepsilon/2}<\infty.
\]

At the critical boundary,

\[
\varepsilon=0,
\]

the global primitive layer becomes

\[
\sum_p\frac1p,
\]

which diverges logarithmically.

Higher valuation depths remain summable over primes because

\[
\sum_p p^{-r}<\infty
\qquad
(r\geq2).
\]

## Structural conclusion

Completion failure is not caused by an infinite tower at any one prime. Each
local tower is a controlled geometric resolvent. The singularity occurs when
the first valuation defect is assembled across all primes at the critical
sector exponent.

Thus the three levels are retyped:

- primitive depth is globally critical;
- square and higher valuation depths are globally summable in this boundary
  norm;
- the parameter \(\varepsilon>0\) is an honest regulator whose removal exposes
  precisely the primitive prime divergence.

## Reciprocal sector

The same argument applies to the reflected comb with translations
\(T_{-r\log p}\). Its local resolvent converges in
\(\mathcal H_{-,\varepsilon}\), and the same primitive global divergence
appears at the critical boundary.

## Next gate

The required relative completion must retain the two divergent primitive
layers as explicit boundary currents and take the \(\varepsilon\downarrow0\)
limit only after reciprocal sewing. Subtracting them independently would erase
the anomaly that the interface is meant to control.

## Falsifier

The theorem fails if the exact valuation transport formula is wrong, if a
fixed-prime tower is not geometric, or if a higher-depth prime sum diverges.
Reindexing and the standard prime-series thresholds settle all three.
