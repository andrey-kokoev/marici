# Integral tame-sign decorated complex

## Question

What is the coordinate-covariant integral boundary after retaining primary tame signs?

## Claim boundary

For `{u,v}`, the exact three-line tame units are `v^-1`, `u`, and `-v/u`. Thus the free secondary edge cycle is `(1,1,1)`, while the primary sign decoration is `(1,1,-1)` on `(X,Y,Z)`.

For `u'=u^a v^b`, `v'=u^c v^d`, with determinant `+1` or `-1`, the free edges are

`det(A) (1,1,1)`.

The primary signs are

- `X`: `(-1)^(ac)`;
- `Y`: `(-1)^(bd)`;
- `Z`: `(-1)^((a+b)(c+d))`, equivalently `(-1)^(1+ac+bd)`.

These formulas agree both with direct tame symbols and with the diagonal Milnor 2-torsion correction. Secondary valuation and rationalization forget the sign layer.

## Disposition

The complete integral localization object is a sign-decorated primitive cycle. The target `(Xi_log,-sigma123)` is complete only in the rational or regulator-visible quotient; an integral horn must specify the K1 sign layer too. The next leaf formulates that target and tests independent torsion cancellation.

## Verification

- `research/voevodsky/check_cosmology_integral_tame_sign_decorated_complex.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
