# All finite atomic states form a classical process category

Finite atomic positive states are closed under the classical operations used in
the process lane:

- deterministic Hamiltonian evolution preserves atom count (N);
- independent product sends ((N,M)) to (NM);
- linear Cut pushforward sends the product support to at most (NM) atoms;
- convex mixture sends ((N,M)) to at most (N+M) atoms.

Coincident images reduce these upper bounds. Therefore no fixed-(N) stratum is
monoidally closed, but the union of all finite atomic strata is closed.

The exact checker audits 64 generic product/Cut cases, 1,296 product atoms, 64
disjoint mixtures, and a nontrivial collision quotient.

