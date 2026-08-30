# Semantic pullback needs a fourth completion gate

## Result

The port/domain/coherence trichotomy is complete only for a fixed finite
presentation. A fourth, independent residual appears when the claimed compiler
must extend through a limit or completion.

The four gates are:

1. source-state separation;
2. target-image admission;
3. preservation of composition and defining relations;
4. continuous, distinction-preserving extension through completion.

The fourth failure requires a completion topology, boundary fiber, graph norm,
or explicit refusal to complete. None of the first three repairs supplies it.

## Exact hostile family

At cutoff \(N\), let

\[
F_N=\operatorname{diag}(1,1/2,\ldots,1/N).
\]

Every \(F_N\) is invertible. Thus source states are separated, its declared
finite target image is attained, and the identity constructor is preserved
exactly. Nevertheless its smallest singular value is \(1/N\). For the final
basis vector \(e_N\),

\[
\lVert e_N\rVert=1,
\qquad
\lVert F_Ne_N\rVert=1/N\longrightarrow0.
\]

Consequently there is no cutoff-independent inverse bound. Finite faithfulness
does not survive as stable faithfulness of the completed system.

## Grothendieck's boundary repair

For the reciprocal theta windows, compactifying prime scale by \(r=1/p\)
produces a boundary value at \(r=0\). The correct completed object is the
labelled graph \((r,W_r)\), not the unlabelled image \(W_r\). Fourier transport
sends the boundary fiber to the already typed constant-delta plane.

This is precisely a fourth-gate repair: retain the limiting provenance as a
boundary object and construct its incidence maps. It does not, by itself, prove
convergence of the primitive or square currents.

## Categorical formulation

Let \(F:C\to D\) pass the first three gates on every finite subcategory
\(C_N\). A completion claim additionally requires a specified extension

\[
\widehat F:\widehat C\to\widehat D
\]

that preserves the distinctions named by the target claim. Existence of all
finite restrictions \(F_N\) does not construct \(\widehat F\), and pointwise
injectivity of the restrictions does not imply a closed image or a uniform
inverse bound.

## Finite falsifier

The checker rejects any compiler that classifies the diagonal family as fully
valid merely because every finite matrix has full rank. It must return the
typed residual `completion_stability` once the lower bounds are not uniform.

