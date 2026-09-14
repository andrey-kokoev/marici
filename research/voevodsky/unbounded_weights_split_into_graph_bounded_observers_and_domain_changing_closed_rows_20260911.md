# Unbounded weights split into graph-bounded observers and domain-changing closed rows

## Question

How far does the exact half-line local-mass criterion extend when the multiplier is not essentially bounded?

## Claim boundary

The packet proves an extension for operator-valued weights with uniform local square-integrability of the operator norm. Such weights may be pointwise unbounded but define bounded observers on the original \(H^1\) graph source. More singular multipliers define closed rows on a smaller intersection domain; their apparent coercivity may come from domain restriction and is not promoted to observability of the original graph source.

## Two constructor types

Let \(K\) be a Hilbert space and let

\[
W:(0,\infty)\to B(K)
\]

be weakly measurable, with finite operator norm almost everywhere.

### Graph-bounded multiplier observer

This role requires

\[
M_W:H^1(0,\infty;K)\to L^2(0,\infty;K)
\]

to be bounded on all of \(H^1\). It can enter the existing graph-observer Gramian and Calkin calculus.

### Domain-changing closed multiplier row

The maximal multiplication operator has domain

\[
\operatorname{Dom}M_W
=
\{f\in L^2:Wf\in L^2\}.
\]

The row

\[
T_Wf=(f',Wf)
\]

is defined on

\[
\mathcal D_W=H^1(0,\infty;K)\cap\operatorname{Dom}M_W.
\]

With norm

\[
\|f\|_{\mathcal D_W}^2
=
\|f\|_2^2+\|f'\|_2^2+\|Wf\|_2^2,
\]

this is a Hilbert graph domain when the multiplication operator is closed. A lower bound on \(\mathcal D_W\) is a theorem about this smaller source. It does not certify observation of every vector in the original \(H^1\) source.

## Uniform local upper mass

Fix \(\ell>0\). Assume

\[
\Lambda=
\sup_{|I|=\ell}
\int_I\|W(r)\|^2dr
<\infty.
\]

This condition permits pointwise-unbounded weights. It implies graph boundedness.

Indeed, for \(f\in H^1(I;K)\), choose any \(r\in I\). The Bochner variation estimate gives

\[
\|f(s)\|^2
\le
2\|f(r)\|^2
+2\ell\int_I\|f'\|^2.
\]

Averaging an unweighted point estimate for \(f(r)\), or using the standard one-dimensional local Sobolev inequality, yields

\[
\sup_{s\in I}\|f(s)\|^2
\le
\frac{2}{\ell}\int_I\|f\|^2
+2\ell\int_I\|f'\|^2.
\]

Therefore

\[
\int_I\|Wf\|^2
\le
\Lambda
\left(
\frac{2}{\ell}\int_I\|f\|^2
+2\ell\int_I\|f'\|^2
\right).
\]

Summing a disjoint partition into intervals of length \(\ell\) proves boundedness \(H^1\to L^2\).

## Exact local-mass theorem in the graph-bounded unbounded class

Under the uniform local upper-mass assumption, the following are equivalent.

1. There is \(\delta>0\) such that

   \[
   \|f'\|_2^2+\|Wf\|_2^2
   \ge
   \delta^2\|f\|_2^2
   \]

   for every \(f\in H^1(0,\infty;K)\).

2. There is \(\beta>0\) such that every interval \(I\) of length \(\ell\) satisfies

   \[
   \int_IW(r)^*W(r)\,dr
   \ge
   \beta I_K.
   \]

The fixed length in condition 2 may differ from the original upper-mass length; replacing both by a common integer multiple preserves finite upper mass and positive lower mass.

## Sufficiency

Let \(I\) have length \(\ell\), and assume both

\[
\int_IW^*W\ge\beta I_K
\]

and

\[
\int_I\|W\|^2\le\Lambda.
\]

For fixed \(r\in I\), apply the lower operator inequality to the constant vector \(f(r)\), then compare \(f(r)\) with \(f(s)\):

\[
\begin{aligned}
\beta\|f(r)\|^2
&\le
\int_I\|W(s)f(r)\|^2ds\\
&\le
2\int_I\|W(s)f(s)\|^2ds
+2\int_I\|W(s)\|^2\|f(r)-f(s)\|^2ds\\
&\le
2\int_I\|Wf\|^2
+2\ell\Lambda\int_I\|f'\|^2.
\end{aligned}
\]

Integrating in \(r\) gives

\[
\int_I\|f\|^2
\le
\frac{2\ell}{\beta}\int_I\|Wf\|^2
+
\frac{2\ell^2\Lambda}{\beta}\int_I\|f'\|^2.
\]

Summation over the half-line gives the lower bound with the admissible constant

\[
\delta^2=
\frac{1}{
\max\left(
2\ell/\beta,
2\ell^2\Lambda/\beta
\right)}.
\]

This recovers the bounded-weight estimate by taking \(\Lambda\le\ell\|W\|_\infty^2\).

## Necessity

Graph boundedness ensures that every compactly supported sine packet lies in the observer domain. If condition 1 holds, use

\[
f_{I,\xi}(r)
=
\sin\!\left(\frac{\pi(r-a)}{L}\right)\xi
\]

on an arbitrary interval \(I=(a,a+L)\), where \(\|\xi\|=1\). Then

\[
\int_I\|W(r)\xi\|^2dr
\ge
\frac{\delta^2L}{2}-\frac{\pi^2}{2L}.
\]

Any fixed \(L>\pi/\delta\) gives a positive uniform lower mass. Thus the necessity argument does not require pointwise boundedness, only admissibility of the sine packets.

## Form-bounded formulation

A multiplier quadratic form

\[
q_W[f]=\|Wf\|_2^2
\]

is graph-form-bounded when

\[
q_W[f]
\le
a\|f'\|_2^2+b\|f\|_2^2
\]

for all \(f\in H^1\). This condition is sufficient to keep the observer on the original graph source. Uniform local upper mass supplies an explicit form bound.

For scalar nonnegative \(|w|^2\), uniform local integrability is also the standard one-dimensional criterion behind such a bound. For general operator-valued fields, the operator-norm upper condition is sufficient but may be stronger than necessary because different fiber directions can vary with \(r\). No converse in terms of \(\int_I\|W\|^2\) is asserted for arbitrary infinite-dimensional \(K\).

If only a relative form estimate on a proper form core is known, the source, closure, and form domain must be declared before any reconstruction claim.

## Singular domain-change example

Take the scalar weight

\[
w(r)=\frac1r
\]

near \(r=0\). Multiplication by \(w\) is not bounded from all of \(H^1(0,\infty)\) to \(L^2\): a function with nonzero trace at zero produces \(f/r\notin L^2\).

The intersection domain forces sufficient vanishing at the endpoint and is closely related to an \(H^1_0\)-type condition. Hardy's inequality may then give coercivity. That coercivity partly reflects the restricted domain. It cannot be reported as an observer completion of the original unrestricted \(H^1\) source.

This is a constructor-role distinction:

- bounded or graph-form-bounded \(W\): observer on the existing graph source;
- singular \(W\) with proper intersection domain: new closed source constructor plus observer.

## Reciprocal and Real compatibility

For multiplicity-valued block fields \(\mathcal M_\pm(A,C)\), reciprocal and Real covariance are pointwise algebraic conditions. They remain meaningful for pointwise-unbounded fields on their maximal multiplication domains only if those domains are invariant under \(W_u\) and \(J_u\).

Equal formal block identities do not prove domain invariance. In the graph-bounded class, invariance follows when the multiplier fields satisfy the classified covariance identities as bounded maps \(H^1\to L^2\). In the domain-changing class, invariance must be checked separately.

## Calkin eligibility

If \(M_W:H^1\to L^2\) is bounded, then its graph Gramian is a bounded endomorphism of \(H^1\) and has a graph Calkin class. Pointwise unboundedness does not obstruct this conclusion.

If \(M_W\) is only defined on the proper domain \(\mathcal D_W\), then the old \(H^1\) Calkin class is unavailable. One may instead study bounded observation on the newly declared Hilbert source \(\mathcal D_W\), but that changes the reconstruction objective.

## Deliberate failures

1. Pointwise unbounded does not imply graph-unbounded.
2. A closed row on \(H^1\cap\operatorname{Dom}M_W\) does not imply an observer on all of \(H^1\).
3. Coercivity created by a singular endpoint domain is not evidence of bulk observation on the unrestricted source.
4. Lower local mass without an upper regularity hypothesis does not justify the sufficiency proof used here.
5. Operator-valued graph form boundedness is not identified with operator-norm local upper mass without a converse theorem.
6. Formal reciprocal or Real covariance does not imply invariance of a singular multiplier domain.

## Disposition

The exact uniform-local-mass characterization extends from essentially bounded weights to pointwise-unbounded weights with uniform local operator-norm square mass. This class remains bounded on the original \(H^1\) graph source. More singular weights define a different closed graph domain; their coercivity must be typed as reconstruction on that new source, not as completion of the original observer. The unresolved frontier is a necessary-and-sufficient form criterion for general operator-valued fields beyond the operator-norm upper class.
