# Mixed-prime rectangle parity: Lean packet

Source: `research/grothendieck/mixed-prime-rectangle-parity-positivity-theorem.md`.

For real coefficients `r s c d`, `mixedPrimeRectangleEnergy` is the quadratic
form of the normalized matrix

\[
\begin{pmatrix}
1&r&s&c\\ r&1&d&s\\ s&d&1&r\\ c&s&r&1
\end{pmatrix}.
\]

`mixedPrimeRectangle_parity_decomposition` proves the exact change-of-variables
identity: twice this energy is the sum of the even block with entries
`1+c`, `1+d`, `r+s` and the odd block with entries `1-c`, `1-d`, `r-s`.
`mixedPrimeRectangle_nonnegative_iff_parity` proves universal nonnegativity of
the four-variable form iff both two-variable parity forms are universally
nonnegative. The reverse direction uses the decomposition; the forward
direction embeds arbitrary even and odd vectors separately.

The two `exactTensor_*_parity_determinant` theorems prove that when
`c = d = r*s`, each block determinant equals

\[
(1-r^2)(1-s^2).
\]

`mixedPrimeRectangle_individual_bounds_hostile` takes `r=s=3/5` and `c=d=0`:
all four individual edge bounds hold, but the even vector `(1,-1)` has negative
energy.

Typing boundary: every coefficient and test vector is real. The module does
not promote the scalar theorem to complex or operator-valued correlations,
where adjoints and noncommuting entries must be specified. It does not derive
the coefficients from a completed Weil distribution and does not control
larger nonchordal cycles.

Verification boundary: Nima's active no-build instruction remains in force.
The file was checked only by bounded static scans and stays outside
`MariciFormal.lean` pending authorized elaboration.
