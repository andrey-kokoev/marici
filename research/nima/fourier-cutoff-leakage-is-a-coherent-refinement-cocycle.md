# Fourier cutoff leakage is a coherent refinement cocycle

## Question

Finite diagnostic projection does not commute with completed Fourier sewing.
Does that failure compose coherently under cutoff refinement, or is every
cutoff defect independent?

## Leakage by shells

Let \(P_X\le P_Y\) be nested orthogonal cutoff projections and let \(F\) be
the completed sewing operator. The leakage seen at cutoff \(X\) is

\[
\mathfrak A_X=P_XF(I-P_X).
\]

Insert the refinement decomposition

\[
I-P_X=(P_Y-P_X)+(I-P_Y).
\]

Then

\[
\mathfrak A_X
=P_XF(P_Y-P_X)+P_XF(I-P_Y).
\]

The first term is leakage from the newly exposed finite shell. The second is
the transported leakage still lying beyond the refined cutoff.

For a chain \(P_0\le P_1\le\cdots\le P_r=I\), iteration gives

\[
P_0F(I-P_0)
=\sum_{k=0}^{r-1}P_0F(P_{k+1}-P_k).
\]

This decomposition is independent of how adjacent shells are parenthesized,
because it is induced by additive decomposition of the identity.

## Categorical meaning

Finite diagnostic projection is not a strict natural transformation with
respect to completed sewing. It carries a source-derived additive defect
cell. Under refinement, those cells compose by shell addition.

Thus the finite system is best typed as a lax diagnostic functor:

- objects are cutoff diagnostic spaces;
- refinement arrows enlarge the visible source region;
- the comparison with global sewing has leakage cells;
- the coherence law is the shell cocycle above.

The defect is not freely fitted at each cutoff. One global operator \(F\) and
the nested projections determine every cell.

## Relation to route effects

The leakage cells carry an additive route effect. Their composition is a
commutative accumulator even though the underlying completed sewing need not
be commutative. This separates two layers:

1. ordered operator transport in the global source;
2. additive accounting of what each diagnostic projection omits.

Confusing the second layer with the first would erase operator order.
Ignoring the second would falsely declare the finite square strict.

## What this repairs

Finite diagnostics need not be discarded merely because they are not source
subobjects. They remain lawful observations of the global construction when
their leakage cells are retained and satisfy refinement coherence.

This does not reconstruct omitted information. It records exactly how much
of the global arrow fails to descend at each stage.

## DPC verdict

Resolved: coherence of Fourier cutoff defects under nested refinement.

Unresolved: convergence and continuity of the shell cocycle in the actual
restricted-product topology, and calibration of its finite optical readout.

The route closes immediately if an empirically or analytically proposed
cutoff defect fails the shell-additivity identity.

## Verification

The checker `check_fourier_cutoff_leakage_cocycle.py` verifies exact shell
decomposition and parenthesization independence in an integer four-mode
Fourier witness.

