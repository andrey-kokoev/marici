# Fourier transform from coherent translation: finite and locally compact theorem

## Theorem and foundations

Let G be a second-countable locally compact abelian group, with additive notation and a fixed nonzero Haar measure dx. Let X=N(BG) be its topological group nerve, interpreted as a simplicial topological space. Write

\[
\widehat G=\operatorname{Hom}_{\rm cont}(G,U(1))
\]

with the compact-open topology. There is a unique Haar measure dχ on G-hat for which character evaluation

\[
\mathcal F f(\chi)=\widehat f(\chi)
=\int_G f(x)\overline{\chi(x)}\,dx
\]

extends from C_c(G) to a unitary map L²(G,dx) → L²(G-hat,dχ). It satisfies:

1. The push-pull composition of X linearizes to convolution.
2. The scalar continuous unitary coherent realizations of X are the characters.
3. F(f*h)=F(f)F(h) for f,h∈L¹(G).
4. F(f*)(χ)=overline(F(f)(χ)), where f*(x)=overline(f(-x)).
5. If f∈L¹(G) and F(f)∈L¹(G-hat), then
   \[
   f(x)=\int_{\widehat G}\widehat f(\chi)\chi(x)\,d\chi
   \]
   almost everywhere; the right side is the continuous representative of f.
6. Plancherel and its polarized identity hold on L².
7. Product translation systems yield partial Fourier transforms that commute on their common L² domain, with the product of the dual Haar measures.

The finite abelian Fourier transform is the counting-measure case of this theorem.

The proof uses the following foundational results, in their standard independent formulations:

- existence and uniqueness of Haar measure;
- Pontryagin duality: G-hat is locally compact abelian, evaluation identifies G with its bidual, and characters separate points;
- Bochner's theorem: every continuous positive-definite function on G is uniquely the Fourier–Stieltjes transform of a finite positive measure on G-hat;
- density of C_c in L^p for p<∞, approximate identities, Fubini–Tonelli, and the monotone-class theorem.

Bochner's theorem includes uniqueness of the representing measure. Neither Fourier inversion nor Plancherel is used as an input below. Pontryagin duality and Bochner are the substantive harmonic-analysis foundations on top of the coherence construction. Standard sources include Rudin, *Fourier Analysis on Groups*, and Folland, *A Course in Abstract Harmonic Analysis*.

## 1. The translation coherence object

There is one object in BG, and its morphisms are G. Thus

\[
X_n=G^n.
\]

The interior face maps add adjacent translations, outer faces omit an endpoint translation, and degeneracies insert 0. The Segal maps are homeomorphisms

\[
X_n\cong X_1\times_{X_0}\cdots\times_{X_0}X_1.
\]

Every polygonal membrane reconstructs the same composable string. Consequently X is unital 2-Segal. The long edge of (g₁,…,gₙ) is their sum; all parenthesizations agree.

This model uses strict simplicial topological groups and strict realization maps. In the terminology of decomposition spaces, completeness of a degeneracy means a homotopy-monomorphism condition. That extra condition is unnecessary here and is not asserted for every topological G. Likewise, topological nerve and classifying-space realization play distinct roles: the Fourier construction uses the topology of the individual spaces Gⁿ.

## 2. Haar linearization of the composition correspondence

The binary correspondence is

\[
G\times G\xleftarrow{\mathrm{id}}G\times G
\xrightarrow{m}G,\qquad m(a,b)=a+b.
\]

Its fibers are parametrized by a↦(a,x−a). Haar integration along these fibers sends f⊗h to

\[
(f*h)(x)=\int_G f(a)h(x-a)\,da.
\]

For C_c inputs this is a continuous compactly supported function. It extends to L¹ inputs, with

\[
\|f*h\|_1\le\|f\|_1\|h\|_1.
\]

For three inputs, the two composition correspondences both integrate over

\[
a+b+c=x.
\]

Fubini identifies the two resulting integrals. This is the analytic image of the quadrilateral 2-Segal comparison. The same argument gives every higher parenthesization comparison.

The precise linearization used here consists of these multiplication correspondences and their iterates, with the specified Haar fiber measures. A functor on an unrestricted category of topological spans is unnecessary.

The unit is δ₀ in the measure convolution algebra M(G). For nondiscrete G it acts as a multiplier of L¹(G); approximate identities implement it inside L¹(G). This keeps the degeneracy and its analytical realization correctly typed.

## 3. Classification of scalar realizations

A scalar continuous unitary realization is a continuous map χ:G→U(1) preserving the unit and composition:

\[
\chi(0)=1,\qquad \chi(a+b)=\chi(a)\chi(b).
\]

Equivalently, it is a strict continuous functor BG→BU(1). It evaluates a history as

\[
\prod_j\chi(g_j)=\chi\left(\sum_jg_j\right).
\]

Thus all the coherent history comparisons are preserved, and the set of these realizations is precisely G-hat.

Conjugation permutes these realizations. Simultaneous integration against the conjugate realizations defines F above. Here “universal character evaluation” means exactly this family of all scalar unitary realizations, with its compact-open parameter topology; it is not a claim that every higher representation is scalar.

For each χ, evaluation is a bounded multiplicative functional on L¹(G). Directly, by Fubini,

\[
\begin{aligned}
\widehat{f*h}(\chi)
&=\int_{G^2}f(a)h(b)\overline{\chi(a+b)}\,da\,db\\
&=\widehat f(\chi)\widehat h(\chi).
\end{aligned}
\]

The bound |F(f)(χ)|≤||f||₁ follows immediately. Dominated convergence gives continuity in χ. Inversion of translations gives χ(−x)=overline(χ(x)), and substitution gives F(f*)=overline(F(f)). These statements require no dual Haar normalization.

## 4. Constructing the dual measure from positive coherent histories

We now derive the measure needed for inversion and Plancherel.

For f∈C_c(G), let

\[
c_f(x)=(f*f^*)(x)=\int_G f(y)\overline{f(y-x)}\,dy.
\]

This function is continuous and positive definite: each finite positive-definiteness test is the squared L² norm of a finite linear combination of translates of f. Also c_f(0)=||f||₂². Bochner's theorem gives a unique finite positive measure μ_f such that

\[
c_f(x)=\int_{\widehat G}\chi(x)\,d\mu_f(\chi),
\qquad \mu_f(\widehat G)=\|f\|_2^2.
\]

For f,h∈C_c, associativity yields

\[
c_{h*f}=h*h^**c_f.
\]

Insert the Bochner representation and apply Fubini (μ_f is finite and h*h* is integrable). Uniqueness in Bochner's theorem gives

\[
\boxed{\mu_{h*f}=|\widehat h|^2\mu_f.}
\]

Commutativity then gives the compatibility identity

\[
|\widehat h|^2\mu_f=|\widehat f|^2\mu_h.\tag{1}
\]

For each f define U_f={χ: F(f)(χ)≠0}. These open sets cover G-hat. Indeed, given χ₀, choose a nonnegative ψ∈C_c with integral 1 and set f(x)=χ₀(x)ψ(x); then F(f)(χ₀)=1.

On U_f put

\[
d\nu=|\widehat f|^{-2}d\mu_f.
\]

Equation (1) makes these local definitions agree on overlaps. They therefore define a Radon measure ν on G-hat. Local finiteness follows by choosing a neighborhood where |F(f)| is bounded below. Second countability permits a countable covering by such neighborhoods.

We must also check μ_f on the zero set of F(f). On any U_h, equation (1) gives

\[
d\mu_f=\frac{|\widehat f|^2}{|\widehat h|^2}\,d\mu_h.
\]

Thus μ_f vanishes on that zero set, and globally

\[
\boxed{d\mu_f=|\widehat f|^2d\nu,\qquad
\int|\widehat f|^2d\nu=\|f\|_2^2.}\tag{2}
\]

### Translation invariance of ν

For η∈G-hat define M_η f(x)=η(x)f(x). Then

\[
c_{M_\eta f}(x)=\eta(x)c_f(x),
\qquad
\widehat{M_\eta f}(\chi)=\widehat f(\chi\eta^{-1}).
\]

Bochner uniqueness identifies μ_{M_η f} as the translate of μ_f by η. Dividing on the nonzero-character charts shows that ν is translation invariant. It is nonzero by (2), so ν is Haar measure. Set dχ=dν.

Its normalization is unique: every other Haar measure is cν, and (2) for any nonzero f forces c=1.

This constructs the dual Haar normalization from the positive-definite autocorrelation and compatibility of convolution.

## 5. Isometry and completeness of the character realization

Polarizing (2) gives, for f,h∈C_c(G),

\[
\int_G f\overline h\,dx
=\int_{\widehat G}\widehat f\,\overline{\widehat h}\,d\chi.
\tag{3}
\]

Density extends F uniquely to an isometry

\[
U:L^2(G)\longrightarrow L^2(\widehat G).
\]

We prove its surjectivity explicitly.

Let H be its closed range. For h∈C_c, convolution by h is bounded on L², and the convolution theorem implies that H is invariant under multiplication by F(h). Since F(h*)=overline(F(h)), H is also invariant under the adjoint multiplier. Hence the orthogonal projection P_H commutes with all these multipliers.

The functions F(h), h∈C_c, separate points of G-hat: if χ≠η, the continuous functions overline(χ) and overline(η) differ on an open set, and integration against a suitably supported C_c function detects that difference. They also vanish nowhere jointly, as shown above.

A countable subfamily separates points, using second countability (choose separating functions on a countable subcover of the off-diagonal in G-hat×G-hat). By the standard Borel embedding theorem its functions generate the Borel σ-algebra. The bounded functional calculus and monotone-class theorem therefore imply that P_H commutes with multiplication by every bounded measurable function.

For a σ-finite measure space, a projection commuting with all scalar multipliers is multiplication by an indicator 1_E. One proof restricts to sets of finite measure, applies the projection to their indicator functions, and uses commutation with smaller-set indicators to recover a single measurable multiplier; projection and self-adjointness make its values 0 or 1. Thus H=L²(E).

Every F(h) belongs to H and vanishes almost everywhere on Eᶜ. A countable collection of nonvanishing charts U_h covers G-hat. Consequently Eᶜ has measure zero. Therefore

\[
\boxed{U:L^2(G)\simeq L^2(\widehat G)}
\]

is unitary. Equation (3) now holds for all L² inputs, with transforms understood through completion.

### Agreement with the integral transform

For f∈L¹∩L² choose f_n∈C_c converging to f simultaneously in L¹ and L². The integral transforms converge uniformly to F(f), while U f_n converges in L² to U f. An almost-everywhere convergent subsequence identifies U f with F(f). Hence the unitary extension agrees with the original integral on its natural joint domain.

## 6. Inversion

First let f∈L¹∩L² and F(f)∈L¹. Define

\[
v(x)=\int_{\widehat G}\widehat f(\chi)\chi(x)\,d\chi.
\]

This is bounded and continuous. For h∈C_c, Fubini and (3) give

\[
\int_G v(x)\overline{h(x)}\,dx
=\int_{\widehat G}\widehat f(\chi)
  \overline{\widehat h(\chi)}\,d\chi
=\int_G f(x)\overline{h(x)}\,dx.
\]

Testing against C_c shows v=f almost everywhere.

Now let f∈L¹ and F(f)∈L¹. Choose a nonnegative C_c approximate identity e_n with integral 1 and supports shrinking to 0. Each f*e_n lies in L¹∩L² by Young's inequality. Moreover

\[
\widehat{f*e_n}=\widehat f\,\widehat e_n,
\quad |\widehat e_n|\le1,
\quad \widehat e_n(\chi)\to1.
\]

The previous case applies. Dominated convergence makes their inverse integrals converge uniformly to v, while f*e_n→f in L¹. Passing to an almost-everywhere convergent subsequence gives v=f almost everywhere.

Finally, the inverse unitary operator has the positive-character kernel on its integral domain. If q∈L¹(G-hat)∩L²(G-hat), define

\[
Vq(x)=\int_{\widehat G}q(\chi)\chi(x)\,d\chi.
\]

Testing against h∈C_c and using Cauchy–Schwarz plus Plancherel gives

\[
\left|\int_G Vq\,\overline h\right|
\le\|q\|_2\|h\|_2.
\]

The Riesz representation theorem identifies this locally integrable function with an L² function, and the same pairing identifies it as U* q. Density gives V=U⁻¹ on all L² in the completed sense.

## 7. Product systems and nested composition

For G×H, characters are uniquely pairs (χ,η), with

\[
(\chi,\eta)(x,y)=\chi(x)\eta(y).
\]

The product of the separately constructed dual Haar measures satisfies (2) on simple tensors, hence is the uniquely normalized dual measure of G×H. For f⊗h,

\[
\mathcal F_{G\times H}(f\otimes h)
=\mathcal F_G f\otimes\mathcal F_H h.
\]

Fubini extends the pointwise statement to L¹ and density extends the tensor identity to L². Thus the two partial transforms commute as unitary operators between the corresponding mixed-domain L² spaces.

This is the product-translation instance of compatible composition in two directions. An iterated Waldhausen S-construction has additional exact-diagram structure; identifying its specific directions with these translation actions requires a realization functor.

## 8. Classical Euclidean kernel

For G=Rᵈ, every continuous unitary character is

\[
\chi_\xi(x)=e^{i x\cdot\xi}.
\]

To see this, lift a character on a sufficiently small interval of each coordinate axis through the covering R→U(1). Local additivity and continuity force a linear lift. The homomorphism law extends it globally. Characters on the product are products of these coordinate characters.

Thus

\[
\widehat f(\xi)=\int_{\mathbb R^d}f(x)e^{-ix\cdot\xi}\,dx.
\]

Translation invariance makes the dual measure c dξ. Its constant follows from the Gaussian, without using Fourier inversion. In dimension one, differentiating the absolutely convergent Gaussian integral and integrating by parts gives

\[
\int_{\mathbb R}e^{-x^2/2}e^{-ix\xi}\,dx
=\sqrt{2\pi}\,e^{-\xi^2/2}.
\]

Taking products and applying (2) to the Gaussian forces c=(2π)⁻ᵈ. Consequently

\[
f(x)=(2\pi)^{-d}\int_{\mathbb R^d}\widehat f(\xi)e^{ix\cdot\xi}\,d\xi,
\]

on the inversion domain. The unitary transform with Lebesgue measure on both sides is (2π)⁻ᵈ⁄² F. This fixes the exponential sign and normalization completely.

## 9. Finite groups

For finite G use counting measure. Every character is continuous, and |G-hat|=|G| by the finite abelian group decomposition. A nontrivial character θ has sum zero: translation by an a with θ(a)≠1 multiplies the sum by θ(a). Applying this both to G and its dual gives

\[
\sum_{\chi\in\widehat G}\chi(g-a)=|G|\delta_{g,a}.
\]

Therefore the dual Haar measure assigns mass 1/|G| to each character, and

\[
\widehat f(\chi)=\sum_g f(g)\overline{\chi(g)},
\quad
f(g)=\frac1{|G|}\sum_\chi\widehat f(\chi)\chi(g).
\]

The same orthogonality proves the polarized Plancherel formula directly. The finite proof is elementary and independent of the Bochner construction.

## 10. Relation to the nested closure language

The proof constructs a translation realization of coherent cutting and joining. Its specific mathematical carrier is N(BG), whose stronger Segal property supplies the required 2-Segal comparisons. Fourier evaluation uses the resulting composition algebra and the complete family of its scalar unitary realizations.

The nested stable-category model X_n=(S_n(C))^core has its own cofiber-based closure structure. Applying this theorem there requires a source-specified map to a translation convolution system, preserving the relevant compositions, and a compatible measure and dagger realization. This note proves the full Fourier theorem for the translation realization. It records that adapter as a distinct construction for any particular nested source.

The information content is also precise. Fourier transformation is unitary and invertible on the linearized L² carrier. Information loss, when present, occurs in the earlier passage from resolved histories to their net-translation function: distinct histories can share one translation. The subsequent Fourier coordinates retain that function completely.

## 11. Fourier decomposition of the nested stable closure object

There is an explicit realization inside the iterated S-construction for finite abelian G. Work over C and take

\[
\mathcal C_G=\operatorname{Perf}(\mathbb C[G]).
\]

Define the central idempotents

\[
p_\chi=\frac1{|G|}\sum_{g\in G}\overline{\chi(g)}\,\delta_g.
\]

Character orthogonality and δ_a δ_b=δ_(a+b) give

\[
p_\chi p_\eta=\delta_{\chi,\eta}p_\chi,
\qquad \sum_\chi p_\chi=1,
\qquad \delta_g p_\chi=\chi(g)p_\chi.
\]

For example, the coefficient of δ_t in p_χ p_η is

\[
\frac{\overline{\eta(t)}}{|G|^2}
\sum_a\overline{\chi(a)}\eta(a),
\]

which is the asserted orthogonality formula. Thus every perfect complex M splits functorially as

\[
M\simeq\bigoplus_{\chi\in\widehat G}p_\chi M.
\]

Differentials and module maps preserve these summands. Conversely, a finite family of perfect complex vector spaces becomes a G-module complex by making g act as χ(g) on its χ-summand. These constructions are inverse exact equivalences:

\[
\boxed{\mathcal C_G\simeq
\prod_{\chi\in\widehat G}\operatorname{Perf}(\mathbb C).}
\tag{4}
\]

An exact equivalence preserves the zero objects and bicartesian squares that define S_n. Finite products of stable categories compute these structures componentwise. Hence (4) induces, for every finite nesting depth r and all flag lengths,

\[
S_{n_1}\cdots S_{n_r}(\mathcal C_G)
\simeq
\prod_{\chi\in\widehat G}
S_{n_1}\cdots S_{n_r}(\operatorname{Perf}(\mathbb C)).
\tag{5}
\]

Taking cores gives the equivalence of nested closure spaces. It commutes with every restriction of interval diagrams, every face and degeneracy, every cut-change equivalence, and the interchange comparisons, since these are all constructed from the same exact diagrams and their limits or colimits. Thus Fourier decomposition preserves the entire finite nested closure system in this realization.

For an element a=Σ_g f(g)δ_g, its action on the χ-summand is the scalar

\[
\lambda_\chi(a)=\sum_g f(g)\chi(g)=\widehat f(\bar\chi).
\]

Relabelling summands by conjugate characters gives exactly the Fourier convention of the theorem. This realizes the ordinary finite transform as the coefficient-level shadow of an exact equivalence of nested stable closure systems.

The complex-linear, translation-equipped category C_G is specified here as part of the construction. For a different stable category, a G-action and a compatible linear realization supply the input for the corresponding decomposition. For locally compact G the L² theorem above supplies the regular-representation spectral decomposition; extending (5) to a chosen category of measurable fields and analytical complexes additionally requires its declared domain and exactness conventions.

## Verification status

This is a mathematical proof using the explicitly named foundational theorems. It is not a proof-assistant artifact. The finite checker supplies floating-point regression tests for cyclic and product groups; it is supplementary to the proof. No bounded numerical test is used to establish the locally compact theorem.
