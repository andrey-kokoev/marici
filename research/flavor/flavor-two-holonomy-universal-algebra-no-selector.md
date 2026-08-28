# Two noncommuting holonomies generate a universal algebra, not a selector: WP944

## Question

Does the minimum repair proposed by WP943—two noncommuting family holonomies—select a viable proper family in `physical16`?

## Exact source carrier

Let

\[
\omega=-\frac12+\frac{\sqrt3}{2}i,
\qquad
D=\operatorname{diag}(1,\omega,\omega^2),
\qquad
S=\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix}.
\]

Both `D` and `S` are unitary, and they obey the source relation

\[
DS=\omega SD.
\]

The nine words `D^a S^b`, with `a,b` in `{0,1,2}`, are linearly independent and therefore span the complete complex matrix algebra on family space:

\[
\operatorname{span}_{\mathbb C}\{D^aS^b\}=M_3(\mathbb C).
\]

This is the opposite failure mode from WP943. Commuting holonomies confine both Yukawa Grams to a CP-blind locus. The Weyl pair removes that obstruction so completely that arbitrary Yukawa matrices can be written as word combinations. Unless the source independently fixes the allowed words and their coefficients, the image is the full matrix family rather than a proper selected subfamily.

## Hostile coefficient fiber

The same fixed pair admits a commuting packet and a mixed packet. Take the commuting packet

\[
Y_u=D,
\qquad
Y_d=D^2,
\]

whose Grams are both the identity and whose commutator cubic vanishes. Because the Weyl words span `M_3(C)`, the same carrier also admits

\[
Y_u=\operatorname{diag}(1,2,4),
\qquad
Y_d=\begin{pmatrix}2&1&i\\1&3&1\\-i&1&5\end{pmatrix}.
\]

For the second packet, the down Gram has leading principal minors `6,40,400`, while

\[
\operatorname{Tr}[H_u,H_d]^3=-842400i.
\]

Thus the fixed holonomy carrier does not determine even the zero-versus-nonzero value of this weak-basis invariant. The smallest exact falsifier is this two-point coefficient fiber over one source pair.

## Quotient, instrument, and classification

Simultaneous conjugation of `(D,S)` and both Yukawas leaves the Gram commutator trace invariant, so the hostile distinction descends under the full weak-basis groupoid. The argument concerns algebraic generation and quotient descent; composition order is not assigned physical time or causal meaning.

The pair is a presentation rigidifier and universal algebraic carrier. It is not a source selector when arbitrary word coefficients are admitted. Algebraic span supplies neither executable control nor a physical instrument. A viable successor must derive a proper coefficient module or conditional expectation from the source, prove that it is stable under admitted completions, and type a calibrated holonomy-sensitive instrument. If extra marked ports provide that instrument, they define a new relational experiment over their stabilizer groupoid.

## Disposition

The minimum noncommuting repair is necessary to escape WP943 but insufficient for flavor selection. The next missing arrow is

\[
\text{source-related holonomy pair}
\longrightarrow
\text{proper executable word module}
\longrightarrow
\text{physical16}.
\]

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp944_two_holonomy_universal_algebra_no_selector.py

Generated result: `research/flavor/results/wp944_two_holonomy_universal_algebra_no_selector.json`.
