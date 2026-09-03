# Higher-probe parity matching obstructions

## Question

Can a constraint on \(n\) jointly placed probes remain invisible on every proper subconfiguration, and therefore require a genuinely \(n\)-ary Interaction Net cell?

## Claim boundary

This packet constructs a family of finite-set presheaves. It does not claim that parity is the universal form of higher interaction, that SCC currently supports higher matching cells, or that the obstruction is physical.

## Construction

Fix \(n\ge2\) binary probes indexed by \([n]\). On the face poset of the full \((n-1)\)-simplex, assign

\[
\mathcal K_n(S)=\{0,1\}^{S}
\quad\text{for every proper }S\subsetneq[n],
\]

with coordinate restrictions. At the full configuration assign the even-parity relation

\[
\mathcal K_n([n])=
\left\{x\in\{0,1\}^{n}:\sum_i x_i=0\pmod2\right\}.
\]

Every proper projection of the even-parity relation is surjective. Given values on a proper face, at least one omitted coordinate can be chosen to enforce even parity. Hence every proper face appears unconstrained even though the full configuration excludes half of all assignments.

## Matching object and obstruction

The compatible family of all proper-face assignments reconstructs a unique binary \(n\)-tuple, so the matching object is

\[
M_n\mathcal K_n\cong\{0,1\}^{n}.
\]

The matching map is the inclusion

\[
\mathcal K_n([n])\hookrightarrow M_n\mathcal K_n.
\]

Define the obstruction label

\[
\omega_n(x)=\sum_i x_i\pmod2.
\]

Then \(\mathcal K_n([n])=\ker\omega_n\). The excluded odd assignments form the nonfillable matching boundary. Both the admitted and excluded sets have cardinality \(2^{n-1}\).

This is stronger than failure of pairwise reconstruction. No collection of proper-face constraint objects, including every \((n-1)\)-probe face, distinguishes even from odd full assignments. The missing datum is the top matching map itself.

## Interaction Net interpretation

An \(n\)-ary cell is warranted when:

1. all proper boundary configurations are typed;
2. their restrictions form a compatible matching family;
3. the full joint constraint object maps into that matching object;
4. the map is not an isomorphism;
5. an explicit obstruction or residual classifies nonfillability.

Calling this a horn obstruction requires choosing a horn category and omitted face. The present construction establishes a full-boundary matching obstruction; it does not silently identify that object with every horn-filling formalism.

## Hostile fixtures

- Replacing the top relation by the full cube makes the matching map an isomorphism and removes the higher interaction.
- Removing one even assignment breaks surjectivity onto at least one codimension-one face, so the claim that all lower faces are unconstrained fails.
- Assigning parity restrictions to lower faces makes the interaction visible below arity \(n\) and no longer realizes the stated irreducibility.
- Treating an inadmissible full placement as an odd obstruction confuses absence of a configuration with nonfillability of an admitted one.

## Finite diagnostic

The checker enumerates \(2\le n\le8\). For each arity it verifies full projection onto every proper face, matching and obstruction cardinalities, exact kernel equality, rejection of the factorized top cube, and detection of the deleted-even-assignment mutation.

## Disposition

For every finite arity \(n\ge2\), a constraint can be invisible on all proper probe configurations yet nontrivial jointly. Higher Interaction Net cells therefore cannot in general be reconstructed from cells of lower arity. The parity family is an exact counterexample to lower-face completeness, not a classification theorem.
