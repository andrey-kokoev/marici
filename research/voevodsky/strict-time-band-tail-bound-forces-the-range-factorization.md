# A strict time-band tail bound forces the range factorization

## Question

Once the time--band argument makes the local Weil tail positive, can the finite/tail coupling be factored through the square root of the tail form?

## Claim boundary

Yes, provided the time--band threshold is chosen with a strict positive \(L^2\) margin and the finite trial vectors have \(L^2\)-bounded cross functionals. Under these explicit premises, the range-compatible factorization follows by continuity in the tail energy norm. This reduces local positivity to a finite-dimensional Schur form, but does not prove that form positive.

## Strict tail margin

Choose \(R,M\) so that

\[
\delta_{L,R,M}
=
m_R-(m_R+C_{\rm low}(R))\lambda_{M+1}(L,R)
-C_{\rm prime}(L)
>0.
\]

After adjoining endpoint representers to the finite trial space, every tail vector \(y\) obeys

\[
C_M[y]
\geq
\delta_{L,R,M}\lVert y\rVert_2^2.
\]

This is a strict bound in the \(L^2\) norm, not a coercive bound in the ambient positive Sobolev norm. It is compatible with compactness of the Sobolev representing operator.

## Cross-functional bound

Let \(X_M\) be the finite trial space. Require each \(x\in X_M\) to lie in the domain for which the gamma cross multiplier is square-integrable. Then

\[
|\Gamma_L(x,y)|
\leq
\lVert m\widehat x\rVert_2\lVert y\rVert_2.
\]

The finite prime translation sum gives

\[
|P_L(x,y)|
\leq
K_{P,L}(x)\lVert y\rVert_2.
\]

Endpoint cross terms vanish on the chosen tail. Hence for a finite constant \(K_L(x)\),

\[
|B_M(x,y)|
\leq
K_L(x)\lVert y\rVert_2.
\]

Combining this with the strict tail margin gives

\[
|B_M(x,y)|
\leq
\frac{K_L(x)}{\sqrt{\delta_{L,R,M}}}
C_M[y]^{1/2}.
\]

## Riesz factorization

Complete the tail modulo its null space in the energy norm \(C_M[y]^{1/2}\). The displayed inequality makes \(B_M(x,\cdot)\) continuous on that energy space. Riesz representation supplies \(D_M^*x\) satisfying

\[
B_M(x,y)
=
\langle D_M^*x,C_M^{1/2}y\rangle.
\]

Equivalently,

\[
B_M=D_MC_M^{1/2}.
\]

Because \(X_M\) is finite-dimensional, the individual bounds assemble into a bounded operator \(D_M\).

## Finite reduction

The completed square is

\[
Q_L(x+y)
=
\lVert C_M^{1/2}y+D_M^*x\rVert^2
+
\langle S_Mx,x\rangle,
\]

where

\[
S_M=F_M-D_MD_M^*.
\]

Therefore

\[
Q_L\geq0
\quad\Longleftrightarrow\quad
S_M\geq0
\]

once the strict tail and cross-domain premises are verified.

## Remaining effective data

A finite certificate still requires:

1. explicit \(R,M\) with \(\delta_{L,R,M}>0\);
2. a declared trial basis satisfying \(m\widehat x\in L^2\);
3. interval-enclosed matrix entries for \(S_M\);
4. proof of \(S_M\geq0\) for every support window required by the Weil criterion.

The last condition is RH-bearing. It is not inferred from this reduction.

## Disposition

The range-factorization obligation is discharged conditionally on explicit time--band constants and trial-vector regularity. The remaining local obstruction is the finite Schur form \(S_M\), together with effectiveness and support-uniform quantifiers. No RH implication is asserted.

## Verification

- `research/voevodsky/checkers/check_strict_tail_range_factorization.py`
- `research/voevodsky/results/strict_tail_range_factorization.json`
