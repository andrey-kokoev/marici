# Critical review: all-arity Catalan/QTDS proposal

## Verdict

The proposal contains a plausible combinatorial theorem, but it is not paper-ready and should not yet be called a discrete-Morse theorem or a publishable amplitude theorem. The strongest defensible core is the explicit marked bijection plus its inverse and distance formula. The route coherence and QTDS promotion need separate formalization.

## What appears structurally sound

1. A zero-physical-core triangulation of a `2m`-gon reduces to a triangulation of one parity `m`-gon with opposite-parity ears. This gives `2 C_{m-2}` objects.
2. Marking one of the `2m-3` scalar diagonals produces the cardinality `2(2m-3)C_{m-2}`.
3. A full quadrangulation has `m-2` physical diagonals and `m-1` cells. The lower bound of `m-2` flips from zero core to full core is therefore valid.
4. The directed-tree criterion used for contact extraction is elementary: a tree orientation has every outdegree at most one exactly when it has one sink.

These observations support the counts and the intended contact criterion, conditional on the local predecessor/successor construction.

## Proof gaps requiring repair

### 1. Legality and independence of the direct flips

The proof asserts that selected edges form disjoint chains, that reversing each chain makes every flip legal, and that arbitrary interleavings of distinct chains remain legal. The stated separation by unselected scalar edges does not by itself prove that a flip in one chain cannot alter the quadrilateral supporting a flip in another. A local commuting-square lemma with explicit polygon intervals is required.

### 2. The inverse is asserted locally, not proved globally

The inverse section says the predecessor/successor rules undo one another at each triangle/quadrilateral pair. It does not prove that reverse flips preserve the marked parity sheet, remain legal for every interleaving, and recover the identical rooted parent structure rather than merely an isomorphic triangulation. This needs an induction on the rooted dual tree.

### 3. Geodesic classification is stronger than the distance proof

Minimal length excludes temporary diagonals, but it does not alone imply that every minimal path obeys precisely the proposed chain order. One must prove that each target physical edge has a unique prerequisite set and that no alternative legal ordering exists outside the asserted disjoint-chain poset.

### 4. “Discrete Morse” is currently unsupported terminology

No Forman matching, acyclicity proof, critical-cell classification, Morse differential, or chain contraction is defined. A geodesic average is not automatically a discrete-Morse transfer. Unless those data are constructed, the result should be called a marked flip-poset bijection and averaged chain homotopy.

### 5. Canonicity has undeclared coefficient assumptions

The all-geodesic average divides by the number of geodesics. It is defined over a characteristic-zero field, not integrally and not in characteristics dividing that number. The coefficient category must be stated. “Canonical” is relative to the chosen cyclic labels, parity sheet, polarity, root mark, and averaging field.

### 6. QTDS promotion relies on an external normalization contract

The coefficient `-1` combines a local numerator sign with a fixed diagram convention. The theorem needs a complete definition of the QTDS term, momentum convention, propagator orientation, and extraction map. Otherwise the combinatorial bijection is self-contained but the amplitude identification is not reproducible from the paper.

### 7. Finite certificates do not verify all arity

Enumeration through fourteen points tests the formulas but does not promote them. The all-arity result rests entirely on the prose lemmas above; each must become a formal proposition independent of the enumerator.

## Prior-art pressure

Full-text searches show that arXiv:1703.09953 already discusses accordion-lattice orientations with unique sources and sinks, while arXiv:1505.05990 contains quadrangulation bijections and linear-extension language. Those occurrences are not yet the same theorem, but they invalidate novelty arguments based merely on absence of matching titles or abstracts. The exact maps and theorem statements in arXiv:1505.05990, 1703.09953, and 1704.01534 must be compared against the proposed rooted predecessor/successor map.

The amplitude side also overlaps arXiv:1811.05904 on quadrangulation/Stokes-polytope scalar amplitudes and arXiv:2402.06719 on tropical colored-Lagrangian amplitudes. The proposed contribution must identify a coefficient or chain map not already implied by those constructions.

## Full-content prior-art findings

Shell-based inspection of the paper contents sharpens the comparison:

- arXiv:1703.09953 uses “unique sink” for the maximal element of an oriented accordion lattice obtained by rotating a reference dissection. It is not the unique sink of the dual tree of each quadrangulation. This is terminology overlap, not the same construction.
- arXiv:1505.05990 gives several quadrangulation bijections, including compatible quadrangulations with rooted binary trees and flips with rotations. The inspected content did not state the marked parity-sheet bijection, exact distance, or the proposed prerequisite-chain formula. Its existing bijections mean our map must be compared explicitly on common special families.
- arXiv:1704.01534 bijects accordion-complex facets with serpent nests. It contains no `unique sink`, `linear extension`, or `flip distance` occurrence. This appears adjacent rather than duplicative.
- arXiv:1811.05904 develops quadrangulation/Stokes-polytope canonical forms but contains no `unique sink`, `contact term`, `bijection`, `flip distance`, or `linear extension` occurrence in the rendered full text.
- arXiv:2402.06719 discusses contact terms, numerator functions, and quadrangulations but contains no `unique sink` or `QTDS`. Full-content inspection falsifies the proposed direct translation: its quartic numerator deliberately multiplies overlapping quadrilateral factors and produces the Catalan Lagrangian, whose `m`-point contact coefficient is `C_{m-2} g^{m-3}` and whose general interaction sums over all triangulations. It is not indexed by unique-sink quadrangulations.

These findings reduce the risk that the exact combinatorial statement was already printed in the closest combinatorics papers, but they do not repair the proof gaps. They also expose a presentation defect: `QTDS` is repository-local terminology rather than a searchable standard object. The unique-sink/QTDS theorem cannot claim equivalence to arXiv:2402.06719. A paper must either present the bijection as standalone combinatorics or independently define QTDS and derive its amplitude relevance without that identification. Detailed residual: `research/nima/unique-sink-tropical-numerator-falsification.md`.

## Minimum publishability gate

A defensible paper requires all of the following:

1. state and prove the marked bijection as a standalone combinatorics theorem;
2. prove the commuting-square and prerequisite-poset lemmas;
3. either construct genuine discrete-Morse data or remove that terminology;
4. state the coefficient ring and all choices underlying canonicity;
5. define QTDS independently and derive the contact coefficient under declared conventions;
6. provide theorem-by-theorem prior-art comparison.

Until these gates pass, the correct status is “promising theorem proposal with unresolved proof and priority questions.”
