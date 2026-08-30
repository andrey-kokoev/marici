# Two source matchings create relational chirality

Work package: WP609  
Owner: marici.Figueiredo

## Repair question

WP608 failed because a single matching between independently labelled
(A) and (B) families can always be diagonalized by relabelling one family.
The smallest proposed repair puts two independently source-derived relations
on the same physical ports:

\[
D=I,
\qquad
K=P_+.
\]

Here (D) is a diagonal anchor and (K) is the forward cyclic matching. Both
relations must refer to the same physically instantiated (A_i,B_i) objects.

## Full permutation audit

Allow arbitrary permutations (R_A,R_B\in S_3). A symmetry of the joined
source must satisfy

\[
R_A^TDR_B=D,
\qquad
R_A^TKR_B=K.
\]

The anchor forces (R_A=R_B). The second condition then restricts that common
permutation to the centralizer of the three-cycle. Exact enumeration gives

\[
\operatorname{Aut}(D,K)=C_3.
\]

No transposition survives. By contrast:

- (D) alone has all six simultaneous (S_3) relabellings;
- (K) alone has six paired relabellings, including WP608's shifted
  reflection;
- deleting either relation therefore restores a reflection.

This is an exact relational repair of WP608. It does not define an absolute
handedness: the reversed source is an isomorphic presentation under a change
of external convention. What is invariant inside the admitted source object
is the absence of a reflection automorphism.

## Hard-to-vary content

The reduction from six automorphisms to three depends on the support pattern,
not on a fitted numerical coefficient. Arbitrary nonzero weights may multiply
the two relations while their distinct supports remain. Restoring reflection
requires deleting a relation, merging the physical port identities, or
changing the incidence.

Thus the pair is a source-defined relational carrier and a presentation
rigidifier. It is not yet a numerical flavor selector. It fixes no quark mass
ratio, mixing angle or CP invariant.

## Executable criticism

The minimum experiment measures both relations on the same physically tagged
ports. It must establish that the (A_i,B_i) identities used for the anchor
are the same identities used for the forward channel. Separate experiments
with an inferred coordinate matching do not compose.

The smallest exact falsifiers are:

- absence of the diagonal anchor;
- absence of the forward matching;
- loss of the shared physical port identity;
- an observed reflection channel that enlarges the support stabilizer.

If the common alignment is supplied only by a detector reference port, the
experiment is still legitimate but its groupoid is the stabilizer of that
added port. It does not establish an absolute orientation of the unreferenced
source.

The temporal phase process remains an independent gate for any signed
interference record. A monitor can select histories but cannot be credited
with restoring coherence.

## Remaining flavor-selector gate

The joined carrier becomes a flavor explanation only if one microscopic
grammar also:

- realizes the shared port identities as weak-basis-invariant flavor
  composites;
- derives both support relations without reading the fitted answer;
- makes their joint source action select a proper `physical16` family;
- predicts numerical relations that survive the complete fitted ensemble;
- supplies a calibrated common-port and temporal instrument.

WP609 establishes the relational carrier required for such a grammar. It does
not claim that the grammar or its physical instrument already exists.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp609_anchored_two_matching_relational_carrier.py

The generated result is
research/flavor/results/wp609_anchored_two_matching_relational_carrier.json.
