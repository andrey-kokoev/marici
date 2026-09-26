# Index identities inside the retained package

## Question

Can the index's own comparison structure become part of Q, with fibre transport, E/Pi compatibility and higher comparisons checked uniformly?

The active obligation is route/coherencer compatibility. The conjecture is that retaining a coded index, recursively decomposing its identity witnesses and acting by dependent transport supplies these operations without replacing index paths by endpoint equality. Rivals are: retaining only a bare index type; treating every loop as reflexivity; and comparing fibre values without transport. The discriminating test is a nontrivial index loop that permutes its fibre and obstructs a global section.

## Claim boundary

`IndexIdentityCoherence.agda` adds Family = (index:Code, fibre:El(index)->Code). The index code survives with the fibre family, selected values and proof fields in whole-package records. This is an index-aware interface over the existing code universe; the earlier resolution engine's Rule datatype is unchanged.

IndexEvidence(F,i,j) recursively uses the checked Evidence(index(F),i,j). It is therefore structured when the index itself is built from E/Pi, rather than always imported as one opaque equality. Primitive identities of the declared index types remain source data.

Checked constructions:

* identity, inverse and composition of index evidence;
* left-unit, cancellation and associativity paths between those index witnesses;
* action on fibres respecting identity, composition and inverse;
* action of higher index comparisons on transported fibre values;
* compatibility of every dependent section with every index path;
* an equivalence between recursively decomposed index-plus-fibre evidence and equality of dependent pairs, including recovery of the original witness;
* reification of full sum/section packages, action certificates and higher-action certificates as Complete values.

The dependent-pair comparison has the form

Sigma(c:IndexEvidence(F,i,j)). Evidence(FibreCode(j),act(c,x),y).

Its equivalence with (i,x)=(j,y) uses the index evidence equivalence, transported fibre comparison equivalence, and dependent Sigma-path equivalence. It retains rather than assumes trivial the path between i and j.

## Disposition

Fresh Agda dependency-closure verification passed under `--safe --cubical --guardedness`, with no added postulates or holes. The regression declares a circle and its Bool double cover using univalence, with index code E(Unit, Circle):

* a nonreflexive index loop exchanges true and false;
* two applications restore the value;
* inverse transport restores the value;
* the loop gives an equality between the two corresponding dependent pairs;
* replacing the index witness by reflexivity cannot give that equality;
* the family admits no global dependent section;
* the index witness and a higher cancellation witness survive reification.

The no-section theorem is the substantive hostile: Pi compatibility places a real constraint on possible global resolutions. A loop at one index can act nontrivially on its fibre. The source here is a declared mathematical double cover, with no temporal interpretation.

This closes the omitted-index-structure gate for the new interface. It does not establish a finite basis for all comparison laws of arbitrary resolution trees, synthesize paths of opaque source types, or equate different code presentations.

### Verification and reproducibility

```
pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module IndexIdentityCoherenceRegression -Fresh
```

The PS1 uses the same installed Agda executable and Cubical library as the existing launcher, adds `--transliterate` for readable Windows errors, and enables `--ignore-interfaces` with `-Fresh`. It records compiler/source hashes and a log. The source inventory is not claimed to be a dependency graph.

* Receipt: `research/nima/results/agda-IndexIdentityCoherenceRegression.json`.
* Compiler: Agda 2.8.0-3d04bac, Cubical 0.9; exit 0.
* Log: `research/nima/results/agda-IndexIdentityCoherenceRegression.log`.
* SCC model: `research/nima/scc-models/index-identity-coherence.json`.
* SCC freshness audit: `research/nima/checkers/check_index_identity_receipt.py`; passed, including rejection of tampered/failed receipts. It checks recorded evidence and never substitutes for compiler execution.

Development defects fixed before the final check: imported-name collisions and an underdetermined base point in the regression's transport-reflexivity proof. The original launcher also exposed a Unicode diagnostic failure; transliteration in the owner-local runner removed that reporting defect.
