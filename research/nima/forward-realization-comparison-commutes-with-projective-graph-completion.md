# Forward realization comparison commutes with projective graph completion

## Direction matters

The comparison axis is the forward rigged synthesis

\[
U_4:\mathcal A_{\exp}\longrightarrow\mathcal G_4,
\]

not an equivalence. Its Hilbert lower margin is zero, so no bounded inverse or completion-level Morita equivalence is available. That obstruction does not prevent continuity of the forward comparison.

## Completion square

Let `D_0` be the finite-support labelled source. Equip it with the projective exponential seminorms `q_delta`, augmented by the finite occurrence/Laurent fibers required by rooted substitutions and physical cuts. Let

\[
\kappa_A:D_0\to\widehat{\mathcal A},
\qquad
\kappa_G:U_4(D_0)\to\mathcal G_4
\]

be the source and retained-graph completion maps.

The established classification of `U_4` as a continuous graph-valued synthesis means that for every continuous target seminorm `p_a` there are finitely many source seminorms and a constant such that

\[
p_a(U_4x)\le C_a\sum_{j=1}^{m_a}q_{\delta_j}(x).
\]

Therefore the restriction `U_{4,0}` to `D_0` sends source-Cauchy nets to graph-Cauchy nets and has a unique continuous extension

\[
\widehat U_4:\widehat{\mathcal A}\longrightarrow\mathcal G_4.
\]

By construction,

\[
\widehat U_4\kappa_A=\kappa_GU_{4,0}.
\]

This is the generic `R x C` square.

## Occurrence and Laurent fibers

At a fixed local cubical state, the marked occurrence decoration is a finite direct sum, and each physical cut is a finite sum of bounded Laurent translations. The comparison acts coefficientwise on these source labels. Finite direct sums and bounded translations preserve the seminorm estimate above. Thus adjoining the local `H` and `V` decorations does not create a new completion obstruction for the forward map.

This assertion does not supply the separate `C x H` and `C x V` semantic intertwining laws. It says that wherever the finite labelled comparison is already defined, its forward map survives completion.

## Dagger and observations

The comparison dagger remains the continuous transpose

\[
U_4^\dagger:\mathcal G_4'\to\mathcal A_{\exp}'.
\]

It is not promoted to a Hilbert adjoint. Endpoint and other declared boundary rows factor continuously through `U_4` on their individual domains, so their forward completion squares follow from the same uniqueness argument. Assembly on one common Green domain remains the separate `L/O` gate.

## Exact boundary

The theorem proves a directed completion comparison:

\[
\boxed{\text{finite labelled source}\to\text{completed retained analytic graph}.}
\]

It does not prove:

- a bounded inverse for `U_4`;
- equivalence of source and analytic completions;
- the fourth-chart inverse;
- a common graph domain for all Green and boundary operators;
- the missing semantic chart-to-arity intertwiners.

The prime-power atom sequence rules out the first two stronger readings. Therefore `R x C` is strict for the forward comparison and unavailable in the reverse direction.
