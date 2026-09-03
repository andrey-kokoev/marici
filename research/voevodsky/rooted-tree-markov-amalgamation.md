# Rooted-tree Markov amalgamation

## Question

Is there a branching analytic constructor extending path-chain amalgamation and Beck–Chevalley?

## Claim boundary

This packet treats finite scalar rooted trees with one parent per nonroot vertex and edge contractions \(|a_e|<1\). Amalgamation is admitted only when rooted subtrees agree on their common rooted connected part and new branches are conditionally independent over it. Cycles, conflicting parents, and general graph amalgams are excluded.

## Tree kernel

Assign every vertex variance one. For vertices \(u,v\), let \(w\) be their lowest common ancestor and define

\[
K_{uv}=\left(\prod_{e:w\leadsto u}a_e\right)
       \left(\prod_{e:w\leadsto v}a_e\right).
\]

This is the covariance of the recursion

\[
X_c=a_{p\to c}X_p+\sqrt{1-a_{p\to c}^2}\,Z_c
\]

with independent innovations. Hence \(K\) is positive semidefinite.

## Branch amalgamation

A rooted subtree extension adds vertices with unique parents while preserving all existing parent and edge labels. Two extensions over a common rooted connected subtree amalgamate by union when their new vertex sets are disjoint and no parent assignment conflicts. Cross-branch covariances are forced by the lowest-common-ancestor formula, expressing conditional independence over the common subtree.

Set union and the fixed parent map make admitted amalgamation strictly associative. All parenthesizations of three compatible branch extensions yield the same tree kernel, so associators and the pentagon are identities.

## Beck–Chevalley

Restriction to a rooted ancestor-closed subtree commutes with kernel construction. Nested rooted-subtree restrictions compose strictly, giving invertible identity Beck–Chevalley cells. Pullback of two branch inclusions is their common rooted subtree when their intersection is ancestor-closed.

## Hostile boundary

A proposed extra edge creating a cycle has no unique-parent tree type. A vertex assigned different parents in two branches has no amalgam. A non-ancestor-closed vertex subset is not a rooted-subtree restriction; it requires effective-edge derivation as in ordered-subset path restriction.

## Disposition

A branching partial-double-category constructor exists for compatible finite rooted Markov trees. It extends path coherence and supplies a restricted non-monic-looking branch pullback, but does not establish arbitrary graph or cyclic amalgamation.

## Verification

- `research/voevodsky/checkers/check_rooted_tree_markov_amalgamation.py`
- `research/voevodsky/results/rooted_tree_markov_amalgamation.json`
