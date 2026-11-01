# Su-32: independent checks of native-window operation and packet-square conjecture

**Date:** 2026-10-28  
**Input:** `su32-native-window-operation-v1.md` (user supplied); previous local packet-square notes used only for comparison.  
**Method:** exact lattice algebra, descent/equalizer analysis, integer chain complexes, obstruction/counterexample, index-five subgroup counting. No native JS source or its receipts were supplied. The code here does not replay the original source geometry, wire registry, or physical cell projection.

## A. Lattice and finite residue structure

Let \(A_3=\{t\in\mathbb Z^4: \sum_i t_i=0\}\) and \(\Lambda=\sum_{i=0}^2 \mathbb Z g_i\), \(g_i=\mathbf1-4e_i\). Relative to coordinates \((t_0,t_1,t_2)\), the generator matrix is

\[
 B=\begin{pmatrix}-3&1&1\\1&-3&1\\1&1&-3\end{pmatrix}.
\]

The gcd of entries is 1, the gcd of all 2x2 minors is 4, and \(|\det B|=16\). Thus its Smith invariants are \((1,4,4)\):

\[
 A_3/\Lambda\cong (\mathbb Z/4)^2.
\]

An explicit quotient map is

\[
\phi(t)=((t_0-t_3)\bmod4,\;(t_1-t_3)\bmod4).
\]

It is surjective. The kernel is exactly \(\Lambda\), because \(t_0\equiv t_1\equiv t_3\pmod 4\) and \(\sum t_i=0\) force \(t_2\equiv t_3\pmod4\), and the source formula then reconstructs integer period coordinates \(a_i=(t_3-t_i)/4\). In particular, \(\sum_i a_i g_i=t\).

**Meaning:** the ambient root-lattice quotient has 16 classes and supports a 4x4 group chart after choosing reference coordinates. It is *not* \((\mathbb Z/2)^4\). Nor does the group quotient alone supply physical edges, square fillers, a canonical P/E splitting, or an embedded torus. The identification with the 16 physical residue types in the source is plausible but needs the source's definition of the ambient translation lattice/occurrence map.

## B. Open boundary = exact gluing of two views

Take the native note's stated 420 distinct completed wire identities and 320 internal P slots, 320 internal E slots. If every wire is observed internally on at least one side and each slot denotes one wire, then

- 220 wires occur in both views (the fully internal P-N-E passages);
- 100 wires occur only internally on the P side (requiring external E output);
- 100 occur only internally on the E side (requiring external P input).

Let \(C,P_0,E_0\) denote disjoint sets of 220,100,100 wire labels, respectively. For *any set* \(X\), the complete wire state is

\[
 W(X)=X^{C\sqcup P_0\sqcup E_0}
  \cong X^{C\sqcup P_0}\times_{X^C}X^{C\sqcup E_0}.
\]

The equalizer condition is equality of contents at each common wire. The two restricted views separately omit 100 independent wire contents, but jointly reconstruct all 420 exactly. The result is a strict pullback of **set-valued observations**; it is not a new topological fibration or a simplicial 2-cell.

For additive coefficients, the same splitting gives a canonical integral exact sequence

\[
0\longrightarrow\mathbb Z^{420}
\xrightarrow{(r_P,r_E)}\mathbb Z^{320}\oplus\mathbb Z^{320}
\xrightarrow{\delta}\mathbb Z^{220}\longrightarrow0,
\qquad \delta(p,e)=p|_C-e|_C.
\]

Surjectivity of \(\delta\) is explicit (place any vector in P's common coordinates and zeros in E). The kernel consists precisely of matching profiles, reconstructed by amalgamation. This is a split exact sequence, so the integer descent has no hidden torsion. **Its applicability to native data depends on the wire identities and common-slot incidence asserted in the source note**, not on counts alone.

## C. Periodic-state restriction

The native note states that the old base has 64 wires and both internal views observe all base wire labels. For canonical pullbacks, the 420 wire values are obtained from 64 values by repeated labels. For a vector-valued state:

- the 64-dimensional periodic image has codimension 356 inside the unrestricted 420-dimensional state space;
- either 320-slot internal view restricts to a 64-dimensional image of codimension 256;
- boundary completion from one internal view is valid *only on that 64-dimensional image*.

This independently confirms why 80 internal P cells cannot be treated as 80 independent four-slot states in a closed carrier. Without a separate physical restriction, 100 external values remain irreducible.

## D. Does the 4x4 residue chart have torus topology?

Choose two coordinate translations as generators of \((\mathbb Z/4)^2\). Their Cayley graph can be the 4x4 periodic grid: 16 vertices and 32 undirected edges. Its first Betti number is **17**; it is *not* a torus as a 1-dimensional space.

If and only if 16 compatible grid-square 2-cells are included, with standard oriented boundaries, the cellular chain ranks are

\[
\operatorname{rank}(\partial_1)=15,\quad
\operatorname{rank}(\partial_2)=15,\quad
\partial_1\partial_2=0.
\]

The filled grid then has Betti numbers \((1,2,1)\) and geometric realization \(T^2\). This is the precise *higher admissibility* obligation. The additive quotient and commutation of permutations do not automatically authorize those source-level 2-cells or their history-aware fillers. They allow the filled torus as a candidate **once the square admission is constructed**.

## E. Reversible generators do not force square transport

Consider \((p,e,h)\in(\mathbb Z/2)^3\) and operations

\[
P(p,e,h)=(p+1,e,h+e),\qquad
E(p,e,h)=(p,e+1,h),
\]

with arithmetic mod 2. Both are involutions. Their projected action on \((p,e)\) commutes, but \(PE\) and \(EP\) differ by 1 on the retained witness \(h\). A four-step square circuit returns to the same visible point and flips \(h\). The eight-state system is an explicit countermodel to the inference "two reversible visible releases imply a uniquely filled compatible square." It could be represented with an extra comparison witness, but that is not supplied by the visible incidence.

## F. Cover obstruction and fibration interpretation

All index-five sublattices of a rank-three integer lattice are kernels of nonzero linear forms \((\mathbb Z/5)^3\to\mathbb Z/5\), modulo nonzero scalar, giving

\[
(5^3-1)/(5-1)=31.
\]

This independently verifies **exhaustiveness of the 31 candidate index-five covers**. It does **not** reverify the note's 31 native collision cases, which require the native window occurrence coordinates/receipts. The reported collision histogram sums to 31 and is internally consistent.

The integer-indexed source graph is a discrete \(\mathbb Z^3\)-cover of a wire graph. On that graph, \(H^2=0\), so it cannot already carry the nonzero first Chern class of the Hopf circle bundle. A topological Hopf structure requires a distinct space with admitted 2-cells and 3-dimensional topology, as well as continuous circle transport. A homomorphism from the discrete deck group into U(1) defines flat monodromy; that alone cannot produce \(|c_1|=1\) over \(S^2\).

## G. Exact native square test now available

For each *source-identified* two-order square with oriented translation labels \(t_1,t_2,t_3,t_4\in\Lambda\), calculate the integer deck discrepancy

\[
\Delta=a(t_1)+a(t_2)-a(t_3)-a(t_4)\in\mathbb Z^3,
\qquad a_i(t)=(t_3-t_i)/4.
\]

- \(\Delta=0\): routes end at the same lifted occurrence, so an incidence-level square comparison is eligible.
- \(\Delta\ne0\): the routes differ by an actual deck translation; equality in a finite quotient or equality of projected labels is insufficient to identify them.
- In either case: the source must still supply, or derive through its constructors, a **history-aware comparison/filler** and its compatibility under extension.

This is a smaller, source-faithful next experiment than requiring a full Hopf action immediately. It is not possible to calculate the actual \(\Delta\) values from the uploaded note alone: the individual release-path edge labels and source-certified square records are not included.

## Verification and provenance

`su32_independent_methods_audit.py` checks Smith invariants, finite period reconstruction, explicit 16-class coordinates, cubical chain ranks, common-wire gluing, 200 independent missing-coordinate examples, the 8-state counterexample, and all 31 abstract index-five subgroups. `su32_independent_methods_results.json` records results. The checker uses only the native note's stated lattice generators and aggregate slot census, not the original Node.js source or physical occurrence records. All direct source-specific collision, geometry and history assertions remain separate from this independent mathematical audit.
