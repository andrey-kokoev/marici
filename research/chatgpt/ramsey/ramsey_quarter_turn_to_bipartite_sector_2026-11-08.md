# From four-phase symmetry to a forced bipartite Ramsey sector

2026-11-08. Exact finite construction, with independently reproducible certificate in `ramsey_17_to_22_successor_certificate.py`.

## Statement

Let \(G_{13}\) be the triangle-free Cayley graph on \(\mathbb Z_{13}\) with difference set \(\{\pm1,\pm5\}\). It has \(\alpha(G_{13})=4\). Multiplication by five is an automorphism \(\sigma\) of order four, with one fixed vertex and three four-cycles on the other vertices.

Select one vertex from each nonzero four-cycle to form an independent seed \(S\). Adjoin a red four-cycle \(a_0,a_1,a_2,a_3\), with red neighborhoods \(\sigma^t S\) in the original graph. Among 64 such transversals, 20 are independent; exactly four yield a triangle-free 17-vertex graph of independence number five. All four are one orbit of \(\langle\sigma\rangle\). Denote the resulting graph by \(G_{17}\).

The four-cycle successor cannot simply be repeated at parameter \(k=7\). Exhausting every independent seed in \(G_{17}\) and adding its four rotated neighborhoods with an internal red \(C_4\) yields 20 valid 21-vertex graphs, five modulo quarter-turn rotation. **All five are terminal:** no independent neighborhood produces an admissible 22nd vertex with independence number at most six. Alternative invariant four-vertex attachments consisting of a blue independent four-set or a red matching produce no valid 21-vertex successor.

A different, smaller-internal-symmetry attachment is successful:

1. Add two vertices with old red neighborhoods \(L_0=\{a_0,a_2\}\) and \(L_1=\{a_1,a_3\}\), the two opposite pairs of the inherited four-cycle.
2. Let \(\mathcal M_4\) contain the 39 maximum independent four-sets of the original 13-vertex core. Construct their **pair compatibility graph** by
   \[
   U\sim V \quad\Longleftrightarrow\quad \alpha(G_{17}-(U\cup V))\le4.
   \]
   There are exactly 129 edges among its 39 vertices.
3. The compatibility graph has exactly **four triangles**, all related by the quarter-turn. Every such triple \(U,V,W\) also satisfies \(\alpha(G_{17}-(U\cup V\cup W))\le3\).
4. Introduce three further vertices with old red neighborhoods \(U,V,W\). Among all \(2^{10}=1024\) red/blue assignments to the ten possible new-new edges, exactly **one** avoids red triangles and blue independent sets of size seven. It is the complete bipartite graph \(K_{2,3}\), with the pair \(L_0,L_1\) on one side and the triple \(U,V,W\) on the other.

The resulting \(G_{22}\) has 22 vertices, 64 red edges, no red triangle, and independence number six. An independent graph-isomorphism calculation matches it to a graph in McKay's complete catalog of 191 extremal \(R(3,7)\) witnesses: <https://users.cecs.anu.edu.au/~bdm/data/ramsey.html>. Consequently this finite construction proves \(R(3,7)\ge23\) and reproduces an extremal witness given the independently known upper bound.

## A concrete representative

For the initial quarter-turn, choose \(S=\{1,7,11\}\) in \(G_{13}\). The four rotating neighborhoods are

\[
\{1,7,11\},\quad\{3,5,9\},\quad\{2,6,12\},\quad\{4,8,10\}.
\]

A representative successful right-side triple in the five-vertex successor is

\[
\begin{aligned}
U&=\{1,5,8,12\},\\
V&=\{0,3,6,10\},\\
W&=\{0,2,4,11\}.
\end{aligned}
\]

The set \(U\) is the unique four-element maximum independent set fixed under multiplication by five; \(W=\sigma(V)\). The other three successful triples are the successive rotations of this choice. Selecting one breaks the inherited quarter-turn symmetry. The resulting 22-vertex witness has trivial full graph automorphism group (independently checked with graph isomorphism software).

## Proof mechanism

For any old graph \(G\), new-vertex red graph \(F\), and their old red neighborhoods \(S_i\), triangle-freeness is equivalent to: \(G\) and \(F\) are triangle-free; every \(S_i\) is independent in \(G\); and \(S_i\cap S_j=\varnothing\) for every red edge \(ij\in F\).

The exact independence-number identity is

\[
\alpha(G\cup_F\{v_i\})=
\max_{J\in\operatorname{Ind}(F)}
\left(|J|+\alpha\left(G-\bigcup_{j\in J}S_j\right)\right).
\]

The certificate uses this identity to enumerate all neighborhood and edge-color possibilities without trusting the catalog to determine their validity. It independently checks the final 22-vertex graph by a second maximum-independent-set algorithm.

For the five-vertex attachment, every failure of the 1,024 new-edge assignments is classified as follows, in this check order:

| Classification | Assignments |
|---|---:|
| Red triangle entirely within the new five | 636 |
| Red triangle involving an old vertex | 141 |
| Independent seven-set | 246 |
| Admissible | **1** |

## What is proved, and what is not

This proves a **uniqueness theorem inside a specific symmetry-informed construction family**. Once the first two neighborhoods are chosen as opposite pairs of the inherited red \(C_4\), the remaining three old neighborhoods are chosen from the 39 maximum independent sets of the 13-vertex core, and the three right-side vertices are constrained to be mutually blue, the allowable triple is unique up to the old quarter-turn; the five-vertex edge coloring is then forced.

The choice of the \(2+3\) attachment family is **not derived as uniquely necessary among all possible additions**. Its relevance was first recognized by comparison with an existing 22-vertex witness, then tested independently and exhaustively within the declared family. The existence of 191 nonisomorphic extremal 22-vertex graphs also prevents interpreting this single family as a complete classification of successors.

No universal formula for \(R(3,k)\) follows. The next discriminating mathematical question is whether the selection of a two-vertex opposite-pair orbit and a maximal compatible triple can be obtained from a general source-defined rule rather than a choice of construction family. If it can, test the rule **without a predefined next-size target** against other 17-vertex extremal graphs and the 22-to-27 transition.

## Reproduction

```sh
python ramsey_17_to_22_successor_certificate.py
```

The script uses Python's standard library, exhaustive integer-mask independence and exact graph checks; it prints the complete 22-vertex edge list for independent verification.
