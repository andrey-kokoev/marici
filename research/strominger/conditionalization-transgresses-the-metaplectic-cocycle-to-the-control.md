# Conditionalization Transgresses the Metaplectic Cocycle to the Control

## From projective multiplication to control phase

Choose local lifts \(s(g)\) of symplectic operations to the metaplectic cover.
Their multiplication has the form

\[
s(g)s(h)=\omega(g,h)s(gh),
\qquad
\omega(g,h)\in\{+1,-1\}.
\]

Before conditionalization, \(\omega\) is a projective multiplication phase.
For controlled lifts,

\[
C_{s(g)}C_{s(h)}
=
Z_{\omega(g,h)}C_{s(gh)},
\]

where \(Z_{+1}=I\) and \(Z_{-1}=Z\) act on the selector. The extension cocycle
has become an observable control correction.

The minimal cyclic model is

\[
0\longrightarrow\mathbb Z_2
\longrightarrow\mathbb Z_4
\longrightarrow\mathbb Z_2
\longrightarrow0.
\]

For the section \(s(0)=0\), \(s(1)=1\), composing the nontrivial base element
with itself produces the central carry. On the control this carry is a minus
phase.

## Triple coherence

Associativity of the central extension implies

\[
\omega(h,k)\omega(g,hk)
=
\omega(g,h)\omega(gh,k).
\]

Thus the two-cocycle identity is precisely the coherence cell equating the two
controlled triple composites. For the genuine metaplectic extension, no new
three-fold anomaly is introduced: the next coherence rung is constructively
filled by group associativity.

This is not automatic for a table of pairwise phase corrections. A hostile
phase table on the Klein four group has valid values on every pair but a
nonzero three-coboundary. Its controlled composites depend on parenthesization.

## Categorical interpretation

Conditionalization performs a transgression:

```text
central extension cocycle on lower operations
  -> relative selector phase on controlled operations
  -> cocycle identity as the next associativity filler
```

This gives the first exact answer to the higher-tower question. A new tower is
needed because lower central data becomes a morphism at the controlled level.
Its next rung is not arbitrary: it is the coboundary test for that data.

For a source-derived central extension, the filler is guaranteed. For fitted
pairwise phases, it may fail, and the first nonzero three-coboundary is the
typed anomaly.

## Boundary

This proves mathematical coherence of controlled metaplectic lifts once a
phase-lifted controlled implementation is supplied. It does not supply that
physical implementation. Entry 3707's no-control theorem remains the
executable boundary.

## Evidence replay

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/controlled_metaplectic_cocycle_coherence_checks.py
```

The exact checker verifies the nontrivial central carry, all cocycle identities,
gauge persistence, and a hostile pairwise table with failed triple coherence.
