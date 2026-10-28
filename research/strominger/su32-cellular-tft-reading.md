# Cellular TFT: a global construction and a revised role for gauge choices

## Source and question

Alberto S. Cattaneo, Pavel Mnev, Nicolai Reshetikhin, *A Cellular Topological Field Theory*, `references/1701.05874v2.pdf` (2020 version). Targeted reading: PDF pp. 1–3, 10–11, 19–22, 57–62, 64, 70, 88. The 90-page source is now in the main index: 5,869 pages / 73 PDFs.

Question: does this source supply the global extension machinery missing from our rational-cochain comparison, rather than another isolated local analogy?

## 1. A theorem for the already fixed global complex

**Theorem 8.6, pp. 57–59:** given a finite regular CW complex X and a unimodular Lie algebra g, the authors construct a cellular BF action from cell-supported building blocks. It satisfies the quantum master equation; its restriction to every subcomplex does too. The construction's linear part is the cellular differential, and its vertex part is fixed by the Lie bracket of g.

Our finite abstract support complex is a regular CW complex, so this is an applicable algebraic construction once a coefficient algebra is declared. It does not require X to be a manifold. The stronger cobordism/BV-BFV gluing results do require the additional manifold/boundary data; they cannot be imported just from our support counts.

This respects the operator's global-first requirement: X is fixed before its action is constructed. The induction over its cells constructs operations on that input complex, not wiring by extending independently accepted local readers.

**Remark 8.12, p. 62:** rational induction data give rational structure constants. Exact rational implementation is supported by the source, not merely a numerical approximation strategy.

## 2. Exact composition law for contraction packages

Equation (16), p. 21, composes retractions `C0 -> C1 -> C2` by

```
i02 = i01 i12,
p02 = p12 p01,
K02 = K01 + i01 K12 p01.
```

This is a direct next test for our staged reductions. The target should retain the full homotopy package, not only `p02` or equality of decoded data. Section 4.2 also provides induced packages on duals, tensor products and polynomial functions, needed to reach actions rather than only linear cochains.

## 3. Correction to the earlier interpretation of the free parameter

The previous checker found that incidence does not uniquely determine lambda in its local contractions. That remains correct. **It does not follow that a physical source must select a unique lambda before transfer can proceed.**

- Lemma 4.4(a), p. 22: retractions onto cohomology inducing the canonical cohomology projection form a contractible space.
- Lemma 4.4(b): for a general target complex, the full space has the homotopy type of its chain automorphism group; the contractibility claim must not be indiscriminately extended to every retraction.
- Lemma 8.7, pp. 60–61: cellular actions satisfying Theorem 8.6's ansatz and conditions are related by canonical BV transformations.
- Remark 8.9: higher-cell action representatives need not be unique.

Thus contraction freedom can be gauge freedom. The correct obligation is to construct and compare the resulting complete transferred structures, not to demand uniqueness of the representative. Our computed binary homotopy is a first piece of such a comparison, not yet the full canonical BV transformation.

The native coefficient algebra remains a separate missing input. Gauge independence does not select a Lie bracket from four record labels.

## 4. Keep the seven additional classes; do not force them to disappear

The paper explicitly handles non-acyclic complexes. Residual fields retain cohomology (pp. 3, 20, 64). In the abelian theory, torsion with nonzero cohomology is determinant-line-valued rather than an ordinary scalar; Appendix A relates gluing through the determinant line of the Mayer–Vietoris sequence (p. 88).

For our untwisted support model, a global reduction should retain `H0=Q` and all `43` dimensions of H2. The 36 local route spheres do not exhaust that space: the seven additional classes are residual data, **not automatically obstructions to constructing a global theory**. This paper gives a framework for carrying them through the calculation rather than adding unsupported fillers to kill them.

That statement is about the existing rational support complex. Changing the local system, adding cells or constructing an involutive integral theory requires a new computation.

## 5. Geometry-side operations and coefficient-side interactions are distinct inputs

Appendix B, p. 88, explains the construction summarized by `C-infinity tensor Lie -> L-infinity`. This addresses our scalar Whitney observation: higher homotopy-commutative cochain operations and a Lie algebra of coefficients combine into Lie-type higher operations. One should not infer a nontrivial internal Lie interaction just from the scalar Whitney associator.

For the quantum BF construction the unimodularity condition also matters: it is used explicitly to remove the quantum extension obstruction in the proof on p. 59.

## What not to import

The source's own open questions on pp. 10–11 include cellular Chern–Simons theory, gluing with codimension-two-or-higher corners, and a sign-refined partition function. The present construction is cellular **BF** theory, not a completed arbitrary Chern–Simons or fully extended corner theory. Our overlapping cone comparisons are not automatically its proven cobordism gluing interface.

## Disposition

This source gives the most direct global construction method among the PDFs reviewed in this sequence. It changes the next task from “make the local choices uniquely native” to:

1. construct one global contraction retaining the full cohomology;
2. compare staged contractions using equation (16);
3. supply a declared coefficient algebra and build the higher operations with their transformation witnesses;
4. separately determine whether the native reversal admits the Real/Quaternionic lift from the FKMM paper.

No new checker or BV action was implemented in this reading pass. The prior cochain numbers and binary comparison remain unchanged; their interpretation is sharpened. Canonical reindex execution: `structured_command_execution:e_29164_1793126179096485500_68`.
