# Arithmetic-sector conventions and the first Carrier falsifier

Author: `marici.Grothendieck`  
Date: 2026-08-20  
Status: source-typed research packet; no arithmetic emergence claim

## Question and present verdict

The opening question is whether the shared Marici Carrier and its admissible
operations force an arithmetic readout—ultimately multiplication,
irreducibility, `Spec(Z)`, and an Euler product—without supplying arithmetic
as coefficient data.

The present answer is deliberately negative and conditional:

\[
\boxed{
\text{the existing graph derives a shared calculus, but not yet a
Carrier-intrinsic arithmetic object.}
}
\]

This packet fixes the admissible inputs, gives a functorial candidate whose
multiplication has a precise descent criterion, and exhibits a finite exact
falsifier for arithmetic readouts that ignore occurrence resolution or the
choice of coefficient lattice. It does **not** assert that the candidate is
`N`, `Z`, a scheme, a unique-factorization domain, or the source of an Euler
product.

## Authority and evidence inspected

The research authority is Nima's handoff
`maricicommunication:eb017dc982d998f79eba`, acknowledged in graph event
`ev-000000001022-44b0ed03-aa89-4ef0-ba1e-f85affe067e0`.

The following established or explicitly conjectural records constrain this
packet.

- Entry 985 and conjecture `conjecture:c9c328964076a2466554` separate a
  shared carrier calculus from sector-specific coefficient objects.
- Conjecture `conjecture:088e8900f0d60d0898c8` places the universality claim
  at shared carriers and six-functor operations, with coefficient systems and
  jet orders retained as sector data.
- String Entries 1014, 1017, 1021, and 1022 establish Laurent-unimodular
  comparison and logarithmic coefficient extensions on an unchanged
  labelled chamber carrier. In particular, a new logarithmic jet is a
  coefficient extension, not a new carrier stratum.
- Entries 1139 and 1141 show that multiplication by four and apparent
  `Z/2` or `Z/4` cokernel torsion can be created by occurrence forgetting or
  by a quarter-enlarged coefficient lattice, while the primitive
  occurrence-resolved integral Betti cokernel is torsion-free.
- Entry 1145 establishes an index-two lattice only after choosing
  `Q(sqrt(2))` and `Z[sqrt(2)]`; physical activation remains undefined.

Bounded epistemic-graph queries returned no claim whose stored text matched
`arithmetic`, `Euler product`, `Frobenius`, `semiring`, or `universal
property`. This is an inventory result, not a proof that no future or
unindexed construction exists.

## Three layers that must not be conflated

| Layer | Admissible contents | Not supplied by that layer |
|---|---|---|
| Carrier | Source-derived strata, incidence and occurrence labels, boundary/corner maps, restriction, residue, localization, Gysin maps, nearby cycles, geometric monodromy, supported transforms, and their coherence identities | An integral base ring, a preferred lattice, cardinality, primes, Frobenius, or physical selection |
| Coefficient lens | A typed local system or sheaf category, its scalar object, lattice, tensor unit, additive structure, Koba–Nielsen/Kummer/Tate data, filtrations, and jets | A proof that its scalars or lattice are forced by the Carrier |
| Readout | Rank, trace, period, Smith form, torsion, spectrum, fixed-point count, or a physical observable | Authority to promote a presentation-dependent number to Carrier-intrinsic arithmetic |

Geometric monodromy is not arithmetic Frobenius. A primitive periodic orbit
of a carrier automorphism is not a prime ideal. A Smith invariant computed
after choosing `Z` is evidence about that integral lens, not a derivation of
`Z`.

## Allowed pre-arithmetic inputs

The arithmetic sector may use the following only with their existing typing
and provenance.

1. The source-derived carrier objects and occurrence-resolved incidence
   diagrams already admitted in the graph.
2. Restriction, residue, localization, Gysin, nearby-cycle, monodromy, and
   supported-transform operations with their proved variance and coherence.
3. Finite coproducts, a tensor product, or a tensor unit only where those
   structures have been established on the common calculus rather than
   silently inherited from a chosen coefficient category.
4. Existing exact integral matrices as audit inputs. Their use may falsify a
   proposed Carrier-intrinsic readout, but it does not make their integral
   coefficient ring Carrier-derived.
5. Sector realization functors only when their source, target, support,
   grading, and comparison maps are explicit.

## Forbidden imported arithmetic

The following may not be premises of an arithmetic-emergence argument:

- `N`, `Z`, primes, factorization, valuations, `Spec(Z)`, or an arithmetic
  scheme;
- finite fields, residue fields, a prime-indexed family, arithmetic
  Frobenius, point counts, or a counting measure;
- Euler products, zeta/L-functions, modular forms, Hecke operators, or
  Fourier coefficients;
- a preferred integral/rational/number-field coefficient ring or lattice;
- a rank, dimension, cardinality, or physical readout used to prove that the
  very arithmetic it already presupposes has emerged.

These objects remain legal metalanguage for stating and checking a
falsifier. They become candidate outputs only after the construction that
produces them is typed.

## Candidate internal arithmetic object

### Carrier-only candidate

Suppose the shared calculus supplies, without a coefficient choice, an
essentially small symmetric monoidal category
`U_C` generated by a source-derived unit `1_C` under finite coproduct and
tensor product. Suppose further that tensor distributes over coproduct.
Define

\[
S_C=\pi_0(U_C),
\qquad
[A]+[B]=[A\amalg B],
\qquad
[A][B]=[A\otimes B].
\]

This is a commutative semiring. Multiplication descends because isomorphic
representatives have isomorphic tensor products and distributivity makes the
coproduct relation multiplicative:

\[
(A\amalg B)\otimes C
\simeq
(A\otimes C)\amalg(B\otimes C).
\]

Its additive group completion

\[
R_C=G(S_C)
\]

inherits a commutative ring structure by the universal property of group
completion. This proves multiplication **conditionally**; it does not prove
that the required monoidal category is part of the coefficient-neutral
Carrier.

There is a canonical unit-generated map from the free commutative rig to
`S_C`, and after group completion a characteristic map from the initial ring
to `R_C`. Identifying these maps with isomorphisms requires the unbounded
unit-freeness statement

\[
1_C^{\amalg m}\simeq1_C^{\amalg n}
\quad\Longrightarrow\quad m=n,
\]

together with uniqueness of finite unit decomposition. Neither statement is
currently established. Without it, `S_C` may be a quotient, may fail
cancellation, or may contain additional carrier classes.

### Coefficient-lens candidate

Once a coefficient lens `K` supplies an additive monoidal realization
category `D_K(C)`, there is a less ambiguous ring

\[
R_K=\operatorname{End}_{D_K(C)}(1_K),
\]

with addition from the additive Hom group and multiplication from
composition. This multiplication is automatically well-defined, but the
ring is lens-relative. Existing Laurent, rational, Betti, Kummer, and Tate
examples therefore do not by themselves define `R_C`.

No spectrum should be formed until one of these rings is established with
its dependence on `C` or `K` explicit.

## First finite falsifier: resolution and lattice dependence

Use the six occurrence rows in the order

\[
(12|23),(12|31),(23|31),(23|12),(31|12),(31|23).
\]

Entry 1141's primitive Betti boundary and occurrence-forgetting map are

\[
d_B(1)=(1,1,1,1,1,1)^T,
\qquad
F=
\begin{pmatrix}
1&1&0&0&0&0\\
0&0&1&1&0&0\\
0&0&0&0&1&1
\end{pmatrix}.
\]

The exact Smith data are

\[
\begin{array}{c|c|c}
\text{presentation}&\text{boundary column}&\text{cokernel torsion}\\
\hline
\text{resolved primitive Betti}&(1,1,1,1,1,1)^T&0\\
\text{occurrence-forgotten}&(2,2,2)^T&\mathbb Z/2\\
\text{quarter-enlarged lens}&(4,4,4,4,4,4)^T&\mathbb Z/4
\end{array}
\]

If the forgotten target is silently assigned its primitive generator
`(1,1,1)^T`, the nonprimitive residual is

\[
F d_B-(1,1,1)^T=(1,1,1)^T\ne0.
\]

Thus the naive readout

\[
A(d)=\operatorname{tors}\operatorname{coker}(d)
\]

is not invariant under occurrence forgetting or coefficient-lattice
normalization. The result falsifies any proposal that calls this torsion
Carrier-intrinsic while omitting those choices. It does not falsify the weak
shared-calculus conjecture, and it does not exclude an arithmetic lens that
retains the full typing.

The companion checker reproduces the Smith invariants from Benincasa's
admitted result packets and includes the deliberate-failure residual above:

- `research/grothendieck/checkers/arithmetic_lens_resolution_falsifier.py`;
- `research/grothendieck/results/arithmetic-lens-resolution-falsifier.json`.

Compatibility preflight is fixed at characteristic-zero integral
coefficients, the displayed six-to-three occurrence convention, complex
degree `0 -> 1`, the first-Rees/primitive-Betti comparison stage, and no pole
depth. Input schemas and SHA-256 digests are recorded in the results packet.

## First serious admission test

The proposed serious test is the **unit-generated initial-ring/UFD gate**.

1. Construct `U_C` from source-derived Carrier operations without choosing
   an integral coefficient category, rank, or cardinality functor.
2. Prove tensor distributivity and the semiring/group-completion descent
   above.
3. Prove unit-freeness and unique finite unit decomposition without a finite
   cutoff. Finite checks are discovery evidence only.
4. Derive a decomposition-length norm from that universal construction and
   prove the corresponding division/factorization theorem. Only then may the
   unit-generated ring be identified with the initial ring and its
   irreducibles called primes.
5. Prove invariance under the admitted string and cosmology realization
   functors. If either realization needs an added scalar lattice or
   non-source-derived readout, record the exact entry point and classify the
   arithmetic as lens-relative.

The alternative Euler-product gate is deferred. The graph currently contains
geometric monodromy and finite-field checker specializations, but no
independently derived closed-point object and arithmetic Frobenius. A
dynamical product over primitive carrier orbits would be a dynamical zeta
identity, not yet an arithmetic Euler product.

## Demonstrated strength and scope

- The semiring and ring constructions are conditional categorical
  constructions.
- The matrix obstruction is an exact `source-typed morphism` and
  `physical/readout` falsifier on a finite admitted diagram.
- No unbounded/colimit arithmetic result is claimed.
- No claim is made that `Spec(Z)`, primes, unique factorization, Frobenius,
  an Euler product, or an L-function has emerged.

