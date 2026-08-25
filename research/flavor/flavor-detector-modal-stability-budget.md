# Modal stability budget for the flavor detector (WP100)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

Probability errors live in the zero-sum plane. For the WP99 channel it has
the exact basis

\[
v_o=(1,0,-1),\qquad v_e=(1,-2,1),
\]

with detector eigenvalues

\[
\lambda_o=1-l-2e,\qquad \lambda_e=1-b-l.
\]

The odd mode carries orientation; the even mode carries broken-versus-zero
support. If an observed error is `a_o v_o+a_e v_e`, deconvolution returns

\[
{a_o\over\lambda_o}v_o+{a_e\over\lambda_e}v_e.
\]

Hence the exact modal amplification is

\[
A=\max(|\lambda_o|^{-1},|\lambda_e|^{-1}).
\]

A physically stable detector must declare margins
`|lambda_o|>=gamma_o>0` and `|lambda_e|>=gamma_e>0`. Observed modal error
`epsilon` is then at most
`epsilon/min(gamma_o,gamma_e)` after inversion.

Calibration uncertainty is a separate channel. If certified eigenvalue drift
is bounded by `d_o,d_e`, robust invertibility requires
`|hat lambda_o|-d_o>0` and `|hat lambda_e|-d_e>0`; those reduced margins, not
the central calibration values, control the error certificate.

Classification: stable separator when both robust margins are positive;
neither selector nor rigidifier. Smallest exact falsifier of any fixed error
budget is a sequence approaching either kernel, e.g.
`l=b=0, e=(1-epsilon)/2`, for which odd amplification is `1/epsilon`.

Remaining instrument gate: empirical calibration/drift certificates and a
combined budget including WP98 sampling, WP93 canonical matching, domain
reset/correlation, and detector inversion.

Verification: `uv run --with sympy python research/flavor/checkers/wp100_detector_modal_stability.py`.
