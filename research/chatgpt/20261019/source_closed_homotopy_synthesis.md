# Source-closed nonabelian resolution and its abelian phase quotient

Research date: 2026-10-19.

## Result and scope

For the concrete source instance obtained by suspending Marici's constructed circle, a uniform simplicial-group resolution determines the entire homotopy type and admits an exact calculation of its first higher class. A word made from two degeneracies of one source generator represents a primitive Hopf class. No Hopf element is inserted as a generating relation or attaching-map input.

Degreewise abelianization of the same resolution gives a comparison S^2 -> K(Z,2) ~ BU(1). Its homotopy fiber is S^3. The discarded class is explicitly the primitive commutator calculated below.

This is an application of the existing source circle and the standard Milnor resolution theorem to a specific source-generated suspension. It does not identify this resolution with T9, prove that a physical source selects this suspension, construct the original A4-equivariant identification, or establish all physics. Resolution degree is not a grain size, spatial dimension, or count of WG executions.

The finite checker verifies the actual face/degeneracy formulas, an integral obstruction matrix and two exact free-word certificates. The all-word subgroup proof below establishes pi_2 of the simplicial group, rather than extrapolating from bounded enumeration. The realization, delooping and Hopf-bundle identifications use the stated topological theorems. No Agda or Lean compilation was performed. No remote repository files were changed.

## 1. Prior research reused

The connected repository is `andrey-kokoev/marici`. Search results reported the default-branch commit `ace56bdce2a23bc7627649366c2a1bd49fc26414`.

1. `research/voevodsky/agda/ClosureGluingTreeRegression.agda`, blob `e3b059868de8aa2d3c6d0c795f15c879de9bf932`, constructs

       C = Pushout(Unit <- Bool -> Unit)
       circleEquiv : C ~ S1.

   Its retained two-attachment loop maps to the generator of S1 and is proved nontrivial. We use a pointed comparison to the minimal simplicial circle. This does not preserve all originally discussed A4 markings automatically.

2. `research/kitaev/ascending-rungs-stabilizes-the-law-and-moves-the-problem-to-truncation.md`, blob `b1428d467627737faff87f47cd17fe045b50ec6b`, identifies simplicial groups/hypercrossed complexes as a uniform alternative to inventing unrelated higher rungs. It distinguishes finite law schemas, finite homotopy height and finite computation. The present calculation instantiates that mathematical architecture; the note itself does not authorize a physical higher sector.

3. `research/nima/marici-minimal-mathematical-formulation.md`, blob `22097430b821387eadc95a3c00beaec99fd7f3a7`, distinguishes forming a filler type, exhibiting a filler and adjoining a new cell in a larger space. Our additional source instance is the suspension X = Pushout(Unit <- C -> Unit), made with the same already adopted pushout constructor.

4. `research/nima/four-simplex-horn.md`, blob `907577dd00b035346632e8d0f9e1147c19bbfb37`, distinguishes a missing-face-plus-filler package from a fully fixed boundary. The cycle below is not certified null by a generic horn-completion theorem.

## 2. Fix the source, then resolve it

Let K = Delta[1]/boundary Delta[1], the pointed minimal simplicial circle. It has one nondegenerate edge t and one vertex. Its realization is pointed-homotopy equivalent to C. Let

    X = Sigma C ~ S2.

The use of suspension is an explicit source operation, not something inferred from WG's invocation count.

For n >= 1 the non-basepoint n-simplices of K are the n monotone surjections [n] -> [1]. Let x_j^(n), 1 <= j <= n, denote the one with j zeros followed by n+1-j ones.

Take the reduced free simplicial group G = F[K]:

    G_0 = 1,
    G_n = FreeGroup(x_1^(n),...,x_n^(n)).

There are no independently specified higher generators. All x_j^(n) are degeneracies of t. An element of G_n is a finite freely reduced word; the set of all words is not finite.

Deleting vertex i gives

    d_i(x_j^(n)) = x_(j-1)^(n-1)  if i < j,
                  x_j^(n-1)      if i >= j,

where x_0^(n-1) and x_n^(n-1) mean the identity. Repeating vertex i gives

    s_i(x_j^(n)) = x_(j+1)^(n+1)  if i < j,
                  x_j^(n+1)      if i >= j.

Both maps extend as group homomorphisms. Deletion and repetition of vertices satisfy the simplicial identities in every degree; extending through a free group preserves those equalities. This is an all-degree argument, independent of the finite checker.

Milnor's theorem gives

    |F[K]| ~ Omega Sigma|K| ~ Omega X,
    B|F[K]| ~ X ~ S2.

Thus resolving into more degrees exposes a fixed source homotopy type. It does not replace X by a sequence of unrelated spaces with guessed higher invariants.

## 3. An explicit higher cycle

In degree one, G_1 = FreeGroup(t). In degree two put

    x = s_1 t,
    y = s_0 t.

The face maps are

| generator | d0 | d1 | d2 |
|---|---|---|---|
| x | 1 | t | t |
| y | t | t | 1 |

Use [a,b] = a b a^(-1) b^(-1). The word

    c = [x,y] = x y x^(-1) y^(-1)

has d0(c)=d1(c)=d2(c)=1. It is a Moore 2-cycle.

This is not the same object as the Whitehead square of the fundamental S2 class; their normalizations must not be conflated. The calculation below identifies this simplicial cycle itself as a primitive class.

## 4. Exact computation of the boundary subgroup

Write

    N_n G = intersection_(i=0)^(n-1) ker(d_i),
    Z_n G = intersection_(i=0)^n ker(d_i),
    B_n G = d_(n+1)(N_(n+1)G).

The Moore theorem identifies pi_n(|G|) with Z_nG/B_nG for n>=1. Gamma_k denotes the lower central series of a free group, not a group of spatial symmetries.

### 4.1 Cycles are exactly the commutator subgroup

For a word in F(x,y), let its exponent sums be (a,b). d0 reads b; d1 reads a+b; d2 reads a. Therefore

    N_2G = Z_2G = Gamma_2(F(x,y)).

### 4.2 Every boundary lies in Gamma_3

Let w lie in N_3G, and write G_3 = F(a,b,c0) to avoid confusing the third generator with the degree-two cycle c.

The vanishing of d0(w),d1(w) implies that every exponent sum of w is zero. Thus w lies in Gamma_2(F3).

Modulo Gamma_3(F3), it has unique coordinates (u,v,w0) on

    [a,b], [a,c0], [b,c0].

Their images in Gamma_2(F2)/Gamma_3(F2) under d0,d1,d2,d3 have coefficient rows

    d0: (0,0,1)
    d1: (0,1,1)
    d2: (1,1,0)
    d3: (1,0,0).

The first three rows form a matrix of determinant -1. If d0,d1,d2 vanish, all three commutator coordinates vanish integrally. Therefore w belongs to Gamma_3(F3), and d3(w) belongs to Gamma_3(F2).

Hence B_2G is contained in Gamma_3(F2). This is an argument for every word, not a sampled obstruction.

Equivalently, the coefficient of XY in the degree-two Magnus expansion is an integer homomorphism

    chi: Z_2G -> Z

that vanishes on every B_2G and has chi([x,y])=1.

### 4.3 Two explicit lifts prove the reverse inclusion

For a degree-three word w define Moore projection by applying successively, for i=0,1,2,

    w <- w * inverse(s_i(d_i(w))).

The result P(w) belongs to N_3G. The correction at step i kills face i while keeping earlier faces trivial, by the simplicial identities. This projection is not asserted to be a group homomorphism.

With a,b,c0 the degree-three generators, define

    W_x = P(a c0 b c0^(-1) a^(-1)),
    W_y = P(c0 a b a^(-1)).

Exact free reduction gives

    d0(W_x)=d1(W_x)=d2(W_x)=1,
    d0(W_y)=d1(W_y)=d2(W_y)=1,
    d3(W_x) = [[x,y],x],
    d3(W_y) = [[x,y],y].

Both full reduced words are retained in source_closed_homotopy_results.json. These are finite certificates checked without floating point.

B_2G is normal in G_2: N_3G is normal in G_3, and d3 is surjective with section s2. The normal closure of [[x,y],x] and [[x,y],y] is Gamma_3(F2), since quotienting by these relations makes the basic commutator central, and hence makes the two-generator group nilpotent of class at most two.

Therefore Gamma_3(F2) is contained in B_2G. Together with the previous inclusion,

    B_2G = Gamma_3(F2).

### 4.4 Result

    pi_2(|G|) = Gamma_2(F2)/Gamma_3(F2) = Z.

The class of [x,y] is its primitive generator. For example, mapping x and y to the two elementary unitriangular 3-by-3 integer matrices sends their commutator to a central matrix with top-right entry 1, verifying its infinite order and integral normalization.

Using |G|~Omega X and X~S2,

    pi_3(X) = Z,

and the displayed class corresponds to a Hopf map up to the sign of the chosen source orientation. Its Hopf invariant has magnitude one. The group calculation establishes primitivity; the identification with the geometric Hopf map uses the standard Hopf theorem.

## 5. Abelianization of the same model

Let A = G_ab be the degreewise abelianization. Then A_n=Z^n with exactly the same face and degeneracy matrices.

For n>=2, d0(a_1,...,a_n)=(a_2,...,a_n). Its kernel consists of the first coordinate only. d1 detects that remaining coordinate. Hence

    N_1 A = Z,
    N_n A = 0 for n>=2,
    N_0 A = 0.

The normalized differential is zero. The simplicial abelian-group/Moore theorem therefore gives

    |A| ~ K(Z,1) ~ S1,
    B|A| ~ K(Z,2) ~ BU(1).

The quotient G->A is degreewise exponent summation, not a fitted readout. It takes [x,y] to the identity. After delooping the source comparison is

    X ~ S2  --q-->  K(Z,2) ~ BU(1).

The degree-one source generator is unchanged by abelianization. Thus q induces an isomorphism on pi_2 and represents the primitive degree-two integral class. It is the 2-type reflection of this simply connected X, not its full homotopy equivalence.

The homotopy fiber of q is the circle bundle of first Chern class plus or minus one. Its total space is S3. Equivalently the degreewise exact group sequence

    1 -> [G,G] -> G -> G_ab -> 1

deloops to the homotopy-fiber sequence

    B|[G,G]| ~ S3 -> B|G| ~ S2 -> B|G_ab| ~ BU(1).

The circle-bundle classification/Hopf identification is external topology, not a claim proved by the free-word checker alone.

The source, its abelian description and the lost structure are therefore tied by an explicit universal comparison. The loss is genuinely homotopical; it is not an affine vector-space kernel mislabelled as a new homotopy sector.

## 6. Meaning for WG synthesis

What is forced after fixing this source instance and its free simplicial resolution:

- Every face and degeneracy map comes from the one circle simplex.
- The same schemas define every dimension; none is chosen to fit a requested homotopy group.
- The word [s1 t,s0 t] is forced by applying ordinary commutator formation to two generated degeneracies.
- The boundary subgroup is determined by the next level and the same face maps; it does not kill that word.
- Imposing commutativity is a distinct quotient operation, and its exact effect is the passage from S2 to its abelian phase classifying type K(Z,2).

What is not thereby proved:

- the intended physical source/rung successor is this particular suspension or this resolution;
- an inverse path operation in this pointed loop model equals every occurrence of reversal in the broader source signature;
- the original A4 action or an A4-equivariant Hopf comparison has been reconstructed;
- finite law schemas imply bounded execution, finite homotopy height or full physical coverage;
- the resulting class has a particular particle or interaction interpretation.

This is a completed source-relative structural example: one fixed finite source has a uniform full homotopy resolution and an explicit nontrivial class; a canonical commuting description loses precisely identifiable higher structure. The standard resolution is a model of the source-generated space, not a new physical axiom inferred from matching counts.

## 7. Verification

Run:

    python check_simplicial_source.py --output source_closed_homotopy_results.json

The script uses only the Python standard library. The recorded run checks:

- face-face, degeneracy-degeneracy and mixed simplicial identities on every generator through degree 12;
- the nontrivial degree-two word and all its faces;
- the degree-three integral commutator face matrix and its determinant;
- two exact Moore words whose boundaries normally generate Gamma_3(F2);
- 1,065 additional Moore-boundary regressions (325 have nonempty boundary words);
- the integer detector on powers -20 through 20;
- the normalized abelian complex through degree 12.

Total assertions: 24,246. The unbounded conclusions are proved by the displayed universal definitions and subgroup arguments, not by the total number of assertions.

## References

Repository paths are relative to https://github.com/andrey-kokoev/marici/blob/main/.

- The source files and blob hashes in section 1.
- Hans-Joachim Baues and Roman Mikhailov, *Intersection of subgroups in free groups and homotopy groups*, arXiv:0804.1999. In particular the introduction's F[S1] construction and free-group description of sphere homotopy.
  https://arxiv.org/html/0804.1999v1
- Fedor Pavutnitskiy, *Simplicial James-Hopf map and decompositions of the unstable Adams spectral sequence for suspensions*, arXiv:1703.03960. Free simplicial-group loop models and lower central structure.
  https://arxiv.org/html/1703.03960v1
- Daniel M. Kan, *A Combinatorial Definition of Homotopy Groups*, Annals of Mathematics 67 (1958), 282-312. Historical primary source for the simplicial group method. Not used as a fresh computation by the checker.
- Guillaume Brunerie, *On the homotopy groups of spheres in homotopy type theory*, arXiv:1606.05916. Hopf construction and primitive homotopy class.
  https://arxiv.org/abs/1606.05916

These are classical mathematical tools applied to the identified source instance. No priority or novelty claim is made for the underlying Milnor, Moore, Dold-Kan or Hopf theorems.
