# RS-1 first source audit: modular norm homology versus the free syndrome

## Candidate source object

Grothendieck's finite p-group theorem supplies exactly the kind of independently
derived data RS-1 requires. For a nontrivial finite p-group \(K\),

\[
A=\mathbb F_p[K],
\qquad
\epsilon:A\to\mathbb F_p,
\qquad
I=\ker\epsilon,
\qquad
\nu_K=\sum_{g\in K}g.
\]

Multiplication by \(\nu_K\) is square-zero and has

\[
\ker m_{\nu}=I,
\qquad
\operatorname{im}m_{\nu}=\mathbb F_p\nu_K,
\]

so

\[
H(A,m_\nu)=I/(\mathbb F_p\nu_K),
\qquad
\dim H=|K|-2.
\]

This derives a channel object, augmentation, differential, invariant line, and
reduced residual without reference to our self-model vocabulary.

## Hostile comparison

Our four-constructor decoder gives at its first stable grade

\[
H_1^{\rm free}\simeq
\ker(\mathbb Q^4\mathop{\longrightarrow}^{\sum}\mathbb Q),
\qquad
\dim H_1^{\rm free}=3.
\]

For \(K=C_5\) in characteristic five,

\[
H(\mathbb F_5[C_5],m_\nu)
=I/(\mathbb F_5\nu),
\qquad
\dim H=3.
\]

The ranks agree, but the typed objects do not:

- four channels over characteristic zero versus five channels over
  characteristic five;
- augmentation kernel versus augmentation kernel modulo its invariant norm
  line;
- no declared \(C_5\)-action on the four-constructor syndrome;
- no physical relative-chain pushforward for the modular source object.

Therefore

\[
\boxed{
\dim H_1^{\rm free}=\dim H_{C_5}=3
\quad\text{is a forbidden rank coincidence, not a comparison map}.}
\]

## Source-induced correction to the decoder architecture

If a sector genuinely derives five modular channels, the source architecture
predicts two reductions:

\[
\mathbb F_5^5
\longrightarrow
I\quad(\dim4)
\longrightarrow
I/(\mathbb F_5\nu)\quad(\dim3).
\]

Our free decoder models only the first reduction. The norm correspondence
supplies a second correction direction that our four-symbol mechanism lacks.

This is progressive for RS-1: the source does not merely match a rank; it
predicts a missing differential and an invariant-line quotient.

## Remaining gate

The modular norm packet explicitly lacks a physical relative-chain
pushforward. Consequently it is an algebraic source candidate, not yet a
physical coefficient object. The next admissible question is whether any
Marici sector independently realizes a regular \(C_5\) fiber and its norm
correspondence. Until then, neither three-plane is physically identified.

