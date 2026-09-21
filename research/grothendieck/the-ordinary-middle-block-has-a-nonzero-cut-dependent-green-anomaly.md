# The ordinary middle block has a nonzero cut-dependent Green anomaly

## Result and theorem strength

**Finite-cutoff source comparison and analytical obstruction.** The ordinary degree-zero part of the six-prime common block complex has an injective uncompressed seam realization. However, absorbing its middle record into the left coarse seam or into the right coarse seam does NOT preserve the same full spectral Green packet.

An explicit cross-term is zero on the common carrier and on the right coarse carrier, but on the left it is

4 w_memory K_(g,h)(w,z),

where g and h are specified nonzero event-window combinations. This function of the two spectral arguments is not identically zero for the actual normalized Clark feature carrier. Nonvanishing follows from a Fourier-uniqueness argument, not from a numerical spectral rank or a freely selected Gram matrix.

The shifted 720-channel paired comparison remains valid. The obstruction is localized to the ordinary middle-block grade allocation; it neither determines nor contradicts Nima's critical product self-pairing scalars.

## 1. Keep the ordinary common carrier before compression

Use the common complex H from the six-prime associativity cell. Its degree-zero part is

H^0=direct_sum R_1 tensor B_2 tensor R_3,

of dimension 2160. Here the three two-event blocks and both middle vertices are retained. B_2 is the endpoint terminal quotient of the middle two-event source, not a new scalar index.

Let C_1,C_3 be the local seam complexes of the first and last blocks, and let R_middle be the prescribed typed memory carrier at the middle endpoints, at common capacity N>=6. Form

M=direct_sum C_1 tensor R_middle tensor C_3.

The middle carrier is in cohomological degree zero. M has bottom degree -2. The ordinary common observation is the cycle map

j_0:H^0 -> M[-2]^0,

j_0(a tensor [w] tensor c)=D(a) tensor rho(w) tensor D(c).

It is well-defined and injective: both local relation derivatives are injective, B_2 embeds in its actual terminal records, and all partition labels remain separate. The existing signature-closed memory envelopes supply the ambient pairing; no form is fitted to H^0.

The prepared root carrier is an additional single external factor, retained throughout. The explicit falsifier below uses its vacuum to exhibit failure; this does not replace the state-dependent general construction by a universal vacuum map.

## 2. The two coarse multiplication maps

There are source-derived chain maps kappa_L and kappa_R. The first concatenates the middle record onto the suffix memory of the first seam. The second concatenates it onto the prefix memory of the last seam. Typed endpoints determine these multiplications, and the common capacity avoids overflow on these admitted source templates.

Their source formulas follow from the derivative product rule:

D(a w)=D(a) rho(w),

D(w c)=rho(w) D(c),

because rho(a)=rho(c)=0.

Thus kappa_L j_0 and kappa_R j_0 are precisely the ordinary observations of the two coarse groupings. The chain maps preserve the source comparison; that statement does not say that either preserves the prescribed tensor Green form.

## 3. A two-vector falsifier in the ordinary common cell

Choose successive prime pairs (p,q), (r,s), (t,u), starting at the root x. Let l be the endpoint after p,q and m the endpoint after r,s.

Write a_0,a_1 for the forgotten and one-retained local relations in the first block, and c_0 for the forgotten relation in the last block. Let w_1 be the middle route that retains its first event r and forgets its second event s. Let w_0 be the same route with both events forgotten.

The two common vectors are

A=a_0 tensor [w_1] tensor c_0,

B=a_1 tensor [w_0] tensor c_0.

Their retained feature allocations are respectively (0,1,0) and (1,0,0). On the uncompressed common tensor carrier these allocations are orthogonal, so q_M(j_0 A,j_0 B)=0.

On the right coarse carrier, the first factor still pairs D(a_0) with D(a_1). Their distinct retained degrees are orthogonal. Hence the right coarse pairing is also zero.

On the left coarse carrier, the middle feature has moved into the suffix memory of D(a_0). It can now pair with the suffix-memory terms of D(a_1). Only the two first-edge Omega terms match in type and memory shape. The last forgotten cycle contributes its norm 4. Therefore the full spectral pairing is exactly

q_L(A(w),B(z))=4 w_memory K_(g,h)(w,z),

where

g=g_(l,l+r),

h=g_(x+p,l)+g_(x+q,l).

Both features are nonzero compact positive-half-line window forcings. The coefficient 4 comes from the last forgotten diamond. The weight is the degree-one MEMORY weight, tau^2 in the weighted convention. No seam-feature weight occurs in this cross-term, since both matching seam letters are Omega.

The signs in the reversed route occur in both paired arguments and multiply to plus. In arbitrary feature Gram coordinates the residual is the same expression; no chamber orthogonality is assumed.

## 4. Correct port normalization

The four raw traces of a compact forcing f are

h_f(z)=(h_(+,0),h_(-,0),h_(+,1),h_(-,1)).

Let A_Cl be the fixed two-by-four normalized sewing matrix, and put hhat_f=A_Cl h_f. The actual two-sheet signature is J=diag(1,-1). The raw four-port coefficient is

C_raw=A_Cl^* J A_Cl.

It has rank two. It is not an invertible four-dimensional fundamental symmetry. The nondegenerate ambient paired envelope uses the normalized two-sheet carrier and its J-closure.

The earlier shifted-pairing note has been corrected to distinguish these objects. The exact checker verifies the fixed sewing matrix, the rank of C_raw, and J squared equals identity.

The kernel in section 3 is

K_(g,h)(w,z)=hhat_g(w)^* J hhat_h(z) / [-i(z-conjugate(w))]

             =h_g(w)^* C_raw h_h(z) / [-i(z-conjugate(w))].

This preserves the actual normalization and the pairwise spectral denominator.

## 5. Four-trace span lemma: actual analytical nonvanishing

Let f be a nonzero integrable compact forcing supported in an interval strictly inside the positive half-line, nonzero on a set of positive measure. The four scalar entire functions comprising h_f are linearly independent.

Indeed, a constant linear relation among them is the Fourier transform of a density consisting of

(alpha+beta x) f(x) on the positive support,

and the reflected density with another linear polynomial on the negative support.

If that transform vanishes on an open spectral region, entire continuation makes it vanish everywhere. Fourier uniqueness gives zero density. The positive and negative supports are disjoint, so each polynomial times f vanishes separately. A nonzero linear polynomial cannot vanish on a set of positive measure. All four coefficients are therefore zero.

Equivalently, the vectors h_f(z), with z in any nonempty open spectral region, span the raw four-port space. Since A_Cl has full row rank, hhat_f(z) spans the two-sheet space.

Apply this first to h: there exists z with hhat_h(z) nonzero. Since J is invertible and hhat_g(w) spans the two-sheet space, there exists w with

hhat_g(w)^* J hhat_h(z) nonzero.

The upper-half-plane denominator never vanishes. Thus K_(g,h) is not identically zero on the prescribed spectral region squared.

This proves an analytical failure of equality of the FULL spectral packets. It does not claim that a particular diagonal integral is nonzero: an integrated scalar could hide this mismatch, which is precisely why the spectral indices must be retained.

The same span argument also verifies injectivity of the normalized function-valued feature on finite chamber combinations: a nonzero shell forcing cannot have identically zero sewn two-sheet amplitude. It does not furnish a uniform quantitative lower bound as the packet grows.

## 6. Relation to the critical product Gram theorem

Nima's critical product formula is

Gamma_local=diag(4,gamma_local),

gamma_local=(w_memory+w_seam) sum_e q_W(g_e,g_e),

followed by labelled tensor products. That theorem concerns products of local RELATION cycles, retaining each block separately.

The present ordinary vector instead has a terminal record in the middle block. Concatenating that record moves a feature between previously independent grade allocations and produces the displayed cross-term. There is no contradiction with the diagonal critical product Gram formula.

In particular this result says nothing about the sign or vanishing of any integrated gamma_local. Function-valued injectivity and the nonzero cross-spectral anomaly do not establish positivity of a restricted relation form.

## 7. What can still be transported canonically

Retain the cut-dependent pulled-back packets

Q_L=(kappa_L j_0)^* q_L (kappa_L j_0),

Q_R=(kappa_R j_0)^* q_R (kappa_R j_0),

and the nonzero relative packet Delta_LR=Q_L-Q_R. These are derived from the same independent source operations and prescribed forms. Their difference is not a new adjustable metric parameter.

If further cuts are added, differences of these existing pulled-back packets obey the telescoping identity Delta_LR+Delta_RU=Delta_LU wherever all are defined on the same common carrier. That elementary coboundary identity does not make Delta_LR vanish or prove descent to a compressed carrier. Do not add independent triangle parameters for it.

At the integrated finite Hilbert-observation level there is also a natural correspondence. Let O_L and O_R be the conjugate-dual observations on the ordinary source image, using the prescribed ambient beta maps. Both are surjective, because the two ordinary source-image maps are injective and the ambient forms are nondegenerate. Define

Obs_LR={(y_L,y_R):O_L(y_L)=O_R(y_R)}.

Its two projections are surjective. Its quotient by the two observation kernels is the conjugate dual of the ordinary common source space. This uses annihilators of the specified source image, not an invented nondegenerate self-form on that image.

This correspondence matches integrated linear observations. It is NOT asserted to repair the entire spectral packet anomaly, nor to supply a canonical isometry or a unique lift between the two coarse carriers. The full pairwise-indexed Delta_LR must still be retained.

## 8. Localized conclusion and next gate

Closed:

- an injective uncompressed ordinary common seam realization;
- the source-derived coarse multiplication maps;
- an explicit ordinary-sector cross-term discrepancy;
- proof that its actual full spectral kernel is nonzero;
- the distinction between normalized two-sheet signature and raw four-port coefficient.

Still open: a source-admitted relative sewing or counterterm construction that retains this cut-dependent spectral packet while matching the desired complete comparison. It cannot be replaced by a claim that the two coarse Green forms are already the same. Completion and global positivity remain separate.

The shifted-product paired theorem survives unchanged after the port-notation correction. The ordinary 2160-coordinate sector has not been declared radical, and the counterexample proves why discarding its cut/grade allocation would be invalid.

## Verification

`uv run --with sympy python research/grothendieck/checkers/check_ordinary_middle_block_green_obstruction.py`

The checker reruns the exact source comparison, differentiates the actual selected relations, verifies the residual with independent formal Gram entries, and rejects equality of the two compressed forms. A positive-coordinate fixture gives common=0, left=-8, right=0; those fixture values are not actual Clark spectral evaluations. Analytical nonvanishing is the proof in section 5.

It also checks the actual fixed port-sewing ranks and an algebraic observer correspondence with unequal pulled-back forms.

References:

- `research/nima/the-critical-joint-seam-green-form-reduces-to-local-function-valued-pairings.md`;
- `the-six-prime-associativity-cell-retains-the-derived-middle-block.md`;
- `the-six-prime-shifted-attachment-has-a-function-valued-paired-comparison.md`;
- `research/voevodsky/clark-source-interface-domain-and-positivity-audit.md`;
- `research/voevodsky/function-valued-clark-faithfulness-supersedes-finite-spectral-rank-probes.md`.
