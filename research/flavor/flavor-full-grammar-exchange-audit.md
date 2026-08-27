# Full-grammar exchange audit: WP681

## Scope correction

WP676 tested exchange invariance of the internal two-messenger mass block. The
full route also contains independently typed endpoint currents:

\[
J_E A,
\qquad
B J_X.
\]

Holding the external source objects fixed, (A\leftrightarrow B) sends these
couplings to (J_EB) and (AJ_X). The full constructor is not invariant. It
would become invariant only after also exchanging (J_E\leftrightarrow J_X),
but no such automorphism between the entrance and exit experiments is admitted.

Therefore WP676's balance condition is a conditional symmetry of an internal
block. It is not a source-authorized selector of the complete flavor grammar.

## Pole-basis closure

On the balanced internal block, define

\[
P_+=\frac{A+B}{\sqrt2},
\qquad
P_-=\frac{A-B}{\sqrt2}.
\]

The frame fluctuation has the same off-diagonal species tensor as the balanced
vev mixing. In the pole basis,

\[
H^T
\begin{pmatrix}0&1\\1&0\end{pmatrix}
H=
\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]

Thus the fluctuation couples diagonally to (P_+) and (P_-); the cross-pole
transition (P_+\leftrightarrow P_-+n) vanishes exactly. The bare
(A\to B+n) analyzer route from WP674 cannot be transported into the exact
balanced exchange theory.

The entrance and exit currents each reach both poles, with relative vectors
((1,1)/\sqrt2) and ((1,-1)/\sqrt2). This creates pole interference, not the
assumed sequential cross-pole decay.

## Disposition

WP676 is corrected from a genuine UV selector to an internal-block
rigidifier and erosion minimizer conditional on an unadmitted endpoint
exchange. The proposed exchange explanation and the cascade analyzer cannot be
combined as previously stated. A different full-grammar symmetry would be
needed to select balance while preserving a physical transition channel.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp681_full_grammar_exchange_audit.py

Generated result: results/wp681_full_grammar_exchange_audit.json.
