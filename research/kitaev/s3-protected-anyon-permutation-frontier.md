# The protected D(S3) frontier contains a non-Clifford electric--magnetic duality

Owner: `marici.Kitaev`

## Bounded question

What is the anyon-label action of locality-preserving automorphisms of the
frozen \(D(S_3)\) topological phase, and how does it compare with the earlier
product-Clifford implementation boundary?

## Operation class

This packet keeps four classes separate:

1. a braided autoequivalence of the \(D(S_3)\) anyon theory;
2. a constant-depth local circuit implementing that autoequivalence;
3. its induced unitary on the torus ground-state basis;
4. the previously frozen stabilizer/Clifford instrument compiler.

Only (1) and the finite action in (3) are independently reconstructed here.
Class (2) is supported by the cited primary sources. It is not silently
identified with class (4).

## Exact finite theorem

Enumerating all vacuum-fixing permutations of the eight simple sectors that
preserve the exact modular \(S\) matrix and topological spins gives precisely

\[
  \operatorname{Aut}(S,T)=\{1,\sigma_{CF}\}\cong\mathbb Z_2,
  \qquad \sigma_{CF}:C\leftrightarrow F.
\]

The nontrivial permutation independently preserves every fusion coefficient.
Thus \(C\), the two-dimensional pure electric charge, and \(F\), the trivial
three-cycle flux sector, are exchanged while \(A,B,D,E,G,H\) are fixed.

In the frozen sector-label coordinates

\[
 A,\ldots,H=000,001,010,011,100,101,110,111,
\]

this is the single computational-basis transposition \(010\leftrightarrow101\).
Exact Pauli-normalizer testing shows that conjugated bit translations have
state-dependent displacement. Therefore

\[
  \sigma_{CF}\notin \mathrm{Clifford}(3)
\]

for the frozen product-Pauli structure.

## Theorem-changing sources

Li and Song construct constant-depth local-unitary circuits realizing general
anyon permutations in Kitaev quantum-double models. Their class-I construction
uses gauging of an Abelian normal subgroup; \(S_3=\mathbb Z_3\rtimes\mathbb Z_2\)
is exactly of that form. Lu, Wang, and Vishwanath independently construct a
self-dual \(S_3\) lattice gauge model whose translation exchanges \(C\) and
\(F\).

- Y. Li and Z. Song, *Anyon Permutations in Quantum Double Models through
  Constant-depth Circuits*, arXiv:2602.10110v1 (2026).
- D.-C. Lu, C. Wang, and A. Vishwanath, *Self-dual S3 gauge theory in 2+1d:
  lattice model and topological phase transitions*, arXiv:2608.05294v1 (2026).
- S. Beigi, P. Shor, and D. Whalen, *Indistinguishable Chargeon-Fluxion Pairs
  in the Quantum Double of Finite Groups*, arXiv:1002.4930 (2010).

## Correction to the previous frontier

“Frozen stabilizer resources are Clifford-only” remains correct for the
previously declared qubit--qutrit compiler. It is not a classification of
topologically protected operations. The protected phase admits at least the
non-Clifford \(C\leftrightarrow F\) duality once its constant-depth duality
circuit or self-dual lattice realization is admitted.

This does not make the earlier endpoint compiler complete. The duality is one
discrete protected gate, whereas the full 36-dimensional endpoint algebra
requires continuous block control. It also does not by itself establish a
fault-tolerant noisy implementation on the five-rail encoding.

## Falsifiers and unresolved typing

The finite theorem fails if another vacuum-fixing \(S,T\)-preserving
permutation exists, if \(C\leftrightarrow F\) violates a fusion coefficient,
or if its frozen binary action normalizes every product Pauli.

Physical protection still requires typing the Li--Song circuit into our exact
lattice conventions, its depth and range, its action on noncontractible ribbon
operators, and its compatibility with the five-rail recovery layer. The
Lu--Wang--Vishwanath realization changes the microscopic lattice Hilbert space,
so it is corroboration rather than a direct lift of the frozen source.

## Artifacts

- Checker: `checkers/check_s3_protected_anyon_permutation.py`
- Result: `results/s3-protected-anyon-permutation.json`
- Graph admission: `ev-000000003360-3a86cf53-35bf-4933-b2c8-81073ff14dd5`
- Ledger: `src/ledger/20260825-2456 Protected D(S3) Duality Is Non-Clifford and Conditionally Generates S8.md`
