# The two-slot residual attachment has a rigged Tate comparison

## Result and scope

The residual-retaining paired comparison has an explicit two-slot test/dual realization. Finite-place responses converge in operator norm with a quantitative cutoff bound. Positive compression, negative leakage, endpoint swap and the two residual cross-terms remain separately labelled.

Letter substitution respects the actual two-seam balancing maps. On the sector with at most two retained forcing slots, including the critical four-event diamond products, the limiting test/response pairing is the prescribed Clark pairing with its nonzero attachment observation.

Two seam factors and two retained feature slots are different counts. This note proves the response estimate for two retained slots, not a uniform theorem over arbitrarily many features in a two-seam record.

Inputs:

- `../grothendieck/the-all-prime-tate-response-converges-in-a-two-sided-weighted-dual.md`;
- `the-residual-port-restores-the-labelled-two-seam-comparison.md`;
- `an-explicit-residual-observer-detects-the-nonzero-attachment-class.md`.

## 1. Declare test and response spaces before tensoring

Fix gamma>1/2. Let H_+^+, H_+^- be the positive/negative half-line restrictions of L2(exp(2 gamma|u|)), and H_-^+, H_-^- their unweighted-pairing duals. Let D^+,D^- be the corresponding unrestricted-trace half-line Sobolev graph spaces. Their traces at zero are independent.

The port input space is

`V=D^+ direct-sum H_+^+`,

with sum norm. Write a port as (u,r), with r the retained window-moment residual, not the Tate leakage.

Use the labelled test space

`Z=D^+ direct-sum D^- direct-sum C^2
       direct-sum H_+^+ direct-sum H_+^+`

and labelled response space

`R=H_-^+ direct-sum H_-^- direct-sum C^2
       direct-sum H_-^+ direct-sum H_-^+`,

both with sum norms. Pair them componentwise using the ORIGINAL unweighted integrals and standard endpoint coordinate pairing. This is a continuous test/response duality with bound one. R embeds into Z^h; it is not asserted to exhaust that continuous dual.

The five labels are positive compression, negative leakage, endpoint response, residual paired against the even test, and even response paired against the residual test.

## 2. The one-slot source graph and response

Let beta_end(u)=(ell_+(u),ell_-(u)) and let J_end be the fixed swap matrix. Define

`E(u,r)=(u,0,beta_end(u),u,r)` in Z,

`R_P(u,r)=(B_P u,-leak_P u,J_end beta_end(u),r,u)` in R,

and define R_infinity by the proved weighted-dual limits B_rig,leak_rig. The minus sign in the leakage component follows from using the negative Tate response in the arithmetic form.

The finite-place comparison gives

`<E(u,r),R_P(v,t)>
 =q_ar,P(u,v)+<u,t>_0+<r,v>_0`.

At the limit this is exactly Q_res. Negative-side tests in Z observe leakage directly. E has zero negative-side component, so its arithmetic source pairing does not observe that component; the response itself still retains it.

The window port substitution remains the FIXED map

`Psi(f)=(U_f,W_f-L_ar U_f)`.

It uses the full convergent half-line L_ar and is not changed with P. At a finite cutoff the pairing differs from the Clark pairing by the finite arithmetic form error. At the limit it agrees exactly. No cutoff-dependent residual has been fitted to force finite-cutoff equality.

## 3. Uniform bounds and the one-slot cutoff error

Let C_A bound all finite and limiting full Tate responses from the piecewise graph domain into H_-. One may take the fixed archimedean graph bound plus twice the convergent prime majorant. Let

`C_beta=sqrt(1/(2 gamma+1)+1/(2 gamma-1))`.

With the chosen sum norms,

`||E||<=C_E=2+C_beta`,

`||R_P||,||R_infinity||<=M=2 C_A+C_beta+1`.

The factor two bounds the sum of the positive and negative response norms. The unchanged cross ports contribute ||u||+||r||.

If P contains every prime <=N, N>=3, put sigma=gamma+1/2 and

`T_N=N^(1-sigma)[log N/(sigma-1)+1/(sigma-1)^2]`.

The supplied positive response error is at most 2T_N and the negative leakage error at most T_N. Hence

`||R_infinity-R_P||_(V->R)<=3 T_N`.

The endpoint and residual cross-ports have zero cutoff error. The archimedean operator is held fixed here; its independently proved regulator error can be added if it too is approximated.

## 4. Projective two-slot tests and continuous-dual responses

Use V tensor_pi V for two-slot inputs and Z tensor_pi Z for tests. Keep the ordered labels, not a symmetrized tensor quotient. The response is first retained in R tensor_pi R, with the canonical evaluation map

`R tensor_pi R -> (Z tensor_pi Z)^h`.

On elementary tensors its pairing is the product of the two one-slot pairings; the projective norm gives a continuous extension with norm at most one. No claim that this map is onto the full dual is needed. The labelled projective response is retained rather than quotienting it by the narrower source test graph E tensor E.

The two-slot response operator is R_P tensor R_P. Its difference from the limit is the exact telescoping identity

`R_infinity tensor R_infinity-R_P tensor R_P
 =(R_infinity-R_P) tensor R_infinity
   +R_P tensor (R_infinity-R_P)`.

Therefore

`||R_infinity^(tensor 2)-R_P^(tensor 2)|| <= 6 M T_N`.

For two different cutoffs with one-slot errors e_1,e_2, the bound is M(e_1+e_2). Both negative-side leakage slots and mixed leakage/other slots converge in this declared response topology.

After applying the source test graph E tensor E, the paired-form error on two port inputs a,b is at most

`6 M C_E^2 T_N ||a||_pi ||b||_pi`.

On compact-spectral forcing inputs the residual-port bound ||Psi||<=C_Psi adds C_Psi^4 to this bilinear bound. Spectral labels may differ in the two slots; the one-slot constants are uniform on the fixed compact set.

Vacuum slots are adjoined as independent unit scalar sectors. They have identity response and zero cutoff error. The same estimates therefore cover words with zero, one or two retained features.

## 5. Actual balancing, not an arbitrary response tensor identification

The maps E Psi and R_P Psi are linear substitutions on each actual forcing letter. Extend them to ordered coefficient words by tensoring, preserving edge labels, endpoints and vacuum. For a permitted artificial-cut normalization N,

`N_test (E Psi)_external=(E Psi)_balanced N`,

`N_response (R_P Psi)_external=(R_P Psi)_balanced N`.

These identities express ordinary word concatenation and reassociation. They hold at each finite P and at the limit. The response tensors are concatenated in their labelled projective record algebra; they are not multiplied as L2 functions or treated as Hilbert-Fock response vectors.

Every zero formal record remains zero under either letter substitution. Thus the original relation and action-balancing kernels are annihilated. The derivative product identities and D2(I^3)=0 survive. No new ideal is defined from a response Gram.

In particular, for two diamond relations with zero or one retained feature apiece, the genuine four-event product and its two-seam realization have at most two retained slots. Their source-balanced images satisfy the displayed comparison, with all memory/seam multipliers unchanged. Finite nonminimal comparisons with at most two retained slots satisfy it as well.

The limiting paired observation is the same Q_res tensor pairing already shown to equal the original labelled Clark packet. Hence the previously constructed nonzero residual-sensitive attachment observer retains its nonzero value. This is a two-slot paired realization of that witness, not a new assertion of projectivity of the completed target.

## 6. Preserve all labels and the topology boundary

The response has five one-slot labels and their ordered two-slot combinations. In particular:

- negative-side leakage is present even though the positive source graph cannot test it;
- endpoint swap remains correlated with the same u;
- the window residual r is neither leakage nor an adjustable subtraction;
- no two independently prepared root states are multiplied.

If Fourier transport is desired, use the supplied dual Fourier map F_- on H_- responses and its tensor evaluation. Ordinary L2 Fourier transformation is not asserted for responses known only to lie in H_-.

The theorem excluding ordinary-L2 endpoint-subtracted leakage on nonzero finite Euler packets remains intact. None of these tensor bounds improves the response topology to L2 or removes its zero-pole obstruction.

## 7. Disposition

Closed: a declared two-slot projective test/dual comparison, quantitative prime-cutoff convergence, labelled leakage retention, and compatibility with the actual two-seam balancing maps on the at-most-two-feature sector.

Still separate: uniform summation over all retained feature counts in this rigged response construction, angular sectors, unweighted operator equivalence, and completed perfect-module duality. The source arithmetic-only even-port identity remains insufficient for arbitrary windows; the residual is retained throughout.

## Verification

`uv run --with sympy python research/nima/checkers/check_two_slot_rigged_response.py`

The checker verifies signed labelled response pairing, direct negative-side leakage detection, tensor telescoping, the cutoff majorant derivative, and actual balanced product comparisons with at most two retained slots. Its finite matrices are algebraic fixtures, not sampled Tate multipliers or Clark spectra.
