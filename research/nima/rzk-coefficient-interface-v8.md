# Coefficient interface v8: split support fibre contraction

## Rzk implementation

`rzk/13-split-support-fibre.rzk.md` adds 16 checked definitions. In the graded
splitting K = B + Q it implements

\[
F_n=B_n\oplus Q_n\oplus Q_{n+1},\qquad
D(b,q,u)=(d_Bb+\alpha q,d_Qq,q-d_Qu),
\]

\[
I(b)=(b,0,0),\qquad \Pi(b,q,u)=b-\alpha u,\qquad
H(b,q,u)=(0,u,0).
\]

B denotes the full support complex, including both endpoint packets. The
identification of this block model with the original fibre of
E -> Q + V[1] still requires its concrete graded splitting. It is not the
endpoint-relative object B/V.

With explicit additive/subtractive laws, zero-map laws and the attaching-block
identity d_B alpha = -alpha d_Q, the module proves:

- I and Pi commute with the differential;
- Pi I = 1;
- D H + H D = 1 - I Pi, using the actual D/H maps, not just a supplied
  contraction identity;
- H squared, H I and Pi H vanish.

The assembled homotopy proof includes differential-of-zero terms and reduces
them using the supplied laws. Degrees have separate carrier types; these are
not scalars substituted for chain modules. No global axioms are declared.
The ambient cochain structures themselves must be supplied; the module is
not yet a library construction of graded polynomial modules.

## Incoming Q-homotopy has an explicit support effect

For a fixed ambient b and quotient component q, the checked frame-change law is

\[
\Pi(b,q,u)-\Pi(b,q,v)=\alpha(v-u).
\]

Thus the next physical packet has a precise adapter: identify its frame term
u in this model and apply the actual attaching map. Strict endpoint values
cannot substitute for u. This theorem does not decide which homotopy is
physically supplied, nor turn the resulting support representative into a
proved nonzero homology class.

## Fresh verification

Command:

`pwsh -NoProfile -File research/nima/rzk/check-boundary-framed.ps1 -Module 13-split-support-fibre`

Passed with exit 0 and `Everything is ok!`: 37 definitions across the explicit
three-file closure (13 + 8 + 16). Result with dependency and executable
digests: `results/13-split-support-fibre.typecheck.json`. Execution reference:
`structured_command_execution:e_39824_1788730087540498200_13`.
The persistent LSP attempt timed out; only the fresh headless check is claimed.

The supplied concrete checker was also rerun, without changing its directory:

`python -B research/chatgpt/normalization-framed-support/check_normalization_framed_support.py --output research/nima/results/normalization-framed-support-recheck.json`

It passed 30,713 assertions for independent/Rees coefficients, each in finite
and permitted-localization Cech form. It verifies the 222-to-208 contraction,
the normalization-source tests and both frame examples. Its output matches
the supplied certificate as parsed JSON. Execution reference:
`structured_command_execution:e_39824_1788729969469602400_12`.
This is a rerun of supplied code, not an independent implementation or formal
Rzk instantiation of all 215 polynomial generators; pinned upstream provenance
has not been authenticated. The result retains the checker digest.

## Remaining formal integration

The contraction algebra is no longer merely a proposed interface. The remaining
formal task is to construct the actual indexed coefficient modules and their
maps in Rzk and instantiate these laws, including the original-to-block
coordinate change. The external spatial Gysin construction must identify its
source map and Q-homotopy in those modules. The mapping-space realization of
the cochain adapter and the concrete secondary homology quotient remain
separate obligations. No outcome for physical vanishing or parity is selected.
