# Finite Deck Pull–Push Satisfies Beck–Chevalley

For a pullback square of finite deck sets

\[
\begin{array}{ccc}
P&\xrightarrow{a}&G\\
\downarrow b&&\downarrow f\\
H&\xrightarrow{g}&K,
\end{array}
\]

use ordinary pullback on functions and unnormalized fiber-sum pushforward.
Then

\[
\boxed{b_!a^*=g^*f_!.}
\]

On the delta basis, both sides evaluate at \(h\in H\) to

\[
\mathbf 1_{f(x_0)=g(h)}.
\]

The checker exhausts every pair of cyclic homomorphisms
\(C_a\to C_k\leftarrow C_b\) for
\(1\le a,b,k\le8\), constructs the literal pullback fiber, and verifies
the identity on every delta basis vector and target point.

This promotes the algebraic deck readout from isolated pullback and transfer
formulas to a finite-correspondence/Mackey-type calculus.  It does **not**
admit that calculus physically.  The cosmological source currently supplies
equivariant chamber transport and pairing, but no quotient-cover
pushforwards.  Thus the precise missing resource is an admissible
correspondence leg with oriented relative-chain pushforward.

Artifact:

- `research/nima/check_finite_deck_beck_chevalley.py`
- `research/nima/results/finite-deck-beck-chevalley.json`
