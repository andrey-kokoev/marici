# The source endpoint has an explicit sine tail, but the gamma–prime energy is not Dirichlet energy

## Question and tested route

Can the preceding Dirichlet leverage estimate be transferred directly to the differentiated gamma–prime bulk, or should the source endpoint be expanded in the actual bulk representation instead?

The first candidate is an unsmoothed identification of the two energies. The rival retains the actual gamma–prime form and computes the source endpoint coefficients and tail explicitly. The latter gives a source-normalized finite-reduction input without asserting the missing positive factorization.

This is a range/metric comparison obligation. The intended source is the fixed-support logarithmic observer core, not an arbitrary finite matrix substituted for the semilocal bulk.

## Differential-order obstruction to the direct Dirichlet comparison

The source formula in `research/voevodsky/combined-gamma-prime-symbol-localizes-the-bad-frequency-set.md` is, for fixed support L,

\[
a_L(u)=\frac{\operatorname{Re}\psi(1/4+iu/2)-\log\pi}{4\pi}
-\sum_{\log n\le2L}\frac{\Lambda(n)}{\sqrt n}\cos(u\log n).
\]

The prime sum is finite and bounded. The digamma asymptotic gives

\[
a_L(u)=\frac1{4\pi}\log|u|+O_L(1)
\]

as |u| grows. Keep the Fourier normalization of the cited source formula; changing conventions changes constants, not the logarithmic order.

For a real nonzero smooth phi compactly supported strictly inside (-L,L), let f_R(x)=exp(iRx)phi(x). The actual gamma–prime quadratic form has

\[
q_{\Gamma+P}(f_R)=O_L(\log(2+R)).
\]

Indeed its Fourier transform is a translate of the Schwartz function phihat. The bound log(2+|R+u|)<=log(2+R)+log(1+|u|) gives an integrable majorant. The finite prime term remains uniformly bounded. Finite-rank endpoint pairings with exponential vectors decay faster than any power of R by integration by parts on the compactly supported smooth envelope.

In contrast, direct calculation gives

\[
q_D(f_R)=R^2\|\phi\|^2+\|\phi'\|^2+\tfrac14\|\phi\|^2.
\]

Therefore no fixed positive multiple of this unsmoothed Dirichlet energy can be bounded above by the cited gamma–prime form on the full common observer core. This rejects the identity identification; it does not reject a nonlocal smoothing intertwiner or prove a statement about an unconstructed reduction C_k.

If a candidate intertwiner preserves packets near frequency R and satisfies q_D(Tf_R)<=q_(Gamma+P)(f_R), its output norm must decay at least on the scale sqrt(log R)/R. A source transform that does not preserve frequency localization requires its own analysis. The previous Dirichlet formula is thus a comparison calculation, not the missing source metric.

## Keep the source endpoint coefficient instead

Retain the source parity vector without renormalizing it:

\[
b_L(x)=\frac{e^{x/2}-e^{-x/2}}{\sqrt2}
=\sqrt2\sinh(x/2).
\]

On the odd subspace of L2(-L,L), the orthonormal basis

\[
e_n(x)=\frac{\sin(n\pi x/L)}{\sqrt L},\qquad n\ge1,
\]

gives explicit coefficients, with beta_n=n pi/L:

\[
b_n=\langle e_n,b_L\rangle
=(-1)^{n+1}\frac{2\sqrt2\,\beta_n\sinh(L/2)}{\sqrt L\,(1/4+\beta_n^2)}.
\]

They follow by evaluating the antiderivative

\[
\frac{\tfrac12\cosh(x/2)\sin(\beta_nx)
-\beta_n\sinh(x/2)\cos(\beta_nx)}{1/4+\beta_n^2}.
\]

The denominator inequality beta^2/(1/4+beta^2)^2<=1/beta^2 yields

\[
\sum_{n>N}|b_n|^2
\le\frac{8L\sinh^2(L/2)}{\pi^2N},\qquad N\ge1.
\]

This is an analytic all-mode tail bound, not a finite sampling extrapolation. It retains the growing source normalization. If the physical row has an additional declared factor eta_L, the squared bound is multiplied by |eta_L|^2; that factor may not be discarded.

## Coupled leverage, not separate diagonal estimates

Suppose the actual positive bulk operator in the same transported representation has the low/high block form

\[
C=\begin{pmatrix}A&B^*\\B&D\end{pmatrix},\qquad D\succeq c_NI>0.
\]

The endpoint tail contribution then has the certified conditional bound

\[
\langle b_>,D^{-1}b_>\rangle
\le\frac{8L\sinh^2(L/2)}{\pi^2N c_N}.
\]

This is not the full leverage. When the Schur block S=A-B*D^-1B is positive invertible, block elimination gives

\[
\langle b,C^{-1}b\rangle
=\langle b_>,D^{-1}b_>\rangle
+\langle b_<-B^*D^{-1}b_>,
S^{-1}(b_<-B^*D^{-1}b_>)\rangle.
\]

For singular blocks the source range conditions must be checked before using reduced inverses. Neither positivity of separate diagonal blocks nor a small endpoint tail removes the mixed term B.

The checker uses one independent rational matrix solely to test this algebraic issue: coupled leverage is 61/8, whereas ignoring the off-diagonal block gives 41/6. That fixture is not represented as a Weil matrix.

## Source interface and next executable inputs

The coefficients above express the recorded odd exponential endpoint in its logarithmic-position L2 representation. To use them in the genuine canonical/dual metric, the bulk form and endpoint functional must be transported together by the declared source transforms. This has not been replaced by the source-pulled counting metric from the earlier window.

The precise required inputs are now:

1. the actual bulk low block A and low–high map B in this representation;
2. a certified high-block bound c_N with its domain and cutoff dependence;
3. a certified corrected low Schur block and transported endpoint row.

The prior source symbol and concentration construction provide candidates for extracting such bounds; this packet does not assert that a sine cutoff already has a proved c_N. If a concentration-eigenfunction cutoff is used instead, its basis comparison must transport the explicit endpoint row.

## Disposition and verification

Rejected: identifying the actual logarithmic gamma–prime energy with an unsmoothed second-order Dirichlet energy. Constructed: explicit coefficients of the source-shaped odd endpoint in a fixed complete basis, a quantitative tail bound, and the coupled inverse formula needed to keep the endpoint and bulk interaction.

The physical Schur inequality and the global prolate Mosco theorem remain unproved. This does not reopen the already constructed signed Sonin/endpoint map.

`uv run --with sympy python research/nima/checkers/check_source_odd_endpoint_sine_tail.py` exits 0 with six exact checks. Result: `research/nima/results/source-odd-endpoint-sine-tail.json`. The growth comparison uses the displayed analytic asymptotic argument; it was not inferred from the rational matrix fixture.
