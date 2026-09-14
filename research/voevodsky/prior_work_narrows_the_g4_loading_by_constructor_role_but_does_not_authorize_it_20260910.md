# Prior work narrows the G4 loading by constructor role but does not authorize it

## Question

Do historical G4 and radial-response packets contain clues that distinguish the two analytically admissible arithmetic loadings?

## Claim boundary

Yes. The source roles strongly favor the Euler-to-theta coefficient for forward radial shell synthesis and reserve the mixed primitive--square coefficient for the determinant counterterm block. This narrows the missing loading arrow to one candidate. It remains a conjectural interface assignment because the materialized G4 contract does not declare the source map.

## Problem

Two loadings satisfy the same convergence and codiagonal tests:

\[
\omega_p^{\rm mix}(\sigma)=\frac12p^{-3/2-\sigma}
\]

and

\[
c_p=2(\log p)\sum_{k\ge1}p^{-k/2}\Phi'(k\log p).
\]

Analytic admissibility alone cannot choose between them.

## Bold conjecture

Historical constructor roles contain no information that distinguishes these loadings.

## Named rivals

1. Forward shell synthesis selects \(c_p\), while determinant renormalization selects \(\omega_p^{\rm mix}\).
2. The two coefficients are interchangeable because they land in the same radial feature space.
3. The older SCC dependency graph already certifies one loading implicitly.

## Prior-work clues

### Forward radial synthesis

The radial-interface audits require a source injection

\[
U_X^{\rm rad}
\]

from completed theta shells into the conservative radial graph, followed by endpoint and Wronskian feature extraction. The ordered-pair response target is built directly from completed-theta correlations and their Laplace transforms.

The coefficient \(c_p\) is explicitly named the Euler-to-theta coefficient and contains the theta derivative \(\Phi'(k\log p)\). Its source role therefore matches forward theta-shell incidence.

### Determinant counterterms

The coefficient \(\omega_p^{\rm mix}\) is explicitly derived as the product of primitive and square endpoint weights. Its source role is the renormalized primitive--square Adams block used around the order-three determinant. It is not presented as the forward shell injection.

### Required shell response

Historical work fixes the local radial bordered operator shape

\[
\mathbb T_X(z)
=
\begin{pmatrix}
D_t-z&U_X^{\rm rad}\\
N_X^{\rm rad}&B_X(z)
\end{pmatrix}
\]

and the diagonal shell readout

\[
R(z)+2E(z)
=
\frac{\rho(0)+E(z)-\frac12W(z)}{z}+2E(z).
\]

The reciprocal shell target is the ordered-pair entire section

\[
I_{nm}^{[a,b]}(z)
=-\int_0^\infty e^{-zt}\rho_{nm}^{[a,b]}(t)\,dt.
\]

These formulas are theta-shell response formulas, supporting the forward-incidence role rather than the mixed determinant-weight role.

### Weak SCC interface check

The historical `all_interfaces_checked` result verifies only that constructors reference the coarse `g4_common` descriptor. It does not compare carriers, coefficients, traces, metrics, or return maps. Therefore it supplies no implicit loading selection.

### Existing comparison target

Prior response work already names the missing arrow

\[
C_{\rm FP}:X_{\rm FP}^{\rm ret}
\longrightarrow X_{G4}
\]

and requires it to intertwine sewing and contragredient response. This confirms that equality with G4 was withheld rather than silently established.

## Strongest falsification attempt

Rival 2 fails by source typing. The same codomain and convergence do not identify a forward theta incidence with a product of determinant counterterms. Their asymptotics are also inequivalent.

Rival 3 fails because the SCC interface checker inspects descriptor membership only. Older packets even show that node statuses and digests have changed across contract revisions; historical `constructed` metadata cannot override the current open formal slot.

Rival 1 survives all available role tests:

- candidate forward loading: \(c_p\);
- determinant counterterm loading: \(\omega_p^{\rm mix}\).

## Acceptance test for the candidate

The candidate assignment becomes authoritative only if a G4 source declaration proves

\[
U_X^{\rm rad}
=
\sum_{p\le X}c_pU_p^{\rm theta\to rad}
\]

with retained prime and grade labels, and shows that its return/codiagonal produces the fixed endpoint-minus-Wronskian shell formula before scalar aggregation.

A declaration using \(\omega_p^{\rm mix}\) must instead explain why a determinant-counterterm product is the source coefficient of forward shell synthesis.

## Disposition

The no-clue conjecture is rejected. Prior work narrows the canonical forward G4 loading to the Euler-to-theta coefficient \(c_p\) by constructor role. The mixed coefficient belongs to the primitive--square determinant block. This is the strongest source-based candidate assignment available, but the loading arrow remains unauthorized until G4 declares and verifies the forward synthesis equation.
