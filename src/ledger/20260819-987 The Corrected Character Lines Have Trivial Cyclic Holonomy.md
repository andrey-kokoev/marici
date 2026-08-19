# 987 — The Corrected Character Lines Have Trivial Cyclic Holonomy

## Descent test

Entries 984 and 986 produced, in each repeated character, the corrected reflection-odd line

\[
\mathcal L_{\chi,-}
=\mathbb Q(Z)
\left(
L_\chi-
\frac{1+Z^2}{Z^2-1}N_\chi
\right),
\qquad \chi\in\{++,--\}.
\]

It was only known to be canonical in one maximal-flag chart.  Test descent under the source cycle

\[
\sigma=(234).
\]

## Frozen cyclic atlas

The pair-shift generators in the three charts are

\[
(B_{24},B_{34}),
\qquad
(B_{23},B_{24}),
\qquad
(B_{34},B_{23}).
\]

On the common dense six-word order

\[
(234,243,324,342,423,432),
\]

the labelled cycle acts by

\[
(3,2,5,4,0,1).
\]

The normal coordinate is retained occurrencewise:

\[
Z_0=e^{i\pi s_{25}}
\mapsto
Z_1=e^{i\pi s_{35}}
\mapsto
Z_2=e^{i\pi s_{45}}
\mapsto Z_0.
\]

## Exact result

In every chart the loaded and normal rows were reconstructed independently from the relabelled source formulas and projected using that chart's own pair-shift generators.  For both (++) and (--), exact symbolic reduction gives

\[
\sigma(\mathcal L^{(0)}_{\chi,-})
=\mathcal L^{(1)}_{\chi,-},
\]

\[
\sigma(\mathcal L^{(1)}_{\chi,-})
=\mathcal L^{(2)}_{\chi,-},
\]

\[
\sigma(\mathcal L^{(2)}_{\chi,-})
=\mathcal L^{(0)}_{\chi,-}.
\]

There is no return unit or residual mixing:

\[
\boxed{
\operatorname{Hol}_{C_3}(\mathcal L_{++,-})
=
\operatorname{Hol}_{C_3}(\mathcal L_{--,-})
=1.
}
\]

## Consequence

The reflection correction is not an artifact of one occurrence chart.  Together with Entry 986,

\[
\boxed{
\mathcal L_{++,-}\oplus\mathcal L_{--,-}
\text{ is a global source-derived degree-zero occurrence submodule.}
}
\]

The normal-symbol (+1) lines descend by the same relabelling, so each repeated rank-two plane has a global occurrence-equivariant splitting.

This remains a coefficient statement.  It does not identify either line with a physical string period, nor does it provide the degree-changing map excluded in Entry 983.

## Next falsifier

Test compatibility of this global splitting with the first nontrivial boundary specialization.  Apply the six source-wall residues to both eigendirections and determine whether the split lines remain separate or recombine in the supported boundary object.  Recombination would show that occurrence descent does not extend through the localization/Gysin calculus.

## Verification artifacts

- `research/benincasa/marici-gm/src/bin/string_six_point_corrected_line_cyclic_descent.rs`
- `research/benincasa/string-six-point-corrected-line-cyclic-descent.json`

The checker uses independent chart projectors, the full six-word permutation, labelled kinematic substitutions, and direct three-step equality—not a rank or dimension surrogate.

Epistemic graph event: `ev-000000000604-48e0d290-c6f8-445f-b168-c05ceb9b9c74`.
