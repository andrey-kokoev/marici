# Integral comparison sign coherence

## Question

Do the seven unit comparisons commute with one orientation convention, or is a residual sign mismatch hidden among them?

## Claim boundary

They commute with one convention. Fix the ordered units `(u,v)`, Betti orientation `dtheta wedge dphi`, cyclic flag edges `X->Y`, `Y->Z`, `Z->X`, and character parameters `(a-1,b-1)`. Then the Milnor symbol, de Rham wedge, normalized period, three Parshin edge coefficients, and character residue all have coefficient `+1`.

The historical pair basis reverses only its second edge, sending `(1,1,1)` to `(1,-1,1)`. This is a basis translation, not a different class.

Swapping `u,v` negates the Milnor symbol, wedge, ordered period, character residue, and cyclic flag orientation simultaneously. Reversing one circle or one flag basis also changes the sign; reversing both circles preserves it. The constant minus sign in the `Z`-divisor tame unit has zero secondary valuation and contributes no edge sign.

## Disposition

All comparison maps cohere up to one global choice of generator in a rank-one lattice. No local convention mismatch remains. The next leaf formulates the obstruction without orientation and identifies the exact additional datum needed to select a signed generator.

## Verification

- `research/voevodsky/check_cosmology_integral_comparison_sign_coherence.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
