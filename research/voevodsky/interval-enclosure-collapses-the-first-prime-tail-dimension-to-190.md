# Interval enclosure collapses the first-prime tail dimension to 190

## Question

Once the corrected bad set is known to lie in \([-100,100]\), should one retain its many-component resonance geometry when constructing the concentration projection?

## Claim boundary

No. Enlarging the bad set to the single interval \([-100,100]\) preserves the tail lower bound and gives an explicit sinc-kernel concentration operator. Its transition trace is logarithmic with a small constant. Exact rational estimates reduce the strict-tail dimension from \(35051\) to \(190\).

## Interval concentration operator

Let \(T_R\) be the time--band concentration operator for

\[
[-L,L]
\quad\text{and}\quad
[-R,R],
\qquad
L=\frac7{20},
\quad R=100.
\]

Its kernel is

\[
K_R(x,y)
=
\frac{\sin(R(x-y))}{\pi(x-y)}.
\]

Because the actual negative-frequency set is contained in \([-R,R]\), controlling concentration into the larger interval is sufficient.

## Transition trace

The endpoint amplitude of \([-R,R]\) is

\[
E(t)=2i\sin(Rt).
\]

Therefore

\[
\operatorname{Tr}(T_R-T_R^2)
=
\frac2{\pi^2}
\left[
\int_0^{2L}\frac{\sin^2(Rt)}{t}dt
+
2L\int_{2L}^\infty
\frac{\sin^2(Rt)}{t^2}dt
\right].
\]

Split the first integral at \(1/R\). Using

\[
\sin^2(Rt)
\leq
\min(1,R^2t^2)
\]

gives

\[
rac2{\pi^2}
\int_0^{2L}
\frac{\sin^2(Rt)}t dt
\leq
\frac{1+2\log(2LR)}{\pi^2}.
\]

The exterior term satisfies

\[
\frac{4L}{\pi^2}
\int_{2L}^\infty
\frac{\sin^2(Rt)}{t^2}dt
\leq
\frac2{\pi^2}.
\]

Hence

\[
\operatorname{Tr}(T_R-T_R^2)
\leq
\frac{3+2\log(2LR)}{\pi^2}.
\]

## Rational bound

Here \(2LR=70\). Since

\[
\log70<\frac{17}{4}
\]

and \(\pi^2>9\),

\[
\operatorname{Tr}(T_R-T_R^2)
<
\frac{23}{18}.
\]

Also,

\[
\operatorname{Tr}(T_R)
=
\frac{2LR}{\pi}
<
\frac{70}{3}.
\]

With the strict threshold \(\eta_*>1/130\),

\[
M
>
\operatorname{Tr}(T_R)
+130\operatorname{Tr}(T_R-T_R^2)
<
\frac{1705}{9}.
\]

Thus

\[
M=190
\]

is sufficient, and the tail compression still satisfies

\[
QAQ\geq\frac1{40}Q.
\]

## Remaining gate

The sufficient finite form is now only

\[
G_{190}
=
PAP
-40\left(PA^2P-(PAP)^2\right).
\]

The projection \(P\) is onto the first \(190\) eigenfunctions of the explicit sinc-kernel operator \(T_R\). Constructing certified enclosures for these eigenfunctions and the two compressed matrices remains open, but the matrix dimension is no longer the obstacle.

## Disposition

The resonance decomposition was useful for the actual bad set but is unnecessary for a conservative finite reduction. Single-interval enlargement reduces the certified first-prime Schur problem to dimension \(190\). Positivity of that matrix is not verified.

## Verification

- `research/voevodsky/checkers/check_interval_enclosure_concentration.py`
- `research/voevodsky/results/interval_enclosure_concentration.json`
