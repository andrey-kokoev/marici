# Uniform local mass exactly characterizes bounded-multiplier completion of half-line derivative observation

## Question

For a bounded scalar or operator-valued weight on the half-line, is uniform local mass merely sufficient for graph observability, or is it necessary as well?

## Claim boundary

The theorem concerns the row observer consisting of the weak derivative and a bounded multiplication operator on \(H^1(0,\infty;K)\), where \(K\) is a Hilbert space. It gives an equivalence with a fixed-scale weak-operator local-mass condition. It does not cover unbounded weights, fractional derivatives, higher-dimensional domains, or boundary conditions that change the test space.

## Setup

Let \(K\) be a Hilbert space and let

\[
W:(0,\infty)\to B(K)
\]

be weakly measurable and essentially bounded, with

\[
M=\operatorname*{ess\,sup}_{r>0}\|W(r)\|<\infty.
\]

Define

\[
T_W:H^1(0,\infty;K)
\longrightarrow
L^2(0,\infty;K)\oplus L^2(0,\infty;K)
\]

by

\[
T_Wf=(f',Wf).
\]

The source carries the graph norm

\[
\|f\|_{H^1}^2=\|f\|_2^2+\|f'\|_2^2.
\]

## Exact characterization

The following are equivalent.

1. There is \(\delta>0\) such that

   \[
   \|f'\|_2^2+\|Wf\|_2^2
   \ge
   \delta^2\|f\|_2^2
   \]

   for every \(f\in H^1(0,\infty;K)\).

2. There exist \(\ell,\beta>0\) such that every interval \(I\subset(0,\infty)\) of length \(\ell\) satisfies

   \[
   \int_I W(r)^*W(r)\,dr
   \ge
   \beta I_K
   \]

   in the weak-operator order.

Condition 1 is equivalent to bounded-below observation in the full graph norm, since adding \(\|f'\|_2^2\) to the right changes the constant only by a fixed algebraic conversion.

## Sufficiency

Assume condition 2. Partition the half-line into intervals \(I_n\) of length \(\ell\). Fix one interval \(I\). For \(r,s\in I\), the Bochner fundamental theorem and Cauchy--Schwarz give

\[
\|f(r)-f(s)\|^2
\le
\ell\int_I\|f'(t)\|^2dt.
\]

Hence

\[
\|f(r)\|^2
\le
2\|f(s)\|^2
+2\ell\int_I\|f'(t)\|^2dt.
\]

Apply this estimate after pairing the local-mass inequality with \(f(r)\), or equivalently compare \(f(r)\) with the constant vector \(f(s)\), multiply in \(s\) by the positive field \(W(s)^*W(s)\), and integrate. Using

\[
\int_I\|W(s)\|^2ds\le M^2\ell,
\]

one obtains

\[
\beta\|f(r)\|^2
\le
2\int_I\|W(s)f(s)\|^2ds
+2M^2\ell^2\int_I\|f'(t)\|^2dt.
\]

Integrating in \(r\in I\) yields

\[
\int_I\|f(r)\|^2dr
\le
\frac{2\ell}{\beta}
\int_I\|Wf\|^2
+
\frac{2M^2\ell^3}{\beta}
\int_I\|f'\|^2.
\]

Summing over the partition gives

\[
\|f\|_2^2
\le
C_W\|Wf\|_2^2+C_D\|f'\|_2^2,
\]

where

\[
C_W=\frac{2\ell}{\beta},
\qquad
C_D=\frac{2M^2\ell^3}{\beta}.
\]

Thus condition 1 holds with the explicit admissible value

\[
\delta^2=rac{1}{\max(C_W,C_D)}.
\]

The estimate is not claimed sharp.

## Necessity

Assume condition 1 with constant \(\delta>0\). Fix an interval

\[
I=(a,a+\ell)
\]

and a unit vector \(\xi\in K\). Define the sine packet

\[
f_{I,\xi}(r)=
\begin{cases}
\sin\!\left(\dfrac{\pi(r-a)}{\ell}\right)\xi,&r\in I,\\
0,&r\notin I.
\end{cases}
\]

This belongs to \(H^1(0,\infty;K)\), and

\[
\|f_{I,\xi}\|_2^2=\frac{\ell}{2},
\qquad
\|f_{I,\xi}'\|_2^2=\frac{\pi^2}{2\ell}.
\]

Since the sine factor has modulus at most one,

\[
\|Wf_{I,\xi}\|_2^2
\le
\int_I\|W(r)\xi\|^2dr.
\]

The assumed lower bound therefore implies

\[
\int_I\|W(r)\xi\|^2dr
\ge
\frac{\delta^2\ell}{2}
-
\frac{\pi^2}{2\ell}.
\]

Choose any fixed

\[
\ell>\frac{\pi}{\delta}.
\]

Then

\[
\beta=
\frac{\delta^2\ell}{2}
-
\frac{\pi^2}{2\ell}>0,
\]

uniformly in \(I\) and the unit vector \(\xi\). Hence

\[
\int_IW(r)^*W(r)\,dr\ge\beta I_K.
\]

This proves necessity.

## Graph-norm conversion

If

\[
\|f'\|_2^2+\|Wf\|_2^2
\ge
\delta^2\|f\|_2^2,
\]

then

\[
\|f'\|_2^2+\|Wf\|_2^2
\ge
\frac{\delta^2}{1+\delta^2}
\bigl(\|f\|_2^2+\|f'\|_2^2\bigr).
\]

Indeed, the left side already dominates \(\|f'\|_2^2\), and combining the two lower bounds gives the displayed harmonic constant. Conversely, a graph-norm lower bound immediately implies condition 1.

## Scalar specialization

For \(K=\mathbb C\) and \(W=M_w\), the characterization becomes

\[
(f',wf)\text{ is bounded below on }H^1(0,\infty)
\]

if and only if there exist \(\ell,\beta>0\) such that

\[
\int_I|w(r)|^2dr\ge\beta
\]

for every interval \(I\) of length \(\ell\).

Thus the earlier uniform-local-mass hypothesis is not merely sufficient among bounded weights; it is exact.

## Failure criterion

The negation is also exact. Stable observation fails if and only if, for every \(\ell>0\),

\[
\inf_{|I|=\ell}
\inf_{\|\xi\|=1}
\int_I\|W(r)\xi\|^2dr=0.
\]

The direction \(\xi\) may depend on the interval. This is essential for multiplicity-valued weights: large scalar mass in every interval does not help if each interval contains a nearly invisible multiplicity direction.

## Reciprocal and Real observers

Apply the theorem with

\[
K_{\mathrm{bulk}}=K\oplus K
\]

and \(W(r)=\mathcal M_\pm(A(r),C(r))\) from the reciprocal block classification. Since the even and odd fields have equal Gramians,

\[
\mathcal M_-^*\mathcal M_-
=
\mathcal M_+^*\mathcal M_+,
\]

they satisfy the local-mass criterion simultaneously and have identical graph-observability strength. Their reciprocal variances remain opposite.

Fixed-fiber Real covariance restricts \(A\) and \(C\), but it does not imply the local-mass inequality. The covariance and coercivity gates remain independent.

## Comparison transport

If \(C_0:K\to K'\) is boundedly invertible and the weight transports fiberwise by

\[
W'(r)=C_0W(r)C_0^{-1},
\]

then uniform local mass persists with condition-number loss after the source and target metrics are tracked. Exact invariance requires unitary \(C_0\). This is the fiberwise instance of the nonunitary comparison theorem.

## Deliberate failures

1. Positive total mass \(\int_0^\infty\|W(r)\|^2dr\) does not imply uniform local mass.
2. A weight nonzero on every interval need not have a uniform positive local lower bound.
3. Uniform lower mass of the operator norm does not imply the weak-operator inequality; an invisible multiplicity direction can remain.
4. Real or reciprocal covariance does not imply coercivity.
5. Finite positive sampling of intervals does not establish the universal interval condition.

## Disposition

For bounded operator-valued weights on the half-line, fixed-scale uniform local mass is necessary and sufficient for derivative-plus-multiplier graph observability. The theorem is dimension-independent in the multiplicity Hilbert space and applies directly to the reciprocal-even and reciprocal-odd block families. This closes the previously deferred analytic gate and sharpens the scalar sufficient condition to an equivalence.
