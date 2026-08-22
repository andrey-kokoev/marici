# Filtered-Extension Identifiability Falsifier

## Target

The surviving proposal said that interaction data forms a source-derived
filtered extension of boundary/value data by coherence-defect data. The attack
asks whether the existence of such a filtration has explanatory content before
the filtration functor is specified.

## Exact finite control

Take the total object (E=\mathbf F_5^2), with identity transport and identity
total-record map. Every one-dimensional subspace is invariant. There are

\[
|\mathbf P^1(\mathbf F_5)|=6
\]

distinct nonzero proper filtrations

\[
0\to C\to E\to E/C\to0
\]

compatible with the same total transport and record. Moreover,
(\mathrm{GL}_2(\mathbf F_5)) acts transitively on these six choices while
preserving the isomorphism class of the declared total data. No line is
selected canonically. Degenerate filtrations (C=0) and (C=E) exist for
every object regardless.

## Falsification

\[
\boxed{
\text{existence of a filtered extension}
\not\Rightarrow
\text{an explanation of its grades}.
}
\]

The existential version is underdetermined rather than false as algebra: it
can be fitted to every object and can admit inequivalent nontrivial choices.
That makes it non-Popperian.

## Sharpened Deutsch--Popperian conjecture

A Marici filtration is explanatory only when a predeclared, source-natural
construction assigns it before sector records are inspected. The packet must
specify:

1. the ambient category and source object;
2. a filtration or localization functor;
3. naturality under the admitted transports;
4. nonzero proper associated grades;
5. an extension invariant that predicts an independently measured obstruction
   or record coupling; and
6. a failure condition under which the proposed filtration is rejected.

Thus the candidate is no longer “reality is some filtered extension.” It is:

\[
\boxed{
\text{one predeclared witness/localization calculus derives the observed
sector filtrations and their nonsplitting classes.}
}
\]

This is sharp enough to compare across scattering, cosmology, radiative
gravity, flavor, and arithmetic without choosing grades after the fact.

## Reproduction

```text
python research/nima/checkers/check_filtered_extension_identifiability.py
```
