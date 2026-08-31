# Integer coefficient pole-typing fiber: WP1039

## Question

Does selecting the integer coefficient \(C=23\) also select a typed
single-pole threshold operator?

## Zero-momentum collision

Keep the WP1036 capacity data fixed:

\[
k=2,
\qquad
C=23,
\qquad
h=\frac{138\pi^2}{1367}.
\]

At zero momentum, twenty-three unit-residue contributions give the same total
coefficient whether their poles are degenerate or split. The normalized
finite-momentum response at \(q^2=1\) separates the packets.

For twenty-three equal poles with \(M_i^2=1\),

\[
\frac{R(1)}{R(0)}=\frac12.
\]

For twenty-two poles with \(M_i^2=1\) and one pole with \(M_i^2=4\),

\[
\frac{R(1)}{R(0)}=\frac{59}{115}.
\]

The difference is

\[
\frac{59}{115}-\frac12=\frac{3}{230}.
\]

Both packets have the same \(k\), \(C\), zero-momentum \(h\), and number of
unit residues. They differ only in the finite pole spectrum.

## Classification

The first nonfaithful arrow is

\[
\{\text{integer coefficient and zero-momentum normalization}\}
\longrightarrow
\{\text{complete finite-momentum pole spectrum}\}.
\]

Thus even an independent theorem selecting \(C=23\) would not by itself close
the threshold gate. It must also type the operator as one degenerate pole, or
derive the full multi-pole spectrum and its matching map.

## Disposition

Negative for promoting WP1036 arithmetic capacity to threshold-ready physical
normalization. Reopening requires the same source that selects the integer
labels to derive residues, degeneracy, pole masses, and finite-momentum
matching before any `physical16` instrument is invoked.

Checker: `research/flavor/checkers/wp1039_integer_coefficient_pole_typing_fiber.py`

Result: `results/wp1039_integer_coefficient_pole_typing_fiber.json`
