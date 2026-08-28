# Determinant--commutator competition

## Question

WP978 tests whether the exact WP977 benchmark coefficient ray actually favors
a full-rank CP-capable vacuum over the WP973 embedded two-level maximizer. This
is a fixed-radius hostile comparison, not a global-vacuum theorem.

For unit-normalized Hermitian fields define

\[
K=\frac{\lVert[X,Y]\rVert_F^2}
{\lVert X\rVert_F^2\lVert Y\rVert_F^2},
\qquad
P=\frac{|\det[X,Y]|^2}
{(\lVert X\rVert_F^2\lVert Y\rVert_F^2)^3},
\]

and compare \(E=-qK-kP\).

## Exact competitors

For the WP973 two-level maximizer,

\[
K_2=2,\qquad P_2=0.
\]

For the WP972 full-rank control,

\[
K_3=\frac{2}{9},\qquad P_3=\frac{2}{27783}.
\]

The full-rank control wins only if

\[
\frac{k}{q}>
\frac{K_2-K_3}{P_3-P_2}
=24696.
\]

WP977's benchmark generates \(q=1/2\) and \(k=32\), hence \(k/q=64\).
Its exact normalized energies are

\[
E_2=-1,\qquad E_3=-\frac{3151}{27783}.
\]

The two-level state remains decisively lower.

## Consequence

WP977 repairs operator construction but not coefficient-ray selection. Its
benchmark does not produce the desired full-rank vacuum even against this
single exact hostile competitor. This falsifies the benchmark, not the whole
mediator grammar: the masses and couplings can vary the induced ratio.

A successor must derive a ratio above the relevant global threshold and then
prove the full coupled minimum, rather than tune the ratio after inspecting
the target.

## Reproduction

Run:

    python research/flavor/checkers/wp978_determinant_commutator_competition.py

The generated result is
research/flavor/results/wp978_determinant_commutator_competition.json.
