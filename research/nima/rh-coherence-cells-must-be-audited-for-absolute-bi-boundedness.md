# RH coherence cells must be audited for absolute bi-boundedness

## Final generic correction

Completion stability does not follow from bounded condition numbers
\[
\kappa(T)=\|T\|\,\|T^{-1}\|.
\]
For scalar transport \(T=cI\),
\[
\kappa(T)=1
\]
for every nonzero \(c\), while repeated composition multiplies absolute source energy by powers of \(|c|\).

The required composite estimates are separate:
\[
\sup_\gamma\|T_\gamma\|<\infty,
\qquad
\sup_\gamma\|T_\gamma^{-1}\|<\infty,
\]
where \(\gamma\) ranges over canonical coherence transports of arbitrary constructor depth, cutoff, bracketing, and compact off-seam parameter region.

In the projective topology, both forward and inverse seminorm envelopes must be bounded separately.

## Completed generic classification

### Source-unitary

The cell is isometric in the frozen source topology. Arbitrary coherent composites remain isometric.

### Uniformly bi-bounded

The cell is nonunitary, but canonical composites and inverses have separate depth-independent bounds.

### Conditioned only

Only \(\|T\|\|T^{-1}\|\) is controlled. This is insufficient because absolute scale may drift.

### Generatorwise only

Individual cells and inverses are bounded, but long composites are uncontrolled. This is also insufficient.

### Unclassified

The cell exists algebraically or formally, but no source-topology estimate has been established.

## Scalar coboundary hostile

Let a retyping at depth \(n\) be
\[
T_n=c^nI,\qquad c>1.
\]
Every comparison is scalar, all coherence diagrams commute, and
\[
\kappa(T_n)=1.
\]
Nevertheless,
\[
\|T_n\|=c^n\to\infty,
\qquad
\|T_n^{-1}\|=c^{-n}\le1.
\]
Reversing \(c\) exchanges amplification and suppression.

Thus a nonunitary coboundary can preserve categorical coherence and perfect condition number while destroying the absolute source-energy scale.

## Concrete RH cell audit

The current evidence supports the following conservative classification.

### Moving-seam transport

**Current status:** source-unitary at the geometric fiber-transport level.

The SCC report explicitly constructs moving-seam unitary transport. This establishes isometry for the bare geometric continuation. It does not establish unitarity after grade-dependent Adams weighting or Mellin/Green normalization.

Required next check:
\[
U_{\beta\alpha}=U_\beta U_\alpha
\]
in the frozen source topology, with cutoff and reciprocal/Real compatibility.

### Determinant-line phase associators

**Current status:** conditionally source-unitary.

If the associator is genuinely multiplication by a modulus-one phase in the authorized determinant-line Hermitian metric, it is unitary and depth-stable. If represented through nonunitary trivializations, the scalar phase presentation is insufficient.

Required evidence:

- the determinant-line metric;
- unitarity of the authorized trivializations;
- compatibility of the \(H^3\) class under cutoff.

### Real and reciprocal involutions

**Current status:** expected isometric only after source typing; not yet promoted.

An involution may be algebraically invertible without preserving the source energy. The audit must prove separate norm preservation in the actual completed fibers.

### Left and right unitors

**Current status:** schema-constructed, analytic status open.

Formal unitors are part of the finite coherence basis. They are unitary only if insertion/removal of the source unit preserves the frozen energy exactly. Endpoint or archimedean normalization can make them nonunitary.

### Weighted Adams cells

**Current status:** nonunitary and unclassified at composite depth.

The positive Adams cocycle is constructed, but grade-wise weighted/type-fiber naturality remains open. Its multiplicative coefficients are the most direct source of absolute scale accumulation.

Required invariant:
\[
\sup_\gamma\prod_{\alpha\in\gamma}a(\alpha),
\qquad
\inf_\gamma\prod_{\alpha\in\gamma}a(\alpha),
\]
after the exact source-energy renormalization. Either both are controlled or a source-authorized metric must absorb the cocycle.

### Fourier–Tate transport

**Current status:** mixed.

The discrete Fourier–Bohr valuation-port atom and moving-seam Fourier transport are constructed, but discrete-port completion is not norm-continuous Mellin completion. Fourier components may be unitary in their natural \(L^2\) topology while the Tate/Mellin normalization changes scale.

The transform and normalization factors must be separated.

### Mellin half-density normalization

**Current status:** nonunitary candidate; absolute scale open.

The coefficient
\[
\frac1k p^{-k/2}
\]
is source arithmetic data, not a harmless unitary phase. Repeated assembly may suppress norms. Whether this is legitimate source-energy weighting or unstable coherent transport depends on where the weight lives:

- in the object norm;
- in the assembly arrow;
- or in the observer.

These placements are not interchangeable.

### Endpoint and archimedean cells

**Current status:** source inhabitants open.

SCC identifies \(F_{\mathrm{endpoint}}\) and \(F_\infty\) as exact frontier holes. No unitarity or bi-boundedness claim is authorized before these cells are constructed.

### Green coherent/disagreement splitting

**Current status:** generally nonunitary.

The splitting is orthogonal only if derived from the complete Green metric after gauge reduction. Nonorthogonal splittings can accumulate projection constants. Their canonical transports need separate forward and inverse bounds.

### Schur and determinant normalization

**Current status:** nonunitary and local.

Finite Schur reductions are exact, but inverses of retained blocks and determinant normalization can amplify with depth. Exact algebraic elimination does not provide a depth-independent norm bound.

## Source-metric unitarization equation

For a coherence generator \(T_\alpha:H_s\to H_t\), seek positive source metrics \(G_s,G_t\) satisfying
\[
T_\alpha^*G_tT_\alpha=G_s.
\]
A compatible family of such equations would unitarize the cell system.

For the entire constructor category, the metrics must be compatible with:

- cutoff inclusions;
- Adams composition;
- seam transport;
- unitors and associators;
- endpoint and archimedean cells;
- reciprocal/Real structure;
- bounded-energy completion.

Solving each equation independently is insufficient; the metric family itself must satisfy the coherence diagrams.

## Cocycle test for positive weights

Write the positive scale of a cell as \(a(\alpha)>0\). It is absorbable by object weights \(g(s)>0\) exactly when
\[
a(\alpha)^2=\frac{g(s)}{g(t)}
\]
for \(\alpha:s\to t\), consistently across all paths.

This says the logarithmic scale cocycle is a coboundary. If its holonomy is nontrivial, no global source metric unitarizes the system.

Even when it is a coboundary, the resulting \(g\) must be uniformly bounded above and below across cutoff and constructor depth. Otherwise the gauge change merely hides absolute scale drift.

## Concrete next theorem

The next source calculation should produce a table for every RH coherence cell containing:

1. source and target energy spaces;
2. exact operator and inverse;
3. unitary, bi-bounded, conditioned-only, generatorwise-only, or unclassified status;
4. separate forward and inverse envelopes;
5. positive scale cocycle;
6. candidate unitarizing metric;
7. cutoff/depth uniformity;
8. authority locator.

The immediate attack should start with the weighted Adams plus moving-seam composite, because its geometric factor is already unitary and its positive scale isolates the absolute-energy obstruction.

## Next hostile

Use a perfectly coherent positive Adams coboundary with canonical depth-\(n\) transport
\[
T_n=c^nU_n,
\]
where \(U_n\) is unitary and \(c>1\). Then:

- all finite coherence identities pass;
- every condition number equals one;
- the geometric transport is unitary;
- forward norms diverge exponentially.

This falsifies completion stability at the exact open type-fiber Adams frontier.
