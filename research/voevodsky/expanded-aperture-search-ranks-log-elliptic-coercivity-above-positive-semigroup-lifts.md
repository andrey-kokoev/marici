# Expanded-aperture search ranks log-elliptic coercivity above positive semigroup lifts

## Search performed

The audit used:

- repository-wide search across the Grothendieck, Nima, Kitaev, Flavor, and Voevodsky packets;
- the indexed PDF corpus through `pnpm pdf:search`, especially the monographs on boundary triples, Weyl functions, Schur complements, and orthogonal coupling;
- fresh arXiv and Crossref queries for zeta boundary triples, canonical systems, explicit-formula positivity, and operator realizations.

The search recovered the existing canonical-system literature (notably Suzuki) but no external theorem constructing a positive endpoint--gamma--prime Weil carrier unconditionally.

## Correction to the recent search direction

The Adams and polyphase CP lifts are genuine source-positive constructions, but they govern positive prime-grade magnitude and discrete grade transport. They do not retain the negative prime sign or produce the coupled endpoint--gamma--prime observer.

Consequently they are structural models for how primitive arrows become positive at primitive-square level, not the leading global RH route.

## Boundary-triple result

The PDF corpus confirms the standard realization theorem:

- Weyl functions of Hilbert-space boundary triples are Nevanlinna functions;
- conversely, suitable Nevanlinna functions admit reproducing-kernel/boundary-triple realizations;
- orthogonal coupling combines boundary Weyl functions through resolvent and inverse-sum formulas.

This is relevant to the desired archimedean--prime colligation, but it does not create positivity. To realize the completed scalar as a Hilbert Weyl function, one must first prove its Nevanlinna kernel is positive. For the target source, that is another presentation of the Weil gate.

The existing free-resolvent calculation sharpens the obstruction. A prime term

\[
g_a(x)=\frac{e^{-a\sqrt x}}{2\sqrt x}
\]

is an off-diagonal resolvent coefficient and has oscillating Stieltjes cut density. It cannot be the diagonal Weyl coefficient or positive Schur return of one Hilbert boundary channel. Polarization realizes it only in a doubled indefinite carrier. A positive descent of that carrier is again the unresolved Pick/Stieltjes condition.

Thus generic boundary-triple realization, Julia colligation, or Schur complementation is circular unless a source Green identity proves the required positive descent first.

## Literature routes already closed or quarantined

The prior verified literature sweep establishes:

- de Branges positivity conditions proposed for \(\xi\) fail unconditionally in the Conrey--Li test;
- canonical Hamiltonians built after critical-line innerness assume an RH-equivalent property;
- Nyman--Beurling density and Li positivity are equivalent criteria, not source constructors;
- Burnol's Sonine systems give unconditional interpolation infrastructure but no positive Weil factorization;
- exact bandlimited strict-peak interpolation at all zeta ordinates is obstructed by infinite Beurling--Malliavin density;
- Gaussian Beurling--Selberg majorization does not order the signed Weil functional off RH;
- theta-kernel pointwise positivity does not imply positivity of its cosine transform or of the Weil form.

No overlooked published positive measure survives these circularity tests.

## Highest-ranked nonredundant route

The strongest remaining route is not a positive direct-sum construction. It is coercivity of the **already coupled signed operator** on compact logarithmic windows.

Prior work gives the structural decomposition

\[
W_L=A_L^{1/2}(I+K_L)A_L^{1/2},
\]

where:

- the archimedean symbol has positive logarithmic growth
  \(\operatorname{Re}\psi(1/4+iu/2)=\log|u|+O(1)\);
- prime translations are bounded order-zero perturbations on a fixed support window;
- the endpoint is finite rank;
- the preconditioned remainder is compact and self-adjoint.

The missing source estimate is a quantitative interval Gårding inequality

\[
W_L(f,f)
\geq
c_L\|P_{>N_L}f\|_{H^{0,\log}}^2
-C_L\|P_{\leq N_L}f\|^2,
\]

with explicit source-computable constants. If the high-mode block and its coupling to low modes are controlled, positivity reduces to a finite certified Schur complement for each \(L\).

To reach Gaussian tests one then needs:

1. constants controlled as \(L\to\infty\);
2. form-core approximation of Gaussian factors by compactly supported Mellin tests;
3. a tail estimate preserving the full endpoint--gamma--prime cancellation.

This route does not assume a target Gram factor or representing measure. It is therefore ranked above further attempts to manufacture positive semigroups from prime sectors.

## Immediate executable target

The next calculation should derive, from the normalized explicit formula, an explicit high-frequency lower bound for the archimedean block and an operator-norm upper bound for the finite-window prime translations, including localization commutators. The first decisive inequality is

\[
\inf_{|u|\geq U}\operatorname{Re}\psi(1/4+iu/2)
>
\|P_{>U}T_{P,L}P_{>U}\|
+
\text{endpoint/localization error}.
\]

Failure of this inequality for every controllable \(U\), or constants exploding too quickly with \(L\), would terminate the last coercive route. Success would leave a finite low-mode matrix certificate rather than an assumed positive carrier.

## Sources consulted

- `research/grothendieck/past-research-leaves-one-coercive-route-and-two-diagnostic-routes.md`
- `research/grothendieck/prior-research-points-to-order-two-stieltjes-not-more-heat-tests.md`
- `research/grothendieck/prime-trace-offdiagonal-free-resolvent.md`
- `research/grothendieck/minimal-hilbert-schur-prime-no-go.md`
- `research/grothendieck/review-of-prior-rh-positivity-routes-after-the-local-weil-operator-reduction.md`
- `research/grothendieck/references/kimi-finite-double-contact-literature-sweep-2026-09-05.md`
- `research/nima/correction-the-schur-complement-is-the-harmonic-endpoint-energy-not-the-excess-energy.md`
- `references/Boundary Value Problems, Weyl Functions, and Differential Operators.pdf`, especially Chapters 2 and 4
- `references/Generalized Boundary Triples.pdf`, Schur-complement realization material
