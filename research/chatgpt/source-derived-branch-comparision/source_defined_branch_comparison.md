# A source-defined polynomial conductor–road comparison

## Result, provenance, and exact scope

This note constructs a polynomial extension of Marici's explicitly supplied conductor–road endpoint coefficient complex and an exact comparison back to it. It does not assert that the complete filtered support-PC/endpoint-Q geometric functor has thereby been reconstructed.

The new comparison uses the source's normalization map, conductor difference, complete augmented road resolution, and physical road readout. It keeps all branch polynomials at chain level. Positive branch powers become boundaries because their corresponding node functions occur in the previous chain degree. No branch coefficient is silently deleted from the domain.

The comparison is a natural, integral, D3-equivariant quasi-isomorphism. Its kernel consists of two identical copies of the positive-branch ideal connected by the identity differential. It preserves the full base coefficient ring. In particular, a rank-one result over the base ring is not a reduction of that ring to the integers.

Source repository: `andrey-kokoev/marici`. All source inputs were read at commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`. Source files and exact blob hashes are recorded in the JSON certificate.

## 1. Which operation is selected by the source?

The source supplies two different uses of the same normalization–conductor sequence. They must not be confused.

Let R be one of the existing coefficient rings, and set

\[
A=R[x,y]/(xy),\qquad N=R[x]\oplus R[y],\qquad
\nu:A\longrightarrow N,\qquad
\delta(f,g)=f(0)-g(0).
\]

In words: A is the node ring, N consists of its two independent normalization branches, nu is restriction to those branches, and delta compares their conductor values. Each is defined over the entire coefficient ring R.

There is an exact sequence

\[
0\longrightarrow A\xrightarrow{\nu}N\xrightarrow{\delta}R_{\mathrm{or}}\longrightarrow0.
\]

In words: node functions are exactly the pairs with equal conductor value. Reflection swaps the branches and acts by minus one on the quotient.

The previously used conductor *kernel* complex has N in cohomological degree zero and R in degree one. Its cohomology is A. Consequently positive branch functions survive in that complex. The source's kernel checker explicitly retains that entire node kernel, including its polynomial modes.

Entry 142, by contrast, constructs the endpoint pullback using two *quotient resolutions*: the normalization-sheet quotient and the orientation-twisted road augmentation. It explicitly prescribes their homotopy pullback over the common endpoint-orientation line. It does not prescribe taking the conductor kernel and renaming its common unit as the endpoint unit.

The polynomial version of the first quotient resolution is

\[
E_R=[A\xrightarrow{\nu}N],\qquad E_R\longrightarrow R_{\mathrm{or}}.
\]

Here and below chain degrees are homological: A is in degree one and N in degree zero. In words: keep the node functions as relations on normalization-sheet functions. The augmentation is the source conductor difference, not a fitted scalar functional.

Geometrically, for the finite normalization map, this is the relative normalization cofiber. It is a complex of A-modules, hence also a quasi-coherent complex on the affine node. This is a genuine ringed construction on that node. Identifying that particular ringed construction with all of the source's support-PC and endpoint-Q operations is a separate question addressed in Section 9.

## 2. Why the polynomial relations are forced

The source's constant quotient resolution contains the diagonal relation

\[
1\longmapsto(1,1).
\]

In words: equal sheet constants represent a node function and are identified in the relative normalization quotient.

Once the sheet module is upgraded from two copies of R to the full N, the normalization map is A-linear. Thus

\[
\nu(a)=a\nu(1),\qquad
\nu(x^m)=(x^m,0),\qquad
\nu(y^m)=(0,y^m)\quad(m\ge1).
\]

In words: the same relation necessarily supplies every positive branch polynomial as a relation. These are not newly chosen counterterms or generators added merely to make a contraction work. They are already the elements of the source node ring under its canonical restriction map.

Keeping N but retaining only the old diagonal copy of R as relations would fail A-linearity: multiplying the diagonal by x produces the nonzero pair (x,0), while x acts by zero on a conductor-supported copy of R. Such a hybrid is a different, merely R-linear model and has extra positive-branch homology. It is not the source normalization quotient.

This argument selects the relative polynomial completion once the ringed normalization operation is selected. It does not claim that the earlier kernel complex is wrong; that complex performs a different operation and correctly retains A.

## 3. Retain the entire road resolution

Let r cyclically permute the three road coordinates, set M=1-r, and write

\[
M=\begin{pmatrix}1&0&-1\\-1&1&0\\0&-1&1\end{pmatrix},\qquad
n(c)=(c,c,c),\qquad \epsilon(q)=q_0+q_1+q_2.
\]

In words: M is the source triangle boundary, n is its norm map, and epsilon is the road augmentation. Both identities Mn=0 and epsilon M=0 hold integrally.

The polynomial endpoint comparison is the same mapping-fibre construction as in entry 142, with the normalization quotient resolved by its full node ring:

\[
\begin{aligned}
P_3&=R,\\
P_2&=A\oplus R^3,\\
P_1&=N\oplus R^3,\\
P_0&=R_{\mathrm{or}},
\end{aligned}
\qquad
\begin{aligned}
d_3(c)&=(0,n(c)),\\
d_2(a,t)&=(\nu(a),Mt),\\
d_1(s,q)&=\delta(s)-\epsilon(q).
\end{aligned}
\]

In words: retain both sheet and road resolutions and compare their endpoint quotients. The norm term and both normalization sheets are present. No equivariant section of a quotient has been chosen.

The equations d2 d3=0 and d1 d2=0 follow from the exact source sequences. With the above chain placements, this is the suspension of the homotopy fibre of the difference between the two augmented degree-zero quotient-resolution maps. The displayed four-term complex, not an unstated shift convention, fixes the normalization.

The physical coefficient readout is exactly the source road readout:

\[
\varphi(s,q)=\epsilon(q).
\]

In words: add the road coefficients. On cycles this agrees with the sheet difference, and it vanishes on every boundary. It is not the common conductor value of a node function.

The ring A acts naturally on A and N and through A/(x,y)=R on every road, top, and endpoint module. With these actions all differentials are A-linear.

## 4. The comparison to the supplied finite endpoint complex

Let C_R be the source's four-term integral complex tensored with R. It has modules of ranks 1,4,5,1 over R, with precisely the matrices in `check_physical_derived_pullback_after_transform.py`.

Define

\[
\begin{aligned}
p_3(c)&=c,\\
p_2(a,t)&=(a(0),t),\\
p_1((f,g),q)&=((f(0),g(0)),q),\\
p_0(c)&=c.
\end{aligned}
\]

In words: evaluate the node and normalization branches at their actual conductor, leaving the base coefficient ring and all road/endpoint terms unchanged.

Unlike a scalar coefficient extraction, these evaluations are the conductor maps already in the source. They form an A-linear chain map into C_R, where A acts on the target through its conductor quotient. On the constant sector they reproduce every source differential entry exactly.

Let

\[
J=xR[x]\oplus yR[y].
\]

In words: J is the conductor ideal, represented by the independent positive-degree parts of the two branches. It sits canonically both in A and in N. There is a degreewise exact sequence of complexes

\[
0\longrightarrow [J\xrightarrow{1}J]\longrightarrow P_R\xrightarrow{p}C_R\longrightarrow0,
\]

where the kernel is in homological degrees two and one. In words: every extra polynomial relation maps to the identical extra polynomial sheet term. This kernel is contractible as an A-complex. Therefore p is a quasi-isomorphism of A-complexes, not merely a numerical rank match.

For an explicit R-linear deformation retraction, let j include constants and define

\[
h_1((f,g),q)=(f-f(0),\ g-g(0))\in J\subset P_2,
\qquad h_i=0\quad(i\ne1).
\]

In words: lift the positive branch part into its actual node relation. Directly,

\[
dh+hd=1-jp,\qquad pj=1,\qquad h^2=0.
\]

In words: the polynomial comparison has explicit integral null-homotopies for its discarded relative modes.

The displayed ambient splitting j and homotopy h are R-linear, not A-linear. This is not hidden: multiplication of a constant sheet generator by x demonstrates the failure of A-linearity of h. The comparison p itself is A-linear, and its kernel's identity contraction is A-linear. Thus the derived A-module equivalence does not depend on falsely asserting an A-linear ambient splitting.

## 5. Exact classification of cycles

Write a normalization pair and its matching road coefficients as

\[
s=(a_0+xa(x),\ b_0+yb(y)),\qquad
q=(q_0,q_1,q_2),\qquad
k=q_0+q_1+q_2.
\]

In words: keep both branch constants, all positive branch terms, and the three road coefficients.

This is a physical endpoint-coefficient cycle exactly when

\[
a_0-b_0=k.
\]

In words: the sheet difference must match the road augmentation. Failure of this equation means the proposed data are not a closed state; they are still legal cochain inputs.

Let

\[
z=((1,0);(1,0,0)),\qquad
t=(0,q_1,q_1+q_2),\qquad
a_*=b_0+xa(x)+yb(y)\in A.
\]

In words: z is the source's primitive representative; t is an integral tag correction; a-star collects the common constant and branch tails as a node function. Then

\[
(s,q)-kz=d_2(a_*,t).
\]

In words: every cycle differs from exactly k times the primitive state by an explicitly supplied source boundary. No division by two, three, or a polynomial coordinate occurs.

The readout sends z to one and kills boundaries. The norm term resolves the entire kernel of M. The normalization map is injective. Consequently

\[
H_1(P_R)\cong R_{\mathrm{or}},\qquad H_i(P_R)=0\quad(i\ne1).
\]

In words: the only surviving local homology is one copy of the full base ring, with the source orientation character. The usual once-relative polarity twist makes its reflection character positive. Over the integral polynomial/localization rings in the source, this introduces no integer torsion.

The cases are now distinguished exactly:

| Input direction | Status in the endpoint comparison | Reason |
|---|---|---|
| Positive branch term (x^m a,0) or (0,y^m b) | Legal input; zero homology class | Image of the matching node term under d2 |
| Equal constants (c,c) with zero roads | Legal cycle; zero homology class | Image of the diagonal node constant |
| Sheet difference k with matching road sum k | Retained | Class k[z], detected by the source road readout |
| Road difference with sum zero | Legal cycle; zero homology class | Image of the complete triangle boundary M |
| Sheet difference not matching road sum | Not a physical cycle | Nonzero d1; it is not removed from the chain module |
| Negative powers of x or y | Outside this polynomial source module | No such branch localization is present |
| Coefficient-base poles not allowed at the given source stalk | Outside that stalk | Violates the source's occurrence/Rees localization rule |

No permitted positive-degree branch polynomial is excluded from the input simply for having positive degree.

## 6. The earlier conductor-normalized markings are not the physical unit

In the kernel complex Q, the pairs (1,1) and (1+x,1) are distinct cohomology classes. Both have common conductor value one. The present relative construction gives

\[
((1,1);0)=d_2(1,0),\qquad
((1+x,1);0)=d_2(1+x,0).
\]

In words: both are boundaries in the relative endpoint object. They do not become the primitive endpoint state. The primitive state requires a nonzero sheet difference together with the matching road class.

This is not a contradiction with the earlier computations. The operation has changed from a conductor kernel to a relative normalization quotient followed by the source road pullback. The canonical map from node functions into this relative object is null-homotopic, with the node term itself supplying the null-homotopy. It therefore cannot send the common conductor unit to the nonzero physical unit.

This prevents a false comparison between differently normalized marking problems.

## 7. Source transport and filtration compatibility

The source D3 action extends to arbitrary polynomial degrees without averaging. Rotation fixes the sheets and rotates roads and tags. Reflection swaps x and y on both A and N. On road coordinates it is minus the permutation fixing road zero and swapping roads one and two. On tags it is the permutation r-inverse times that road permutation. Reflection fixes the top term and negates the endpoint quotient.

Every differential, p, and the R-linear polynomial homotopy commutes with these actions. Thus the polynomial removal preserves the existing integral orientation extension; it does not choose a reflection-invariant sheet splitting or a rotation-invariant road representative. The original strict unit section obstruction remains: over the integers rotation would require 3c=1 and reflection would require 2a=1. The derived quotient itself requires neither fraction.

All maps are natural in R. Therefore they commute with the source's coefficient localizations and branch-preserving conductor-compatible ring maps. They act as the identity on occurrence and Rees parameters. They do not illegally evaluate an already inverted base parameter at zero.

For the branch-adic filtration, the positive filtration terms in degrees two and one are the same ideals with identity differential. Their contraction preserves this filtration. For filtrations on the coefficient ring R, all formulas are R-linear and preserve the induced coefficient filtration. Derived coefficient change and coefficient-only Koszul/Cartier constructions preserve the quasi-isomorphism.

These statements do not establish commutation with a still-unspecified geometric operation that mixes branch coordinates with Rees coordinates, changes admissible support, or changes variance. In particular the distinct raw chart relation u=Xt is not silently replaced by the independent split-node relation xy=0.

## 8. Assembly and the retained base-polynomial directions

For any of the existing diagrams of coefficient rings and conductor-compatible maps, the maps p form a natural transformation which is an objectwise equivalence in the derived category. Homotopy limits therefore give

\[
\operatorname*{holim}_{j}P_{R_j}\simeq
\operatorname*{holim}_{j}C_{R_j}.
\]

In words: after the stated relative operation, branch tails contribute no additional obstruction under that coefficient descent. No indexing contraction is being used to replace a nonconstant coefficient diagram by a constant one.

The rings R_j are still present. Their localization and derived-section information survives on both sides. A class whose coefficient is an occurrence polynomial remains such a class. Reducing this full retained coefficient to an integer or to a numerical period requires the actual prescribed additional readout. Neither p nor the generic interval trace supplies that reduction.

No new enumeration of the octagon's full geometric endpoint/PC diagram is claimed here. The assembly assertion is the functorial consequence for the coefficient diagrams to which these specified maps apply.

## 9. What is—and is not—physically identified

Completed here: a full polynomial, ringed, equivariant comparison to the exact conductor–road endpoint coefficient complex supplied by the source, with explicit witnesses for every branch-polynomial direction and the actual road readout.

Not completed here: a proof that this relative normalization operation is the complete physical filtered support-PC functor, including the generic Q leg, both endpoint connector cells, the geometric Cartier maps, and their variance-sensitive comparison squares.

The reason is concrete. The inspected `check_global_mixed_variance_transform.py` compares a transform signature to a dictionary copied from that same signature and invokes earlier checks. It does not define a chain map on arbitrary branch polynomials for those geometric operations. The local polynomial comparison in this note cannot convert that signature check into such a chain map.

The source's generic logarithmic Thom trace computes coefficient one on the relative interval generator and keeps the base ring. It defines no separate operation erasing branch polynomials. Thus the quotient established here is justified by the *relative normalization map*, not by an invented claim about the generic logarithmic trace.

Any promotion to the full physical category must identify its actual sheet-to-endpoint map with this relative normalization map while retaining the based generic leg and both endpoint connectors. The source-defined coefficient result is useful precisely because it specifies the required map on every polynomial, rather than merely matching its value on one primitive state.

## 10. Verification

Run:

```sh
python check_source_defined_branch_comparison.py --output source_defined_branch_comparison_certificate.json
```

The default run passes 2,966 exact assertions. It checks differential and comparison identities; the explicit branch contraction; the complete D3 action and covariance; A-linearity of the differential and comparison; the failure of the ambient splitting to be A-linear; source matrix equality; polynomial boundary witnesses through degree twelve; and explicit integral cycle normal forms for 875 integer choices.

Sparse symbols are not multiplied modulo a degree truncation. The bounded list selects test inputs only. The formulas and exact kernel argument prove the results for arbitrary polynomial degrees and every commutative coefficient ring. This is executable verification together with an algebraic proof, not proof-assistant certification. The source integration script was not executed, and no repository files were modified.

## Source record

- `src/ledger/20260815-142 Unsplit Conductor-Road Endpoint Pullback and the Spatial Realization Blocker.md`, blob `992943c89edb9d6ae39650bf5cbde4f0497233f8`: quotient resolutions, complete road complex, source orientation and readout, and the geometric scope limitation.
- `research/voevodsky/check_conductor_road_endpoint_pullback.rs`, blob `cfe13e928e911f8914de6670f34cc4c8859b3402`: exact D3 actions and integral matrices.
- `research/voevodsky/check_normalization_conductor_bimodule_kernel.py`, blob `2982163ca939dd1e09bb0b66b4229e31430e3c30`: full polynomial branches, conductor evaluations, and the retained node kernel for the different kernel operation.
- `research/voevodsky/check_physical_derived_pullback_after_transform.py`, blob `7993b2b1bbdba03d05c3f443a45717d7b8efeec5`: supplied four-term target and primitive road readout.
- `research/voevodsky/check_multirees_conductor_stalk_kernel.py`, blob `1237d71e8c9fd56e064226825049d84dd03f42e2`: occurrence/Rees admissibility and conductor evaluation/localization compatibility.
- `research/voevodsky/check_global_mixed_variance_transform.py`, blob `3b23d8a71a374435e8f54d4fe9451a08cb8ab98e`: the inspected signature-based integration test and its limitations.
- `research/voevodsky/check_generic_log_dnc_thom_trace.py`, blob `95fd466d144bafea6838cfeacc4aaf485b124275`: relative interval/logarithmic orientation computation, not a branch-polynomial scalar trace.
