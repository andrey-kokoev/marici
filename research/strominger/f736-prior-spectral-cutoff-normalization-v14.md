# Prior spectral normalization and common-domain Tate compression

## Fresh source discovery

Read completely:

- `research/voevodsky/the-trivial-sector-arithmetic-form-is-a-tate-compression-with-explicit-leakage.md`;
- `research/voevodsky/unitary-fourier-transport-rescales-the-gamma-tail-by-two-pi.md`;
- `research/voevodsky/normalized-source-formula-family-mismatch-audit.md`;
- `research/voevodsky/endpoint-gamma-prime-normalization-audit.md`.

Also inspected the source convention and trace-theorem sections of `research/voevodsky/connes-semilocal-theorem-4-realizes-finite-place-weil-terms-as-the-finite-part-of-a-product-cutoff-trace-not-a-positive-trace.md` and the characterwise Tate scattering note.

No tests, checkers or certifications were run. The comparison below retains the differing test families, sign conventions and publication-authority qualifications.

## 1. Independently frozen Tate multiplier

The trivial-sector compression paper fixes the even branch

    gamma_infinity(t)
      =pi^(it) Gamma(1/4-it/2)/Gamma(1/4+it/2),

and the self-adjoint logarithmic connection convention

    a_infinity(t)=-i partial_t log gamma_infinity(t)
      =log(pi)-Re psi(1/4+it/2).

For a finite prime set P it fixes

    a_p(t)=2 log(p) sum_(k>=1) p^(-k/2) cos(k t log p),
    a_P=a_infinity+sum_(p in P) a_p.

The operator A_P is maximal multiplication by a_P. These are independently specified symbols: their signs are not chosen afterward to force agreement with a target arithmetic form.

This resolves a concrete convention choice for the intended spectral coordinate. The often displayed positive gamma expression d(t)=Re psi(1/4+it/2)-log pi is MINUS a_infinity, not the same symbol.

## 2. Actual common-domain comparison already proved

The paper uses a weighted half-line source D_gamma=H1(R_plus,exp(2 gamma u)du), gamma>1/2, with unrestricted boundary trace. Its map is

    U=unitary_Fourier o zero_extension.

For source v in D_gamma, integration by parts gives O(1/|t|) spectral decay with a source graph-norm bound. Because a_P grows only logarithmically, U maps D_gamma continuously into the MAXIMAL OPERATOR domain of A_P, not only a formal distributional pairing domain.

The theorem then proves on that domain

    q_regular,P(v,w)=-<Uv,A_P Uw>.

The negative sign is essential. The complete arithmetic form adds its source endpoint swap:

    q_arithmetic,P(v,w)
      =-<Uv,A_P Uw> + beta(v)* J_end beta(w),
    J_end=[[0,1],[1,0]].

The source is correlated: both Fourier and endpoint coordinates come from the same v. No endpoint state is fitted independently.

This is a source-defined operator-domain/form comparison. It is more concrete than the generic source-chart equality previously used as context.

## 3. The endpoint names and divisor normalization differ across notes

The compression paper names its half-line endpoint integrals with ell_plus attached to exp(-u/2) and ell_minus to exp(+u/2). The frozen Strominger convention m_h(t)=integral h(u)exp(-itu)du assigns plus i/2 to exp(+u/2). Thus the ORDERED endpoint labels are exchanged between those conventions.

The symmetric swap form J_end is invariant under exchanging its two labels, but separately retained channels are not. The F736 binding must carry the permutation explicitly.

The compact-support half-divisor source formula has gamma multiplier d/2 and endpoint contribution Re(L_plus conjugate(L_minus)). The full symmetrized arithmetic formula above uses d=-a_infinity and the full swap form, which is twice that endpoint expression on the diagonal. Its prime symbol likewise contains twice the half-divisor coefficient.

Consequently, on a genuinely common compact half-line test subcore and with matching finite prime/support truncations, the displayed normalization dictionaries are consistent with a full-form versus half-divisor factor TWO. This is a scoped formula comparison, not permission to transfer constants between unrelated test families or to identify an entire semilocal trace convention from one coefficient.

Keep the full source/convolution, Fourier measure, endpoint permutation and prime multiplicity conventions together when performing the actual match.

## 4. Independent 2pi correction is explicitly documented

The unitary-Fourier correction distinguishes

    Fv(t)=integral v(u)exp(-itu)du,
    Fourier_unitary(v)=(2pi)^(-1/2)Fv.

Therefore

    (1/(4pi)) integral d(t)|Fv(t)|^2 dt
      =(1/2) integral d(t)|Fourier_unitary(v)(t)|^2 dt.

The unitary multiplier is d/2, NOT d/(4pi). The paper explicitly supersedes numerical tail/dimension scouts using the smaller scale. Those old numbers should not be imported as normalization evidence.

This is a different issue from full versus half-divisor normalization: one is a Plancherel measure conversion, the other is the overall source-form/multiplicity convention.

## 5. Compression is NOT invariant intertwining: leakage is explicit

The common-domain paper defines the negative-side leakage of the full-line Tate operator applied to a zero-extended half-line source. It proves

    A_P Uv = -U B_P v + Fourier_unitary(leak_P v).

The last term must not be omitted. For one prime and v supported in (0,log p), it computes

    ||leak_p v||^2=(log p)^2/(p-1) ||v||^2.

This gives an infinite-rank nonzero prime leakage map. A rank-two endpoint adjustment cannot cancel that increment on all source vectors.

Thus this paper supplies the exact comparison that can be used, while ruling out the stronger false equation A_P U=-U B_P. For F736 the retained comparison carrier must include any applicable leakage/residual coordinate, not use a fictitious reducing subspace or unitary operator equivalence.

The theorem covers the trivial character and fixed finite prime sets. It does not prove all-prime full-line multiplier/leakage convergence, arbitrary characters, additional Sonin restrictions or positivity.

## 6. Relation to the physical fixed-cutoff kernel

The previous Strominger source fixes a true even cosine cutoff. Its large-cutoff kernel AWAY from the identity has the positive log-coordinate profile

    k_infinity(u)
      = (1/4)[1/|sinh(u/2)|+1/cosh(u/2)]
      = exp(-|u|/2)/(1-exp(-2|u|)), u!=0.

This is an algebraic rewriting of the existing off-diagonal limit, not a completed distributional normalization proof. It is consistent with keeping the local cutoff/Tate orientation distinct from the positive arithmetic gamma multiplier d=-a_infinity.

An off-identity kernel does NOT fix a delta-at-identity normalization. The actual match still needs the local principal-value prescription and the centered diagonal/counterterm constant. Use the existing diagonal finite-part representation and the source Fourier/PV normalization, rather than infer the full spectral distribution from off-diagonal agreement.

The Connes trace source explicitly fixes the local principal value by the basic additive character and its Fourier condition at1. Its product-cutoff theorem is not a positive trace identity. The physical log/half-density dictionary from v13 must also be retained when connecting this theorem to the cosine-sector operator.

## 7. Other normalization fixtures are not substitutes

The Gaussian/heat endpoint-gamma-prime audit fixes algebraic factors and multiplicities in its own inverse-Laplace setting, but retains source-owner/authoritative-Hadamard confirmation gates. The test-family mismatch audit warns that shifted spectral Gaussians, modulated Gaussian correlations and compact-support interval forms are not interchangeable merely because prime coefficients look alike.

Use those fixtures as consistency checks after constructing the general source comparison. Do not call them proofs of the physical finite-cutoff or compact-support family identification.

The later compact-support derived-source note does give an internal bridge at its stated strength; its external-source verification qualification is still separate.

## Refined next calculation

Prior research now supplies an independent even Tate symbol, its common-domain negative compression theorem, explicit endpoint permutation, Fourier scale correction and the leakage term. These should be inputs, not generic missing-normalization requests.

For the F736 carrier attempt:

1. freeze which source form is used: local cutoff/Tate, full arithmetic, or centered half-divisor;
2. write its measure, sign, overall factor and ordered endpoints explicitly;
3. match the physical centered diagonal and PV constant to that source distribution, not just the off-identity kernel;
4. retain leakage if using the half-line arithmetic compression;
5. carry the resulting actual scalar/relative coordinates into the source-retaining graph before asking for the modification-level inverse mate.

This remains a scoped normalization/continuity input to the carrier task. It is not a claim that the full native analytical F736 witness or its two bottom/filler pairs have been calculated.
