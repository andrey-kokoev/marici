# The Full Quadratic Source Forbids a Nontrivial Selector Projector

## Commutant theorem

Let (H_+) be one irreducible oscillator parity sector and let the full
quadratic endpoint algebra act on it. Any bounded operator commuting with that
action is scalar. In particular, an orthogonal projector in the commutant is
either zero or the identity.

This is Schur's lemma applied to the irreducible metaplectic sector. It turns
the conditional survival law

\[
[W,P]=0
\]

into a source-level no-go: if every quadratic endpoint operation remains
admissible, there is no nontrivial source-derived projector selecting the
finite grades (n_v=2,4).

## Local boundary witness

On the even chain

```text
0 -- 2 -- 4 -- 6 -- 8 -- ...
```

let (P_{2,4}) select grades two and four. The quadratic raising and lowering
operators cross both boundaries of this window. Therefore

\[
[P_{2,4},K_+]\ne0,
\qquad
[P_{2,4},K_-]\ne0.
\]

The commutator is precisely the boundary incidence of the selected interval.
This identifies the defect geometrically: the proposed code is a subspace but
not a subrepresentation.

## Consequence

Figueiredo's projector criterion does not ask us to discover a projector
already hidden inside the full magnetic interaction algebra. It forces a
choice between two genuinely stronger constructors:

1. restrict admissible operations to the stabilizer algebra of the chosen
   projector;
2. add a new superselection label on which the source algebra acts blockwise.

The first changes the operation contract. The second enlarges the object. A
prepared finite-grade state, spectral filter, or successful terminal readout
does neither and cannot authorize the missing closure.

## Transfer boundary

This theorem applies to preservation under the complete quadratic/metaplectic
endpoint algebra. A narrower experiment may legitimately declare only a
projector-preserving subalgebra. The remaining physical question is then not
whether the projector commutes, but which source constructor authorizes that
restriction and implements the complementary readout.

## Evidence replay

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/full_quadratic_commutant_selector_no_go_checks.py
```

The exact finite models compute the simultaneous commutant of raising and
lowering generators on parity-chain cutoffs of dimensions two through ten.
