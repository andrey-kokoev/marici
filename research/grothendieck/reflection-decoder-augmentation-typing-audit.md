# Reflection decoder homology is relative fiber homology, not yet physical support

## Question

Nima's reflection-depth decoder over

\[
A=\mathbb Q[z]/(z^2)
\]

has a finite constructor alphabet \(S\), chain groups

\[
C_n=A\otimes\mathbb Q[S^n],
\]

and differentials given, up to alternating nonzero rational scalars, by

\[
d_n=z\,\pi_!,
\]

where \(\pi:S^n\to S^{n-1}\) forgets the last letter and \(\pi_!\) sums over
each child fiber. For \(|S|=4\), are the three surviving directions a
predeclared relative object or merely the four-letter augmentation ideal?

## Exact identification

Write an element of \(C_n\) uniquely as \(a+zb\), with
\(a,b\in\mathbb Q[S^n]\). Since \(z^2=0\),

\[
d_n(a+zb)=z\pi_!(a).
\]

Therefore

\[
\ker d_n
=\ker\pi_!\oplus z\mathbb Q[S^n].
\]

The parent-folding map is surjective, so

\[
\operatorname{im}d_{n+1}=z\mathbb Q[S^n].
\]

The entire nilpotent summand cancels in homology, leaving the canonical
isomorphism

\[
\boxed{
H_n\cong\ker(\pi_!: \mathbb Q[S^n]\to\mathbb Q[S^{n-1}]).
}
\]

Fiberwise,

\[
\mathbb Q[S^n]
\cong
\mathbb Q[S^{n-1}]\otimes\mathbb Q[S],
\qquad
\pi_!=1\otimes\epsilon_S,
\]

where \(\epsilon_S:\mathbb Q[S]\to\mathbb Q\) is augmentation. Hence

\[
\boxed{
H_n\cong
\mathbb Q[S^{n-1}]\otimes I_S,
\qquad
I_S=\ker\epsilon_S=\widetilde H_0(S;\mathbb Q).
}
\]

For four letters, \(I_S\) is exactly the three-dimensional sibling-difference
space. Thus it is both:

1. a genuine relative object internal to the free branching construction,
   namely reduced degree-zero homology of each child fiber; and
2. the augmentation ideal of the chosen constructor alphabet.

Those descriptions are identical, not competing explanations.

## Naturality and the decisive failure

For a map of alphabets \(f:S\to T\), linearization commutes with augmentation:

\[
\epsilon_T\mathbb Q[f]=\epsilon_S.
\]

Consequently \(\mathbb Q[f]\) induces \(I_S\to I_T\), and the decoder homology
is natural under alphabet maps. But it is invariant only under bijective
relabeling. If a refinement \(r:S'\twoheadrightarrow S\) splits constructor
letters, then

\[
\dim I_{S'}-\dim I_S=|S'|-|S|,
\]

and the induced map has a new vertical kernel recording differences among
letters that the coarser presentation identifies. This is exactly Nima's

\[
\dim H_n^{(k)}=(k-1)k^{n-1}
\]

constructor-dependence falsifier in structural form.

Therefore ordinary functoriality is too weak. A physical interpretation would
require a source-derived channel object \(S_{\rm src}\), source-derived fold,
and a comparison to a predeclared relative/support object that is covariant
under the sector's admissible presentation changes. No such comparison is
supplied by the four-letter self-model vocabulary.

## Verdict

\[
\boxed{
\text{The three directions are canonical relative fiber homology of the
chosen constructor, but are not a presentation-independent physical object.}
}
\]

The exact identification clarifies rather than rescues the rank coincidence.
It says what the syndrome means internally: it measures information discarded
by sibling folding. To give it Marici-sector meaning, one must derive the
siblings and their folding from a source carrier and then prove descent of the
role, not merely existence of the augmentation kernel.

## Sharp next falsifier

Given a proposed source comparison

\[
\tau:\mathbb Q[S^{n-1}]\otimes I_S\longrightarrow\mathcal R_{\rm src},
\]

choose two source-equivalent presentations connected by an admitted
refinement or regrouping. Transport both decoder objects and test the square
with \(\tau\). A nonzero image of the refinement kernel, or disagreement after
regrouping, proves that \(\tau\) detects constructor vocabulary rather than
source-relative information.

This is a faithful-coordinate test: dimension, a fitted basis, or a scalar
readout cannot establish the comparison.
