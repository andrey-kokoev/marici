# Cross-context channel coherence (WP391)

## Bounded question

Does WP390's rank-one response factor through the same causal middle object in
every source context and RG frame?

## Joint-context theorem

Let two source-generated contexts have positive rank-one responses

\[
K_1=\chi_1vv^T,
\qquad K_2=\chi_2ww^T.
\]

Each determinant vanishes separately. Their joint response satisfies

\[
\det(K_1+K_2)
=\chi_1\chi_2(v_1w_2-v_2w_1)^2.
\]

Hence both contexts factor through one common channel exactly when their
coupling vectors are collinear after transport into a declared common frame.
Per-context rank one does not establish contextual coherence.

The smallest hostile pair is $v=(1,0)$ and $w=(0,1)$. Both contexts have rank
one, and their projectors even commute, but their sum has rank two. Commutation
is therefore weaker than common-channel factorization.

## RG coherence

For diagonal infinitesimal transport

\[
\frac{dv}{dt}=
\begin{pmatrix}\gamma_1&0\\0&\gamma_2\end{pmatrix}v,
\]

the direction obstruction is

\[
v\wedge\frac{dv}{dt}=g_1g_2(\gamma_2-\gamma_1).
\]

For a channel with both components nonzero, the flavor ratio is constant only
if the two anomalous dimensions agree or a more general transport makes $v$
an eigenvector. Otherwise the response remains rank one at every scale but
does not define the same kernel across scales.

This distinguishes two claims: instantaneous rank-one selection and universal
parallelized channel identity. The latter is strictly stronger.

## Instrument typing

Testing contextual coherence requires two independently sourced contexts,
one named source-to-readout parallelization, and a calibrated positive metric
for normalized response directions. Without the common-frame constructor,
coordinate comparison is unauthorized. With a reference port, the comparison
belongs to the augmented stabilizer groupoid and is relational.

The executable falsifier is a nonzero wedge or a positive second singular
value of the combined response beyond declared uncertainty. This prediction
is independent of fitting the flavor shell in either context separately.

## Disposition

WP391 turns channel uniqueness into a novel cross-context consequence. The
single-channel explanation survives only if every authorized context and RG
scale yields the same normalized response direction after legal transport.
It does not determine that direction or its numerical ratio.

The remaining gate is an admitted parallelization together with a calibrated
two-context rank experiment. A source theory must also explain why all
anomalous dimensions and threshold channels preserve the common line.

Run `uv run --with sympy python
research/flavor/checkers/wp391_cross_context_channel_coherence.py` to
regenerate the result.
