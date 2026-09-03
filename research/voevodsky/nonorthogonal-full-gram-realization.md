# Nonorthogonal full-Gram analytic realization

## Question

Can the candidate partial equipment retain nonzero typed cross pairings while preserving associative quotient composition and mixed coherence?

## Claim boundary

This packet constructs an exact finite-dimensional positive-definite model whose certificates retain the full Gram matrix. It realizes nonorthogonal Green data but does not supply the missing source maps for the Stieltjes or unbounded sectors.

## Objects and under arrows

An object is a finite tagged rational vector space together with its complete positive-definite Gram matrix. Under arrows are inclusions of principal tagged blocks. Amalgamation is admitted only when a complete positive joint Gram matrix on the union is supplied.

Associativity is strict after tag normalization because every parenthesization restricts the same certified global Gram matrix. Pairwise certificates without a global block remain inadmissible.

## Over arrows

For a decomposition into kernel tags \(K\) and quotient tags \(X\), the over form is the Schur complement

\[
G_{X/K}=G_{XX}-G_{XK}G_{KK}^{-1}G_{KX}.
\]

The projection is therefore interpreted with the quotient form induced by elimination, not with the raw coordinate restriction. This retains nonorthogonal loading without falsely claiming that coordinate projection preserves the original form.

## Exact fixture

Use tags \((k,u,x)\) and

\[
G=
\begin{pmatrix}
2&1/2&1/3\\
1/2&1&1/4\\
1/3&1/4&1
\end{pmatrix}.
\]

The checker verifies every leading principal minor is positive.

Eliminating \(k\) transports the \(u\)-to-\(x\) cross pairing to

\[
\frac14-\frac{(1/2)(1/3)}2=\frac16.
\]

Eliminating \(u\) next gives the same quotient form on \(x\) as eliminating the joint block \((k,u)\) directly. Thus Schur-complement composition is associative on the fixture.

## Beck–Chevalley content

The mixed comparison commutes only when the transported cross block is retained. Reusing the raw value \(1/4\) after eliminating \(k\) gives the wrong second quotient. Hence the Beck–Chevalley cell carries the Schur-updated cross pairing as certificate data.

## Completion

Finite completion is identity, with zero radical and coercivity equal to the smallest eigenvalue. The model therefore realizes completion pasting at finite rank while leaving unbounded closure as a separate gate.

## Disposition

A nonorthogonal full-Gram partial equipment exists at finite rank. It contains the scalar shape of the enlarged Green block and realizes associative over composition by Schur complements. The next executable branch is to test functorial embedding of the actual enlarged Green fixture and gauge quotient into this model, including whether their source conventions select the Schur quotient form.

## Verification

- `research/voevodsky/checkers/check_nonorthogonal_full_gram_realization.py`
- `research/voevodsky/results/nonorthogonal_full_gram_realization.json`
