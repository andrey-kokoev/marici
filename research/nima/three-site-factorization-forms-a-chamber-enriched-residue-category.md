# Three-site factorization forms a chamber-enriched residue category

## Question

Can the smallest connected cosmological graph carry normalized sequential residue morphisms without an unsourced choice of physical regulator chamber?

## Claim boundary

The source data define a chamber-enriched integrand-level residue category. They do not select one physical boundary value or prove an integrated factorization theorem.

Let

$$
\Sigma=\{(--),(-+),(+-),(++)\}.
$$

After the first residue on a compatible pair, the two remaining polar coordinates satisfy `B=-A` and have boundary signs `s,t` in `{ -1,+1 }`. The exact distribution identity is

$$
\frac1{A+i0s}+\frac1{-A+i0t}
=-i\pi(s+t)\delta(A).
$$

Therefore the normalized chamber-valued current is

$$
J(s,t)=-(s+t),
$$

in units of `i*pi*delta(A)`. Its ordered values are

$$
J(--)=2,
\qquad
J(-+)=J(+-)=0,
\qquad
J(++)=-2.
$$

This retains exactly the source ambiguity rather than fitting a contour-side selector.

## Objects and morphisms

The objects are the ten physical connected-subgraph divisors already frozen in `three-site-physical-residue-link.json`. The nontrivial maximal compatibility link is the six-cycle with edges

$$
(q_{G12},q_{g23}),
(q_{G12},q_{g31}),
(q_{G23},q_{g31}),
(q_{G23},q_{g12}),
(q_{G31},q_{g12}),
(q_{G31},q_{g23}).
$$

Each oriented edge carries its source residue sign and the function

$$
J:\Sigma\longrightarrow\mathbb Z.
$$

Reversing residue order reverses the oriented two-normal form, so the reverse morphism carries `-J`. Exchanging the two regulator signs leaves `J` unchanged. Cyclic relabelling preserves the edge set and the chamber table.

Pairs not joined in the physical link are not composable residue sequences in this category. For example,

$$
(q_{G12},q_{G23})
$$

is rejected as an incompatible pair; no vanishing residue is inferred from non-composability.

## Coherence

The source signs around the six-cycle alternate. Combining those signs with the order-antisymmetric residue form reproduces the oriented fundamental cycle with zero simplicial boundary. This is integrand-level coherence with chamber coefficients. It is not equality of scalar periods.

A physical contour prescription would be a section

$$
\sigma_\Gamma:\Gamma_{\rm phys}\longrightarrow\Sigma
$$

or a compatible family of probability/distributional weights on `Sigma`. Applying such a section to `J` produces scalar residue morphisms. No canonical section is supplied by the frozen source; equal regulators land in a mixed chamber and give zero.

## Verification

`research/nima/checkers/check_three_site_chamber_enriched_residue_category.py` verifies with exact integers:

- the table `(2,0,0,-2)`;
- symmetry under exchange of regulator labels;
- antisymmetry under residue-order reversal;
- cyclic preservation of all six compatible edges;
- rejection of one explicit incompatible pair.

The machine-readable result is `research/nima/results/three-site-chamber-enriched-residue-category.json`.

## Disposition

The lowest-level divisor/residue category is now complete as a chamber-enriched category. The former blocker is retyped: what is absent is not the residue morphism but a physical-chain evaluation functor from chamber-valued currents to scalar boundary values. Carrier-wall comparison can proceed at the enriched level only if the Carrier target retains the same chamber object; scalar physical factorization still requires `sigma_Gamma` or an equivalent relative-chain prescription.
