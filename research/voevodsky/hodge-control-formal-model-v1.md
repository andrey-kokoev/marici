# Formal Hilbert control: commuting matrices with a smooth section factor

## Fresh task and precise deformation problem

Execute control-formal-commuting-matrix-model. Fix the abelian sixfold X, an ample L, and the smooth complete intersection Z cut out by three independent sections of L. Set E=L tensor C^3 and n=h^0(X,L). We consider deformations of Z INSIDE fixed X over local Artinian complex algebras, with the central fiber identified. No ambient moduli direction is included.

The result is a noncanonical isomorphism of completed local rings

    completed O_(Hilb(X),Z)
      ~= C[[ entries of M_1,...,M_6, z_1,...,z_(3n-9) ]]
          / (entries of [M_i,M_j], 1<=i<j<=6),

where each M_i is a 3 by 3 matrix centered at zero. This is a statement about the full formal germ, not just its tangent cone. The comparisons below, rather than the presence of quadratic primary obstructions alone, justify it.

## 1. A strict multiplicative comparison removes higher bundle equations

Let V=H^1(X,O_X), identified with invariant (0,1)-forms. The inclusion

    (Mat_3(C) tensor Lambda^* V, d=0)
      -> A^(0,*)(X,End E)

preserves multiplication and hence the graded commutator bracket. On an abelian variety every Dolbeault cohomology class with trivial coefficients has an invariant representative. End E is holomorphically trivial, so the inclusion induces an isomorphism on every cohomology group. It is a strict differential graded Lie quasi-isomorphism, not merely an isomorphism of vector spaces in degrees1 and2.

The standard characteristic-zero deformation comparison for nilpotent Artinian coefficients therefore identifies the corresponding Deligne groupoids. Write an invariant Maurer-Cartan element as a=sum M_i u_i with M_i in Mat_3(m_A). Since the invariant differential is zero, its complete equation is

    a wedge a=0  iff  [M_i,M_j]=0 for all i<j.

The invariant degree-zero gauge group is 1+Mat_3(m_A), acting by simultaneous conjugation. This supplies all-order sufficiency for the BUNDLE problem: commuting matrices give the actual integrable operator bar-d_E+a, and the quasi-isomorphism shows that noninvariant corrections hide no additional deformation classes or obstruction equations. All series here terminate over Artinian algebras; inverse limits are formal, with no assertion of analytic convergence.

## 2. Sections contribute smooth parameters, equivariantly

Since H^q(X,E)=0 for q>0, sections lift across every small Artinian extension whenever the bundle does. For a deformation E_A, H^0(E_A) is free of rank3n and higher cohomology vanishes, by induction and base change. Section lifting is therefore formally smooth, but its parameters must still be retained before quotienting gauge.

One can choose a compatible gauge-equivariant formal trivialization of these section spaces. Choose a contraction of the Dolbeault complex of L onto H^0(L), and tensor it with C^3. The contraction, inclusion and projection commute with constant matrices. Formal homological perturbation by a=sum M_i u_i gives a trivialization of H^0(E_A) with H^0(L) tensor C^3 tensor A. The transferred differential is zero because the original cohomology is concentrated in degree0. The formulas are equivariant under simultaneous matrix conjugation and the natural action on section vectors.

Thus a pair can be represented by a commuting tuple M and a 3 by n coefficient matrix S reducing to the central section matrix S0. Gauge acts as

    (M_i,S) -> (g M_i g^(-1), g S).

This equivariant construction matters: an arbitrary choice of section coordinates would not by itself justify this simple gauge formula.

## 3. The section fixes gauge rather than being discarded

Choose the basis of H^0(L) so that S0=[I_3 | 0]. For any deformation, the first three columns Q of S reduce to I_3 and are invertible. There is a unique allowed gauge element g=Q^(-1) putting those columns back to I_3. The remaining 3(n-3) entries are free formal section coordinates.

This operation also conjugates the M_i, which preserves their commuting equations. After imposing Q=I_3, there is no residual gauge: g I_3=I_3 forces g=I_3. In particular one must NOT further quotient the commuting tuples by GL_3. Doing so would discard the frame supplied by the defining section and change the Hilbert problem into a different bundle-moduli problem.

The result for pairs is exactly the formal product of the commuting-matrix scheme at zero and a smooth factor of dimension3n-9. No claim that its quadratic equations form a regular sequence is made.

## 4. The zero-locus comparison is valid over all small extensions

The previous construction supplied the natural pair-to-Hilbert map with obstruction-compatible tangent complex comparison

    C=[End E -> E] -> i_*N[-1].

Its kernel is quasi-isomorphic to F=ker(End E->I_Z E), and Koszul gives

    0 -> E tensor Lambda^3 E* -> E tensor Lambda^2 E* -> F -> 0.

Negative-line-bundle vanishing implies H^q(F)=0 for q<5. Thus tangent and obstruction comparison maps are isomorphisms. There are no infinitesimal automorphisms of the central pair: a constant endomorphism annihilating all three independent defining sections is zero.

For completeness, the formal lifting argument uses the FULL small-extension obstruction theories, not only the primary quadratic calculation. Given a pair over A and a Hilbert lift over a small extension A'->A, naturality sends the pair obstruction to the zero Hilbert obstruction. Injectivity of the obstruction comparison makes the pair lift exist. Its zero locus may initially differ from the prescribed Hilbert lift, but the difference is a tangent torsor element; tangent surjectivity adjusts the pair lift to match it. Tangent injectivity and the absence of infinitesimal pair automorphisms give uniqueness up to the required isomorphism. Induction on Artinian length identifies the two deformation functors.

This uses standard complete Cech obstruction theories for bundles with section and for regular embeddings. Regularity of the central section ensures flat zero loci throughout these infinitesimal liftings. It proves the asserted completed local Hilbert model, not just equality of dimensions.

## 5. Checks and interpretation

There are54 matrix tangent variables and3n-9 smooth section variables. Since the commuting equations start in degree2,

    dim T_Z Hilb(X)=54+3n-9=3n+45.

The normal-bundle calculation agrees: the twisted Koszul sequence gives h^0(L|Z)=n-3+3h^1(O_X)=n+15, hence h^0(N)=3n+45.

The 15 pairs of matrices each contribute eight independent trace-free quadratic entries, giving120 independent quadratic equations. They have higher syzygies; subtracting120 from the variable count is NOT a dimension calculation. The previously exhibited noncommuting tangent fails the quadratic equations at order t^2, while any commuting formal tuple yields all-order pair and Hilbert deformations after choosing the section coordinates.

This establishes a formal model, not yet an explicit finite-type algebraic family for a chosen arc, nor a description of its irreducible components, reducedness or global Hilbert component. It concerns the already algebraic class l^3 and cannot be assigned to an unknown Weil-cycle representative.

## Next constructive test

Choose a genuinely nontrivial commuting nilpotent arc, for example M_1=tJ with J a regular nilpotent 3 by 3 matrix and M_2=...=M_6=0. Construct its section lift and zero locus, and use proper formal existence to audit algebraization over C[[t]]. Track the unipotent filtration of the bundle and the resulting cycle/Chern class. Determine its Weil-plane readout explicitly; do not infer that the flexibility of this formal germ supplies a representative of R.

Verification separates the strict invariant-form comparison, equivariant section contraction and all-order zero-locus argument from exact gauge, commutator and tangent/quadratic-count checks. Standard deformation-comparison and formal perturbation results are imported; no proof-assistant certification or original Hodge verdict is claimed.
