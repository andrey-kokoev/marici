# Formal lifting problem for the triple-incidence p-normal line

## Question

What is the smallest formal object that captures the remaining p-normal obstruction without route-specific narrative?

## Claim boundary

This packet defines the lifting problem and tests current candidates against it. It does not construct a new source object, relative Bockstein, global contour, or physical period.

## Disposition

The obstruction is the horn in chain complexes

\[
\mathbb Z\langle \tau_p^{\rm src}\rangle
\longrightarrow
\mathbb Z\langle \Xi_{\log},-\sigma_{123}\rangle
\overset{D}{\longrightarrow}
\mathbb Z\langle q_1q_2,q_1q_3,q_2q_3\rangle
\]

with

\[
D=
\begin{pmatrix}
1&-1\\
-1&1\\
1&-1
\end{pmatrix}.
\]

A filler must have differential column

\[
(1,1)
\]

in rows \((\Xi_{\log},-\sigma_{123})\). This column is primitive over \(\mathbb Z\) and satisfies \(D(1,1)=0\). It is the universal cell \(\tau_p\).

Current candidates have these signatures:

- abstract \(\tau_p\): column \((1,1)\), but unsourced;
- residue-level monic comparison: column \((1,1)\) after residue, but unsourced before residue because the residue functor has kernel;
- ordered blow-up exceptional face: sourced, but column \((0,1)\), so it misses the \(\Xi_{\log}\) leg;
- gradient-pivot normal adapter: sourced prior art, but no column after fixed-fiber restriction because the required triple face disappears.

Over \(\mathbb F_{101}\) and \(\mathbb F_{103}\), \(D\) has rank \(1\), the \(\tau_p\) column has rank \(1\), and the span of the exceptional column with the required column has rank \(2\). Thus the formal horn has a universal filler, but no current sourced candidate fills it.

The theorem to use for future proposals is now exact: a source route advances the p-normal line if and only if it supplies a sourced degree-one filler whose differential is the primitive column \((1,1)\), with source provenance and \(d^2\) compatibility. Everything else is either unsourced, non-closed, nonprimitive, or typed in the wrong cover.

## Reproducibility

Checker:

- `research/voevodsky/check_cosmology_tau_lift_formal_problem.py`

Result:

- `research/voevodsky/results/cosmology_tau_lift_formal_problem.json`

Command:

- `python research/voevodsky/check_cosmology_tau_lift_formal_problem.py`
