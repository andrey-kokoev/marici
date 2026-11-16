# Native boundary selection, Fourier null directions, and the quadratic square relation

Date: 2026-10-30  
Pinned source: `andrey-kokoev/marici@cb0c25477b0b710fc1feb9dd5cc1e82e8ecdef6c`  
Status: executed native tests; exact algebraic counterexamples and conditional constructions. No shell-energy, spin, neutron-count, or stability law is derived.

## 1. Question and result

The preceding work constructed a transport-compatible contraction on the four-dimensional mean-zero part of the native five-coefficient carrier. Its degree-k harmonic sector has dimension `(k+1)^2`. The present question is whether native boundary/admission rules select that sector rather than merely preserve it.

**The current rules do not select it.** Native geometry/contact/exit admission does not depend on coefficient values. The spectral constructor admits common and non-common branches and arbitrary finite complex context coefficients. Its explicitly assumed identity boundary returns every admitted input, rather than filtering them.

There is a nontrivial partial mechanism already in the source: the non-common Fourier inputs, when the two context coefficients are zero, are mean-zero and null for the complex bilinear coefficient pairing. Their symmetric powers are therefore harmonic. But their entire permutation orbit gives only twenty projective directions. The coherent-power span has dimensions

`1, 4, 9, 16, 20, 20, 20, ...`,

not `1, 4, 9, 16, 25, 36, 49, ...`. The first mismatch persists even if **every** permutation of the five coefficients is allowed, a larger class than proved native reachability.

A precise additional boundary law would repair the algebraic selection: after removing mean dependence, impose the quadratic relation `q=0`. Over the complex numbers this is equivalent to the determinant relation on a 2-by-2 square, `z00*z11 = z01*z10`. Its graded coordinate ring has dimension `(k+1)^2` in degree k. This is a mathematically defined completion, not a law derived from the current native grammar.

## 2. Scope, execution, and provenance

Ten upstream modules were copied unchanged from the retained source archive. Their Git blob hashes were verified against the pinned manifest. There were no repository writes or changes to the native rules.

The Node test rebuilt all complete packets reachable through eight operations for all 24 root markings. Charts, species, geometry aliases, absolute origins, and all five coefficient permutations were retained. This is a bounded packet exploration, not an enumeration of all occupied assemblies.

| Executed check | Result |
|---|---:|
| Source blobs verified | 10 |
| Root markings | 24 |
| Complete packets visited | 2,752 |
| Native transfers validated | 3,888 |
| Explicit coefficient transport checks | 15,552 |
| Direct PN/NE exit-certified paths | 24 |
| Boundary trials: 24 markings, 3 branches, 3 context choices | 216 passed |
| Full five-coordinate permutation orbit of one Fourier vector | 60 vectors |
| Distinct projective Fourier directions | 20 |
| Independent missing harmonic quartics | 5 |
| Exact vanishing checks for missing quartics on Fourier directions | 100 |
| Conditional full-null-cone spanning tests | degrees 0–6 |
| Harmonic projection checks | all 70 monomials through degree 4 |
| Projected-product associativity checks | 64 triples of linear generators |

Native floating-point spectral reconstruction is only a supplemental test; its maximum error was about `1.99e-15`. The boundary return was exactly unchanged in those numeric trials. Orbit ranks and polynomial identities were calculated separately using exact rational or algebraic-number arithmetic, not floating-point rank tolerances.

The code uses Node.js 22.16.0, Python 3.13.5, and SymPy 1.14.0 in this environment. Exact computations use `Q`, `Q(omega)` with `omega^2+omega+1=0`, and `Q(i)`.

## 3. Definitions and the distinction between a coefficient and an observable

For a coefficient vector `a` in `C^5`, write

\[
\mu(a)=\frac15\sum_{j=0}^{4}a_j,
\qquad C=I_5-\frac15\mathbf1\mathbf1^T,
\qquad q(a)=a^TCa.
\]

The mean-zero sector is `U={a : sum a_j=0}`. Its dimension is four. Every native coefficient permutation preserves the mean and q.

The polynomial contraction on coefficient **observables**, with independent variables c, is

\[
D=\sum_{i,j}C_{ij}\partial_{c_i}\partial_{c_j}.
\]

For a specified coefficient vector a, consider the proposed symmetric-power encoding

\[
F_{a,k}(c)=(a^Tc)^k.
\]

This encoding is an explicit observable construction; it is not itself a new native reader operation. Direct differentiation gives

\[
\left(\sum_i\partial_{c_i}\right)F_{a,k}
 =k\left(\sum_i a_i\right)(a^Tc)^{k-1},
\]

\[
D F_{a,k}=k(k-1)q(a)(a^Tc)^{k-2}.
\]

Thus mean-zero, bilinearly null a give mean-independent harmonic powers. This does **not** assert that every polynomial observable on an admitted coefficient carrier is harmonic.

Nullity here is complex bilinear: `a^T a=0` on U. It is not a zero Hermitian norm. For nonzero real a in U, `q(a)>0`, so this nonzero null construction needs complex coefficients, which the native API already permits. It is not a physical energy condition.

## 4. The existing admission and boundary do not impose the condition

### 4.1 Source-level separation

`GenerativeAssemblyRules.describe` checks occupied species, C/M roles, and face compatibility. `inspect` checks selected contact witnesses and exit reachability. Neither predicate receives a coefficient vector or polynomial observable. Therefore, for any certified packet support in this grammar, those predicates cannot distinguish coefficient values by mean or quadratic norm. This is a source-level all-depth observation, not a conclusion extrapolated from the finite traversal.

`applyPhasePermutation` accepts arbitrary finite five-slot complex vectors. `spectralReadout` retains all three Fourier components, together with the two complementary coefficients. It does not project away the common branch.

`createDeuteriumTunnel` is a more specialized input constructor, but it explicitly admits all three branch labels and arbitrary finite complex complements. The source calls its cycle boundary `canonical-identity-hypothesis` and constructs it as the inverse of the preceding within-cycle transport. This is an assumed identification, not a derived physical boundary. Consequently, its round trip is the identity on the full carrier.

### 4.2 Exact admitted counterexamples

Let `omega=exp(2*pi*i/3)`. The normalized positive active triple is `(1,omega,omega^2)/sqrt(3)`.

| Allowed input | Mean | Bilinear contrast q | Native geometry and identity-boundary return |
|---|---:|---:|---|
| Positive branch, context `(0,0)` | 0 | 0 | Accepted |
| Positive branch, context `(1,-1)` | 0 | 2 | Accepted |
| Common branch, context `(0,0)` | `sqrt(3)/5` | `2/5` | Accepted |

The second input is decisive: even choosing a non-common active branch and zero total mean does not force q=0 when the retained context is allowed to vary. Its degree-two coherent observable has `D F=4`, rather than zero.

The invariant observable `q(c)` itself satisfies `Dq=8`. Mean dependence is also retained and measurable. No native exit/contact predicate removes either of them.

### 4.3 A stronger local filter would remove valid signals

An alternative would require the common Fourier component to vanish at every local readout. This is not what the code does. It also fails as a repair.

For the positive seed `(1,omega,omega^2,0,0)`, the first P reader advance uses permutation `(2,3,0,1,4)`. Its newly active triple has sum `omega^2+1=-omega`, which is nonzero. The full five-vector still has zero mean and q=0. Local common suppression and global mean removal are different conditions.

The exact matrix of all active-triple sums observed through depth eight has rank five in the eight winding-compatible markings. Imposing all of those local conditions would force the entire carrier to zero. The other sixteen markings give rank two in this bounded test, leaving dimension three, not the desired four-mode sector. No unbounded rank claim is made for that second class.

## 5. The Fourier input supplies genuine harmonic candidates

Ignoring normalization, let

\[
a_+=(1,\omega,\omega^2,0,0),
\qquad a_-=(1,\omega^2,\omega,0,0).
\]

The identities `1+omega+omega^2=0` give

\[
\sum_i (a_\pm)_i=0,\qquad
 a_\pm^Ta_\pm=0,\qquad
 a_+^Ta_-=3.
\]

Both inputs therefore produce harmonic powers in the proposed encoding, and permutations preserve this property. Their Hermitian norm squared is three before normalization.

Ordinary multiplication is still not closed on this family: `D[(a_+^Tc)(a_-^Tc)]=6` in this unnormalized convention. Taking linear superpositions of coefficient seeds and then taking powers is likewise not automatically harmonic, because the null cone is not a vector subspace.

The general theorem that homogeneous harmonic polynomials are spanned by powers of isotropic linear forms is established mathematics; Canino and Flavi discuss exactly this construction in *Isotropic Rank of Harmonic Polynomials* [1]. Our test concerns whether the finite set supplied by the native Fourier/permutation mechanism is sufficient.

## 6. Exact finite-orbit obstruction

### 6.1 A generous all-depth coefficient bound

Every native coefficient transfer in the inspected grammar is a permutation of five retained entries. Starting from a fixed pure Fourier seed, no sequence of such operations can leave its S5 orbit. Permitting all 120 permutations is a generous bound; this is not a claim that S5 is a native holonomy group or that origins can be identified.

The seed has three distinct nonzero entries and two zeros, giving 60 distinct coefficient vectors. Multiplication by omega cycles its nonzero entries and identifies triples of vectors as scalar-proportional directions. There are therefore 20 projective directions.

At any fixed degree k, each direction supplies one coherent power up to scalar. Its span is thus at most twenty-dimensional at every degree. Absolute origins and alternative histories remain distinct, but they do not produce new coefficient directions in this encoding.

Exact ranks over `Q(omega)` are:

| k | Full four-mode harmonic dimension | Span of all S5 Fourier powers |
|---:|---:|---:|
| 0 | 1 | 1 |
| 1 | 4 | 4 |
| 2 | 9 | 9 |
| 3 | 16 | 16 |
| 4 | 25 | 20 |
| 5 | 36 | 20 |
| 6 | 49 | 20 |
| 7 | 64 | 20 |

The saturation is not merely inferred from the table. Rank twenty in degree four means evaluation on the twenty points is surjective. Multiplication by a linear form nonzero on all twenty points preserves surjectivity in every higher degree. A form with five distinct real coordinate weights has this property for these Fourier points. Hence rank twenty holds at every k>=4.

The negative branch lies in the same full projective orbit as the positive branch: swapping its second and third entries exchanges them. The two Fourier branches therefore do not supply two independent copies of the completed harmonic space or a derived spin factor.

### 6.2 Actual bounded native families are smaller

Including both non-common entry branches, the depth-eight native packet families give:

| Root-marking class | Number of markings | Distinct projective directions | Ranks at k=0,...,6 |
|---|---:|---:|---|
| Winding-compatible | 8 | 14 | `1,4,9,13,14,14,14` |
| Other markings | 16 | 8 | `1,4,7,8,8,8,8` |

These rows are bounded observations. The full twenty-direction obstruction above remains valid independently of how many more native charts or origins become reachable later.

No two distinct directions in the twenty-point set have zero bilinear pairing. Consequently, an ordinary nontrivial sum of two distinct seed directions is not null. A simple two-seed superposition cannot supply a continuous null family while preserving q=0. This is another limitation of this specific finite seed set, not a prohibition of more general superpositions or new boundary laws.

### 6.3 Five explicit missing quartics

The rank loss has a structural witness. Work on U, so `sum c_i=0`, and put `q=sum c_i^2`. For i=0,...,4 define

\[
h_i(c)=\prod_{j\ne i}c_j+\frac{q c_i^2}{40}-\frac{q^2}{100}.
\]

Each h_i is harmonic for the four-mode contraction. Indeed,

\[
D\prod_{j\ne i}c_j=-\frac25 c_i^2+\frac15q,
\]

\[
D(qc_i^2)=16c_i^2+\frac85q,\qquad D(q^2)=24q,
\]

so `D h_i=0`.

Every Fourier direction has q=0 and only three nonzero coordinates. Therefore all five h_i vanish on every one of the twenty directions. Their coefficient matrix has rank five. Under the Fischer pairing, evaluation at a is proportional to pairing with `(a^Tc)^4`. The orbit is closed under complex conjugation, so these are also orthogonal to its span for the positive Hermitian Fischer pairing. Directly appending the five quartics to the twenty coherent-power coefficient rows gives rank 25, verifying that they supply precisely the missing directions. Exact code also verifies all 100 vanishing evaluations.

This explains why a test restricted to degrees two and three would have falsely accepted the generous permutation completion.

## 7. A precise conditional completion: one quadratic square relation

The result suggests a concrete extension rather than another numerical fit. On the mean-zero carrier, consider the **full complex null cone**

\[
\mathcal Q=\{a\in U_{\mathbb C}:q(a)=0\}.
\]

It includes the native Fourier directions but is not restricted to their finite permutation orbit. Existing permutations preserve it, so imposing it at entry would be transport-compatible. The present source does not impose it or provide all of its entries through its pure-branch constructor.

There are two equivalent algebraic formulations of the proposed completion.

1. Allow coherent powers of every null direction and their linear spans. This spans the whole harmonic space in each degree [1].
2. Use polynomial functions on the quadric, namely the graded quotient

\[
\mathcal B=\mathbb C[U]/(q).
\]

The relation q is a nonzero quadratic polynomial. Multiplication by q is injective in the polynomial ring, hence

\[
\dim\mathcal B_k=\binom{k+3}{3}-\binom{k+1}{3}=(k+1)^2.
\]

This is a consequence of the specified relation, not a neutron or shell count entered into the generator. It remains conditional on selecting that relation.

### 7.1 The relation is a 2-by-2 determinant

In complex orthonormal contrast coordinates z0,...,z3, define

\[
M(z)=
\begin{pmatrix}
z_0+i z_1&z_2+i z_3\\
-z_2+i z_3&z_0-i z_1
\end{pmatrix}.
\]

Then

\[
\det M=z_0^2+z_1^2+z_2^2+z_3^2=q(z).
\]

Thus the null constraint is the rank-one square relation

\[
z_{00}z_{11}=z_{01}z_{10}.
\]

A rank-one matrix factors as `M=s t^T`. Its four entries are the pairwise products of two two-component factors. Projectively, this is the Segre quadric `P^1 x P^1` [2]. Homogeneous degree k in the entries corresponds to bidegree `(k,k)` in the two factors. Each factor supplies k+1 monomials, so the product has `(k+1)^2` dimensions.

This is an exact algebraic relationship to the earlier two-path comparison grid. It does not establish that a native occupied square enforces this determinant, nor that the matrix factors are physical spinors, P/E particles, or two independent copies. Factor exchange is an involution, not an automatic doubling of the vector-space dimension.

### 7.2 Conditional spanning test

A dense affine patch is given by

\[
M=\begin{pmatrix}1&t\\r&rt\end{pmatrix},
\qquad
z=\left(\frac{1+rt}{2},\frac{1-rt}{2i},\frac{t-r}{2},\frac{r+t}{2i}\right).
\]

It satisfies q=0 exactly. Taking `r,t=0,...,k` and calculating the ranks of the resulting degree-k powers over `Q(i)` gives

`1,4,9,16,25,36,49`

for degrees zero through six. These are explicitly **constructed non-native test inputs**. The all-degree statement follows from the Segre/Fischer arguments, not from extrapolation of this finite check.

## 8. Product closure and harmonic representatives

Harmonic polynomials are not closed under ordinary multiplication. Nevertheless, the graded quotient `C[U]/(q)` is an associative algebra. The Fischer decomposition gives a unique harmonic representative of each homogeneous quotient class [3]. Consequently,

\[
h\star g=\mathcal H_{k+\ell}(hg),\qquad h\in H_k,
\quad g\in H_\ell,
\]

is an associative commutative graded product on the direct sum of harmonic spaces. It is the quotient product expressed in harmonic representatives. It is not the ordinary product that the native scalar readout algebra originally supplied.

For homogeneous f of degree k in four variables, the projection is

\[
\mathcal H_k f=\sum_{j=0}^{\lfloor k/2\rfloor}a_jq^jD^jf,
\quad a_0=1,
\quad a_j=-\frac{a_{j-1}}{2j(2k-2j+2)}.
\]

For degree four this is `f-q Df/16+q^2 D^2f/384`. The code checks harmonicity, idempotence, and equality modulo q on all monomials through degree four, plus 64 associativity identities on triples of linear generators. General associativity follows from quotient multiplication.

The source does not already identify q with zero: for example, the admitted positive-branch input with contexts `(1,-1)` has q=2. The quotient therefore changes the observable model or restricts its admissible inputs; it cannot be described as merely re-expressing every current readout.

A unit-norm boundary `q=1` would be a different, filtered construction, not the homogeneous null constraint tested here. Likewise the source's Hermitian normalization is not the bilinear equation q=0. These alternatives must not be conflated.

## 9. Conclusion and the next required native law

The boundary-selection test gives both a partial mechanism and an explicit obstruction:

- A source-defined non-common Fourier input with zero context gives a mean-zero null direction, whose symmetric powers are harmonic.
- Current native admission and the assumed identity boundary also admit nonzero-mean and non-null inputs. They do not select that family.
- Permutation transport of the fixed Fourier seeds cannot generate the full harmonic spaces: even the generous S5 completion misses five modes at degree four and is bounded by twenty in every degree.
- A single quadratic relation on the already mean-zero sector, equivalent to a rank-one 2-by-2 comparison square, would provide a product-compatible completion with the squared dimensions.

The next genuinely new requirement is a **coefficient-dependent boundary/comparison rule selecting the full quadratic relation**, or an independently justified quotient identifying its multiples. More traversal depth cannot supply this missing rule in an amplitude-independent admission grammar. Its proposed form is explicit; whether it follows from a strengthened native composition principle remains unproved.

No identification of the defect with an additional neutron is established. The extra factor two, physical state interpretation, angular-momentum action, shell-energy ordering, nuclear magic numbers, and neutron excess remain separate.

## 10. Reproduction

From the accompanying archive root:

```sh
node run/check_boundary.mjs 8
python run/analyze_boundary.py
```

Python requires SymPy. All input paths are relative to the scripts; the source snapshot and manifest are bundled. The native generator and the exact algebraic analyzer are separate programs.

Primary outputs:

- `run/boundary_results.json`: complete bounded packets, validated transfers, admitted boundary trials, and spectral numerical checks.
- `run/exact_results.json`: exact orbit ranks, local-common constraints, admitted counterexamples, missing quartics, conditional quadric tests, and product checks.
- `run/analysis_log.txt`: exact analyzer execution log.
- `SHA256.json`: bundle integrity manifest.

## References

1. Stefano Canino and Cosimo Flavi, *Isotropic Rank of Harmonic Polynomials*, arXiv:2512.05195v1, submitted December 4, 2025. https://arxiv.org/html/2512.05195v1 . This supplies the standard isotropic-power spanning theorem, not evidence for the native boundary selection.
2. The Stacks Project, Lemma 27.13.6, *Segre embedding*. https://stacks.math.columbia.edu/tag/01WD . For two two-component factors, the displayed determinant calculation gives the quadric equation directly.
3. Sheldon Axler and Wade Ramey, *Harmonic Polynomials and Dirichlet-Type Problems*, Proceedings of the American Mathematical Society 123 (1995), 3765–3773. Author page: https://www.axler.net/HarmonicPolynomials.html . See also Axler, Gorkin, and Voss, *The Dirichlet Problem on Quadratic Surfaces*, https://www.axler.net/QuadraticDirichlet.html, for Fischer-type decompositions.
4. The Stacks Project, Section 10.13, *Tensor algebra*. https://stacks.math.columbia.edu/tag/00DM . This supplies the standard symmetric-algebra terminology; the choice of an observable algebra is explicit here.
5. Native pinned source: https://github.com/andrey-kokoev/marici/blob/cb0c25477b0b710fc1feb9dd5cc1e82e8ecdef6c/research/strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs ; spectral inputs and boundary: `deuterium-tunnel-model.mjs`, active readouts and phase permutations: `phase-advance-model.mjs`, in the same directory. The bundled ten-module manifest records their exact Git blob hashes.

The finite ranks, admitted counterexamples, missing-quartic witnesses, and native traversal results in this note are original computations recorded in the accompanying receipts. Literature references do not certify the proposed native-to-physical interpretation.
