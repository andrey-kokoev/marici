# Ramsey generator: current position of the matrix and symmetry programme

**Date:** 8 November 2026  
**Scope:** The two-colour off-diagonal Ramsey numbers \(R(3,k)\).  
**Status:** Exact phase/adjacency algebra and several certified finite constructions; no general closed formula, universal successor law, or universal extremality theorem.

## 1. Question and standard of proof

We seek an operation that starts from the symbolic row family

```text
k=3   R 0 0
k=4   R G 0 0
k=5   R G R 0 0
k=6   R G R G 0 0
k=7   R G R G R 0 0
k=8   R G R G R G 0 0
k=9   R G R G R G R 0 0
k=10  R G R G R G R G 0 0
```

and generates the admissible coloured adjacency matrices, including the appropriate successor sector as \(k\) increases. The conjectural explanation is that new Ramsey capacity comes from the formation and compatibility of successive symmetry sectors.

An **exact Ramsey formula** would have to give \(R(3,k)\) for arbitrary \(k\) with proof. An **exact lower-bound constructor** produces triangle-free graphs with independence number below \(k\), but does not exclude larger graphs. A **presentation-level phase operation** rotates symbolic coefficients; it does not, by itself, produce a valid red/blue edge colouring.

The problem is naturally expressed using a symmetric binary red adjacency matrix \(A\), with zero diagonal and blue complement

\[
B=\mathbf1\mathbf1^{T}-I-A.
\]

Ramsey admissibility at parameter \(k\) is exactly

\[
\operatorname{tr}(A^3)=0,
\qquad
\alpha(A)\le k-1.
\]

The first condition excludes red triangles, and the second excludes blue \(K_k\)'s. These are the acceptance conditions for every proposed matrix operation.

## 2. Original reflection and source phase carrier

Index a row by \(0,\ldots,k-1\). Encode \(R=+1\), \(G=-1\), \(0=0\), obtaining \(x_k\). The two final empty slots select the index involution

\[
H_k(j)=k-3-j\pmod k.
\]

Reversing the alternating nonempty prefix gives, for all \(k\ge3\),

\[
\boxed{H_k x_k=(-1)^{k+1}x_k.}
\]

For odd \(k\), reflection preserves the signed row; for even \(k\), it exchanges the two symbolic colours. This is a statement about the source record, **not** a permission to exchange red/blue roles inside the asymmetric Ramsey problem.

On the full \(\mathbb R^k\), a real operator \(P\) with \(P^2=H_k\) does not always exist. That requirement is stronger than our source needs. The source-generated invariant carrier has:

- **even \(k\ge4\):** a two-dimensional real quarter-turn plane; four distinct source phases;
- **odd \(k\ge5\):** a fixed line plus a two-dimensional quarter-turn plane; four distinct source phases;
- **\(k=3\):** a degenerate seed for this particular empty-slot contrast construction.

On these restricted subspaces, \(P^4=I\) and \(P^2=H_k\). These identities were checked for \(k=4,\ldots,10\), with algebraic parity proofs valid beyond the tested range. They do **not** require a real square root of the reflection on all \(k\) coordinates.

Reference: `ramsey_rooted_matrix_reflection_and_phase_carrier_2026-11-08.md`; checker: `ramsey_original_matrix_sector_audit.py`.

## 3. Four binary incidence columns require a second harmonic

The nontrivial Ramsey example starts with the 13-vertex graph

\[
G_{13}=C_{13}(\pm1,\pm5),\qquad \alpha(G_{13})=4.
\]

Its order-four automorphism is \(\sigma(v)=5v\pmod{13}\). The seed \(S_0=\{1,7,11\}\) generates red-neighbourhood supports

| Phase | Support |
|---:|---|
| 0 | \(\{1,7,11\}\) |
| 1 | \(\{3,5,9\}\) |
| 2 | \(\{2,6,12\}\) |
| 3 | \(\{4,8,10\}\) |

Let \(n_t\) be their 13-entry binary indicators and \(X=[n_0\ n_1\ n_2\ n_3]\). The supports are disjoint, so

\[
\boxed{X^{T}X=3I_4,\qquad\operatorname{rank}X=4.}
\]

The four normalized phase states \(q_0=(1,0),q_1=(0,1),q_2=(-1,0),q_3=(0,-1)\) obey \(q_0+q_2=q_1+q_3\). The binary incidence columns do not obey the corresponding equality. No affine decoder of those four phase points can reproduce the columns.

A degree-two decoder works exactly. Define

\[
\begin{aligned}
M&=(n_0+n_1+n_2+n_3)/4,\\
C&=(n_0-n_2)/2,\quad D=(n_1-n_3)/2,\\
E&=(n_0-n_1+n_2-n_3)/4.
\end{aligned}
\]

Then

\[
\boxed{
\Phi(c,s)=(c^2+s^2)M+cC+sD+(c^2-s^2)E
}
\]

satisfies \(\Phi(q_t)=n_t\) and commutes with the prescribed quarter-turn action. The incidence representation decomposes as

\[
\mathbf1\oplus V_{90^\circ}\oplus\varepsilon
\quad\text{(dimensions }1+2+1=4\text{)}.
\]

The new component \(E\) is the alternating, second-harmonic character: it reverses sign under a single quarter-turn. This is an exact explanation of why the binary incidence orbit contains one mode absent from the affine quarter-turn presentation.

**Qualification:** the decoder coefficients \(M,C,D,E\) were computed from *already known* adjacency columns. The polynomial reconstructs and transports those columns; it does **not** derive the 13-vertex graph, the seed orbit, or the sector length from the short symbolic row.

More generally, \(q\) linearly independent columns assigned to \(q\) equally spaced phases on the circle require real polynomial degree at least \(\lfloor q/2\rfloor\), and Fourier interpolation achieves that degree. This describes incidence decoding, not Ramsey thresholds.

Reference: `ramsey_quadratic_phase_to_incidence_2026-11-08.md`; checker: `check_ramsey_quadratic_phase_decoder.py`.

## 4. The full block-matrix operation and its acceptance test

For an old adjacency matrix \(A\), a permutation matrix \(P\) with \(PAP^T=A\), a seed binary column \(x\), and \(q\) new vertices, define

\[
X=[x,Px,\ldots,P^{q-1}x],\qquad
A'=\begin{pmatrix}A&X\\X^T&C\end{pmatrix},
\]

where \(C\) is a symmetric zero-diagonal binary matrix on the new vertices. For \(q=4\) one can require \(P^4=I\), but a general successor need not have orbit length four.

The red-triangle constraint is the exact nonnegative decomposition

\[
\operatorname{tr}((A')^3)=
\operatorname{tr}(A^3)
+3\operatorname{tr}(X^TAX)
+3\operatorname{tr}(CX^TX)
+\operatorname{tr}(C^3).
\]

The independent-set condition can be evaluated without enumerating every colouring of the new block. If \(F\) has adjacency \(C\) and the red old-neighbourhoods of its vertices are \(S_j\), then

\[
\boxed{
\alpha(A')=
\max_{J\in\operatorname{Ind}(F)}
\left(|J|+\alpha\left(G-\bigcup_{j\in J}S_j\right)\right).
}
\]

**Proof:** every independent set of the enlarged graph is uniquely determined by its independent subset \(J\) of new vertices and an independent subset of the old graph avoiding all red neighbours of \(J\). The formula also gives the independence-polynomial identity

\[
I_{A'}(z)=\sum_{J\in\operatorname{Ind}(F)}
z^{|J|}\,I_{G-\cup_{j\in J}S_j}(z).
\]

These formulas are complete acceptance tests for *specified* blocks. They are not a rule selecting the next block.

## 5. Verified finite successor results and limits

### \(13\to17\): unique cyclic sector within a declared family

Fix \(G_{13}\), its order-four automorphism \(\sigma\), and four new vertices permuted cyclically. Exhaustively test all 183 independent seed sets and all four cyclically invariant internal red graphs: empty, matching, \(C_4\), and \(K_4\).

Exactly **four** combinations pass triangle-freeness and \(\alpha\le5\); all use the internal red \(C_4\) and are cyclic translates of \(\{1,7,11\}\). Each yields a 17-vertex graph with 42 red edges and independence number five.

Thus the seed and internal edge orbit are forced **conditional on the supplied 13-vertex parent, four-cycle symmetry, and four-vertex attachment family**. This constructs a lower-bound witness for \(R(3,6)\ge18\), not the upper bound.

### \(17\to22\): a locally selected pair, then a forced bipartite continuation

McKay's catalog has seven nonisomorphic extremal 17-vertex \(R(3,6)\) graphs. Each contains a red induced four-cycle \(T\) whose removal leaves the unique 13-vertex \(R(3,5)\) graph. Selecting two red neighbourhoods consisting of opposite pairs of \(T\) minimizes the red-neighbourhood support of a compatible **blue** pair in each of these seven graphs.

Once that initial pair \(a,b\) is attached, the exact next-neighbourhood family, in all fourteen qualifying four-cycle decompositions, is

\[
\boxed{
\mathcal E_7(H)=\{\{a,b\}\cup U:U\in\operatorname{Ind}(G_{13})\}.
}
\]

Every later vertex must therefore be red-adjacent to \(a,b\); two later vertices cannot have a red edge between them (it would form a triangle through \(a\)). Consequently the new-vertex graph has the forced form \(K_{2,t}\), **after** the initial minimum-compatible pair has been chosen.

Of the fourteen decompositions, ten admit three further vertices, reaching a valid 22-vertex graph with \(\alpha=6\); four stop at 21. In successful cases the four compatible triples form a \(2\times2\) square of choices. The terminal size emerges from the restricted continuation constraints, rather than being specified as an input to that search.

**Known limitation:** in a sample of twenty published extremal 22-vertex \(R(3,7)\) graphs, two have no decomposition as a red \(K_{2,3}\) attachment to an extremal 17-vertex predecessor. Hence this attachment shape is **not universal**. Nor does Ramsey admissibility force the initial minimum-support pair: that is a declared optimization criterion.

References: `ramsey_four_cycle_forced_successor_2026-11-08.md`, `ramsey_quarter_turn_to_bipartite_sector_2026-11-08.md`; checkers: `ramsey_forced_sector_successor_2026-11-08.py`, `ramsey_17_to_22_successor_certificate.py`.

## 6. What is and is not a general formula for \(R(3,k)\)

For a fixed \(k\), let \(\mathcal F_k(n)\) be the family of all nonisomorphic triangle-free graphs on \(n\) vertices with independence number at most \(k-1\). The exact vertex-extension recurrence is

\[
\mathcal F_k(n+1)=\operatorname{Iso}\left\{
G+v_S:
G\in\mathcal F_k(n),\;
S\in\operatorname{Ind}(G),\;
\alpha(G-S)\le k-2
\right\}.
\]

Every admissible graph is obtained in this way: delete any vertex from it and recover that vertex as an allowed extension. Therefore

\[
\boxed{R(3,k)=1+\max\{n:\mathcal F_k(n)\ne\varnothing\}.}
\]

This is an exact, proved **enumerative recurrence**, not a closed form. A finite matrix sum can equally count all admissible colourings. Neither representation compresses the state space enough to explain the thresholds.

Reference values as of November 2026:

| \(k\) | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(R(3,k)\) | 6 | 9 | 14 | 18 | 23 | 28 | 36 | 40–41 |

Known asymptotic bounds are

\[
\left(\tfrac12+o(1)\right)\frac{k^2}{\log k}
\le R(3,k)\le
\left(1+o(1)\right)\frac{k^2}{\log k}.
\]

The existence of a limiting leading constant is unknown. Thus an optimal universal successor cannot add only a bounded number of vertices at every increment of \(k\): its total size would be \(O(k)\), contradicting the superlinear lower bound.

External references:

- Brendan McKay, [Ramsey graphs and critical-graph catalogs](https://users.cecs.anu.edu.au/~bdm/data/ramsey.html).
- Tao's [asymptotic-constant problem bibliography](https://teorth.github.io/optimizationproblems/constants/17b.html), including Hefty–Horn–King–Pfender's 2025 lower-bound improvement.
- Vigleik Angeltveit, [\(R(3,10)\le41\)](https://doi.org/10.37236/12936) (2025).

## 7. Previously investigated mechanisms: retained versus retired

The geometric spiral of nonadjacent three-mark arrangements produced exact gap-coordinate simplices and commuting insertion cubes. Their higher cells already have canonical fillings. The spiral, by itself, does not impose graph edge-colour consistency.

Constraint-compatibility complexes exposed genuine minimal incompatible families and sometimes nonzero homology. These are properties of particular graph-extension systems; they did not yield a cross-\(k\) completeness theorem. Matching circuits and Bonferroni overlap bounds refined obstruction certificates but likewise did not derive Ramsey thresholds.

Group names such as \(C_{12}\), the octahedral rotation group, \(S_5\), and \(M_{24}\) have appeared as mathematical candidates or in particular associated constructions. No universal identification of the Ramsey generator with any of those groups has been established.

The earlier numeric matches obtained by counting rotated symbolic cells, including 23, 28, and 36, are **not proofs of Ramsey values**. Requiring all symbolic phases to be literal permutations of the same row was also too restrictive: the source allows retained real coefficient phases, while the graph demands binary incidence.

## 8. Current bottleneck and a decisive next experiment

The unresolved map has three parts:

\[
\boxed{
\text{symbolic row }x_k
\ \longrightarrow\
\text{selected old graph and phase/sector carrier}
\ \longrightarrow\
(A,X,C)
\ \longrightarrow\
\text{Ramsey-extremal successor}.
}
\]

The restricted phase carrier and a *conditional* quadratic decoder are known. The old graph, the orbit length, the binary incidence coefficients, and the initial attachment selection are still supplied by graph-specific data or optimization choices. The verified \(K_{2,3}\) counterexamples show that at least one apparently natural family is incomplete.

**Single most discriminating experiment:** freeze one rule taking only a symbolic source record and inherited matrix incidence to the next block, including its sector size and seed selection, before consulting the next Ramsey value or target graph. Test the unchanged rule on all known predecessor types, and report both constructions and counterexamples. A family that fails on one legitimate extremal successor is not complete; a family that constructs some extremal successors establishes lower bounds only. A full solution additionally requires a universal upper-bound argument excluding larger admissible graphs.

The current research result is an exact algebraic separation between **phase transport**, **incidence reconstruction**, and **Ramsey extremality**, with nontrivial certified instances of the first two and a sharply localized, unresolved completeness problem in the third.

## 9. Reproduction index

The following files are part of the current local research artifacts (not committed to the repository):

| Artifact | Purpose |
|---|---|
| `ramsey_original_matrix_sector_audit.py` | Original rows; reflection; restricted phase-carrier identities |
| `check_ramsey_quadratic_phase_decoder.py` | Rank obstruction; quadratic decoder; exhaustive cyclic four-sector selection |
| `ramsey_quarter_turn_sector_generator.py` | Explicit \(13\to17\) block constructor |
| `ramsey_forced_sector_successor_2026-11-08.py` | All seven 17-vertex parents; 14 selected decompositions; forced continuation; counterexamples |
| `ramsey_17_to_22_successor_certificate.py` | Selected \(17\to22\) finite certificate |
| `ramsey_two_channel_extension.py` | General one-/two-vertex extension formulas and checks |
| `ramsey_disjointness_saturation_audit.py` | Terminal-extension conditions and cyclic constraint incidence |

The principal phase and successor checkers were rerun while preparing this note. Their claims are **finite exact checks**, with general statements separately justified by algebraic proofs; no universal Ramsey formula is claimed.
