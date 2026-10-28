# Realization equivalence and the complete predictive-state quotient

## 1. A precise mathematical realization gauge

`contracts/native-query-realization-equivalence.v1.json` specifies finite real carrier and pointer spaces with labelled bases, a positive product pairing and fixed pointer overlap eta. The eight frozen operations are their exact linear extensions. All source preparations, pointer labels and literal words remain named.

An allowed comparison consists of invertible factor maps A and B that carry every labelled basis vector to its namesake, preserve both pairings, and intertwine every generator. Word intertwining follows by induction. Carrier/pointer factors cannot be mixed by a gauge transformation, and source/record labels cannot be permuted silently.

The relation is therefore concrete: labelled bases uniquely determine a candidate comparison, and it exists precisely when their labelled Gram matrices agree. Different coordinate matrices may represent the same object, but different labelled Grams do not become equivalent merely because both are positive.

A nonorthogonal coordinate shear is admitted when basis vectors, metric and operations are transported together. Keeping the basis fixed while changing H from I/3 to (I+J/9)/4 is rejected. Changing eta or swapping false and true is also rejected.

Scale is now explicit. Before unit-feature normalization, H=cI contains a free scale; different c are not isometric while the named basis is fixed. Normalization sets c=1/3. That is a mathematical convention, not an absolute energy calibration or a new physical theorem.

The Boolean reader is defined on distinguished labelled states only. The contract does not manufacture a deterministic Boolean reader or a Born instrument on arbitrary superpositions, particularly when pointer vectors are nonorthogonal.

## 2. Complete finite behavioural classification

Use precisely the frozen one-object word language with two left translations and six query-controlled XOR operations. State is (g,b) in A4 x Bool; output is b. Retained word provenance is not a new observable.

For states s,t, future equivalence means equal Boolean readings after EVERY finite authorized word, including the empty word. Standard finite Moore refinement begins with equal current outputs and repeatedly splits classes according to successor classes for each generator.

The checker runs this refinement to stability and independently searches the complete paired-state graph for a shortest separating word for every unordered pair. It also constructs access words from the single identity/false state.

Result: every one of the 24 states is reachable, and every distinct pair is separated. The stable quotient therefore has exactly 24 predictive states. The receipt contains the complete transition table, partition sizes, all access words and all 276 separating continuations, not merely the final count.

Completeness is finite and exact: a stable observation-preserving transition partition preserves outputs after every word by induction. The independent separating words prove that no distinct pair can be merged. This is not a finite-depth guess at arbitrary-word equivalence.

## 3. Hostile interface control

If the two left translations are removed while keeping all 24 supplied states and the six queries, the quotient has 20 classes. Three group elements have the same six query answers; their corresponding states with equal pointer bit merge. Translations expose those hidden distinctions in the full interface.

This is a different intervention contract, not a simplification of the frozen task. It demonstrates why current readings or a restricted query list cannot replace all authorized continuations.

## 4. What the count does not prove

The result is a lower bound on the number of states in a deterministic finite predictive machine realizing this exact behaviour with the admitted preparations. It is not a lower bound of 24 on real coordinate dimension or physical Hilbert dimension.

A finite set of 24 states can be encoded in other spaces. Whether its operations and readings extend appropriately to a physical representation is a separate question. The earlier oscillator rank obstruction applies to its explicitly declared faithful LINEAR amplitude/single-excitation encoding, not every nonlinear encoding of these classical states.

Behavioural minimality also does not establish source identifiability: a lookup table can implement the same finite behaviour without explaining a physical mechanism.

## 5. Verification and disposition

    python research/strominger/checkers/check_native_query_behavioural_minimality.py

The dependency-free checker uses exact finite permutations and rational matrix arithmetic. It derives the group from the actual native triangle tables, reads the frozen generator names, checks reachability and full paired-state separation, and validates the positive shear and three forbidden gauge examples. No new Agda compilation or physical experiment is claimed.

Receipt: `results/native-query-behavioural-minimality/verification.json`.

The realization-equivalence specification and behavioural-minimality deliverables are complete at these scopes. Output-A assembly, physical-model disposition, comparison-witness typing and all physical/tetrahedral claims remain separate. This run does not rewrite the existing net revision or its pins.
