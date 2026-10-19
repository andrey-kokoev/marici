# Hodge iteration 6: a substantial witness library is exhausted, not all cycles

## Findings

Keep the fixed exponential-period sixfold X, alpha=R and projector O=P((2+i)*) from iterations 4–5. The result of this turn is **not** nonalgebraicity. It is:

1. End^0(X)=Q(i), proved using the prior genericity argument and a new exact rank-142 centralizer certificate. In particular X is simple.
2. Every divisor class on every power X^r is fixed by the diagonal automorphism tau=i. Pull/push, products and Poincare-kernel operations preserve this symmetry. But tau acts by -1 on the Weil plane. Thus this whole explicitly typed witness library has zero Weil projection on X.
3. A direct search through 43 rational algebraic correspondence cycles on X x X produces four nonzero cohomology classes, all multiples of E^3. None gives a Weil witness.
4. The Fourier correspondence is checked on all 4096 exterior basis vectors. In particular Phi_E(alpha)=3 alpha, not zero: the correspondence preserves possible witnesses rather than supplying a universal annihilator.
5. A sharper remaining positive route is to find an algebraic vector bundle G with nonzero O(kappa_3(G)), its normalized third Chern component. This existence is equivalent to alpha algebraic. No such bundle has been constructed.

The new `tautological-power-witness-search` node rejects **this source library as a route to a nonzero projected witness**. The unrestricted `algebraic-witness-search` and all-cycle annihilation gates remain open.

## 1. Endomorphisms: from finite certificates to the actual fixed point

Write V=Q^12 with its marked lattice, and use the rational complex-structure family J(Z) of the candidate note. A rational matrix M defines an element of End^0(X) exactly when

    J(Z) M - M J(Z)=0.

Indeed a rational matrix commuting with J becomes a lattice-preserving holomorphic homomorphism after multiplying by an integer. Such a homomorphism of projective complex tori is algebraic. Conversely any algebraic homomorphism has this property. Using V rather than its dual only exchanges the opposite algebra; Q(i) is commutative.

For the actual specified Z, its 18 real coordinates are algebraically independent over Q by the existing exponential-prime/Lindemann–Weierstrass proof. The entries of J(Z) are rational functions over Q. Consequently, for rational M, commuting at this Z implies that the cleared commutator equations are polynomial identities in all 18 variables. In particular M commutes at every nonsingular rational sample of this chart.

Stack the 144 scalar equations at each of the same 19 samples used in the Picard certificate. The resulting rational constraint matrix on 144 entries has rank **142**. The receipt records 142 independent row indices; an independent dense rational RREF confirms their independence. The identity and the native multiplication matrix T=i lie in the kernel. They are independent and commute with J universally, not merely at the samples. Hence the rational centralizer at the specified transcendental point is exactly Q Id + Q T, giving

    End^0(X)=Q(i).

The finite rank certificate supplies an upper bound; algebraic independence and the two universal endomorphisms supply the missing logical steps. It is not a claim that a rational sample has generic endomorphism algebra.

By Poincare complete reducibility, a nontrivial proper abelian subvariety would give a nontrivial idempotent in End^0(X). A field has none, so X is simple and not isogenous to a nontrivial product. This does not prevent special fibers in the same family from being products.

## 2. Why even arbitrary divisor classes on powers do not help

Use the product polarization on X^r. Then

    End^0(X^r)=M_r(Q(i)),
    Rosati(A)=conjugate(A)^transpose.

The Rosati involution sends i to -i: this follows directly from E(Tv,Tw)=E(v,w) and T^2=-1. The standard Neron–Severi/Rosati identification identifies NS(X^r)_Q with the Hermitian matrices. Its rational dimension is r^2, not merely r. This admits all off-diagonal Poincare divisor classes, not just divisor powers pulled from individual factors.

Every such matrix commutes with the central diagonal T, and conjugate(T)T=1. Thus every divisor form D satisfies

    (tau^r)*D=D.

Equivalently, express D(v,w)=E_r(Cv,w) with C a Rosati-symmetric rational endomorphism. Commutation with T and E_r(Tv,Tw)=E_r(v,w) give the displayed identity directly.

The degree-zero unit and point classes are invariant too. Every actual homomorphism between powers commutes with these diagonal automorphisms, since all its entries lie in Q(i). Proper pushforward and pullback therefore commute with tau on rational cohomology. Cup products, external products and rational combinations preserve invariant classes. A graph correspondence is proper pushforward along (Id,f), so is included.

### Explicit operation license and degree shifts

This successor considers smooth powers only. For f:X^r -> X^s, rational Chow-ring pullback preserves codimension and uses the usual smooth-target refined-intersection construction; proper pushforward sends CH^p to CH^(p+6(s-r)), with the standard zero convention where appropriate. These are imported classical intersection-theory operations, not a silent assertion of a general pullback API from iteration 1. Cycle classes commute with the licensed operations. Graphs, projection, addition, diagonal, and Q(i)-endomorphism correspondences satisfy the stated source/target hypotheses.

If a supplied bundle has a certified formula ch(G)=rank(G) exp(c1(G)/rank(G)), its Chern character is in the same invariant library. This is a **conditional exponential-Chern ansatz**, not an assumption about arbitrary vector bundles or arbitrary higher Chern classes.

The Poincare kernel used below is itself a divisor class on X x X, so each component of its exponential and the associated correspondence also belong to the library. Finite sequences of these operations, on any finite powers, preserve tau-invariance. This is an induction on the typed expressions, not a finite enumeration of all cycles.

On the determinant generators, T*u_j=i u_j, so

    tau*R=-R,  tau*I=-I.

The projector O commutes with tau, being a polynomial in the commuting multiplication 2+i. If v is an invariant class of degree six produced by the library, O(v) is both invariant and anti-invariant. Therefore 2 O(v)=0, hence O(v)=0 over Q.

This is a necessary failure of the specified witness construction, not an all-algebraic-cycle theorem. An arbitrary codimension-three algebraic cycle need not be tau-invariant.

## 3. Actual correspondence-class search on X x X

Let L be the ample line bundle with c1(L)=E, with polarization Euler characteristic chi(L)=3. Put

    ell=m*E-p1*E-p2*E.

It is the first Chern class of the Poincare line bundle pulled back by (Id,lambda_L):X x X -> X x X-dual. The line bundle M=m*L tensor (p1*L)^(-1) tensor (p2*L)^(-1) is algebraic. Every class

    beta_abc=p2_*(E1^a/a! * E2^b/b! * ell^c/c!),
    0<=a,b<=6, c>=0, a+b+c=9,

is therefore the class of an actual rational algebraic codimension-three cycle. Negative line bundles and factorial denominators cause no issue in CH_Q. The pushforward degree is 9-6=3, as required.

There are 43 triples. Each ell contributes one first-factor and one second-factor one-form, so first-factor integration can be nonzero only when 2a+c=12. The only nonzero outputs, relative to E^3/3!, are

| a | b | c | coefficient |
|---|---|---|---|
| 3 | 0 | 6 | -3 |
| 4 | 1 | 4 | 9 |
| 5 | 2 | 2 | -9 |
| 6 | 3 | 0 | 3 |

The receipt records all 43 triples and exact coefficients. Every output has O(beta_abc)=0. This search includes divisor intersections and integration on a product, rather than retesting E^3 on X alone. Nevertheless it produces no new Weil component.

## 4. Exact Fourier calculation and sign controls

Define the unnormalized cohomological correspondence

    Phi_E(eta)=p2_*(p1*eta exp(ell)).

This is an algebraic rational correspondence. If interpreted through a Fourier–Mukai functor, the tangent Todd class is one because X is abelian; no extra Todd correction is being dropped. We use the correspondence description and make no assertion about arbitrary derived objects being tautological.

For native plane j with d_j in (1,1,1,-1,-1,-3), write x,y for first-factor forms and x',y' for second-factor forms. Its kernel is

    ell_j=d_j(x wedge y' - y wedge x').

Integrating this local exponential in the ordered real plane sends

    1 -> -d_j^2 x' wedge y',
    x -> -d_j x',
    y -> -d_j y',
    x wedge y -> 1.

Factor the even kernel exponentials over the six planes. The marked global real orientation is opposite to the complex orientation (three negative complex planes at Z=0, constant on the connected chart). Multiply the tensor product of these local rules by -1. This gives the sparse exact Fourier implementation; no floating-point period approximation is used.

It verifies

    Phi_E(E^k/k!)=3 (-1)^(6-k) E^(6-k)/(6-k)!, k=0,...,6,
    Phi_E^2 on H^k =9 (-1)^k Id,
    Phi_E(R)=3R, Phi_E(I)=3I.

The square identity is checked on all 4096 basis vectors of H*(X,Q), not only the selected class. In particular the signs distinguish Phi_E(E^3)=-3E^3 from Phi_E(R)=3R. This is not a map annihilating all known or all possible algebraic classes. Acting nontrivially on R does not manufacture an algebraic source for R.

## 5. The remaining positive source: normalized third Chern data

For a positive-rank algebraic vector bundle G of rank n define

    kappa(G)=ch(G) exp(-c1(G)/n),
    kappa_3(G)=ch_3(G)-(c1(G)/n)ch_2(G)+c1(G)^3/(3n^2).

Here the subscript denotes complex codimension, so these are degree-six classes. On the fixed X, c1(G) is a rational multiple of E by the prior Picard certificate. Also

    O(E wedge H^4(X,Q))=0.

To see the latter, E has one K character of each embedding. Every monomial in E wedge H^4 therefore has at least one character of each kind. It has neither endpoint character selected by O. In native coordinates every such monomial contains some dx_j wedge dy_j, the same statement in an explicit basis. The checker verifies this support assertion on all 495 degree-four basis vectors, with additional direct projector controls.

Consequently

    O(kappa_3(G))=O(ch_3(G)).

Line-bundle twists preserve kappa, by multiplying ch by exp(c1(line bundle)) and shifting normalized c1 by exactly the same quantity. Thus they cannot create this missing component. Bundles with certified exponential Chern character have kappa_3=0. Arbitrary bundles are not subject to that restriction.

There is an exact positive-route equivalence:

    exists algebraic G with O(kappa_3(G)) !=0
      iff alpha is algebraic.

Forward: kappa_3(G) is a rational algebraic cycle class, so its nonzero Weil projection yields a representative of alpha by iteration 5's explicit rational correspondence and 2x2 inverse.

Backward: if alpha is algebraic, some codimension-three cycle in a rational representative has nonzero Weil projection. For an integral codimension-three subvariety Z, ch_3(O_Z)=[Z]. On a smooth projective variety, O_Z has a finite locally free resolution. Its ch_3 is therefore an alternating sum of third Chern characters of positive-rank bundles (zero terms may be omitted). At least one summand has nonzero projected ch_3, hence nonzero projected kappa_3. The same reasoning applies to a rational combination of Z. These are standard resolution and Chern-character facts, not a construction of the required bundle.

A concrete next calculation is the full generic degree-six Hodge kernel in the 924-dimensional exterior space. If it is exactly Q E^3 + Q R + Q I, its tau-anti-invariant part is W; then any algebraic cycle not fixed by tau in cohomology would already supply the needed Weil witness. That kernel dimension and this simplified criterion are **not yet certified** here.

### Literature boundary

Fresh searches used the mandated `pnpm pdf:search` interface. The existing local index warns of repository-wide added/removed PDFs; no completeness conclusion is drawn from it. On its already retained PDFs, `markman-2502-03415v2:p48` mentions a *simple semihomogeneous* normalization bundle Q and a projective-bundle construction. This does not license replacing an arbitrary sheaf by an exponential-Chern bundle without losing the sought higher component. `deligne-clay:p2` explains cycle expressions through locally free resolutions and Chern classes, matching the standard positive-route reduction above.

This turn does not extend the older bounded literature audit, claim an exhaustive search, or apply a split-discriminant result to the fixed nonsplit sixfold. Next research should seek an actual higher-Chern/sheaf or non-tautological subvariety construction with verified hypotheses at this X, not repeat the divisor/Poincare library.

## 6. Why the old elliptic-product control is not contradicted

At Z=0 the commutant dimension is **72**, not two; the checker verifies this separately. The fiber is an elliptic product with far more endomorphisms. The native T is not central in that larger algebra, so its divisor classes need not all be T-invariant. Indeed the earlier r_j,s_j divisor classes can be anti-invariant, and their determinant product R is detected.

Thus the fixed-point genericity step in Section 1 is indispensable. This library exclusion cannot be promoted to a uniform family statement. It also cannot be promoted to fixed-X annihilation of arbitrary cycles, which is still precisely the hard open question.

## 7. Artifacts and verification boundary

Contract: `research/conjecture_net/contracts/hodge-tautological-witness-search.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_tautological_witness_search.py`.
Receipt: `research/voevodsky/results/hodge-tautological-witness-search-v1.json`.

    python research/voevodsky/checkers/check_hodge_tautological_witness_search.py

Trust is explicit: the centralizer certificate, finite algebraic-class search and exterior identities are exact rational computations. Genericity, rational torus homomorphism algebraization, Rosati theory, Poincare reducibility and cycle-class functoriality are written arguments using standard imported mathematics, not proof-assistant certification. Arbitrary cycles and arbitrary vector bundles remain unenumerated. No Hodge verdict, all-cycle annihilation, nonalgebraicity or actual representative of alpha follows.
