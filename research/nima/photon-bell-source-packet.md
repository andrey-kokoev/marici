# Photon Bell source packet

## Source and scope

The first external packet is Sinha and Zahed, *Bell inequalities in 2-2
scattering*, arXiv:2212.10213v3, Phys. Rev. D 108, 025015 (2023).

The paper supplies exactly the data absent from the internal census:

- a fixed unentangled incoming helicity state;
- two outgoing photon helicity qubits sent to Alice and Bob;
- two Hermitian binary analyzers per wing;
- a normalized outgoing state and Born joint probabilities;
- a Bell functional and the quantum bound.

This is source-defined external input. It is not yet a derivation from the
Marici scattering Carrier.

## Exact low-energy specialization

For incoming helicity \(++\), the source's low-energy outgoing state is

\[
|\psi\rangle
=
\frac{\Phi_1|00\rangle+\Phi_2|11\rangle}
{\sqrt{|\Phi_1|^2+|\Phi_2|^2}}.
\]

For real \(\Phi_1=r\), \(\Phi_2=s\), its declared MES analyzers yield

\[
I=\frac{4\sqrt2\,rs}{r^2+s^2}.
\]

The exact checker constructs all sixteen joint probabilities for the four
setting pairs. Their four normalization residuals and eight no-signalling
residuals vanish identically. Moreover,

\[
2\sqrt2- I
=
\frac{2\sqrt2(r-s)^2}{r^2+s^2}
\geq0
\qquad(r,s\geq0),
\]

so the Tsirelson bound follows from the normalized Hilbert-space pairing, and
is saturated at \(r=s\ne0\).

## What changed

Entry 1569 was a census of the admitted repository and remains correct: the
internal transmutation packet does not contain detector instruments. The
external source shows that the missing layer is finite and explicit rather
than conceptually ambiguous.

The Marici question is now a comparison-map question:

\[
\text{Ward-reduced amplitude object}
\longrightarrow
\text{positive helicity density object with local effects}.
\]

The sharp test is whether this map, its conjugate copy, and the local projector
effects commute with physical Cut and survive the complete relative
totalization. Importing the source's probability formula proves that a Bell
packet exists in scattering theory; it does not prove that the Carrier
generates it.
