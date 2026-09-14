# Constructor-role signatures reject scalar substitution before response comparison

## Question

Can constructor-role typing detect the wrong substitution of a mixed primitive--square coefficient into the forward radial synthesis slot before a scalar response is computed?

## Claim boundary

Yes. A constructor role is determined by a typed signature containing source arity, codomain, variance, parameter dependence, support, and required naturality squares. The mixed primitive--square coefficient fails the forward-synthesis signature at source arity and variance. Its different numerical value is not the first defect.

## Problem

Two prime-indexed expressions occur near the same analytic construction:

\[
c_p
=
2(\log p)\sum_{k\ge1}p^{-k/2}\Phi'(k\log p)
\]

and

\[
m_p(\sigma)=\frac12p^{-3/2-\sigma}.
\]

Untyped scalar calculus permits either expression to be placed in a prime-indexed sum. The programme needs a rejection criterion that precedes numerical comparison.

## Bold conjecture

Any prime-indexed scalar family can replace another in forward synthesis; correctness can be decided afterward by comparing the resulting response.

## Named rivals

1. Source arity already distinguishes the constructors.
2. Spectral-parameter variance distinguishes them even after currying.
3. Only the final determinant or response reveals the mismatch.
4. Coefficient sign and decay are sufficient role identifiers.

## Constructor-role signature

Assign each constructor \(f\) the signature

\[
\operatorname{sig}(f)
=
(\operatorname{src},\operatorname{tgt},\operatorname{arity},
\operatorname{variance},\operatorname{support},\operatorname{cells}).
\]

The fields mean:

- `src`: the typed source object, including labels and completion;
- `tgt`: the typed codomain or output line;
- `arity`: linear, bilinear, multilinear, or operator-valued input structure;
- `variance`: dependence on spectral parameters, conjugation, orientation, and dualization;
- `support`: prime, grade, wall, shell, or pair support retained by the arrow;
- `cells`: naturality, domain, sewing, trace, and response squares the constructor must satisfy.

A substitution \(f\rightsquigarrow g\) is admissible only after explicit isomorphisms identify all six fields and transport the required cells. Scalar codomain equality alone does not define a substitution.

## Forward-synthesis signature

For each prime, the Euler-to-theta incidence coefficient belongs to a linear labelled arrow

\[
S_{\theta,p}:E_p^{\rm odd}\to\Theta_p,
\qquad
S_{\theta,p}e_p=\eta_pe_p.
\]

Composition with local radial realization gives

\[
L_p^{\rm rad}
=c_pU_p^{\theta\to {\rm rad}}:
E_p^{\rm odd}\to\mathcal G_p^{\rm rad}.
\]

Its signature is:

- source: one prime-labelled Euler odd coordinate;
- target: one prime-labelled radial Green graph;
- arity: linear;
- variance: independent of the return spectral parameter;
- support: all retained prime-power grades within the prime fiber;
- cells: cutoff naturality, reciprocal orientation, radial codiagonal, and all declared Laplace jets.

## Mixed-counterterm signature

The mixed primitive--square factor occurs after separating two source grades. Before scalar contraction it belongs to a bilinear pairing

\[
B_{p,\sigma}:
E_p^{(1)}\otimes E_p^{(2)}
\longrightarrow
\mathbb C,
\]

with coefficient

\[
m_p(\sigma)=\frac12p^{-3/2-\sigma}.
\]

Its signature is:

- source: a primitive coordinate and a square coordinate;
- target: a determinant or scalar counterterm line;
- arity: bilinear;
- variance: holomorphic dependence on the return parameter \(\sigma\);
- support: the mixed grade pair \((1,2)\);
- cells: determinant expansion and counterterm cancellation.

It is not a map into the radial Green carrier.

## First failed cell

Attempt the substitution

\[
c_pU_p^{\theta\to {\rm rad}}
\rightsquigarrow
m_p(\sigma)U_p^{\theta\to {\rm rad}}.
\]

The first failure occurs before radial response:

\[
E_p^{\rm odd}
\not\cong
E_p^{(1)}\otimes E_p^{(2)}.
\]

The left constructor is linear in one source coordinate; the right coefficient is extracted from a bilinear mixed-grade contraction. No diagonal, multiplication, or pairing map from the Euler odd coordinate to the tensor source has been declared.

Even if one inserts an unauthorized diagonal to hide the arity mismatch, the next failure is variance: the proposed forward loading depends on \(\sigma\), so it no longer defines a fixed source injection before the resolvent/return parameter is chosen. The source-to-state arrow would vary with the downstream probe.

Only after these failures would the codiagonal and response squares be evaluated.

## Deliberate failure trace

The rejected construction would have the form

\[
U^{\rm bad}(\sigma)
=
\sum_pm_p(\sigma)U_p^{\theta\to {\rm rad}}.
\]

It fails in this order:

1. no source-arity comparison;
2. no map transporting mixed-grade support to the full prime-power incidence;
3. forbidden dependence of forward state preparation on the return parameter;
4. no proof of the forward codiagonal coefficient;
5. resulting response disagreement.

Stopping at item 1 localizes the defect most sharply.

## Sign and decay do not type the role

Both coefficient families decay with \(p\), and scalar rescalings can alter signs. These properties cannot identify constructor role. The strict sign theorem for \(c_p\) is useful inside the admitted forward arrow, but it does not supply the arrow's source or codomain.

## Green/Real consequence

The legitimate forward loading is transported by the canonical fold and then participates in

\[
C_uF^2=W_uC_u
\]

and

\[
U^\top=U^*.
\]

The mixed counterterm belongs to the determinant pairing downstream. It may transform compatibly under conjugation as a scalar, but that does not make it a Green-state column. Real compatibility cannot repair a source-arity mismatch.

## General substitution rule

Given constructors \(f\) and \(g\), do not test equality of outputs until the pullback of their signatures exists. The comparison order is:

1. source and target typing;
2. arity and variance;
3. support and label retention;
4. required naturality cells;
5. only then numerical or analytic equality.

A failure at an earlier stage invalidates all downstream comparisons.

## Disposition

The bold conjecture is rejected. Constructor-role typing catches the wrong coefficient at the source-arity gate, before any response computation. The principal example demonstrates that role typing adds information unavailable from scalar values, signs, or decay. The next frontier is to express quotient descent, subgroup restriction, comparison cells, and presentation lifts in the same signature language and verify their composition rules.
