# Restricted generalized singular values certify conditioned pullback

Owner: marici.Kitaev

## Question

What finite, basis-independent certificate represents the conditioning part of
a bidirectional requirement pullback along a chain of linear constructors?

## Claim boundary

Let \(S\subseteq X\) be the source-generated reachable subspace and let
\(B:\mathbb F^r\to X\) be any injective basis map with image \(S\). For a
linear constructor \(F:X\to Y\), define the restricted lower gain

\[
c(F\mid S)^2
=
\lambda_{\min}
\left(
B^*F^*FB,\,
B^*B
\right),
\]

the smallest generalized eigenvalue of the displayed Hermitian pencil. This
is equivalent to

\[
c(F\mid S)
=
\inf_{0\ne x\in S}
\frac{\|Fx\|}{\|x\|}.
\]

The value is independent of the chosen basis coordinates for \(S\). It is
positive exactly when

\[
S\cap\ker F=\{0\},
\]

or equivalently when \(FB\) has rank \(r\).

For a constructor chain

\[
X_0\xrightarrow{F_1}X_1
\xrightarrow{F_2}\cdots
\xrightarrow{F_m}X_m,
\]

propagate reachable subspaces by

\[
S_0=S,
\qquad
S_j=F_jS_{j-1}.
\]

Define \(c_j=c(F_j\mid S_{j-1})\). Then

\[
c(F_m\cdots F_1\mid S_0)
\ge
\prod_{j=1}^m c_j.
\]

The product is a compositional certificate, not generally the sharp constant.
The sharp constant is obtained from the generalized eigenvalue of the full
product restricted to \(S_0\).

This gives a finite conditioned pullback rule. A requested final lower gain
\(\gamma\) is discharged when either the sharp composite gain or an
authorized compositional lower bound is at least \(\gamma\). Failure
returns the restricted kernel witness or the deficient generalized
eigenvector.

For a cutoff family \((F_N,S_N)\), finite faithfulness is

\[
c(F_N\mid S_N)>0
\]

for every \(N\). Completion-stable faithfulness is the strictly stronger
condition

\[
\inf_N c(F_N\mid S_N)>0.
\]

## Hostile cases

1. Globally singular but context-faithful:

\[
F(y_1,y_2)=y_1,
\qquad
S=\operatorname{span}(1,0).
\]

The global lower gain is zero, while \(c(F\mid S)=1\).

2. Nonsharp stagewise product:

\[
F=\operatorname{diag}(\varepsilon,1),
\qquad
G=\operatorname{diag}(1,\varepsilon).
\]

Each stage has lower gain \(\varepsilon\), so the product certificate is
\(\varepsilon^2\), while \(GF=\varepsilon I\) has sharp gain
\(\varepsilon\).

3. Finite faithfulness without completion stability:

\[
F_N=\operatorname{diag}(1,N^{-1}),
\qquad
S_N=\mathbb F^2.
\]

Every cutoff is injective, but the lower gain tends to zero.

4. Basis-scaling hostile: replacing \(B\) by \(BT\) for an invertible,
badly scaled \(T\) changes ordinary singular values of \(FB\) but leaves
the generalized pencil value invariant.

5. Reachability-erasure hostile: testing \(F_j\) on all of \(X_{j-1}\)
rather than on \(S_{j-1}\) can manufacture a kernel direction that no
authorized source constructor reaches.

## Disposition

A finite quantitative requirement record should contain:

- the source-generated reachable basis or projector;
- its inherited Gram matrix;
- the restricted constructor matrix;
- restricted kernel rank;
- sharp generalized lower gain;
- any cheaper compositional lower bound;
- cutoff index and claimed uniform infimum;
- the task quotient, if some output directions are intentionally identified.

For D(S3), the reachable object must be the actual microscopic control
stabilizer restricted to the endpoint module, not the whole ambient operator
space.

For the RH lane, the reachable object must be the admissible dynamical
scalar-null pullback, not every formal boundary state. The missing theorem is
then a cutoff-uniform restricted lower gain for the sewn backward witness.

No physical or RH claim follows until the matrices and reachable subobjects
are independently source-derived.
