# Canonical matching correction for FDM-2 (WP93)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

WP90's Schur complement is an exact zero-momentum algebraic kernel, but it is
not generally the canonically normalized physical light mass at finite `M`.
For the one-generation block

\[
\mathcal M=\begin{pmatrix}m&A\\B&M\end{pmatrix},
\qquad m_{\rm Schur}=m-AB/M,
\]

the physical masses are the singular values of `Mcal`. At the exact hostile
point `(m,A,B,M)=(1,1,1,2)`, the Schur mass is `1/2`, whereas the light squared
singular value is `(7-3 sqrt(5))/2`; its square is not `1/4`.

The mismatch is the omitted kinetic/canonical-normalization channel generated
when the heavy field is eliminated at nonzero momentum. Equality is recovered
only asymptotically under declared mixing bounds `|A|/M << 1`, `|B|/M << 1`.
Therefore WP90/WP92 remain valid existence witnesses for a quotient CP-odd
direction, but their finite-threshold numerical readout is not exact physical
matching.

Classification: finite-threshold **selector candidate**, not rigidifier; its
physical readout still requires canonical matching. Smallest exact falsifier:
the displayed `2x2` block. Instrument gate: full canonically normalized
matching with electroweak and singlet vevs, loop order, and error budget.

Verification: `uv run --with sympy python research/flavor/checkers/wp93_fdm2_canonical_matching.py`.
