# Finite Euler Gram and polarization: Lean packet

Sources:

- `research/grothendieck/finite-euler-cross-weyl-positivity-and-diagonal-no-go.md`;
- `research/grothendieck/minimal-hilbert-schur-prime-no-go.md`.

For an arbitrary real inner-product space, `twoVectorGramDeterminant` is

\[
\langle u,u\rangle\langle v,v\rangle-\langle u,v\rangle^2.
\]

`twoVectorGramDeterminant_nonnegative` proves its nonnegativity directly from
Cauchy--Schwarz. This is the reusable finite positivity theorem for the two
resolvent boundary vectors; it does not assert convergence of an infinite
prime source.

`inner_finset_weighted_source` proves that a finite weighted source remains
linear in the cross channel. In the Euler fixture, the finite index type is a
prime-power cutoff, the weights are the source-authorized von Mangoldt
coefficients, and the source vectors are propagated point masses.

`real_cross_term_polarization` proves

\[
4\langle u,v\rangle
=\langle u+v,u+v\rangle-\langle u-v,u-v\rangle.
\]

The signed difference makes the Krein character explicit: polarization does
not turn a cross term into one positive Hilbert Schur channel.
`orthogonal_nonzero_cross_hostile` records that a zero cross term need not
mean either source vector is zero.

Typing boundary: the coefficient field is `ℝ`; `E` is any seminormed additive
commutative group with a real inner-product-space instance; finite source
indices have a `Fintype` instance. The free Green kernel, von Mangoldt weights,
prime-diagonal divergence, Stieltjes cut density, relative/Krein quotient,
and identification with the completed Xi resolvent remain external.

The separate packet
`research/grothendieck/orthogonal-prime-penalty-two-prime-no-go.md` remains
gated: its decimal determinant sign needs a replayable rational interval
certificate for the three digamma differences and logarithmic prime weights.

Verification boundary: Nima's active no-build instruction remains in force.
Only bounded static scans were run; the module is outside `MariciFormal.lean`.
