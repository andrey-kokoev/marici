# 886 — The Five-Point String Circuit Cancels Intermediate Resonances

## Record

Date: 2026-08-18

Status: exact source-normalized five-point circuit/basis-expansion theorem. This verifies one nontrivial row of the circuit matrix; it is not yet the full two-period-matrix twisted-period identity.

## Frozen source circuit

Mizera's equation (5.4) expands

\[
\mathcal A^{\rm open}(12354)
\]

in the basis

\[
\bigl(\mathcal A^{\rm open}(13254),
\mathcal A^{\rm open}(14253)\bigr).
\]

Write \(x_{ij}=\pi\alpha's_{ij}\). The source intersection row is

\[
H'=
\left(
-\csc x_{45}(\cot x_{12}+\cot x_{23}),
-\csc x_{12}\csc x_{35}
\right).
\]

Entry 883 supplies the diagonal kernel

\[
H^{-1}=\operatorname{diag}
\left(
\sin x_{23}\sin x_{45},
\sin x_{24}\sin x_{35}
\right).
\]

## Exact circuit reduction

Multiplication gives

\[
H'H^{-1}
=
\left(
-\sin x_{23}(\cot x_{12}+\cot x_{23}),
-\frac{\sin x_{24}}{\sin x_{12}}
\right).
\]

The first component reduces by the sine addition identity:

\[
\sin x_{23}(\cot x_{12}+\cot x_{23})
=
\frac{\sin(x_{12}+x_{23})}{\sin x_{12}}.
\]

Therefore

\[
\boxed{
\mathcal A^{\rm open}(12354)
=
-\frac{\sin\pi\alpha'(s_{12}+s_{23})}
       {\sin\pi\alpha's_{12}}
 \mathcal A^{\rm open}(13254)
-\frac{\sin\pi\alpha's_{24}}
       {\sin\pi\alpha's_{12}}
 \mathcal A^{\rm open}(14253).
}
\]

This exactly matches the primary source.

## Resonance cancellation

Before composition, \(H'\) and \(H^{-1}\) display factors on

\[
s_{45},s_{23},s_{24},s_{35},s_{12}.
\]

After the typed circuit composition, all displayed denominators except

\[
\sin(\pi\alpha's_{12})
\]

cancel. Thus raw poles of an intersection row or inverse kernel are not individually circuit-invariant.

The surviving divisor is still an existing Koba--Nielsen facet letter, not a new incidence cell. Entry 885 should therefore be read basis-covariantly: circuit transport may move the displayed resonance among existing labelled boundary letters, while composition cancels intermediate factors.

## Field-theory limit

As \(\alpha'\to0\),

\[
H'H^{-1}longrightarrow
\left(
-\frac{s_{12}+s_{23}}{s_{12}},
-\frac{s_{24}}{s_{12}}
\right),
\]

which is the five-point BCJ basis expansion quoted by the source.

## Narrow update

The first nontrivial string circuit closes using exactly

\[
\boxed{
\text{labelled incidence}
+\text{Koba--Nielsen valuations}
+\text{matrix composition}.
}
\]

No extra carrier generator is required. The calculation also confirms that support must be assessed after typed composition, not factor-by-factor.

## Next falsifier

Construct a second independent target row and verify the full \(2\times2\) circuit composition and cocycle-period intertwining. Then test whether the resulting circuit matrices satisfy composition under a third basis without introducing any non-Koba--Nielsen divisor.

## Certificate

Run:

```text
cargo run --quiet --bin string_five_point_circuit_expansion
```

Artifacts:

- `research/benincasa/marici-gm/src/bin/string_five_point_circuit_expansion.rs`
- `research/benincasa/string-five-point-circuit-expansion.json`

## Sources

- Sebastian Mizera, *Inverse of the String Theory KLT Kernel*, arXiv:1610.04230, Section 5, equation (5.4).
- Sebastian Mizera, *Combinatorics and Topology of Kawai--Lewellen--Tye Relations*, arXiv:1706.08527, Section 3.4, circuit matrix equation.
