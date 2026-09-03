# Operator-valued Markov restricted equipment fragment

## Question

Do the finite associator, completion, Beck–Chevalley, and orthogonal gauge results assemble into a restricted equipment fragment?

## Claim boundary

The construction uses fixed finite fiber dimension, contraction transfers, contiguous inclusions, and vertexwise orthogonal gauges. Horizontal companions and conjoints are freely adjoined gauge correspondences with exact matrix realization. This is not a full equipment for arbitrary vertical maps or the full coherence pyramid.

## Partial double category

Objects are finite operator-valued path-product Markov kernels and their uniformly contractive one-sided completions. Horizontal arrows are seam-compatible transfer-list extensions and contiguous inclusions. Vertical arrows are vertexwise orthogonal gauge isometries. Squares are equalities of full block kernels admitted only when shared vertex gauges agree.

Ordered matrix multiplication supplies strict horizontal associativity, unitors, and pentagon. Orthogonal composition supplies strict vertical associativity and units. Telescoping internal gauge factors proves interchange. Contiguous principal block compression supplies invertible Beck–Chevalley identity cells with strict nested pasting.

## Equipment extension

For every orthogonal vertical gauge \(U:G\to UGU^T\), adjoin a horizontal companion with witness \(U\) and a horizontal conjoint with witness \(U^T\). Unit, counit, and triangle realizations reduce to

\[
U^TU=UU^T=I.
\]

Unlike sign gauges, a general orthogonal \(U\) need not be self-inverse, so companion and conjoint witnesses remain directionally distinct. Composition comparisons use matrix multiplication and satisfy pentagon by associativity.

## Completion

A uniformly bounded vertexwise orthogonal family defines a block-diagonal unitary on \(\ell^2(\mathbb N;\mathbb R^d)\). Completion preserves the companion and conjoint witnesses, contiguous Beck–Chevalley cells, and associators strictly.

## Refusal boundary

The constructor refuses varying fibers without typed transport, arbitrary bounded vertical maps without an adjoint-equivalence certificate, noncontiguous probes without effective transfers, and completion without a uniform contraction or alternative Schur certificate.

## Disposition

The scalar restricted equipment extends to fixed-fiber noncommutative Markov chains with the full orthogonal gauge groupoid. This is a larger genuine analytic/formal fragment, while general vertical maps, varying fibers, arbitrary pullbacks, and cross-sector coherence remain open.

## Verification

- `research/voevodsky/checkers/check_operator_valued_markov_restricted_equipment.py`
- `research/voevodsky/results/operator_valued_markov_restricted_equipment.json`
