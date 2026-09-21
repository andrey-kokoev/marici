# Generator-to-derived extension with the Clark dual receiver

## The theorem

Let Q be a finite typed source graph, with its marked arrows retained, and let S=C[Q] be its chronological path algebra. The construction also allows an explicitly specified ideal of relations, provided the receiver satisfies those relations. Distinct routes are not silently identified.

For each vertex x suppose given:

1. a finite-dimensional complex carrier X_x;
2. a nondegenerate Hermitian pairing q_x, conjugate-linear in its first argument;
3. for every generator e:x->y, a linear map A_e:X_x->X_y.

Let X_x^h be the space of conjugate-linear functionals on X_x. The pairing defines a linear isomorphism

beta_x:X_x->X_x^h, beta_x(y)(x')=q_x(x',y).

Define the mate A_e^sharp:X_y->X_x by

beta_x A_e^sharp=A_e^vee beta_y,

where A_e^vee is precomposition on conjugate-linear functionals. The mate exists and is unique by nondegeneracy.

Then:

**A. Path extension.** The generator representation extends uniquely to the path algebra. The mates extend contravariantly, and beta is an isomorphism from the mate representation to the contragredient representation. The pairing square holds on every path, linear combination, and retained typed cut, with conjugation on reversed scalar coefficients.

**B. Derived extension.** The receiver has a canonical exact C-linear extension

E_X:Perf(S)->Perf(C),

unique up to the equivalence specified by its complete generator action. The mate representation has its own exact extension E_Y on the conjugate opposite algebra.

**C. Derived duality square.** For every perfect source object P there is a natural equivalence

D_C^h E_X(P) equivalent to E_Y D_S^h(P),

where

D_S^h(P)=conjugate(RHom_S(P,S))

is a perfect left module over conjugate(S)^op, and D_C^h is the cochain conjugate dual. Under this equivalence, a cofiber is taken to the corresponding fiber, with its cohomological shift and sign. The square extends to retracts and complete interval-closure diagrams.

The theorem establishes existence, uniqueness in the enhanced exact sense, and duality compatibility. It does not assert that E_X is faithful, conservative, monoidal, or a physical realization.

## 1. Constructing the module from the generators

Let X=direct_sum_x X_x. It is a RIGHT S-module: the vertex idempotent selects X_x, and the right action of e:x->y is A_e. For a chronological path e_1...e_n,

x (e_1...e_n)=A_(e_n)...A_(e_1)x.

Thus composition of receiver matrices has the usual reverse order relative to writing source events chronologically. Noncomposable algebra products act by zero.

The freeness of the path algebra proves existence and uniqueness of this action from the generator assignments. If relations are imposed, their vanishing under the receiver is an additional hypothesis. It is not supplied by mere equality of terminal objects.

For composable e and f, applying their pairing squares gives

(A_f A_e)^sharp=A_e^sharp A_f^sharp.

For a scalar lambda,

(lambda A_e)^sharp=conjugate(lambda) A_e^sharp.

Consequently the mate carrier Y=direct_sum_x X_x, with reversed arrows acting by the mates, is a right module over conjugate(S)^op. The conjugate algebra is necessary for complex scalar consistency. In the path algebra's real generator basis it may be identified with the ordinary opposite path algebra, but this identification must retain the conjugation of coefficients in the source reversal.

The same opposite module structure on X^h is induced by precomposition. The component beta_x maps combine into a module isomorphism

beta:Y -> X^h.

This proves the path-level theorem. It does not equate Y with the vacuum-preserving opposite-history creation representation.

## 2. Formal propagation proof

`agda/GeneratorMateExtension.agda` proves the propagation from generator squares on an arbitrary typed graph. It takes two contravariant generator actions, the components beta, and the local commuting squares as explicit inputs.

It constructs:

- `path-square`: the square on every route;
- `fold-composition`: the contravariant composition law;
- `Uniqueness.unique`: uniqueness from the unit and generator-extension laws;
- `cut-square`: the same square through a typed cut without discarding its middle vertex.

The proof uses induction on source paths. It needs no metric hypotheses once the local squares have been supplied. Nondegeneracy is used earlier to construct the local mates and beta isomorphisms, not to propagate their equations.

This safe Cubical Agda module compiles. The imported typed-history module retains its documented indexed-pattern computation warnings. No hole or postulate occurs. Derived module categories and their universal property are proved mathematically below, not formalized by this module.

## 3. Explicit derived construction

For a perfect LEFT S-module P, define

E_X(P)=X tensor_S^L P.

To compute it, represent P by a bounded complex of finitely generated projective left S-modules, allowing retracts of such presentations. Replace each vertex projective S e_x by X_x, each path matrix entry by its receiver matrix, and each scalar sum by the corresponding linear sum. Apply the same rule to the differential.

Since the receiver is an algebra representation, d^2=0 remains true. Chain maps, homotopies, and compositions are preserved. Bounded complexes of projectives are K-projective, so the construction computes the derived tensor product without requiring X to be flat over S.

The output is perfect over C: each X_x is finite-dimensional, and finite sums, shifts, cones, and retracts preserve perfection. Derived tensor is exact, hence

E_X(cofib u) equivalent to cofib(E_X u).

An exact C-linear functor out of Perf(S) is determined by its right S-module of values on the vertex projectives and their complete algebra action. Equivalently, Perf(S) is the idempotent-complete pretriangulated envelope of these projective generators. This gives the stated enhanced uniqueness: fixing that module data fixes the extension up to a contractible choice of compatible equivalence.

This is stronger than an assertion about an unspecified triangulated functor. The dg/stable enhancement and the full algebra action are part of the statement.

## 4. Proof of the derived duality square

First use the contragredient module X^h rather than its mate presentation Y. There is a natural equivalence, for perfect P,

D_C^h(X tensor_S^L P)
  equivalent to X^h tensor_(conjugate(S)^op)^L D_S^h(P).

One proof is the finite-projective tensor–Hom duality: it holds on a vertex projective S e_x by evaluation, on finite sums by componentwise evaluation, and on all perfect objects by shifts, cones, and retracts. Both sides are contravariant exact functors in P. The evaluation map is natural, so extending from generators introduces no separately selected comparison on composite objects.

Now apply the module isomorphism beta:Y->X^h. Derived tensor carries it to the natural equivalence

E_Y D_S^h(P) equivalent to D_C^h E_X(P).

The orientation can be reversed to match the theorem's displayed square. At P=S e_x, it is precisely beta_x; on a generator arrow it is precisely the original pairing square. Thus the full comparison extends, rather than replaces, the prescribed local Green-mate data.

## 5. Complex signs and cofiber/fiber conversion

For a cochain complex C,

(D_C^h C)^n=(C^(-n))^h,

d_(D C)^n=(-1)^(n+1) (d_C^(-n-1))^vee.

Let A:X->Y be in degree zero. With Cone(A)^(-1)=X, Cone(A)^0=Y and differential A, its dual has

(D Cone(A))^0=Y^h,

(D Cone(A))^1=X^h,

d^0=-A^vee.

This is Cone(A^vee)[-1], hence Fib(A^vee). Under beta the differential is -A^sharp. The sign is forced by the cochain dual, not fitted to a pairing residual.

For longer complexes the same formula gives d_D^2=0. It transports chain homotopies and all finite cofiber constructions coherently.

A cofiber of a sum of marked arrows is the cofiber of the sum map. No step distributes it as a sum of separate cofibers.

## 6. Retracts: the dual carrier must be retained

Idempotent completion is essential for Perf(S). If p is an idempotent on a represented object, the primal retract is image(p), while its dual observation carrier is image(p^sharp), equivalently the image of the contragredient idempotent under beta.

The pairing between these two images is perfect. Indeed q(px,y)=q(x,p^sharp y), and ambient nondegeneracy then detects every nonzero vector on either image. This does NOT imply that the original signed form restricted to image(p) alone is nondegenerate.

A two-dimensional witness is

Q=diag(1,-1), p=[[1,0],[1,0]], p^sharp=[[1,-1],[0,0]].

The primal image is spanned by u=(1,1), with q(u,u)=0. The dual image is spanned by v=(1,0), with q(u,v)=1. The dual pair is nondegenerate despite the isotropic primal restriction.

This prevents a false extension theorem that would demand a nondegenerate Hermitian form on every primal retract inside the same carrier. Derived duality uses the paired opposite object instead.

## 7. Stable closure, marked lift, and retained cuts

The source-marked algebra maps l:R->S and a:S->R from the earlier construction remain split. The receiver extension satisfies

E_X composed (S tensor_R^L -)
  equivalent to X restricted_along_l tensor_R^L -.

Thus the unmarked generator acts by A_e^0+A_e^1, exactly as in the pilot. The preceding split source extension is compatible with this receiver, but its faithfulness is not inherited automatically by E_X.

Exactness gives pointwise maps of complete interval diagrams. Duality reflects such a diagram Z by

Z^vee(i,j)=D Z(n-j,n-i).

The derived pairing square applies pointwise, so it intertwines the receiver with this reflected closure and its restriction maps, using reflected ordinal indices. In particular it preserves the cofiber/fiber shift rather than merely reversing an ordinary filtration.

For explicitly retained tensor cut records, the finite-dimensional dual of a tensor product is the tensor product of the dual factors, with their order reflected, and the dual of a finite vertex-indexed sum keeps that label. Tensoring the beta maps therefore gives the corresponding joint-cut pairing square.

These are distinct statements: E_X is not asserted to be monoidal, and a tensor cut-record carrier is not automatically identified with the image of a particular source cofiber quotient. Such an identification requires its own specified comparison. The extension theorem does supply all cofiber images generated by the prescribed module representation.

If a cut-chart category with rejoining arrows is included in the source, its composition relations must hold in the receiver. Once they do, the same theorem applies to its category algebra; the reversed mate relations follow automatically. The theorem does not add arbitrary higher source identifications beyond those admitted data.

## 8. Application to the actual finite Clark pilot

Use the finite prepared-source version of Voevodsky's sheet-reduced pilot. At a fixed finite chamber cutoff:

1. W0=Lhat(V) is finite-dimensional and injectively contains the admitted chamber features.
2. W=W0+J W0 is finite-dimensional, J-invariant, and carries a nondegenerate signed pairing.
3. The degree-zero-through-N record space direct_sum_(r=0)^N W^(tensor r) is finite-dimensional and has invertible weighted signed operator direct_sum J^(tensor r).
4. At each cut a, restrict the source-fiber factor to the line generated by the one prepared R_a^(-1)Phi. Reassembly maps this line unitarily to the next prepared line.
5. Both prescribed generator maps T_e tensor I and T_e tensor c_R(g_e) preserve these finite carriers. Their mates preserve the paired carriers because J g_e lies in W.

These are exactly the theorem's hypotheses. Therefore the finite prepared marked Clark receiver has a canonical perfect-module extension, together with a natural duality equivalence whose generator components are the already prescribed beta and Green mates.

This is a mathematical derived extension of the actual finite receiver, not a matrix fitted to source dimensions. Its existence does not require the underlying source-space operations to be physically implemented.

The full infinite-dimensional cut fiber, infinite history completion, and changing prime cutoff are not covered by this finite-dimensional corollary. They require a chosen topological derived category, continuous tensor/dual constructions, and appropriate closed-range or domain control. The theorem does not infer those from bounded generator maps alone.

Receiver reference: `research/voevodsky/the-marked-clark-diamond-has-a-nondegenerate-dual-pair-after-sheet-reduction.md`.

## 9. What has and has not been closed

Closed for the finite prepared receiver:

- generator-to-path uniqueness and pairing naturality;
- construction and enhanced uniqueness of the exact perfect-module extension;
- extension of the contragredient square to perfect complexes and retracts;
- compatible cofiber/fiber signs and reflected interval closure.

Not implied:

- faithfulness of terminal or separate-cut observations;
- identification of the dual contraction representation with the vacuum-pointed opposite creation representation;
- a positive full-history functional or terminal comparison isometry;
- physical event access;
- extension to infinite analytical carriers or equality with an independently specified analytic derived category.

The three-prime marginal ghosts remain valid: an exact receiver functor may lose morphism information. Exactness and duality compatibility do not repair a noninjective observation.

## 10. Verification

Formal path-level command:

    agda --transliterate --safe --cubical --guardedness --no-libraries \
      -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 \
      -i research/grothendieck/agda \
      research/grothendieck/agda/GeneratorMateExtension.agda

Exact algebraic regression:

    uv run --with sympy python research/grothendieck/checkers/check_generator_to_derived_extension.py

Both pass. The finite fixture checks generator pairing squares, conjugate-linearity, path-mate composition, the unmarked sum representation, cone/fiber sign, a three-term dual differential, and the isotropic-retract hostile. It uses independent complex features in a finite two-sheet record, not sampled analytical data.

Artifacts: `results/generator-mate-extension-agda.log` and `results/generator-to-derived-extension.json`. The perfect-module theorem is proved above; it is not claimed to be formally verified by the finite matrix regression or the path-level Agda module.
