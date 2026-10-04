# Augmentation realization and the 11/25, 14/25 dephasing fractions

## Question, boundary, and disposition

Can the four-state coherence shadow supply the tetrahedron, its character axes, and the previously geometric weights without inserting an independent Euclidean tetrahedron?

**Finite theorem:** given V = F2^2 with a nontrivial order-three automorphism, counting/dagger linearization, an oriented tetrahedral boundary, and the prescribed centroid–cyclic-mode witness, the translation Reynolds projection of the resulting pure projector has spectrum {1,7,7}/15. Its retained and transverse **squared** Hilbert–Schmidt norms are 11/25 and 14/25.

This replaces the independent tetrahedral geometry by an augmentation construction. It does not derive the witness prescription from minimal faithful representation theory alone, establish the proposed stable-category origin, identify physical observables, or identify a wheel carrier. The proof below is finite-dimensional; there is no cutoff/completion inference or physical-time interpretation.

Operator provenance: the operator supplied two arguments identifying the Fourier tetrahedron with the augmentation space and the readout with translation dephasing, then requested documentation in `research/nima/`. The proposals are inputs to mathematical review, not evidence by attribution. No external linked reference is treated as independently verified here.

SCC obligation: forward realization of the finite source, attachment transport of the edge witness, and equivariance of the operator projection. Physical readout descent and the upstream stable-source comparison remain separate obligations.

## Explanatory issue

- **Problem:** distinguish a source-defined finite realization from a chosen vector with matching fractions.
- **Conjecture:** augmentation, face averaging, and the cyclic coefficient mode yield the same geometric projector and an intrinsic dephasing formula.
- **Rivals:** a separately supplied tetrahedron is necessary; the character basis is arbitrary; carrier uniqueness alone forces the state; the fractions require the earlier rank-25 mixed state.
- **Risky consequences:** tetrahedral Gram entries arise from delta states; all oriented edges obey the same coordinate-free formula; dephasing is an orthogonal projection; the specified witness gives 11/25 while another equivariant witness can give a different value.
- **Falsifier:** construct the operators in the four-dimensional delta basis and test the formula on all 24 distinct ordered vertex triples, including both boundary orientations. Test the edge-difference witness on the same carrier as a counterexample to state uniqueness.
- **Disposition:** the finite construction and intrinsic readout survive the proof below. Minimal faithful equivariance alone does not select the witness. Machine verification is recorded in the final section.

## 1. Canonical augmentation geometry

Let V = F2^2 and let r be an automorphism cycling its three nonzero elements. Then

\[
A=V\rtimes\langle r\rangle\cong A_4.
\]

Take H = R[V] with orthonormal basis delta_x and augmentation

\[
\varepsilon(f)=\sum_{x\in V}f(x),\qquad
W=\ker\varepsilon,\qquad H=\mathbf R\mathbf1\oplus W.
\]

Translations and r act by orthogonal permutations. An invariant positive measure on the four delta states is constant, since the action is transitive. This proves uniqueness of invariant **diagonal counting weights**, not uniqueness of every invariant inner product on H: the constant and augmentation summands may have different positive scales.

Define

\[
u_x=2\left(\delta_x-\frac14\mathbf1\right).
\]

Direct calculation gives

\[
\langle u_x,u_y\rangle=4\delta_{xy}-1,\qquad \sum_xu_x=0.
\]

Thus the four vectors form a regular tetrahedron in W, without separately specified spatial vertices. The factor 2 fixes the convenient norm squared 3; an overall scale cancels from normalized projectors.

For each nontrivial real character chi of V, the vector chi/2 in H has norm one. These three vectors form an orthonormal basis of W and

\[
\langle\chi/2,u_x\rangle=\chi(x).
\]

Choosing their order gives the vertex coordinates

\[
(1,1,1),\ (1,-1,-1),\ (-1,1,-1),\ (-1,-1,1).
\]

The unordered character lines are intrinsic joint eigenspaces of translation. Fourier coordinates expose them; they do not create the tetrahedron.

### Representation uniqueness and its limit

A V-invariant subspace of W decomposes into character lines. The order-three action cycles all three lines, so no nonzero proper subspace is A-invariant. The same argument over C proves absolute irreducibility. An invariant inner product on W makes distinct V-character lines orthogonal, and r forces their three lengths equal; it is therefore unique up to scale.

More generally, in any faithful real A-representation, a nontrivial V-character must occur. Its C3 orbit contains all three nontrivial characters, so the dimension is at least three. In dimension three each occurs once; after rescaling the three eigenvectors, the order-three action is the cyclic permutation. Hence any faithful three-dimensional real representation is equivalent to W. A unitary equivalence can be chosen after normalizing the invariant metric.

This classifies the **carrier**, not an equivariant family of selected rays on it.

## 2. The specified face witness

Choose one of the two orientations of the tetrahedral boundary. For each directed edge e = (x,y), there is exactly one incident face whose induced boundary orientation traverses x to y; write z for its third vertex. Both incident faces exist geometrically: the uniqueness is orientation-compatible incidence.

The face stabilizer cycles its three vertices. Its unique fixed affine point is the Reynolds average

\[
b_e=\frac{u_x+u_y+u_z}{3}.
\]

Uniqueness follows because invariance makes the three barycentric coefficients equal. It is uniqueness among one-point-per-face affine choices, not a classification of every possible subdivision.

Now impose the witness prescription: the ordered small triangle (b_e,u_x,u_y) carries the nontrivial cyclic **coefficient** eigenline (1,omega,omega^2), with omega = exp(2 pi i/3). In the complexification W_C define

\[
\psi_e=b_e+\omega u_x+\omega^2u_y,\qquad
P_e=\frac{\psi_e\psi_e^\dagger}{\|\psi_e\|^2}.
\]

The geometric face rotation fixing b_e and the coefficient rotation of this small triangle are different operations. The small triangle is not equilateral: its centroid-to-vertex side lengths squared are 8/3, while its selected edge has length squared 8. Consequently its cyclic coefficient permutation is not an ambient Euclidean rotation. Deriving this witness prescription from the source triangle primitive requires an explicit comparison, not that geometric identification.

For the reference vertices A,B,C displayed above,

\[
b=(1/3,1/3,-1/3),\qquad
\psi=(-2/3,\ 1/3+i\sqrt3,\ -1/3+i\sqrt3).
\]

Thus the squared component lengths are (4,28,28)/9 and the total is 20/3.

## 3. Character-free dephasing identity

Let d = y-x, a nonzero element of V, and write rho(v) for translation restricted to W_C. Among the three nontrivial characters, precisely one has chi(d)=+1 and two have chi(d)=-1.

To see the weights without selecting a coordinate order, fix chi and put a=chi(x), b=chi(y), c=chi(z). Its component of psi_e is

\[
\frac{a+b+c}{3}+\omega a+\omega^2b.
\]

If a=b, then c=-a and this component is -2a/3, with squared modulus 4/9. If a=-b, then it is c/3+i sqrt(3) a, with squared modulus 28/9. These cases use only distinctness of x,y,z and the two-element character fibers. Normalization yields weights 1/15 on the +1 line of rho(d) and 7/15 on its two -1 lines.

Define the translation Reynolds conditional expectation on End(W_C):

\[
\mathbb E_V(T)=\frac14\sum_{v\in V}\rho(v)T\rho(v)^\dagger.
\]

It is trace-preserving, unital, positive, idempotent, and self-adjoint for the Hilbert–Schmidt inner product. Its image is the translation commutant, which here is the character-diagonal algebra. Character orthogonality kills precisely the off-diagonal matrix units. Therefore

\[
\mathbb E_V(P_e)=\frac4{15}I_W-\frac15\rho(d).
\]

This formula is intrinsic to the representation and edge displacement. For g in A,

\[
P_{ge}=\rho(g)P_e\rho(g)^\dagger,\qquad
\mathbb E_V(\rho(g)T\rho(g)^\dagger)
=\rho(g)\mathbb E_V(T)\rho(g)^\dagger,
\]

because V is normal in A. Consequently the unordered dephased spectrum is the same for every directed edge. Choosing the opposite boundary orientation also preserves these weights. Conjugating the coefficient mode on a fixed ordered triangle conjugates P_e and preserves its dephasing. Reversing an edge with the boundary orientation held fixed instead selects the other incident face; that operation need not merely conjugate the same P_e.

The spectrum {1,7,7}/15 belongs to E_V(P_e). The pure projector P_e itself has spectrum {1,0,0}.

## 4. Squared norms and their interpretation

Use the ordinary, unnormalized matrix trace on End(W_C). Since rho(d)^2=I_W and Tr rho(d)=-1,

\[
\left\|\mathbb E_V(P_e)\right\|_{\mathrm{HS}}^2
=\operatorname{Tr}\left(\mathbb E_V(P_e)^2\right)
=\frac{75+24}{225}=\frac{11}{25}.
\]

Because P_e has rank one and E_V is an orthogonal projection,

\[
\|P_e\|_{\mathrm{HS}}^2=1,\qquad
\left\|P_e-\mathbb E_V(P_e)\right\|_{\mathrm{HS}}^2=\frac{14}{25}.
\]

The corresponding norms are sqrt(11)/5 and sqrt(14)/5. This is an orthogonal decomposition in operator space, not an 11-dimensional versus 14-dimensional decomposition of a 25-dimensional state space. End(W_C) has complex dimension 9; the dephased and transverse operator subspaces have dimensions 3 and 6.

There is also a defined state–effect pairing:

\[
\operatorname{Tr}\left(P_e\mathbb E_V(P_e)\right)=11/25.
\]

It is the return probability for the mathematical protocol that prepares P_e, applies a uniformly sampled translation, and tests the effect P_e. No apparatus or physical preparation implementing this protocol is established by the algebra.

## 5. Carrier symmetry does not select the witness

Consider the rival rule on exactly the same carrier and metric:

\[
\psi'_e=u_y-u_x,\qquad
P'_e=\frac{\psi'_e\psi_e'^\dagger}{\|\psi'_e\|^2}.
\]

It is A-equivariant. Its character weights are {0,1/2,1/2}, giving

\[
\left\|\mathbb E_V(P'_e)\right\|_{\mathrm{HS}}^2=1/2.
\]

The directed-edge action of A4 is free and transitive: any reference ray can be extended to an equivariant edge-indexed ray family. Thus minimal faithful A4-equivariant dagger linearization alone cannot force P_e or 11/25. This rival does not satisfy the prescribed centroid–cyclic-mode rule; it identifies that rule as a substantive selecting premise.

## 6. Relation to the earlier audit and remaining arrows

The [affine push-pull audit](affine-push-pull-spectral-target.md) retains its conclusions: bare counting averaging does not have native diagonal (1,7,7)/15, and the algebra generated by L,G does not split its rank-25 sector into ranks 11 and 14. Its geometric-normal extension obtains a different, conditional rank split and uses the state K/25.

The present construction does not repair either obstruction by changing counting coefficients. It derives the geometric decoration from augmentation plus the prescribed witness, and uses a different readout on the resulting pure projector. It therefore needs neither selection of K nor the maximally mixed state K/25 to establish these mathematical fractions. No equality of the two constructions' observables is inferred from matching numbers.

The shared finite starting object is V with its order-three action. The earlier sum 108+432+1296=1836 counts three tagged relations, including their diagonal pairs; it is not promoted here to a physical mass or an unqualified count of nonidentity arrows.

The proposed longer source chain is

\[
\mathcal U\longrightarrow K_0(\mathcal U)
\longrightarrow K_0(\mathcal U)/2
\longrightarrow(V,r)
\longrightarrow(W,\{P_e\},\mathbb E_V).
\]

The first absent comparison in this packet is the explicit stable-source-to-finite-shadow map: compute the stated K0, its rotation, and its nontrivial order-three mod-2 reduction for the actual source U. An identification with Z[zeta_6] must specify whether it is an abelian group with an operator, a module, or a ring; equal rank does not provide the extra structure. General paracyclicity is not that computation. After this, a source-witness comparison must carry the triangle primitive to the stated centroid coefficient map. These are acceptance conditions, not newly proved arrows.

A physical identification additionally requires a specified preparation and effect/channel map to this finite realization. This missing physical map does not invalidate the internal finite theorem; neither does the finite theorem supply it.

## Reproduction and verification

Checker: `checkers/check_augmentation_fourier_dephasing.py`.
Result: `results/augmentation-fourier-dephasing.json`.
SCC manifest: `scc-models/augmentation-fourier-dephasing.json`.

```text
python research/nima/checkers/check_augmentation_fourier_dephasing.py
python research/aspect/scc/scc.py validate research/nima/scc-models/augmentation-fourier-dephasing.json
python research/aspect/scc/scc.py check augmentation-fourier-dephasing
```

The checker uses exact rational arithmetic in Q(i sqrt(3)), reconstructs centered delta states rather than importing tetrahedral coordinates, and tests all 24 distinct ordered vertex triples. It tests the Reynolds operator on a spanning set of End(W_C), both orientation families, A4 covariance, and the edge-difference rival. The checker passed with exit code 0: 24 witness triples, 288 A4 covariance checks, nine operator-basis checks, exact squared norms, and the distinct 1/2 value for the rival. Execution receipt: `structured_command_execution:e_25120_1790944900701150800_131`. SCC manifest validation and its registered checker run also passed; SCC's adapter reports exit-code evidence only. These checks do not certify the stable-source or physical comparisons.

Graph provenance: event `ev-000000015679-da183e59-f0da-4fd0-8d0f-a76d6b150c1e`, proposal `ep_36d6f4b2-4790-4f7c-9170-0cb1335c4c0e`, records the stimulus, conditional claim, test, and report to marici.Voevodsky. Admission is policy review, not mathematical verification. The admitted-but-uncommitted interval for this investigation and its immediate affine predecessor is [15678,15679]. The new packet, checker and SCC manifest, plus the predecessor crosslink, remain uncommitted; generated results are local. No commit, push, or deployment was requested or performed.
