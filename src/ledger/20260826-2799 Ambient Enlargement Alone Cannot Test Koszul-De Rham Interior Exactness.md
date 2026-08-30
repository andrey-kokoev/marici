# 2799 — Ambient Enlargement Alone Cannot Test Koszul–de Rham Interior Exactness

## Hostile typing audit

Entry 2797 proposed testing fixed numerator-degree homology under increasing ambient cutoff. Before performing that census, audit whether the current finite reducer contains the mixed Leibniz squares required by its own bicomplex.

The IBP generator loop admits a state only when

\[
k<K_{\max}
\]

and every labelled marked-pole depth satisfies

\[
\ell_i<Q_{\max}.
\]

At the current value (Q_{\max}=2), this means all five marked-pole depths equal one.

## Missing mixed cells

An IBP/(q_i)-multiplication Leibniz square requires the raised IBP state

\[
(\ell_1,\ldots,\ell_i+1,\ldots,\ell_5).
\]

That state has (ell_i=2) and is excluded. Therefore none of the ten axis-labelled IBP/(q_i) state types is internal.

For Cayley–Menger multiplication, only the transition from (k=0) to (k=1) remains internal. The transition from (k=1) to (k=2) is excluded.

Increasing numerator ambient degree changes neither fact.

## Correction

The ambient-only conjecture is mistyped. The admissible stabilization system must enlarge cofinally in:

- numerator degree;
- Cayley–Menger pole depth;
- each of the five labelled marked-pole depths.

The correct hard claim concerns fixed labelled multi-interior degree under this joint filtration.

This correction does not falsify the Koszul–de Rham explanation. It falsifies the proposed one-parameter test of that explanation.

## Numerator margins

The source polynomial degrees force at least the following numerator margins:

- one for marked-pole multiplication;
- four for Cayley–Menger multiplication;
- three for the Cayley–Menger derivative term in IBP.

Pole-depth margins must be tracked independently.

## Artifacts

- `research/benincasa/check_rank26_bicomplex_truncation_typing.py`
- `research/benincasa/rank26-bicomplex-truncation-typing.json`
- `research/benincasa/rank26-koszul-derham-bicomplex-conjecture.md`

## Next falsifier

Generalize the finite presentation to independently declared (K_{max}) and labelled (Q_{i,\max}). Verify that every mixed Leibniz square exists on a frozen multi-interior block before computing any homology.
