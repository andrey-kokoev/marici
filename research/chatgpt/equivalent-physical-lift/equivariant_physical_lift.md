# Strict and homotopy-coherent lifts of the physical endpoint unit

Date: 2026-09-06

## Result

For the supplied conductor–road endpoint coefficient complex, with its actual dihedral transports and orientation character, the integral strict-unit obstruction has exact order six. Its reflection and rotation components have orders two and three. Nevertheless the full space of homotopy-coherent normalized states is contractible. Explicit integral witnesses use only the source's existing node, road-tag, and top norm generators.

The result distinguishes three conditions which must not be conflated: a strictly invariant cycle representative, an invariant homology class, and a coherent equivariant state. The first does not exist for the unit; the latter two do.

All numerical obstruction-group statements below are over the integral coefficient model, retaining its complete polynomial branches. The coherent formulas are integral and extend along compatible changes of the base coefficient ring. No reconstruction of the missing support-PC/generic-Q geometric comparison is asserted.

## 1. Fixed source and the actual lifting problem

The source is `andrey-kokoev/marici` at commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`. The source action and finite coefficient complex were re-read directly from `research/voevodsky/check_conductor_road_endpoint_pullback.rs`, blob `cfe13e928e911f8914de6670f34cc4c8859b3402`. The polynomial extension and its branch contraction are the previously constructed `source_defined_branch_comparison.md` and `check_source_defined_branch_comparison.py`, retrieved from the saved files and rechecked in this calculation.

Set

\[
G=\langle r,s\mid r^3=s^2=1,\ srs=r^{-1}\rangle,
\qquad \chi(r)=1,\quad\chi(s)=-1.
\]

In words: the group is the six-element triangle dihedral group, isomorphic to the symmetric group on three labels. It is not the sixteen-element octagon group used in the earlier boundary-index calculation. The character records reflection reversal.

For the polynomial coefficient model over the integers,

\[
A=\mathbb Z[x,y]/(xy),\qquad N=\mathbb Z[x]\oplus\mathbb Z[y],
\qquad \nu:A\longrightarrow N,
\qquad \delta(f,g)=f(0)-g(0).
\]

In words: node functions map to their two normalization branches; the conductor map takes the difference of their constant values.

The full endpoint complex, in homological degrees three through zero, is

\[
P_3=\mathbb Z,\qquad P_2=A\oplus\mathbb Z^3,
\qquad P_1=N\oplus\mathbb Z^3,\qquad P_0=\mathbb Z_\chi,
\]
\[
d_3(c)=(0,(c,c,c)),\qquad
 d_2(a,t)=(\nu(a),(1-r)t),\qquad
 d_1(f,g,q)=f(0)-g(0)-\sum_{j=0}^2q_j.
\]

In words: retain the complete node, sheet, road, tag, norm, and endpoint terms. The physical readout on cycles is the road sum.

The original action fixes the sheets under rotation and rotates roads and tags. Reflection swaps the branches, acts by minus the road permutation fixing road zero and swapping roads one and two, acts on tags by the permutation sending index j to minus j minus one, fixes the top norm generator, and negates the endpoint line. Thus the original physical readout is reflection-odd.

To compare a state with the same oriented unit after transport, use

\[
g\star v=\chi(g)\,g(v).
\]

In words: tensor the entire complex with the source's once-relative polarity character. Equivalently, seek an equivariant lift from the original orientation line rather than a lift from a falsely trivial line. This is the orientation compensation already specified by the source, not an alteration of its symmetry.

The fixed endpoint conditions are

\[
f(0)-g(0)=q_0+q_1+q_2=1.
\]

In words: both endpoint quotient readouts equal the physical unit. Individual sheet constants and individual road representatives are not fixed separately. Fixing those coordinates would be a stronger and different framing requirement.

Reindex the marking complex as

\[
K_0=\ker(d_1:P_1\to P_0),\qquad K_1=P_2,\qquad K_2=P_3,
\qquad \varphi:K\to\mathbb Z[0].
\]

In words: cycles are degree-zero markings; the supplied node and tag terms give paths; the supplied norm term gives paths between paths. The differential in each positive degree is the corresponding displayed source differential. The readout is the road sum in degree zero and zero in other degrees. All actions are the compensated actions.

Use Dold–Kan [M1] to define the normalized marking space

\[
X=\operatorname{fib}_1\bigl(\operatorname{DK}(K)\longrightarrow\mathbb Z_{\mathrm{disc}}\bigr).
\]

In words: retain exactly the unit markings and all their source-supplied comparisons. The map is a fibration of the displayed simplicial abelian models, so this strict fibre represents its homotopy fibre. Literal fixed points refer to this specified model, whereas homotopy fixed points allow coherent transport.

## 2. The strict obstruction has exact order six

Let a strictly compensated-invariant cycle have sheet constants a and b. Reflection forces b equal to minus a. Rotation forces the three roads to have one common coefficient c. The cycle and readout equations become

\[
b=-a,\qquad q=(c,c,c),\qquad 2a=3c=m.
\]

In words: the strictly invariant readout must be simultaneously twice a sheet coefficient and three times a road coefficient. Over the integers its possible values are precisely multiples of six.

Positive branch tails cannot change these constant-term equations. Consequently

\[
\varphi\bigl(K_0^G\bigr)=6\mathbb Z,
\qquad X^{G,\mathrm{strict}}=\varnothing.
\]

In words: no strictly invariant unit marking exists in the complete polynomial model.

The lower bound is sharp. A strictly invariant cycle of readout six is

\[
z_6=((3,-3);(2,2,2)).
\]

In words: its sheet difference and road sum are both six, and every compensated transport fixes it exactly. Over a ring where two and three are invertible, division by six gives the familiar strict representative with sheet constants one half and minus one half and road coefficients one third. No such division is used below.

### The exact obstruction group, not merely inconsistent equations

Let

\[
L=\operatorname{im}(d_2)=\ker(\varphi:K_0\to\mathbb Z),
\qquad z=((1,0);(1,0,0)).
\]

In words: L is the zero-readout boundary module, and z is the supplied primitive physical cycle. There is an exact sequence of compensated G-modules

\[
0\longrightarrow L\longrightarrow K_0\xrightarrow{\varphi}\mathbb Z\longrightarrow0.
\]

In words: the obstruction to lifting the invariant unit to a strict invariant representative is the connecting class for this sequence. Group cohomology is used here as the derived functor of invariants [M2]. A representative is

\[
c(g)=g\star z-z,\qquad e=[c]\in H^1(G,L).
\]

In words: measure the failure of the chosen representative to be literally invariant; changing the representative by a boundary changes this cocycle by a coboundary.

The constant part of L has basis consisting of the sheet diagonal and the two road differences. Its module structure is

\[
L_{\mathrm{const}}\cong\mathbb Z_\chi\oplus I,
\qquad I=\ker(\mathbb Z^3\xrightarrow{\epsilon}\mathbb Z).
\]

In words: the sheet diagonal carries the sign character after compensation, while the road differences carry the ordinary permutation action restricted to their sum-zero lattice.

In the basis of the two road differences, the rotation and reflection matrices are

\[
R_I=\begin{pmatrix}0&-1\\1&-1\end{pmatrix},
\qquad S_I=\begin{pmatrix}1&0\\1&-1\end{pmatrix}.
\]

In words: these are read directly from the source road action, not fitted to the desired torsion.

A one-cocycle is determined by its values at the two generators. The group relations force, in the basis of the sheet diagonal followed by these road differences,

\[
c(r)=(0,u,v),\qquad c(s)=(\alpha,0,v).
\]

In words: the space of integral cocycles is a free group on three parameters. The relation r-cubed equals one forces the rotation component on the sign line to vanish. The reflection-square and mixed relations force the indicated road coordinates. These implications use exact integer equations, not a field-rank argument.

Coboundaries in these coordinates are the columns of

\[
D=\begin{pmatrix}-2&0&0\\0&-1&-1\\0&1&-2\end{pmatrix}.
\]

In words: the sheet factor gives multiplication by minus two, and the road factor gives rotation minus identity on its integral difference lattice. The Smith factors are one, one, and six. For the primitive state the cocycle has coordinates

\[
(\alpha,u,v)=(-1,-1,0).
\]

In words: it generates both the order-two sheet component and the order-three road component. Indeed, solving D times a vector equal to n times these coordinates gives

\[
\left(\frac n2,\frac{2n}3,\frac n3\right).
\]

In words: the multiple is an integral coboundary exactly when n is divisible by six.

Every positive polynomial degree contributes a branch pair on which rotation is trivial and reflection is negative swap. An integral cocycle on that pair vanishes on rotation and has equal components on reflection; every such pair is a coboundary. Therefore these polynomial modes add no first cohomology, and

\[
H^1(G,L)\cong\mathbb Z/2\oplus\mathbb Z/3,
\qquad \operatorname{ord}(e)=6.
\]

In words: this is the full strict-unit obstruction for the integral polynomial endpoint model. It is an equivariant lifting class, not ordinary torsion in the homology of the endpoint complex.

## 3. A complete integral coherent lift

Denote by a the node unit in P2, by t-j the three source tag generators, and by u the source top norm generator in P3. Thus d2(a) is the sheet diagonal, d2(t-j) is road j minus road j plus one, and d3(u) is the sum of the three tags.

Write group elements uniquely as g equal to r to the i times s to the e, with i in zero, one, two and e in zero, one. Define

\[
h_{r^i s^e}=-e\,a-\sum_{j=0}^{i-1}t_j.
\]

In words: use a node homotopy for a reflection and the oriented initial road-tag path for a rotation. The empty sum is zero. Direct computation gives

\[
d_2h_g=g\star z-z.
\]

In words: every allowed transport of the normalized state has an integral comparison back to that state, preserving both endpoint quotient values.

For g equal to r to the i times s to the e and h equal to r to the j times s to the f, set

\[
k_{g,h}=-\left\lfloor\frac{i+(-1)^e j}{3}\right\rfloor u.
\]

In words: when composing rotation indices, the wrap around the triangle is recorded by the existing top norm cell. Its coefficient is an integer, with possible values minus one, zero, and one.

These satisfy all composition equations

\[
d_3k_{g,h}=g\star h_h-h_{gh}+h_g,
\]

and all triple-coherence equations

\[
g\star k_{h,\ell}-k_{gh,\ell}+k_{g,h\ell}-k_{g,h}=0.
\]

In words: each discrepancy between two composed homotopies has its supplied two-dimensional filler, and the four faces of each comparison tetrahedron agree. The checker verifies all six edge equations, all thirty-six pair equations, and all 216 triple equations, including the mixed reflection–rotation cases and degenerate identities.

These data define a chain map from the full group bar resolution into K. Degree-zero generators map to z, degree-one bar generators to h, degree-two generators to k, and every generator in degree three or higher maps to zero. The degree-three chain equation is exactly the displayed triple-coherence identity; every higher chain equation is then identically zero. Thus this is an all-level coherent lift, not an extrapolation from a few checked simplices.

### What resolves each prime?

For reflection,

\[
h_s=-a,\qquad s\star h_s+h_s=0.
\]

In words: the existing node relation supplies the required homotopy, and its reflection-square comparison closes without a further correction. The order-two defect of choosing a strict sheet representative is not an obstruction to this coherent sheet state.

For rotation,

\[
h_r=-t_0,\qquad
h_r+r\star h_r+r^2\star h_r=d_3(-u).
\]

In words: the three transported homotopies accumulate to the negative tag norm. The existing top cell supplies its filler. No third is taken of any integral coefficient.

## 4. Existence and uniqueness of the coherent state

An explicit contraction proves the readout K to the integers is a quasi-isomorphism. For a cycle v, write its sheet constants as a-zero and b-zero, its positive branch tails explicitly, its road sum as m, and its road coordinates as q-zero, q-one, q-two. Put

\[
H_0(v)=\bigl(b_0+xf(x)+yg(y),\ (0,q_1,q_1+q_2)\bigr),
\qquad H_1(a,t)=t_0u.
\]

In words: lift common sheet constants and branch tails into the existing node relation, then use two tags to remove the road difference. At the next degree extract the first tag coefficient into the top norm generator.

The identities are

\[
d_2H_0(v)=v-\varphi(v)z,\qquad
 d_3H_1(w)+H_0d_2(w)=w,\qquad
 H_1d_3=1.
\]

In words: every marking reduces to its readout, all relations among the reductions are resolved, and no higher ambiguity survives. These identities hold integrally on arbitrary polynomials. The contraction itself need not be strictly G-equivariant; the readout is G-equivariant and is an equivalence in the derived category of G-modules.

Consequently

\[
K\xrightarrow{\simeq}\mathbb Z
\quad\text{in }D_\infty(\mathbb Z[G]),
\qquad X^{hG}\simeq *.
\]

In words: the full space of normalized homotopy-coherent equivariant states is contractible. There is one component and no nontrivial higher ambiguity. This follows from applying the derived mapping-space functor to the readout equivalence, or from taking homotopy fixed points of its contractible normalized fibre. The explicit bar map above supplies a particular coherent representative.

This is not a strict G-equivariant chain splitting from the unreplaced one-term complex. The bar resolution is essential: using it retains rather than deletes the homotopies that resolve the strict obstruction.

## 5. Controlled failures explain the source terms

These are diagnostic changes to the model, not changes made in the construction.

**Remove the node relations.** Reflection changes the sheet constants by a nonzero diagonal of odd coefficient for any unit state. Tags have no sheet component and cannot supply that boundary. The reflection cannot even be compared within the required component. The order-two defect becomes a genuine obstruction under this stronger restriction.

**Keep node and tags but remove the top norm cell.** The normalized marking space acquires a first homotopy group generated by the tag norm. The pair discrepancy is measured by the integer coefficient of k above. It is a two-cocycle with values in the sign module. Its class has exact order three.

To see the order directly, let b(r to the i times s to the e) equal minus i. Then

\[
\delta_G b=3k,
\]

where this equation identifies k with its integer coefficient. In words: three copies of the carry cocycle are a coboundary. Its restriction to the rotation subgroup obeys

\[
\sum_{i=0}^2 k_{r^i,r}=-1.
\]

In words: the cyclic carry is not divisible by three. The same sum for any cyclic coboundary is three times its value at r, so this class cannot itself be a coboundary. Changing the chosen edge homotopies adds a one-cochain of tag norms and changes k only by a coboundary. Therefore no alternate edge choices remove this obstruction when the top norm cell is absent. This agrees with the cyclic cohomology calculation [M3].

**Retain the complete source.** The tag norm is the boundary of u, exactly as supplied by the source. The obstruction disappears as a failure of coherent lifting, but its order-three class still diagnoses the invalid truncation. The strict order-six extension class remains nonzero; existence of a coherent lift does not turn it into a strict splitting.

## 6. Polynomial coefficients, admissibility, and scope

Every displayed coherent witness uses constant node, tag, and norm generators already present in P. No branch polynomial is excluded, no new pole is allowed, and no coefficient coordinate is inverted or averaged. Each first homotopy leaves both endpoint quotient readouts unchanged because the conductor difference of a node function and the augmentation of a tag boundary vanish separately. Each second homotopy is the existing norm relation.

The branch contraction is compatible with the source G action, conductor maps, and coefficient-localization maps. Arbitrary branch tails therefore do not change this coherent lifting result. The integral formulas for z, h, and k extend to every compatible coefficient ring and also to reductions modulo two or three. Strict representative obstructions persist there: the equations requiring two or three times a coefficient to equal one remain impossible in the corresponding characteristic.

For a coefficient ring with trivial G action, a strict unit exists exactly when two and three are both units. The exact order-six statement above is the integral case. If G also acts nontrivially on base coefficients, the complete strict obstruction group must be recomputed with that action; the integral coherent witnesses remain valid under compatible semilinear transport.

The explicit element and ambient contraction formulas are R-linear, not an assertion of a strictly A-linear ambient splitting. The earlier comparison to the finite complex is A-linear with an A-contractible kernel; a derived A-linear statement may be obtained through that equivalence with the appropriate module resolutions. The displayed finite bar calculation addresses the coefficient-marking problem, not an unprovided strict ringed frame.

No conclusion is asserted about further support conditions, independently prescribed representative-level endpoint values, the based generic Q leg, or mixed branch–Rees/Cartier operations whose maps have not yet been defined. Such restrictions could exclude one of the actual witnesses; that would be a different lifting problem and would require its own obstruction calculation. For the supplied endpoint-coefficient source and its stated transports, neither prime prevents the coherent state.

## 7. Reproduction and verification

Run:

```sh
python check_equivariant_physical_lift.py --output equivariant_physical_lift_certificate.json
```

The standalone standard-library script passes **6,643 exact assertions** at its default degree sample of twelve. It checks the source matrices, full compensated group action, endpoint readout, polynomial contraction, normalized marking contraction, all edge/pair/triple bar identities, the actual cocycle parametrization and coboundary lattice, integral Smith factors, exact orders of both obstruction classes, and finite-ring controls for moduli two through thirty.

Polynomial degrees are untruncated sparse symbols. The finite inputs test the formulas; the contraction and direct-sum arguments prove the arbitrary-degree statement. The group is finite and all pair and triple combinations are exhausted. The vanishing of the remaining bar-map components proves the all-higher-degree coherence statement. This is not proof-assistant certification.

The earlier branch-comparison script was separately rerun and reproduced its 2,966 exact assertions. No repository file was modified.

## References

[M1] Stacks Project, *Dold–Kan*, Section 14.24, tag 019D: https://stacks.math.columbia.edu/tag/019D

[M2] Stacks Project, *Group cohomology*, Section 59.57, tag 0A2H: https://stacks.math.columbia.edu/tag/0A2H

[M3] Kiran Kedlaya, *Notes on class field theory*, Section 3.4, *Cohomology of cyclic groups*: https://kskedlaya.org/cft/sec_cohom-cyclic.html

[M4] Stacks Project, *Hom complexes*, Section 15.73, tag 0A8H: https://stacks.math.columbia.edu/tag/0A8H

Source definitions and limitations: the pinned Rust endpoint checker specified in Section 1, and the retrieved `source_defined_branch_comparison.md` Sections 3–7 and 9. Exact source blob hashes are retained in the new executable and certificate.
