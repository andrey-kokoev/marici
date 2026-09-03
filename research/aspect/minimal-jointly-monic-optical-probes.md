# Minimal jointly monic probes on a finite optical quotient

## Question

Which path and polarization probes are jointly monic on a declared finite optical state quotient, and is every probe in the family necessary?

## Claim boundary

This packet proves minimality only within a four-probe candidate family on a twelve-state quotient. It does not establish tomography for arbitrary Jones vectors, mixed states, path superpositions, continuous spectra, or all physically realizable optical effects.

## Source-derived quotient

Consider a one-photon sector restricted to:

- two resolved path eigenstates \(p\in\{0,1\}\);
- six polarization eigenstates

\[
\{H,V,D,A,R,L\},
\]

corresponding to the positive and negative eigenstates of three Stokes axes.

The finite quotient is

\[
Q=\{0,1\}\times\{H,V,D,A,R,L\}.
\]

Its twelve points are distinct by declaration of path and polarization eigenstate labels. No claim is made about coherent superpositions outside this quotient.

## Candidate probes

Use four exact coordinates:

1. path probe \(P(p,s)=p\);
2. first Stokes contrast \(S_1\), separating \(H\) from \(V\);
3. second Stokes contrast \(S_2\), separating \(D\) from \(A\);
4. third Stokes contrast \(S_3\), separating \(R\) from \(L\).

The polarization coordinates are

\[
H\mapsto(1,0,0),\quad
V\mapsto(-1,0,0),
\]

\[
D\mapsto(0,1,0),\quad
A\mapsto(0,-1,0),
\]

\[
R\mapsto(0,0,1),\quad
L\mapsto(0,0,-1).
\]

These are exact contrast values on the restricted eigenstate set, not floating-point approximations.

## Joint monicity

The combined coordinate

\[
c=(P,S_1,S_2,S_3):Q\to
\{0,1\}\times\{-1,0,1\}^3
\]

is injective. The path coordinate separates equal polarization states in different paths. The three Stokes coordinates jointly separate all six declared polarization states.

Hence this probe family is jointly monic on \(Q\).

## Minimality within the candidate family

Every coordinate is necessary:

- deleting \(P\) identifies \((0,H)\) and \((1,H)\);
- deleting \(S_1\) identifies \((0,H)\) and \((0,V)\);
- deleting \(S_2\) identifies \((0,D)\) and \((0,A)\);
- deleting \(S_3\) identifies \((0,R)\) and \((0,L)\).

Exhaustive search over all subsets of the four declared probes shows that only the full family is injective. Thus its cardinality four is minimal relative to this candidate set.

This is not a lower bound over all possible optical observables. A differently designed multivalued detector could encode several coordinates in one record object. Probe count is meaningful only after the admissible detector class and record alphabets are fixed.

## Relation to attachment correspondences

If two attachment lifts differ only in path placement while retaining the same polarization state, the Stokes probes alone cannot distinguish them; \(P\) can. If they differ only by opposite eigenstates on one Stokes axis, the corresponding Stokes probe is necessary.

Therefore correspondence multiplicity is not uniformly operationally invisible. Distinguishability depends on which lawful probe family is attached. Conversely, unresolved lift multiplicity may survive every probe in a restricted family and must then remain as a readout fiber.

## Disposition

The four probes \(P,S_1,S_2,S_3\) form a jointly monic and deletion-minimal family on the declared twelve-state optical quotient. The proof is exact and exhaustive within the candidate family. Extension to continuous optical states requires a new admissible-effect class and cannot be inferred from this finite result.
