# Cauchy expectation exactly normalizes every finite Euler exponential

The Cauchy-character realization does more than linear centering. Its mean is a
multiplicative semicharacter on positive Mellin frequencies.

Let

\[
X_x(T)=e^{-iTx},
\qquad
\mathbb E X_x=e^{-x/2},
\]

for the centered Cauchy observer of scale \(1/2\). For a finite prime set
\(X\), define

\[
L_X(T)
=
\sum_{p\in X}\sum_{k\ge1}
\frac{p^{-k/2}X_{k\log p}(T)}{k}.
\]

Then

\[
e^{L_X(T)}
=
\prod_{p\in X}
\left(1-p^{-1/2-iT}\right)^{-1}.
\]

Expanding by unique factorization and applying the Cauchy mean termwise gives

\[
\mathbb E e^{L_X}
=
\sum_{\substack{n\ge1\\p\mid n\Rightarrow p\in X}}
n^{-1/2}\mathbb E X_{\log n}
=
\sum_{\substack{n\ge1\\p\mid n\Rightarrow p\in X}}
\frac1n
=
\prod_{p\in X}(1-p^{-1})^{-1}.
\]

On the other hand,

\[
\mathbb E L_X
=
\sum_{p\in X}\sum_{k\ge1}\frac1{k p^k}
=
\log\prod_{p\in X}(1-p^{-1})^{-1}.
\]

Therefore the nonlinear identity is exact:

\[
\mathbb E e^{L_X}
=
e^{\mathbb E L_X}.
\]

Equivalently, the normalized Euler exponential

\[
Z_X(T)
=
\exp\left(L_X(T)-\mathbb E L_X\right)
\]

has

\[
\mathbb E Z_X=1.
\]

Thus there is no finite-cutoff centering-versus-exponentiation anomaly in the
mean. The special Cauchy semicharacter and unique factorization make the two
orders agree exactly at the scalar expectation port.

The obstruction moves to topology and quadratic control. As the cutoff grows,

\[
\mathbb E L_X
=
\sum_{p\in X}-\log(1-p^{-1})
\]

diverges, while the normalized positive-density analogue is known to lose
uniform integrability. Mean one at every cutoff does not supply a nonzero
completed state. The finite martingale may converge weakly or almost surely
to zero while its mass escapes into rare events.

This isolates the completion theorem needed by the Green programme:

1. retain \(Z_X\) before taking its scalar mean;
2. compute its two-point Cauchy covariance;
3. split primitive fluctuation from square compensator;
4. attach the theta/archimedean boundary carrier;
5. prove uniform integrability or a source-authorized distributional
   replacement.

The rank-two endpoint transport should therefore be sought in the covariance
of \(Z_X\), not in the covariance of the linear logarithm alone. Its finite
normalization is already exact and source-derived.

The sharp hostile is a mean-one family \(Z_X\) converging almost surely to
zero. Every finite scalar Euler identity passes, but no Hilbert or \(L^1\)
completion survives. Another hostile has bounded first moments but divergent
second moments, destroying the proposed Green Gram.

The new conclusion is precise: nonlinear Euler descent through the Cauchy
observer is solved at finite scalar level; the missing information is exactly
completion-stable quadratic mass.
