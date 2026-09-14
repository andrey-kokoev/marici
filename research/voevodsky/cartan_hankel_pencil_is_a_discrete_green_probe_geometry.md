# The Cartan--Hankel pencil is a discrete Green probe geometry

## Question

What does the comparison between intrinsic adjacent-prime composition geometry and apparatus-induced character geometry actually compute?

## Claim boundary

On the first \(n+1\) prime-valuation coordinates, adjacent-prime replacements carry the finite type-\(A_n\) Cartan form. Comparing it with the probe-induced Hankel form yields an exact generalized eigenvalue problem controlled by the Green kernel of the prime-index path. This is an index geometry; prime magnitudes enter the separate arithmetic cutoff filtration.

## Valuation-root geometry

Let \(F_{n+1}\) have basis \(f_1,\ldots,f_{n+1}\) for prime valuations, and define

\[
\alpha_i=f_{i+1}-f_i,
\qquad 1\leq i\leq n.
\]

The shell-direction space \(W_n\) maps to \(F_{n+1}\) by \(e_i\mapsto\alpha_i\). Pulling back the coordinate pairing gives

\[
C_{ij}=\langle\alpha_i,\alpha_j\rangle
=
\begin{cases}
2,&i=j,\\
-1,&|i-j|=1,\\
0,&|i-j|>1.
\end{cases}
\]

For \(a=(a_1,\ldots,a_n)\),

\[
a^{\mathsf T}Ca
=a_1^2+a_n^2+
\sum_{i=1}^{n-1}(a_{i+1}-a_i)^2.
\]

Thus \(C\) is the Dirichlet discrete-gradient energy on the prime-index path. It is positive definite and

\[
\det C=n+1.
\]

## Green kernel

The inverse Cartan matrix is

\[
(C^{-1})_{ij}
=
\frac{\min(i,j)\bigl(n+1-\max(i,j)\bigr)}{n+1}.
\]

This is the discrete Dirichlet Green kernel. It measures how a probe covector on shell indices is propagated through the intrinsic root geometry.

## Comparison with character probes

For settings \(T=\{t_1,\ldots,t_m\}\), let

\[
M_{ri}=t_r^i,
\qquad
Q_T=M^{\mathsf T}M.
\]

The generalized Rayleigh quotient is

\[
\mathcal R_T(a)
=
\frac{a^{\mathsf T}Q_Ta}{a^{\mathsf T}Ca}
=
\frac{\sum_{r=1}^{m}\left(\sum_{i=1}^{n}a_it_r^i\right)^2}
{a_1^2+a_n^2+\sum_{i=1}^{n-1}(a_{i+1}-a_i)^2}.
\]

It compares sampled character amplitude with discrete prime-index gradient energy. Its zero directions are exactly the blind interpolation polynomials.

The nonzero generalized eigenvalues of

\[
Q_Ta=\lambda Ca
\]

are the ordinary eigenvalues of the smaller effective matrix

\[
H_T=MC^{-1}M^{\mathsf T}.
\]

The determinant lemma gives

\[
\det(Q_T-\lambda C)
=(-1)^n\lambda^{n-m}\det(C)
\det(\lambda I_m-H_T)
\]

when \(M\) has row rank \(m\). The factor \(\lambda^{n-m}\) is the unresolved geometric dimension.

## Meaning of the two forms

The Cartan form \(C\) records the energetic overlap of adjacent valuation transfers. The Hankel form \(Q_T\) records distinguishability by the selected character settings. Their pencil does not identify these geometries; it compares them.

A blind direction has positive intrinsic root energy and zero apparatus energy. At cube completion, arithmetic realizes such a direction as a route class. Adding a setting removes one zero generalized eigenvalue by a rank-one update of \(Q_T\).

## Strongest falsification attempt

Over exact rationals, verify the Cartan determinant and Green formula through dimension eight. For five shell directions, compute \(Q_T\), \(H_T\), and both sides of the determinant identity for four and five settings. Require the four-setting pencil to have one zero factor and the five-setting pencil none. Verify that the known interpolation radical has zero Hankel energy but strictly positive Cartan energy.

## Disposition

The comparison produces a discrete Green probe geometry: character measurements are filtered through the inverse Laplacian of the prime-index path. The remaining question is whether its generalized spectrum predicts arithmetic completion grades or only probe conditioning after a cube is already present.
