# The Full Residue-Character Lift Makes Every Finite Mellin Zero Interference

## Finite labelled packet

Let \(L\subset\mathbb N\) be any finite set of distinct arithmetic labels.
Choose an integer conductor \(Q\) larger than every element of \(L\).
Then reduction modulo \(Q\) is injective on \(L\).

For \(0\leq k<Q\), let

\[
\chi_k(n)=e^{2\pi i kn/Q}
\]

be the additive characters of \(\mathbb Z/Q\mathbb Z\).

Define the character analysis map

\[
\mathcal F_{Q,L}:
\mathbb C^L
\longrightarrow
\mathbb C^Q
\]

by

\[
\bigl(\mathcal F_{Q,L}c\bigr)_k
=
\sum_{n\in L}c_n\chi_k(n).
\]

## Exact injectivity

The full discrete Fourier transform on \(\mathbb Z/Q\mathbb Z\) is
invertible. Extending \(c\) by zero outside the distinct residues represented
by \(L\), one obtains

\[
\mathcal F_{Q,L}c=0
\quad\Longrightarrow\quad
c=0.
\]

Therefore the complete residue-character family is a faithful analysis port
for every finite labelled packet.

## Mellin transport remains faithful

At spectral parameter \(s\), Mellin transport multiplies the label
coordinate by the nonzero scalar \(n^{-s}\). Let

\[
D_s=\operatorname{diag}(n^{-s})_{n\in L}.
\]

Then \(D_s\) is invertible for every complex \(s\), so

\[
\mathcal F_{Q,L}D_s
\]

is injective for every \(s\).

The reciprocal route using \(n^{s-1}\) is likewise injective. No finite
spectral parameter creates a transport kernel once the full residue-character
carrier is retained.

## Scalar Mellin readout

The ordinary scalar Mellin sum is the trivial character row:

\[
M_L(s;c)
=
\sum_{n\in L}c_n n^{-s}.
\]

Its kernel is generally large. But if

\[
M_L(s;c)=0
\]

for nonzero \(c\), the full character packet
\(\mathcal F_{Q,L}D_sc\) is nonzero by injectivity.

Hence every finite scalar Mellin zero is destructive interference created by
projection to the trivial character. It is never route loss in the full
labelled arithmetic transport.

## Correction to the one-prime model

The one-prime depth-two mate retained only the trivial and reciprocal sign
ports. Its seam resonances were genuine kernels of that reduced two-route
packet.

They are not kernels after the complete residue-character lift. A character
that separates the two prime-power residues observes the previously dark
direction.

Thus those local seam resonances diagnose incomplete observation, not
intrinsic loss of the arithmetic source state.

## Profinite completion

As finite label sets grow, one may choose a cofinal family of conductors whose
residue maps separate every retained label. The compatible character systems
form the finite shadows of the Schwartz--Bruhat distributional carrier on the
finite adeles.

This supplies the analysis-side lift suggested by the Ramanujan packet
programme. Completion stability still requires the compatible topology, but
finite injectivity is exact.

## Mechanism theorem

At finite cutoff there are now three distinct possibilities:

1. transport loss, excluded by the complete character lift;
2. scalar interference, the only mechanism for a nonzero trivial-character
   dark packet;
3. transparent reconstruction, possible only when synthesis and analysis
   supports belong to disjoint components of a larger mate.

For the direct labelled Mellin packet with its complete character analysis,
the third mechanism is also absent: every label is in the shared Fourier
corner.

## Consequence for RH

A nontrivial zero of the completed scalar section should not be interpreted as
disappearance of the full arithmetic state. The full source packet remains
distinguishable; only its scalar augmentation is dark.

Therefore an RH proof cannot proceed by showing that off-seam transport
kernels are impossible. There are no finite transport kernels to begin with.

The remaining question is orientation of the interference packet:

> Why can the source-derived trivial-character projection become dark only
> when the reciprocal interference has critical-line orientation?

This requires a cyclic or nonlinear coherence invariant. Additional linear
character ports classify the hidden packet but do not constrain where its
trivial component vanishes.

## Next target

Construct the smallest source-framed cycle involving:

1. Mellin label transport;
2. residue-character Fourier analysis;
3. reciprocal Tate sewing;
4. return to the trivial-character determinant line.

Then compare its holonomy on:

- the actual arithmetic packet;
- a hostile divisor-bearing symmetric modification.

If the cycle is equally coherent for both, the character lift is diagnostic
but not RH-bearing.

