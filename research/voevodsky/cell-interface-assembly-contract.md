# A finite linear interface theory for cell assembly

Status: proposed contract with exact finite tests; not a derived physical assembly law.

Follow-up: `pentachoron-geometric-spin-interfaces.md` now derives the intrinsic face projectors and fold transports. Exact matching has zero global states; a separately declared squared-mismatch functional has a four-dimensional lowest space. The flat rank-two extension below is not the intrinsic geometric connection. In particular, its flat-cocycle requirement must not be confused with a general requirement of zero connection curvature.

## Question and result

Can one define assembly so that the proposed electron pentachoron extends the checked tetrahedral spinor rather than merely displaying it inside a larger shape?

We now have an explicit linear contract, a conditional five-cell extension, and two useful failure controls. A rank-two extension exists with **supplied full-spinor interfaces and flat transport**. Neither that interface capacity nor those transports follow from the retained single-face data. Matching the old rank-one face vectors under a naive common-coordinate convention instead gives zero global states.

The precise frontier is therefore the derivation of the triangle restriction maps and their overlap comparisons. The existence of an abstract rank-two extension does not establish that derivation.

## 1. Typed local data

For each cell c, supply:

- a finite-dimensional complex Hilbert space H_c of raw records;
- an orthogonal return N_c on H_c;
- its retained state space E_c = im(N_c);
- for every incident interface f, a port space F_f and a restriction R_cf: E_c -> F_f (or separate port charts with an explicit comparison).

For a shared face f of cells c and d, supply the comparison T_cd,f. If separate port charts are used, this has type F_cf -> F_df. Compatibility is

    R_df x_d = T_cd,f R_cf x_c.

Collect these equations into a linear map D from the direct sum of the E_c to the direct sum of interface equation spaces. Define

    E_assembled = ker(D).

The return on the declared direct-sum Hilbert space is the orthogonal projector onto this kernel. If the columns of K form any basis of the kernel, it is

    N_assembled = K (K* K)^(-1) K*.

The kernel is algebraic; this projector additionally depends on the declared metric. Thus the metric is part of the contract, not a normalization chosen afterward.

This is a common operation that allows different types of local records. It is not yet a proof that the existing proton and belt protocols arise from the same supplied local-interface data.

## 2. What order independence does and does not mean

Imposing all the equations at once, or intersecting their solution spaces in any order, gives the same kernel. One must retain the remaining constraints when assembling intermediate blocks. Discarding them is not assembly of the same diagram.

This does NOT imply that multiplying local orthogonal projections in arbitrary order gives the global projector. Constraint projections need not commute.

For a genuinely stratified geometric theory, also assign data to edges and vertices and specify restrictions face -> edge -> vertex. Require commuting restriction diagrams, or explicitly supplied coherent comparison maps. Pairwise cell-face equations alone do not provide those maps.

An invertible full-state transport model is a special case. On a triple overlap require

    U_bc U_ab = U_ac.

For the five facets of a 4-simplex:

- pairwise intersections are ten triangular faces;
- triple intersections are ten edges;
- quadruple intersections are five vertices;
- the intersection of all five facets is empty.

Thus the triangle cycles of the dual K5 graph correspond to physical triple-overlap edges, not to another set of physical triangular faces. Exact cocycles on those cycles imply consistency of all longer transport paths and of quadruple comparisons. A full-state constant local system supplies lower-stratum data, but this is additional interface content, not the inherited rank-one face encoding.

## 3. Retained electron cell and its actual face ports

The checked tetrahedral electron cell has H = C^8 and E isomorphic to C^2. For its four outward unit normals n_i,

    P_i = (I - n_i . sigma)/2,
    J z = (P_0 z, ..., P_3 z)/sqrt(2),
    J*J = I_2,
    N = J J*.

The inherited single-face restriction is R_i(Jz) = P_i z/sqrt(2). Its image is a complex line and its kernel on E has dimension one. Therefore a single old face record cannot transmit or recover the full logical doublet by an invertible adapter.

For distinct tetrahedral faces, tr(P_i P_j) = 1/3. Their image lines are distinct, and any two restrictions jointly determine z. Full-cell decoding J* also recovers z. Neither operation is a function of one face record alone.

A rank-one face interface is not thereby ruled out: a network of such constraints can collectively retain a doublet. It must actually be constructed and checked. The rank obstruction only forbids treating a single face restriction as a reversible two-component port.

## 4. Conditional full-spinor assembly

Supply five copies of the old cell and put a full C^2 port on every shared triangle. Use full-cell decoding as the port map and initially declare all logical transports to be identity:

    z_d = z_c.

The ten interface equations have complex rank eight on ten logical coordinates. The global states are

    (z,z,z,z,z),  z in C^2.

All 125 spanning trees of K5 recover the same compatible states; the remaining edges are consistent redundant constraints. The orthogonal logical return has every 2-by-2 block equal to I_2/5.

This result is independent of the regular edge lengths and of the 3D projection. It is the general result for a connected flat rank-two local system, not evidence selecting the electron or the pentachoron.

For arbitrary supplied unitary transports, choose a spanning tree. Every other edge supplies a loop holonomy on one root C^2. The global state space is isomorphic to the common fixed subspace of those holonomies. Hence its dimension can be two, one, or zero.

Exact controls:

- Identity transport everywhere: dimension two.
- Change one non-tree seam to diag(1,-1): dimension one.
- Change that seam to -I: dimension zero.
- Use -I on every seam: dimension zero because K5 has odd cycles.
- Use pure changes of local frame U_cd = G_d G_c*: dimension two, with every triple cocycle satisfied.

All these transports are pairwise unitary. The central -I defect even commutes with every common spin rotation. Pairwise reversibility and rotation covariance therefore do not establish global compatibility. The twisted cases are rejected by the flat-cocycle contract, rather than being rival flat assemblies.

## 5. A failed inherited-face attempt

As a deliberately naive convention, order each cell's four neighbours, assign the four retained projectors in that order, and identify the resulting face vectors in one ambient C^2 without a line adapter:

    P_(c,d) z_c = P_(d,c) z_d.

The exact assembled constraint matrix has rank ten, so its kernel is zero.

This is a failure of that explicit convention, not a no-go theorem for rank-one ports or for geometric spinor assembly. Sorting labels does not derive intrinsic frames on a regular 4-simplex. The example shows why drawing equal face labels and copying the old four-face formula into every cell is not enough.

## 6. Recovery must include normalization and actual operators

For the conditional identity-transport extension, let

    K z = (Jz, Jz, Jz, Jz, Jz)/sqrt(5).

Then K* K = I_2. On the forty raw complex coordinates the assembled return has blocks

    (N_global)_cd = N_local/5.

Coordinate restriction to ABCD sends Kz to Jz/sqrt(5), not Jz. In particular, compression of N_global to ABCD is N_local/5, not N_local.

On the compatible global subspace, scaled restriction sqrt(5) times the ABCD coordinate projection is an isometric recovery of the old cell, with an explicit inverse. That scaling comes from the direct-sum norm. It must not be advertised as literal unchanged coordinate restriction or as a new physical amplitude law.

This constructs only a conditional global return. It does not construct the global L/G/N transfer protocol, establish support minimality, or promote the old 144-transfer count to the five-cell system.

## 7. Acceptance tests for the next source-derived candidate

The next candidate must provide:

1. Intrinsic spin frames for the five regular tetrahedral facets in four dimensions, with the orientation convention and any Spin(4)/chirality choice explicit.
2. Triangle port spaces and maps derived from those frames, not from sorted labels or a desired final rank.
3. Edge and vertex restrictions, or a justified equivalent transport model, with all overlap comparisons checked.
4. The actual global compatibility kernel and return. Rank two is a result to test, not an imposed selection.
5. An explicit recovery comparison with ABCD, including its metric factor and whether its original four-face readout survives.
6. The induced symmetry action. A retained spinorial sign is necessary but does not supply electromagnetic charge, exchange statistics, or mass.
7. If a new transfer protocol is claimed, its operators, supports, adapters and costs separately from the geometric gluing equations.

Only after this should the proton-electron and belt-electron seams be claimed to implement the same rule. Their different carriers cannot be identified merely because both have a triangular attachment face.

## Reproduction

    python research/voevodsky/checkers/check_cell_interface_assembly.py

Nine exact test groups pass using the existing dependency-free arithmetic for Q(sqrt(3), i), including all 125 spanning trees, order and orientation controls, holonomy mutations, the failed naive rank-one matching, and the local/global return comparison.

Result: `research/voevodsky/results/cell_interface_assembly.json`.

Prior source: `electron-charge-spin-frontier.md` and `checkers/check_electron_tetrahedral_spinor.py`. Geometry-only scope: `electron-pentachoron-attachment.md`.
