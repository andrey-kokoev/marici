# Relative rational cycles on a dense open of the product-control base

## Fresh task and actual base

Execute control-locus-relative-cycle-spread. Let S0 be a smooth irreducible component of a sufficiently fine algebraic level moduli space for the two polarized O_K threefold factors of signatures(2,1) and(1,2). Its dimension is four. Work with their universal product abelian scheme pi:mathcal X->S0 of relative dimension six and a relative very ample line bundle, adding the usual level/line-bundle rigidification if needed. This uses standard algebraic moduli and projective-family constructions; explicit moduli equations are not computed.

The map from this factor-parameter base into the full nine-dimensional Weil moduli is retained, but S0 is not silently identified with that full base. Every fiber is decomposable. The prior two-correspondence construction, using the audited all-fourfold theorem, proves pointwise algebraicity of BOTH rational determinant components in every fiber of this family.

## First make the determinant classes global

The integral O_K lattice is the retained Gaussian lattice. Monodromy acts by invertible O_K-linear matrices, whose K-determinants belong to Z[i]^times={1,-1,i,-i}. Its action on the native determinant line therefore has finite image. Pass to the finite etale cover given by the kernel of that determinant character, and choose a connected component. A cover of degree at most four suffices to kill this character, in addition to the already chosen fine level.

After renaming the resulting smooth irreducible base S0, fix a marked rational basis of its now trivial determinant local system:

    R_S, I_S in H^0(S0,R^6 pi_* Q).

Only this rank-two local system is trivialized; the full cohomology monodromy is not asserted trivial. Both sections have type(3,3) and are pointwise algebraic. Without this step trace could average different rotations of a local class to zero rather than recover the desired marked component.

## Countably many proper parameter spaces really cover the control base

For each determinant component j in {R,I}, a rational cycle on a fiber can be written as (1/m_j) sum_i n_(j,i)[Z_(j,i)], with m_j>0 and signed integers n_(j,i). Each irreducible threefold Z_(j,i), taken with its reduced scheme structure, defines a point of a relative Hilbert scheme with a degree-three Hilbert polynomial.

Index all finite tuples of these Hilbert polynomials, signed coefficient lists and the two positive denominators m_R,m_I. There are countably many such choices. For each choice take the fiber product over S0 of the relative Hilbert schemes for BOTH lists. It is projective of finite type over S0, so has finitely many irreducible components. Universal flat subschemes give the two universal signed dimension-three cycle families on its pullback of mathcal X.

Keep exactly those irreducible components T on which the two universal fiber classes equal m_R R_S and m_I I_S. This is a whole-component condition: cycle classes of flat projective families are locally constant in the pulled-back smooth-family local system, and a complex irreducible component is connected. Equality at one point therefore propagates on that component. Lower-dimensional embedded scheme components do not change the top dimension-three cycle class. We use the standard compatibility of cycle classes with flat families here, not a new theorem that every Hodge class deforms algebraically.

Pointwise algebraicity guarantees that the closed images of these retained components cover S0(C). Properness gives closed images. If every image were proper, a small analytic coordinate neighborhood of the smooth base would be covered by countably many closed nowhere-dense analytic subsets, contradicting Baire. Hence at least one retained T dominates S0, and its proper image is all of S0.

This proves existence of a SINGLE parameter component carrying both components with fixed finite cycle lists and fixed denominators. It does not identify an explicit component or bound the Hilbert polynomials. Countability alone would not suffice without the pointwise coverage and proper-image hypotheses.

## A finite multisection, not an unjustified section

Let K=C(S0) and let T_eta be the nonempty generic fiber. A closed point of this finite-type K-scheme has a finite residue extension L/K. Characteristic zero makes it separable. Take its closure in T and normalize. The resulting integral parameter variety W maps properly and generically finitely to S0 and maps to T.

After shrinking to a nonempty dense Zariski open U subset S0, the map

    h:W_U -> U

is finite etale of constant degree d=[L:K]. The shrink removes the non-quasifinite and branch loci; it is not assumed that the original T->S0 was finite or admitted a section. Pull back the universal signed cycles to mathcal X_(W_U), giving classes Z_R and Z_I in CH^3(mathcal X_(W_U)) with fiber classes m_R R_S and m_I I_S, respectively. Both total spaces are smooth here, so the stated Chow codimensions and fiber restrictions are well typed.

## Normalize the trace twice: degree and cycle denominator

Let q:mathcal X_(W_U)->mathcal X_U be the finite etale base change of h. Define

    Xi_R=(1/(d m_R)) q_* Z_R,
    Xi_I=(1/(d m_I)) q_* Z_I

in CH^3(mathcal X_U)_Q. The proper pushforward preserves codimension because q has relative dimension zero.

For each complex u in U, proper/flat base change and fiber restriction give

    cl((Xi_j)|mathcal X_u)
       = (1/(d m_j)) sum_(w in h^(-1)(u)) m_j (j_S)_u
       = (j_S)_u,  j=R,I.

There are exactly d points over u, since h is finite etale over C. All summands compare to the SAME globally marked class because determinant monodromy was killed before selecting T. Omitting d multiplies the class by d; omitting m_j leaves the denominator-cleared class. Rational coefficients license both divisions.

Thus the pointwise algebraic control has been upgraded to two actual relative rational CHOW CLASSES on the total family over a dense open U. This is more than an arbitrary choice of unrelated fiber cycles. It is not an effective single subscheme, a canonical class, explicit cycle equations or a specified flat relative representative after taking the signed trace. The construction is existential and depends on the imported fourfold theorem plus standard parameter-space geometry.

## Scope and next boundary test

The base U is an unspecified nonempty dense open of the four-dimensional factor-parameter cover, not an open of the full nine-dimensional Weil moduli. No prescribed special point is asserted to lie in U. The original fixed simple X is not reached by this family, and neither dominant cycle parameters over the full base nor a cycle for its alpha are constructed.

Next test the exact extension boundary: take closures of Xi_R,Xi_I over the same smooth control base and use refined fiber restriction to decide what persists at omitted control fibers. Then compare this with moving transversely into the full Weil moduli, tracking the base-codimension shift in any attempted pushforward. This distinguishes specialization inside the established base from an unproved extension into new deformation directions.

Verification checks trace normalization, simultaneous denominators, finite monodromy averaging and the scope/dimension controls. Baire, Hilbert projectivity, cycle-class constancy, generic finite multisections and base-change functoriality are the written/imported geometric proof, not conclusions of finite arithmetic tests. No Hodge verdict for the original source or proof-assistant certification is claimed.
