# Audit of the compact-support Weil source instance

## Question

Does `research/voevodsky/compact-support-weil-source-identity-derived-instance.md` correctly transport the repository's centered two-variable formula to compactly supported interval tests, and is an external classical-source verification available locally?

## Claim boundary

The internal transport is consistent with the declared Fourier convention. For

\[
Ff(u)=\int f(x)e^{-iux}\,dx,
\]

Plancherel gives

\[
\frac1{2\pi}\int |Ff(u)|^2e^{iua}\,du=\langle f,T_a f\rangle,
\qquad T_af(x)=f(x+a).
\]

For the Hermitian polarization `h_f(z)=Ff(z) conjugate(Ff(conjugate(z)))`, the two polar values are conjugate:

\[
h_f(i/2)=a_+(f)\overline{a_-(f)},\qquad
h_f(-i/2)=a_-(f)\overline{a_+(f)}.
\]

Therefore the centered half-sum equals `Re(a_plus conjugate(a_minus))`; in a real basis its matrix is `(a_plus a_minus^* + a_minus a_plus^*)/2`. The factor one half is forced.

The closure argument is also valid at its stated scope. A zero-extended interval polynomial is piecewise smooth with endpoint jumps, hence its Fourier transform is `O(1/|u|)`. The integral of `log(2+|u|)|Ff(u)|^2` converges. Interior cutoff and mollification converge in `H^s` for `0<s<1/2`, and the logarithmic weight is bounded by a constant times `(1+|u|^2)^s`. Translation and fixed-support endpoint functionals are continuous in the resulting graph norm.

## External-source audit

The local page-indexed PDF collection contains no classical Riemann/Weil explicit-formula source. Searches for the specific digamma expression returned no match; a broad `explicit formula` search returned unrelated sources. The index also reports seven changed and seven added PDFs, so even the negative local search is not an exhaustive current-corpus claim.

Accordingly I did not verify from an external edition:

- the global sign and factor in the centered divisor convention;
- the archimedean coefficient `1/(4*pi)` against `|Ff|^2 du`;
- the prime coefficient and Fourier-transform convention;
- the exact admissible test class in the cited classical theorem.

## Disposition

The internal Fourier, polarization, endpoint, and logarithmic-domain transport survives audit. Publication authority remains blocked at the absent external classical source. Acceptance requires a pinned edition and theorem/page locator whose test-function and Fourier conventions can be transformed term-by-term into the displayed identity. No further abstraction can discharge that source gate.
