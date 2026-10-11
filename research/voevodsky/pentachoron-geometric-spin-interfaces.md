# Geometric pentachoron spin interfaces: zero parallel states, four lowest mismatch modes

Status: exact finite geometric calculation; no physical electron identification.

Constructive successor: `pentachoron-cycle-spin-energy-transport.md` transports
this rank-four lowest space under the actual source five-cycle. An explicitly
added cycle-defect term selects a doublet using the prior uniform energy rule;
the selection depends on the spin lift. The exact-matching obstructions here
remain unchanged.

## Result

The missing interface calculation can now be performed without assigning projectors by sorted labels or fitting the desired global rank.

For both four-dimensional chiralities:

1. The oriented triangles of every regular tetrahedral facet generate the old tetrahedral Pauli tight frame. The retained ABCD frame is recovered exactly.
2. Opposite incident orientations make the two negative-polarization projectors on a shared triangle complementary.
3. The minimal geometric fold between neighbouring facets preserves the shared triangle and commutes with its chiral projector. It therefore does not map one negative-polarization line to the other.
4. Equating the inherited face records gives zero global states, with either ambient identity transport or the geometric fold transport.
5. Replacing a face port by a full spinor does not recover the earlier flat extension: the geometric connection has loop holonomy with no fixed spinor, so piecewise constant parallel matching again gives zero states.
6. A different, explicitly supplied rule—minimize the equally weighted squared full-spinor seam mismatch—has an exact **four-dimensional lowest eigenspace**, not a doublet.

The previous flat rank-two extension remains a valid abstract construction. Its transports are not the intrinsic facet-fold transports derived here.

## 1. Geometry and orientation

Use the existing regular simplex vertices

    A=(1,1,1,0), B=(1,-1,-1,0),
    C=(-1,1,-1,0), D=(-1,-1,1,0),
    E=(0,0,0,sqrt(5)).

All ten squared edge lengths are eight. Its centroid is o=(0,0,0,sqrt(5)/5). Index facets by their omitted vertex c. Their outward unit four-normals are

    nu_c = -(sqrt(5)/4)(v_c-o),
    nu_c . nu_d = -1/4   for c != d.

The coordinate determinant of [B-A,C-A,D-A,E-A] is -16 sqrt(5). Accordingly the positively oriented simplex is -[ABCDE]. Use its induced oriented facet boundaries to orient each triangle. If b_cd is the full wedge of two triangle edge vectors in the orientation induced by facet c, then

    b_dc = -b_cd.

The wedges are not area-halved. Their norm is 4 sqrt(3).

## 2. Chiral face directions and actual inherited restrictions

For a bivector b in coordinates (x,y,z,w), define

    s_plus(b)  = (b_yz+b_xw, b_zx+b_yw, b_xy+b_zw),
    s_minus(b) = (b_yz-b_xw, b_zx-b_yw, b_xy-b_zw).

These are the two chiral three-component bivector coordinates in the convention used by the checker. Set

    n_cd = s_chirality(b_cd)/(4 sqrt(3)),
    P_cd = (I - n_cd . sigma)/2.

For each facet c, the four n_cd have unit length, pairwise dot product -1/3 and sum zero. Consequently

    sum_d P_cd = 2I,
    J_c z = (P_cd z)_d/sqrt(2)

is exactly the old isometric tetrahedral encoding in its intrinsic frame. No extra fifth-face operator is inserted. On ABCD, in face order ABC, ABD, ACD, BCD, the normals are exactly

    (1,1,-1), (1,-1,1), (-1,1,1), (-1,-1,-1),

all divided by sqrt(3), for either chirality. Thus this calculation recovers the retained source conventions, rather than merely matching its rank.

The shared-face identity is

    n_dc = -n_cd,
    P_dc = I-P_cd.

A negative-polarization line on one incident cell is the positive-polarization line in the other cell's oppositely induced orientation.

## 3. The geometric fold and its spin lift

Let R_cd be the minimal rotation in the plane spanned by nu_c and nu_d that sends nu_c to nu_d and fixes the orthogonal plane. The common triangle's tangent plane is precisely that fixed plane.

Writing theta=arccos(-1/4), put

    a = cos(theta/2) = sqrt(6)/4,
    k_cd = s_chirality(nu_c wedge nu_d)/(2a),
    U_cd = a I - i k_cd . sigma.

The sign convention is checked rather than assumed: the program verifies for all ten folds and all six bivector generators that

    U_cd [s(b).sigma] U_cd* = s(R_cd b).sigma.

It also verifies U_cd* U_cd=I, R_cd nu_c=nu_d, and that R_cd fixes the actual shared triangle edge vectors. Reverse transports are U_dc=U_cd*.

Since the fold fixes b_cd, U_cd commutes with P_cd. Consequently it cannot convert im(P_cd) to its orthogonal complement im(P_dc).

This derivation uses intrinsic boundary folding. It is distinct from comparing every cell through an ambient constant spin frame with identity transport.

## 4. Exact inherited-face matching fails

Consider the actual inherited restrictions and the geometric comparison:

    P_dc z_d = U_cd P_cd z_c.

The left side lies in im(P_dc), while the right side lies in im(P_cd). The two lines are orthogonal; both sides must vanish. Each cell has four such zero restrictions, while any two distinct tetrahedral projectors jointly have rank two. Hence every z_c vanishes.

The exact constraint matrix has complex rank ten on ten logical coordinates. Replacing U_cd by identity leaves the same obstruction. Changing the sign of a spin lift does not affect this orthogonality argument.

Whole-cell polarity reversals do not repair it. Making every seam join equal selected lines would require opposite cell polarities on every edge of K5, which is not bipartite. More strongly, every one of the 32 polarity assignments has a monochromatic triple. Each of those three cells gets two independent zero restrictions, and vanishes; its neighbours then also get at least two zero restrictions and vanish.

This is a no-go for this specified linear rule, not for all rank-one interfaces. An additional line-flipping operation, chirality-changing comparison, or different coupling would be new data that must be justified.

## 5. Full spinor ports still do not make the geometric connection flat

Even if we explicitly enlarge every face port to C^2 and impose

    z_d = U_cd z_c,

the global kernel is zero.

Already the loop through facets 0,1,2 gives

    H = U_20 U_12 U_01,
    tr(H) = 2 sqrt(6)/9.

H is unitary with determinant one. Its trace is neither 2 nor -2; neither H nor -H has a fixed spinor. Choices of signs for the individual spin lifts can only change this loop to +/-H, so they cannot restore a parallel doublet. Direct rank calculation confirms zero global dimension for the declared lifts.

This is curvature, not inconsistent spin geometry. Parallel transport around a loop is not the same datum as a change of bundle chart at one point. Chart transition cocycles must agree, but connection holonomy need not be identity. The flat full-state model in the previous contract was a special additional hypothesis, not a universal requirement for curved geometric assembly.

Nor does absence of a piecewise constant parallel spinor mean that the boundary has no spinor fields. Fields varying within cells, differential operators, and non-parallel couplings were not included in these ten logical coordinates.

## 6. A constructive alternative: least mismatch, not zero mismatch

As a separately declared assembly functional, retain the same full-spinor transports and use

    E(z) = sum_(c<d) ||z_d-U_cd z_c||^2.

This uses equal edge weights and the existing direct-sum metric. The regular simplex symmetry supports equal weights, but the choice to minimize this quadratic functional instead of imposing exact equality is additional modelling input. No mass or energy scale is assigned.

Let D be this full-spinor mismatch matrix and L=D*D on C^10. The exact spectrum is

| Eigenvalue | Complex multiplicity |
|---|---:|
| 4 - sqrt(6) | 4 |
| 4 + 2 sqrt(6)/3 | 6 |

Let kappa=sqrt(6)/3. The lowest-space orthogonal projector is

    Q = ((4+2 kappa)I - L)/(5 kappa).

The checker verifies Q*=Q, Q^2=Q, tr(Q)=4, LQ=(4-sqrt(6))Q, and the complementary eigenvalue identity. This is an exact two-level spectral decomposition, not a numerical rank threshold. Both chiralities give the same eigenvalues and multiplicities.

The ambient-constant configurations (z,z,z,z,z) form a two-dimensional subspace of this lowest space, but the declared mismatch energy does not separate them from the other two lowest modes. Keeping only that doublet would require another selection rule.

Each cell's diagonal block of Q is 2I/5. Restriction of the four-dimensional lowest space to one cell has rank two and a two-dimensional kernel. Thus, unlike the earlier flat two-dimensional extension, one cell cannot faithfully recover the whole assembled lowest space through any scalar normalization.

Four complex components by themselves do not establish a Dirac electron, particle/antiparticle pairing, charge, exchange statistics, or a mass law. Likewise this calculation supplies no five-cell L/G/N transfer count.

## 7. Revised understanding and next gate

We have now derived geometry-dependent face projectors and transports, recovered the old cell locally, and tested their loops and global states. The first common-rule attempt is no longer merely underdefined: its natural exact-matching realization fails on this curved boundary.

Two distinct obstructions have been isolated:

- **Orientation / port obstruction:** inherited negative-polarization face records occupy complementary incident lines.
- **Curvature / parallelism obstruction:** even full spinor ports have no nonzero globally parallel piecewise constant state under the intrinsic folds.

The minimal tested relaxation gives a rank-four low-mode return. The next useful question is whether an independently motivated orientation-sensitive or first-order operator resolves that four-dimensional space, or whether a four-component carrier is what the construction should retain. One must not simply delete two modes to recover the hoped-for answer.

An alternative is to keep the rank-one ports and derive a genuine complementary-line coupling. That is a different branch and must retain its additional operations and costs.

## Reproduction

    python research/voevodsky/checkers/check_pentachoron_spin_interfaces.py

Twelve exact test groups pass over Q(sqrt(2),sqrt(3),sqrt(5),i). The result file contains the exact loop matrices, ranks, and spectral values:

`research/voevodsky/results/pentachoron_spin_interfaces.json`.

Predecessor: `cell-interface-assembly-contract.md`. No viewer or original coefficient protocol was changed.
