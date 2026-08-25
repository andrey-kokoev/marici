# Full-mediator benchmark falsifier for FDM-2 (WP112)

Agent: `marici.Figueiredo`. Date: 2026-08-25.

WP111's fixed benchmark must be tested in the full fermion system, not only
through its zero-momentum Schur complement. In the declared unit convention,
the down-sector mass block is

\[
\mathcal M_d=
\begin{pmatrix}Y_0&a\\-zb&1\end{pmatrix},
\quad z=4/5+3i/5.
\]

Diagonalize `M_d M_d^dagger`, order its four singular states by increasing
mass, and form the charged-current block from the first three gauge-doublet
rows and three light columns. The high-precision checker finds singular values

\[
(1.06962,2.42410,2.68776,5.26836)
\]

and

\[
\|V_{light}V_{light}^\dagger-I_3\|_2=0.9820921052.
\]

Thus the nominal mediator is neither parametrically heavy nor weakly mixed.
The light block is nowhere near the unitary three-generation CKM domain used
by the fitted ensemble.

For a fixed rephasing-invariant quartet, the full light block gives
`J_full=-0.01196527685`, while the Schur-complement three-state model gives
`J_Schur=5.35254948e-5`. Their absolute difference is
`0.01201880234`, exceeding WP111's allowed half-gap by more than four orders of
magnitude. The conjugate vacuum reverses the quartet sign and retains the same
singular values and nonunitarity, so CP covariance survives while canonical
agreement fails.

This **falsifies the physical benchmark instrument**, not the algebraic facts
that the Schur map has a CP-odd direction or that its coarse bound is compatible
with the stored ensemble. The smallest robust checker falsifiers are
`nonunitarity>9/10` and `|J_full-J_Schur|>1/100`.

Classification: the unit-mass WP90 benchmark is neither a viable physical
three-generation selector instrument nor a texture rigidifier. A repaired
model requires a genuinely decoupled mediator with controlled mixings, then a
fresh source margin and ensemble test; WP92 proves that this cannot retain an
order-one effect with bounded couplings in the strict decoupling limit.

Verification: `uv run --with numpy python
research/flavor/checkers/wp112_fdm2_full_mediator_benchmark.py`.
