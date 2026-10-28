# The four-plane arrangement is a tetrahedral–octahedral tiling

## Result and scope

For the **declared unbounded plane arrangement** in Strominger's lattice note, with d>0, the proposed affine map is correct: its full vertex set is an affine copy of the even-sum lattice, and its chambers and faces form the regular tetrahedral–octahedral tiling. This is a geometric identification, not merely recognition of two isolated shapes.

A second result is negative: **a two-coloring exists that splits every elementary tetrahedral and octahedral chamber**. Thus a Ramsey claim restricted to elementary cells at unit scale is false. The net's actual pilot permits positive integer dilations and is not refuted.

Verification level: written all-index proofs with exact rational/integer executable controls. No new proof-assistant theorem, native Marici attachment law, physical proton result or general Ramsey forcing bound is claimed. The ordinary geometric carrier is identified; the source's witnessing/attachment operations are not supplied by this calculation.

## 1. Normalize the source without changing its incidence

Let s0=(1,1,1), s1=(-1,-1,1), s2=(-1,1,-1), s3=(1,-1,-1). They sum to zero and satisfy

$$
s_i\cdot s_j=4\delta_{ij}-1.
$$

The source normals are n_i=s_i/sqrt(3), with planes n_i.x=d+4dh. For d>0 set u=x/(sqrt(3)d). The exact normalized equations are

$$
s_i\cdot u=1+4h,\qquad h\in\mathbb Z.
$$

Let p=(-1,1,1), b=(0,0,0,-1) and define

$$
u=p+2v,\qquad t_i=\frac{s_i\cdot v}{2}.
$$

Then the source plane index is h_i=b_i+t_i. In particular, the four plane equations become t_i integer, not four independent Euclidean coordinates. Always sum(t_i)=0. Conversely,

$$
v=(t_0+t_3,\ t_0+t_2,\ t_0+t_1).
$$

These maps are inverse linear coordinates between real three-space and the sum-zero hyperplane in real four-space.

## 2. Exactly all arrangement vertices

If v is an integer triple with even sum, each s_i.v is even. Thus t is integral, h is integral and sum(h_i)=-1: every such point lies on one plane from each family.

Conversely, choose arbitrary integer indices for any three distinct families. Their normals are independent. Since sum(s_i)=0, the fourth plane has the forced integer index

$$
h_{\mathrm{missing}}=-1-\sum_{\mathrm{selected}}h_i.
$$

Now t=h-b is integral with sum zero. The inverse above gives an integer v with coordinate sum 2t0, hence even. This proves both directions for every triple intersection, not only a finite vertex sample. In a full-rank three-dimensional hyperplane arrangement, vertices are intersections of at least three independent planes. Consequently these are exactly all vertices. The family labels and the offset of the fourth index are retained.

## 3. Every chamber is a tetrahedron or an octahedron

Away from the planes, write

$$
t_i=k_i+\lambda_i,\qquad k_i\in\mathbb Z,\quad0<\lambda_i<1.
$$

Because sum(t_i)=0, the integer q=-sum(k_i) is one of 1,2,3. The closure of that chamber is affinely represented by

$$
0\le\lambda_i\le1,\qquad\sum_i\lambda_i=q.
$$

Every such index tuple gives a nonempty chamber: lambda_i=q/4 is an interior point. Its vertices are exactly the binary four-tuples with q entries equal to one. Indeed, a nonbinary point has at least two fractional coordinates (their sum is integral) and can be perturbed oppositely in those coordinates, so is not extreme. Conversely each binary point is uniquely fixed by its active coordinate bounds, hence extreme.

There are therefore 4,6,4 vertices for q=1,2,3. Adjacent vertices exchange one selected index i for another j, giving

$$
\Delta v=\frac{s_i-s_j}{2},\qquad |\Delta v|^2=2.
$$

For q=1 and q=3 every vertex pair has this distance: the cells are regular tetrahedra. For q=2 each vertex has four neighbors at squared distance two and one opposite at squared distance four: the cell is a regular octahedron. Its eight facets come from lambda_i=0 or 1; tetrahedral chambers have four facets. Each facet is a triangle.

These are all chambers because every off-plane point has its unique floor tuple k. Closures cover the whole space and meet face-to-face by their inherited affine coordinate inequalities. On a lower facet lambda_i=0 the adjacent index is k-e_i; on an upper facet lambda_i=1 it is k+e_i. Whenever the boundary is a facet rather than a lower-dimensional face, the neighboring q remains in {1,2,3}. This supplies the shared triangular face with its retained plane label; affine inversion preserves all intersections, not just face counts.

The net's tetrahedron is the chamber k=(0,-1,-1,-1), q=3. Its octahedron is k=(0,-1,-1,0), q=2. Thus both initial templates are genuine elementary chambers of the declared arrangement.

For a nonzero even-sum integer displacement, squared length cannot be one: an integer unit-axis displacement has odd sum. The minimum is two, attained exactly by the twelve permutations of (plus-or-minus 1, plus-or-minus 1,0). These are the actual chamber-edge directions, not an assumed twelve-endpoint physical readout.

## 4. An exact obstruction to fixed-scale cell forcing

Color the entire lattice by

$$
c(v)=v_1\bmod2.
$$

At a chamber vertex,

$$
v_1=k_0+k_3+\lambda_0+\lambda_3.
$$

For q=1, lambda0+lambda3 takes both 0 and 1. For q=3 it takes both 1 and 2. For q=2 it takes 0,1,2. Each chamber therefore contains both colors, for **every** chamber index k. There is no monochromatic elementary tetrahedral or octahedral chamber anywhere in this coloring.

This disproves the stated fixed-scale variant globally, not merely at a small search radius. It does not disprove the dilation-allowing pilot: for any pattern, an even integer scale makes all first-coordinate parities equal to that of the translation.

## 5. Precise remaining operation gate: dilation requires subdivision

An integer translation in L and signed coordinate permutations preserve this plane arrangement and its elementary cells geometrically. Whether they are admitted native operations with the required histories remains a separate source question.

A positive integer dilation m>1 is different. Under y=a+mv, a plane t_i(v)=h maps to

$$
t_i(y)=t_i(a)+mh.
$$

It maps source planes into source planes, but misses intermediate plane levels. The image of an elementary edge contains m-1 intermediate lattice vertices; its interior is cut by intermediate planes. A dilated elementary cell is a union of smaller chambers, **not** another elementary chamber. A native Ramsey construction that allows dilation therefore needs a typed patch/subdivision construction or an equivalent larger-pattern operation. Calling dilation an elementary-cell automorphism would be incorrect.

Homogeneity in the current pilot concerns the **specified template vertices**, not every newly exposed subdivision vertex. For example, the doubled edge from 0 to (2,2,0) has same-colored endpoints under this parity coloring but an opposite-colored midpoint (1,1,0). A native patch realization must retain which vertices are being compared; silently demanding a monochromatic entire patch changes the problem.

This is the concrete next source-operation boundary. The geometric proof does not settle the parent `space-admission` node, whose statement also requires operation-preserving native identification. No universal-native no-go is inferred from the fixed-scale obstruction.

## Evidence

- Prospective scopes, source parameters and controls: `research/voevodsky/contracts/ramsey-plane-lattice-attempt.v1.json`.
- Checker: `research/voevodsky/checkers/check_ramsey_plane_lattice.py`.
- Receipt: `research/voevodsky/results/ramsey-plane-lattice-v1.json`.
- SCC model: `research/voevodsky/scc-models/ramsey-plane-lattice-v1.json`.
- Source inspected: `research/strominger/tetrahedral-plane-lattice-universal-witness-conjectures-v1.md`, specifically the four plane equations and d>0 convention. No other source theorem is imported.

Finite controls supplement the written all-index proofs. They do not independently prove the infinite tiling or its all-cell counterexample. Geometry and fixed-scale rejection share one evidence group and are not independent support for the governing Ramsey claim.
