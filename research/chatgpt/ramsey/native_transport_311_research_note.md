# Full native 3+1+1 transport: product compatibility, contraction, and four-mode harmonics

Date: 2026-10-30  
Source snapshot: `andrey-kokoev/marici@cb0c25477b0b710fc1feb9dd5cc1e82e8ecdef6c`  
Status: exact algebraic constructions, executed bounded native checks, and explicit counterexamples. No physical shell spectrum, spin multiplicity, neutron number, or stability law is derived.

## Result

The complete five-slot coefficient carrier admits a geometrically defined decomposition into a mean, three affine-gradient coefficients, and one affine-defect coefficient. The resulting full transport extends to products of coefficient observables without losing information.

The three-gradient part is not autonomous. Its isotropic contraction is not preserved. A contraction on the four-dimensional mean-zero coefficient sector is preserved, using the standard coefficient pairing. This operator is distinct from the spatial-coordinate Laplacian reconstructed from geometric stencils in the preceding note.

The compatible four-mode harmonic spaces have dimensions `(k+1)^2`. Their ordinary three-coordinate branching contains the sectors of dimensions `1,3,...,2k+1`, each once. With `n=k+1`, an independently supplied doubling would give `2n^2`. Neither the doubling nor selection of these harmonic spaces as physical states follows from the native grammar.

An additional test addresses actual spatial functions rather than polynomials in coefficient modes. The natural five-dimensional spatial lift spanned by `1,x,y,z,|x|^2` is unisolvent on the five native reference positions, but its native PN action fails to preserve the relation `|x|^2=x^2+y^2+z^2`. Consequently, that linear lift does not extend to an algebra homomorphism on spatial polynomials. The failure occurs for all 24 root markings.

## 1. Scope and reproducibility

All ten upstream source modules were copied without edits. Their Git blob hashes were checked against the pinned manifest. The new Node program regenerated every complete packet reachable within eight operations for each of the 24 root markings. Complete charts, species, coefficient permutations, absolute origins, and all geometric aliases were retained. The E chart's additional geometric context M2 is retained in the raw records; it is not silently introduced as a sixth coefficient.

The experiment is an exhaustive bounded packet traversal, not an enumeration of all occupied or exit-certified assemblies. Each local transfer was checked by the original native validator.

| Check | Executed result |
|---|---:|
| Root markings | 24 |
| Maximum operation depth | 8 |
| Complete packets | 2,752 |
| Native transfers | 3,888 |
| Full coordinate intertwining | 3,888 passed |
| Cumulative transport/composition | 3,888 passed |
| Mean preservation | 3,888 passed |
| Full coefficient metric | 3,888 passed |
| Four-mode contraction covariance | 3,888 passed |
| Pure isotropic three-gradient contraction covariance | 0 passed; 3,888 failed |
| Transfers mixing gradients and defect | 3,888 |
| Distinct numerical transport/metric triples | 64 |
| Quadratic and cubic product checks on those triples | 3,200 passed |
| Independent quadratic and cubic contraction checks | 3,200 passed |
| Four-mode harmonic ranks and branching bases | degrees 0 through 6 passed |
| First-PN radial spatial-lift product test | failed for all 24 markings |

Numerical transport triples were cached for polynomial checks only. This does not identify their reader states, origins, charts, or histories. The exact matrix identities below establish the corresponding arbitrary-degree statements independently of the finite polynomial tests.

Executed software: Node.js 22.16.0; Python 3.13.5; SymPy 1.14.0.

## 2. The geometrically defined 3+1+1 coordinates

Let `c` be the column of five native coefficients, ordered by the retained slots. The first five historical reference positions are denoted `C0,M0,C1,M1,C2`; these bindings are used to define a coordinate decomposition, not assumed to be literal scalar samples after transport.

For a chart p, embed its five positions in the already supplied Euclidean three-space. Let X_p be the 5-by-3 matrix of centered positions. Let l_p be the unique affine circuit, normalized by its C0 coefficient being +1. In the tested native chart family,

\[
\mathbf1^T X_p=0,\qquad l_p^T X_p=0,\qquad
\mathbf1^T l_p=0,\qquad l_p^T l_p=4.
\]

Set

\[
B_p=[\mathbf1\;X_p\;l_p],\qquad
z_p=B_p^{-1}c=(\mu,g_x,g_y,g_z,d)^T.
\]

Thus

\[
c=\mu\mathbf1+X_p g+d l_p,
\qquad \mu=\frac15\mathbf1^Tc,
\qquad d=\frac14l_p^Tc.
\]

Here g is the least-squares affine gradient of the five coefficient values in this chart, and d records their failure to be affine samples. These are coordinates on the coefficient carrier, not additional occupied P/N/E bodies.

For the canonical chart,

\[
l=(1,-1,0,-1,1)^T,
\qquad d=(c_0-c_1-c_3+c_4)/4.
\]

Its gradient Gram matrix is

\[
A=X^TX=\frac15
\begin{pmatrix}6&3&1\\3&14&3\\1&3&6\end{pmatrix},
\qquad \operatorname{spec}(A)=\{1,1,16/5\}.
\]

The supplied coefficient norm becomes

\[
c^Tc=5\mu^2+g^TAg+4d^2.
\]

For complex amplitudes the corresponding norm is Hermitian. The real rational matrices in this experiment also extend algebraically to complex coefficients; that extension does not turn a bilinear differential trace into a Hermitian norm operator.

## 3. Exact full transport and products

A native edge p to q carries a five-coordinate permutation matrix P, with `c_q=P c_p`. Define

\[
T_{qp}=B_q^{-1}PB_p.
\]

Then

\[
z_q=T_{qp}z_p,\qquad B_qT_{qp}=PB_p.
\]

For composable edges the B matrices cancel. If Pi_p denotes the complete root-to-packet permutation,

\[
L_p=B_p^{-1}\Pi_pB_0,
\qquad T_{qp}L_p=L_q.
\]

This identity uses the complete packet permutation. Absolute origin remains a separate retained coordinate, with its original increment rule. Repeated matrices do not equate complete readers with different origins.

For polynomial coefficient observables, pullback is ordinary substitution:

\[
T_{qp}^*f(z_p)=f(T_{qp}z_p).
\]

It obeys

\[
T^*(fg)=(T^*f)(T^*g)
\]

at every degree. This is the symmetric-algebra extension of the invertible degree-one map. It concerns products of scalar-valued observables; it does not make native path histories commute.

The mean is preserved, and the four-dimensional contrast sector is invariant:

\[
U=\{c:\mathbf1^Tc=0\},\qquad P(U)=U.
\]

The three-gradient sector inside U generally is not invariant. The all-edge test found mixing for every tested transfer, including PN, inverse-PN, NE, and both kinds of phase advance. This does not exclude arbitrarily chosen packet-dependent transported three-planes; it excludes autonomy of this specified geometric gradient sector.

## 4. Why the spatial three-mode contraction fails

In the canonical 3+1+1 basis, PN is

\[
T_{PN}=\begin{pmatrix}
1&0&0&0&0\\
0&1/4&-3/4&0&-3/2\\
0&-1/4&3/4&0&-1/2\\
0&1/4&1/4&1&1/2\\
0&-1/2&-1/2&0&0
\end{pmatrix}.
\]

In particular,

\[
d'=-\frac12(g_x+g_y).
\]

Consider the candidate gradient contraction

\[
Q_{\rm grad}=\partial_{g_x}^2+\partial_{g_y}^2+\partial_{g_z}^2.
\]

For the target observable `f=(d')^2`,

\[
Q_{{\rm grad},p}(T^*f)=1,
\qquad T^*(Q_{{\rm grad},q}f)=0.
\]

So covariance already fails at degree two on the first PN edge.

Adding only an independent scalar second derivative does not repair it while leaving an isotropic gradient block. Solving

\[
T_{PN}\,\operatorname{diag}(0,a,a,a,b)\,T_{PN}^T
=\operatorname{diag}(0,a,a,a,b)
\]

gives only `a=b=0`. A compatible nonzero contraction must change more than the scalar coefficient in these unnormalized gradient coordinates.

This calculation is on coefficient observables. It is not a claim that the variables g and the earlier ambient position variables x are identical. The actual spatial-function test below treats that separate identification directly.

## 5. A compatible four-mode contraction

Let

\[
C=I_5-\frac15\mathbf1\mathbf1^T.
\]

This is the orthogonal projector onto U using the standard coefficient pairing. Every native coefficient permutation preserves it. Define

\[
K_p=B_p^{-1}CB_p^{-T},
\qquad
D_p=\sum_{i,j}(K_p)_{ij}\partial_{z_i}\partial_{z_j}.
\]

The exact identity

\[
T_{qp}K_pT_{qp}^T=K_q
\]

implies, by the chain rule,

\[
D_pT_{qp}^*=T_{qp}^*D_q.
\]

This is an all-degree statement for every transfer for which the chart basis is defined. It does not rely on the depth-eight experiment as an extrapolation.

In 3+1+1 coordinates,

\[
K_p=\operatorname{diag}\left(0,(X_p^TX_p)^{-1},\frac14\right).
\]

For the canonical chart its nonzero 4-by-4 block is

\[
\begin{pmatrix}
15/16&-3/16&-1/16&0\\
-3/16&7/16&-3/16&0\\
-1/16&-3/16&15/16&0\\
0&0&0&1/4
\end{pmatrix}.
\]

For the same `d^2` witness, both sides of the covariance equation are now `1/2`.

With normalized coordinates

\[
u=(X_p^TX_p)^{1/2}g,\qquad s=2d,
\]

the contrast norm and contraction become

\[
\rho^2=|u|^2+s^2,
\qquad D=\partial_{u_1}^2+\partial_{u_2}^2+\partial_{u_3}^2+\partial_s^2.
\]

Thus the full construction supports a four-mode Euclidean trace. It uses the standard coefficient pairing already compatible with the declared spectral normalization. It is not the previous spatial-stencil Laplacian: both its variables and its metric construction are different. The square circuit supplies the distinguished defect coordinate; the circuit by itself does not select this metric or differential operator.

The normalized transfers are orthogonal on these four modes. This does not prove that continuous SO(4) is generated by native reader operations, or that coefficient-space rotations are physical spatial rotations.

## 6. Four-mode harmonic dimensions and the earlier squared sequence

Restrict attention to polynomial observables independent of the mean. The full five-generator algebra is still retained as

\[
\mathcal A=\mathbb R[\mu]\otimes\mathbb R[u_1,u_2,u_3,s].
\]

Mean-independence is a specified invariant sector, not a claim that the measured mean is an unobservable gauge direction.

For homogeneous polynomials of degree k in the four contrast coordinates, define

\[
\mathcal H_k^{(4)}=\ker\left(D:\operatorname{Sym}^k(U^*)
\longrightarrow\operatorname{Sym}^{k-2}(U^*)\right).
\]

The nondegenerate Euclidean trace is surjective in characteristic zero. Therefore

\[
\dim\mathcal H_k^{(4)}
=\binom{k+3}{3}-\binom{k+1}{3}=(k+1)^2.
\]

| Degree k | All four-mode monomials | Trace rank | Harmonic dimension | Two independent copies |
|---:|---:|---:|---:|---:|
| 0 | 1 | 0 | 1 | 2 |
| 1 | 4 | 0 | 4 | 8 |
| 2 | 10 | 1 | 9 | 18 |
| 3 | 20 | 4 | 16 | 32 |
| 4 | 35 | 10 | 25 | 50 |
| 5 | 56 | 20 | 36 | 72 |
| 6 | 84 | 35 | 49 | 98 |

The last column is arithmetic conditional on an additional independent two-dimensional multiplicity. No spin representation or such multiplicity was generated in this test. Identifying `n=k+1` with a physical principal shell index also requires a state and energy interpretation.

The harmonic condition is preserved by the new transport, but native admission has not been shown to require it. Preservation of a subspace is not its selection. Also, harmonic polynomials do not form a subalgebra under ordinary multiplication: `D(u_1)=0` but `D(u_1^2)=2`. Product closure belongs to the full observable algebra; the harmonic spaces are invariant linear subspaces within it.

If dependence on the mean is counted as well, the degree-k harmonic dimension becomes the sum of the contrast dimensions from zero to k: `1,5,14,30,55,91,140,...`. Thus `(k+1)^2` specifically refers to the mean-independent sector.

### Explicit three-coordinate branching

For the standard subgroup rotating u while fixing s,

\[
\mathcal H_k^{(4)}\downarrow SO(3)
\cong\bigoplus_{\ell=0}^{k}\mathcal H_\ell^{(3)}.
\]

Consequently,

\[
(k+1)^2=\sum_{\ell=0}^k(2\ell+1).
\]

This is the standard hyperspherical-harmonic branching identity, not a new shell law. The experiment constructs a complete independent polynomial basis through k=6, rather than checking only the dimensions.

For any three-variable harmonic homogeneous h_l(u), put m=k-l and construct

\[
H_{k,l}=h_l(u)\sum_{j=0}^{\lfloor m/2\rfloor}
a_j|u|^{2j}s^{m-2j},\qquad a_0=1,
\]

with

\[
a_{j+1}=-a_j\frac{(m-2j)(m-2j-1)}{2(j+1)(2l+2j+3)}.
\]

Direct differentiation gives `D H_(k,l)=0`. At degree two the nine basis directions split into five spatial traceless quadratics, three products `s u_i`, and the scalar `3s^2-|u|^2`. At degree three the dimensions are `7+5+3+1=16`.

These are mode-space representation statements. Equating the chosen SO(3) subgroup with physical angular momentum is a further requirement.

### Real and complex amplitude qualification

For real coefficients, fixing the mean and a nonzero contrast norm gives a three-sphere inside the four-dimensional contrast space. Native permutations preserve this leaf. The source, however, permits complex coefficients. At fixed complex mean and Hermitian contrast norm the corresponding real sphere is S7, not S3. A physical reduction to real contrasts, or a different complex state construction, must not be silently assumed. The four-variable polynomial dimension formula still holds over the complex field, but a complex bilinear harmonic trace is not the same as the real Laplacian associated with the full Hermitian norm.

## 7. Actual spatial functions: the product obstruction

The prior failure of affine interpolation suggests retaining the defect as a radial quadratic rather than discarding it. Test the spatial function space

\[
L=\operatorname{span}\{1,x,y,z,r^2\},\qquad r^2=x^2+y^2+z^2.
\]

Evaluation on the five native marked positions is invertible, so every five-coefficient vector has a unique representative in L. This is a geometrically specified replacement for the failed affine-only lift.

For the canonical chart, transport by PN followed by interpolation induces the linear map

\[
\Phi(1)=1,\qquad
\Phi(x)=\tfrac34-y-r^2,\qquad
\Phi(y)=\tfrac34-x-r^2,\qquad
\Phi(z)=z,\qquad
\Phi(r^2)=r^2.
\]

It is an involution on the five-dimensional linear space L. It is not an algebra homomorphism on spatial polynomials. Such a homomorphism would have to preserve

\[
\Phi(r^2)=\Phi(x)^2+\Phi(y)^2+\Phi(z)^2.
\]

The right-hand side contains `2 r^4`; the left-hand side has degree two. The exact relation defect is stored in the receipt. For each of the other markings, the corresponding quartic coefficient is also nonzero.

Spatial harmonicity fails even before this product extension. The native barycentric affine sample has representative

\[
f=\tfrac14+\tfrac12(x+y+z),\qquad \Delta_x f=0.
\]

After canonical PN it becomes

\[
\Phi(f)=1-r^2-\tfrac12x-\tfrac12y+\tfrac12z,
\qquad \Delta_x\Phi(f)=-6.
\]

This excludes the specified affine-plus-radial scalar-field lift and its product extension. It is not a theorem excluding every nonlinear, nonlocal, vector-valued, or constrained-state observable map.

## 8. What has changed

The full native observable transport and its product extension are now explicit and verified. The geometric three-gradient sector fails, but the mean-zero four-mode sector has a compatible trace and harmonic decomposition.

This establishes a conditional route to the squared multiplicity of one half of the original triangular construction. It does not derive the electron shell law, the nuclear magic sequence, neutron excess, or any energy functional. The factor two, interpretation of harmonic degree, selection of mean-independent harmonics, and treatment of complex amplitudes remain separate questions.

The next decisive test is whether native boundary/admissibility data select this four-mode harmonic sector, rather than simply allowing its construction. An energy or boundary operator must act on the actual coefficient carrier and specify why traces or mean dependence are excluded. Relabeling the extra scalar as a neutron would not supply that rule.

## Reproduce

From the archive root:

```sh
node run/generate_packets.mjs 8
python run/analyze_transport.py
```

The Python script requires SymPy. It uses exact integer/rational linear algebra. All paths are relative to the scripts. The upstream modules are unmodified.

Main receipts:

- `run/packets.json`: freshly generated complete native records and transfers.
- `run/exact_results.json`: transport, polynomial, metric, counterexample, rank, and branching tests.
- `run/python_log.txt`: execution output.
- `SHA256.json`: integrity hashes of bundled files.

## References and provenance

New transport matrices, scalar-lift counterexamples, and exact checks are original computations in this archive. Standard facts are compared against these primary sources:

1. The Stacks Project, Section 10.13, *Tensor algebra*, definitions of symmetric algebras and polynomial algebras: https://stacks.math.columbia.edu/tag/00DM
2. J. K. Mason and C. A. Schuh, *Expressing Crystallographic Textures through the Orientation Distribution Function: Conversion between Generalized Spherical Harmonic and Hyperspherical Harmonic Expansions*, Metallurgical and Materials Transactions A 40 (2009), 2590–2602, Section IV, Eq. (10) and following index/dimension discussion: https://doi.org/10.1007/s11661-009-9936-8 . This reference supplies the standard hyperspherical mathematics, not a Marici or atomic-physics identification.
3. Sheldon Axler and Wade Ramey, *Harmonic Polynomials and Dirichlet-Type Problems*, Proceedings of the AMS 123 (1995), 3765–3773, author overview: https://axler.net/HarmonicPolynomials.html
4. Native generator and validator: https://github.com/andrey-kokoev/marici/blob/cb0c25477b0b710fc1feb9dd5cc1e82e8ecdef6c/research/strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs
5. Native coefficient transport and spectral readout: `phase-advance-model.mjs` and `deuterium-tunnel-model.mjs` in the same pinned source directory.
6. Preceding local research note: `native_observable_algebra_research_note.md`, dated 2026-10-30. This note preserves its distinction between geometric stencil operators and coefficient observables.
