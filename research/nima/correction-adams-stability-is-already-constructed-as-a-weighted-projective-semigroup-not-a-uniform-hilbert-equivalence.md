# Correction: Adams stability is already constructed as a weighted projective semigroup, not a uniform Hilbert equivalence

## Question

Did the previous candidate-two correction correctly classify Adams stability as
open because no two-sided uniform bound was found?

## Claim boundary

No. Independent reread located the later source-weighted Adams theorem. It
proves exact grade reindexing, weighted incidence naturality, Fourier-saturated
contractivity, cutoff compatibility, and depth-uniform cocycle control. The
absence of a uniform Hilbert lower bound is intentional: weighted Adams raising
is an irreversible semigroup action, not a unitary equivalence. Candidate two
must not require a stronger two-sided Hilbert estimate than its source category
allows.

## Source Adams map

On labelled prime-power grades,

\[
 S_re_{p,k}=e_{p,rk}.
\]

On the projective exponential source,

\[
 q_\delta(S_rc)=q_{r\delta}(c).
\]

Thus \(S_r\) is continuous, has closed range supported on grades divisible by
\(r\), and satisfies

\[
 S_sS_r=S_{sr}.
\]

It commutes with reciprocal reflection and obeys the typed grade-cutoff law.

## Weighted analytic realization

The Euler source weight is

\[
 w_{p,k}=\frac1k p^{-k/2}.
\]

The exact Adams cocycle is

\[
 \rho_r(p,k)
 =\frac{w_{p,rk}}{w_{p,k}}
 =\frac1r p^{-(r-1)k/2}.
\]

The analytic incidence square is

\[
 \mathcal IS_r=M_{\rho_r}U_r\mathcal I.
\]

The geometric transport \(U_r\) is unitary between source-labelled seam
fibres, while \(M_{\rho_r}\) is a strict positive contraction for \(r>1\).

## Fourier-saturated estimate

Because Fourier cyclically permutes four unitary-conjugate analytic
presentations and leaves \(w_{p,k}\) external, the weighted contraction lifts
termwise to the saturated pro-Gram. Along an Adams word, coefficients telescope:

\[
 \prod_j\rho_{r_j}(p,k_j)
 =\frac{k_0}{k_N}p^{-(k_N-k_0)/2}.
\]

Hence there is no constructor-depth amplification or normalization holonomy.
Prime cutoffs commute, and grade cutoffs obey the typed reindexing relation.

## Why a uniform lower Hilbert bound is wrong

For nontrivial grade raising,

\[
 \rho_r(p,k)\longrightarrow0
\]

as \(p\) or \(k\) grows. Therefore no positive constant \(c_r\) can satisfy a
uniform Hilbert inequality

\[
 c_rQ_{\rm sat}
 \le
 (\psi^r)^*Q_{\rm sat}\psi^r.
\]

This is not a defect. Euler half-density makes Adams raising irreversible on
the weighted analytic realization. Source reversibility is only an isomorphism
onto the closed divisible-grade range in the projective category.

Requiring a global Hilbert lower bound would reject the source-derived Euler
cocycle itself.

## Candidate-two status

Adams grade transport is no longer an unresolved boundary-stability gate when
the interfaces are correctly typed:

- source: continuous closed-range grade reindexing;
- seam geometry: unitary fibre transport;
- Euler loading: contractive positive cocycle;
- Fourier saturation: finite unitary orbit with the same coefficient;
- completion: projective and cutoff-natural.

What remains is stability of any other G4 constructors actually crossing the
boundary graph, plus identification of this retained graph with the canonical
`conservative_green_complex` and \(W_{\rm FP}\).

## Correction to the preceding packet

`correction-candidate-two-still-lacks-adams-stability-of-the-fourier-saturated-boundary-gram.md`

misclassified the absence of a two-sided Hilbert estimate as missing Adams
stability. Its listed inequality is too strong for the weighted semigroup. The
valid certificate is the projective closed-range map plus the exact contractive
cocycle above.

## Disposition

Adams stability is constructed in its source-authorized topology. Candidate
two is not closed, but Adams is removed from its open list. The remaining
source-identification and non-Adams constructor checks persist. No RH
conclusion is authorized.
