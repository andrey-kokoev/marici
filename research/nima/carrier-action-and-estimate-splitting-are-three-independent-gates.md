# Carrier, action, and estimate splitting are three independent gates

## The tower

A multisector construction can separate at three different levels.

### Carrier splitting

The state object admits source-authorized idempotents

\[
E_iE_j=\delta_{ij}E_i,
\qquad
\sum_iE_i=I.
\]

This makes sectors distinguishable as subobjects.

### Action splitting

The admitted noncentral action algebra can address those subobjects
independently.  In an aligned repeated-block model, this requires full rank of
the sector coefficient vectors carried by noncentral controls.

### Estimate splitting

The independent controls admit cutoff-uniform bounds, equivalently a uniformly
bounded family of right inverses or a positive lower bound on the smallest
nonzero singular value in the declared source norms.

This makes the splitting survive completion.

Each implication between consecutive gates is false without an additional
hypothesis.

## First hostile: carrier without action

For two equivalent simple blocks, the central label

\[
J=(I,-I)
\]

supplies projectors \((I\pm J)/2\).  The carrier splits.  If every noncentral
control remains diagonal \((K,K)\), the action does not split.

## Second hostile: action without estimate

At cutoff \(N\), let the noncentral coefficient matrix be

\[
C_N=
\begin{pmatrix}
1&0\\
0&N^{-1}
\end{pmatrix}.
\]

It has full rank at every finite cutoff, so both sectors are algebraically
addressable.  But

\[
\sigma_{\min}(C_N)=N^{-1}\longrightarrow0,
\]

and the norm of the inverse grows like \(N\).  Independent action disappears
in the completion topology.

Thus finite rank is not completion-stable controllability.

## Categorical form

Carrier splitting is an idempotent-completion statement about objects.  Action
splitting is a fullness statement for the admitted action functor on the split
summands.  Estimate splitting is an enriched or topological statement: the
fullness witnesses must remain bounded under the directed completion.

The resulting progression is:

The progression is: split object → full sector action → bounded full sector action.

The arrows are obligations, not automatic implications.

## Sector readings

### Kitaev

Central block characters split the semisimple endpoint carrier.  The dynamical
Lie algebra must separately split repeated \(\mathfrak{su}_2\) and
\(\mathfrak{su}_3\) blocks.  Physical controls and fault bounds then supply the
estimate gate.

### Strominger

The universal column quotient may split the finite presentation, and a local
Hall atlas may split representative actions.  Growing transition products or
deep-column support can still destroy the completion estimate.

### Theta

Reciprocal sheets and determinant framing split the carrier.  A noncentral
sheet-asymmetric source operator would split the action.  Eventual compact
exclusion or an equivalent source estimate remains the third and RH-bearing
gate.

### Flavor

Two calibrated observer records may split the readout carrier.  Independent
source interventions must split their response action.  Uniform calibration
and error bounds must then survive the physical limit.

## Compiler contract

A sector-completeness claim should report separately:

1. idempotents and their source authority;
2. noncentral action rank on the split sectors;
3. the sharp completion bound in the declared topology.

Missing values are not inferred from the other two.

## Falsifiers

Reject the claim when any of the following occurs:

1. central labels are used as evidence of independent dynamics;
2. finite full rank is used without a cutoff-uniform lower bound;
3. bounds are stated in a presentation norm not preserved by authorized chart
   changes;
4. algebraic action splitting is promoted to physical executability;
5. a completion estimate is fitted after observing the desired limit.

