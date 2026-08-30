# 1335 — Five-Site Gauss--Manin Variation Is an Unavoidable Mixed-Deck Infinity Class

> **RETRACTED.** This boundary-class claim depended on Entry 1329's purported affine solution module. Generic fibers show that module is empty for the declared degree-two ansatz. The infinity valuation census remains valid, but no Gauss--Manin class follows from intersecting a modularly accidental solution space with its boundary kernel. Retained as provenance; see the next correction entry.

## Starting point

Entry 1329 established affine Kummer exactness at quadratic primitive degree:

\[
\partial_z\Omega=d_u\Xi^{(2)}_{\rm Kum}.
\]

The physical period nevertheless varies. The remaining question is whether some choice in the full affine solution module can remove the projective radial boundary.

## Deck-resolved infinity valuation

Under generic simultaneous scaling

\[
u_i=Rv_i,
\qquad R\to\infty,
\]

all five Kummer roots have the same leading magnitude and retain independent deck signs.

For a signed cut wall \(g_A\):

- equal cut-edge signs give one growing denominator;
- opposite signs cancel the leading root terms and give zero growth.

The source term census yields

\[
\begin{array}{c|c}
\text{number of deck sheets}&\text{minimum denominator growth}\\
\hline
10&2\\
20&4\\
2&9.
\end{array}
\]

The two growth-nine sheets are exactly the uniform-sign sheets.

The leading coefficients of the complete 180-term canonical sum were audited at two independent finite-field directions. No leading cancellation occurs on any of the 32 sheets. Therefore the table gives the actual generic radial orders, not merely termwise lower bounds.

## Boundary map on the full solution module

For every deck sheet and every nonnegative radial exponent, impose vanishing of the radial contraction

\[
\iota_E\Xi^{(2)}_{\rm Kum},
\qquad
E=\sum_i u_i\partial_{u_i}.
\]

The constraints retain:

- all 32 primitive Kummer characters;
- the sheet character \((-1)^{|S\cap T|}\);
- the root weight \(R^{|S|}\);
- every polynomial degree through two;
- every asymptotic exponent allowed by that sheet's decay order.

No primitive representative is selected. The augmented system asks whether the entire affine solution module intersects the kernel of the radial boundary map.

At

\[
(p,z)=(1009,7)
\]

the system has 961 unknowns, 1492 equations, and 404 sampled radial constraints. It has coefficient rank 961 and is inconsistent.

At

\[
(p,z)=(1013,11)
\]

it has 2098 equations and 1010 radial constraints. It again has coefficient rank 961 and is inconsistent.

## Result

\[
\boxed{
\operatorname{Sol}^{(2)}_{\rm Kum}
\cap
\ker R_{\infty,\mathrm{rad}}
=
\varnothing.
}
\]

Thus every quadratic Kummer-resolved affine primitive for \(\partial_z\Omega\) carries nonzero supported radial boundary data on the mixed-sign deck stratification.

Equivalently,

\[
\boxed{
[\partial_z\Omega]_{\rm relative}
=
R_{\infty,\mathrm{rad}}(\Xi^{(2)}_{\rm Kum})
\ne0.
}
\]

This is the first typed five-site Gauss--Manin generator. It is not a fitted scalar operator and not a new carrier divisor. It is a supported class on the existing projective infinity carrier, visible only after retaining occurrence/deck labels.

## Architectural consequence

The mechanism has exactly the H2 form:

\[
\text{shared compactified carrier and support calculus}
+
\text{five-site Kummer coefficient object}.
\]

Collapsing to the two uniform-sign sheets misses the obstruction. The physical sheet alone has growth nine, while the mixed deck sheets carry growth two and four and force the relative class.

## Next test

Compute the image, rank, and deck-character decomposition of

\[
R_{\infty,\mathrm{rad}}:
\operatorname{Sol}^{(2)}_{\rm Kum}\to\mathcal B_{\infty}.
\]

Then transport the resulting boundary module in \(z\). Stabilization gives the minimal vector Gauss--Manin rank; a rank-one quotient would be required before any scalar Picard--Fuchs operator is sought.

## Artifacts

- `research/benincasa/marici-gm/src/bin/five_site_asymmetric_infinity_deck_valuation.rs`
- `research/benincasa/results/five-site-asymmetric-infinity-deck-valuation.json`
- `research/benincasa/marici-gm/src/bin/five_site_asymmetric_kummer_resolved_ibp_pilot.rs`
- `research/benincasa/results/five-site-asymmetric-kummer-resolved-ibp-pilot.json`

Allocator claim: `seqclaim-2d177f726c102f5ec8b8ee18`.
