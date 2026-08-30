# Six-context conditioning gate

Work package: WP554  
Owner: marici.Figueiredo

## Question

Does the exact rank-six context design of WP540 remain separating once a
physical resolution floor is admitted?

## Frozen matrix

WP540 uses the six supported Euclidean momentum-squared nodes

\[
0,quad 2-\sqrt3,quad 1,quad 2,quad 3,quad 2+\sqrt3.
\]

WP554 reconstructs the exact WP539 companion-resolvent matrix at these nodes.
Its determinant is nonzero, so algebraic rank remains six. The twist ladder of
WP541 therefore solves momentum support and aliasing exactly.

## Conditioning

Exact rank does not type experimental separation. At 80-decimal working
precision the singular values are approximately

\[
11.4976, 0.0807591, 0.00157834, 7.82899\,10^{-5},
1.18400\,10^{-5}, 9.03007\,10^{-7}.
\]

The spectral condition number is approximately \(1.27326\,10^7\). The exact
matrix infinity-norm condition number, evaluated at high precision from the
algebraic entries and their exact inverse, is approximately
\(1.52532\,10^7\).

Thus there is a unit coefficient direction whose context response has norm
only about \(9.03\,10^{-7}\). A relative response error of \(10^{-6}\) can
be amplified beyond order one. Exact rank alone cannot authorize contextual
faithfulness for a realized instrument.

## Contextual partition

For a declared whitened resolution \(\varepsilon\), physical equivalence is
the tolerance relation

\[
x\sim_\varepsilon y
\quad\Longleftrightarrow\quad
\lVert C(x-y)\rVert_2\leq\varepsilon.
\]

At zero tolerance the partition is singleton because \(C\) is invertible. At
nonzero tolerance it contains ellipsoidal cells elongated by the inverse
singular values. The partition cannot be claimed until the actual covariance
metric is supplied; an unweighted condition number is a hostile diagnostic,
not a detector likelihood.

## Physical gate

The correct acceptance test is the smallest singular value of the whitened
response

\[
C_{\mathrm{obs}}^{-1/2}C C_{\mathrm{source}}^{1/2},
\]

including scale, ensemble, context, operator, continuum, and finite-volume
covariance. The design is physically separating only relative to a declared
source domain and detection threshold.

The smallest hostile is the right-singular direction associated with the
smallest singular value. It is nonzero, algebraically detected, but its unit
response lies below a \(10^{-6}\) absolute resolution floor.

WP554 is a conditioning criticism of the proposed instrument. It does not
alter the source action and does not supply selection.

WP555 subsequently proves that the unweighted singular spectrum is companion-
presentation dependent. The numerical values above remain diagnostics of the
WP554 chart, but the unit-hostile physical claim is withdrawn until a source
metric is independently declared and transported.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp554_six_context_conditioning_gate.py

The generated result is
research/flavor/results/wp554_six_context_conditioning_gate.json.
