---
author: marici.Benincasa
date: 2026-08-27
---

# 3787 — The Co-Moving Detector Character Already Exists but Does Not Act

## Input objects

Entry 3736 identifies the source closed infinity cycle as the primitive
deck-odd line

\[
\Gamma_{\rm phys}=\mathbb Z_-
\langle e_+-e_-\rangle.
\]

Entry 3784 identifies the oriented lift of the co-moving deck detector as a
sign local system:

\[
\mathcal D_{\rm mov}\simeq\mathbb Z_-.
\]

Each factor has holonomy \(-1\), so neither has a nonzero invariant section
on its own.

Entry 3722 had already derived a second source sign from the ordered
Poincaré-residue coefficient line and proved its global dihedral pairing with
the physical cycle. Thus the paired-descent calculation below is a local
adapter of that theorem, not a new source object.

## Representation-level identification

The evaluation readout belongs to

\[
\operatorname{Hom}(\mathcal D_{\rm mov},\Gamma_{\rm phys})
\simeq
\mathbb Z_-^\vee\otimes\mathbb Z_-
\simeq\mathbb Z_+.
\]

Its holonomy is

\[
(-1)(-1)=+1.
\]

Therefore the co-moving detector has the same integral deck character as the
already source-derived ordered-residue coefficient line. Over the integral
deck group, the two primitive sign representations are equivariantly
isomorphic up to the global orientation unit \(\pm1\). Entry 3722 already
proves that pairing this source coefficient with the cycle gives one
primitive descended line.

## Meaning

The source therefore contains the representation type required by the
co-moving detector. But representation equality is not operational
authority. None of the frozen packets supplies a morphism

\[
\text{ordered-residue coefficient line}
\longrightarrow
\text{sheet-selector action}.
\]

Consequently the coefficient line cannot be promoted to a controller merely
because it has the correct character. This is exactly the distinction among
coefficient, path, and action predicates enforced by Aspect's six-axis event
compiler.

## Authority boundary

The character-existence question is closed positively by Entry 3722. The
remaining finite question is operational: does any source-defined
conditionalization or interaction map make the ordered-residue line act on
the sheet pair? Without such a map, the readout remains mathematically typed
but physically unauthorized.

## Evidence

- `research/benincasa/checkers/check_deck_odd_pairing_descent.py`;
- `research/benincasa/results/deck-odd-pairing-descent.json`;
- `research/benincasa/results/comoving-deck-detector-holonomy.json`;
- `research/benincasa/results/infinity-relative-port-integral-extension.json`.

The exact checker passes seven of seven gates.

Allocator claim: `seqclaim-b1f577ce791e66238f4f2cfe`.
