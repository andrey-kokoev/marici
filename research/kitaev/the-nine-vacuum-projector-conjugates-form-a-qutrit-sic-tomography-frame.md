# The nine vacuum-projector conjugates form a qutrit SIC tomography frame

Owner: `marici.Kitaev`

## Bounded question

What informational capability is supplied by the orbit of the native vacuum
fusion projector under the finite braid-plus-cube-root qutrit group?

Its orbit consists of nine equiangular rank-one projectors forming a qutrit
symmetric informationally complete frame. After normalization by one third,
they form a nine-outcome SIC POVM. Their expectations reconstruct every qutrit
state by an exact linear formula.

Thus the same finite constructor group that is nonuniversal for actuation is
minimal and complete for state tomography, conditional on physical access to
the orbit effects.

## Exact orbit

Use the monomial basis

\[
|q_0\rangle,
\qquad
|q_1\rangle,
\qquad
|q_2\rangle.
\]

The native vacuum fusion state is

\[
|A_L\rangle
=
{|q_1\rangle+|q_2\rangle\over\sqrt2}.
\]

The finite group `G(3,1,3)` permutes the coordinate axes and independently
multiplies them by cube-root phases. Its orbit of the vacuum line is therefore

\[
|\psi_{ij}^{(k)}\rangle
=
{|q_i\rangle+\omega^k|q_j\rangle\over\sqrt2},
\]

where

\[
0\le i<j\le2,
\qquad
k\in\mathbb Z/3.
\]

There are three coordinate pairs and three relative phases, hence nine lines.
This agrees with the orbit--stabilizer count

\[
162/18=9
\]

from the finite group and vacuum-projector stabilizer packets.

Let

\[
P_{ij}^{(k)}
=
|\psi_{ij}^{(k)}\rangle
\langle\psi_{ij}^{(k)}|.
\]

## Equiangularity

For two states on the same coordinate pair with different relative phases,

\[
\left|
\langle\psi_{ij}^{(k)}|\psi_{ij}^{(l)}\rangle
\right|
=
{ |1+\omega^{l-k}|\over2}
=
{1\over2}.
\]

For states on different coordinate pairs, the two supports share exactly one
coordinate. Their inner product contains one unit-modulus term divided by two,
so again

\[
\left|
\langle\psi_{ij}^{(k)}|\psi_{mn}^{(l)}\rangle
\right|
=
{1\over2}.
\]

Therefore every distinct pair obeys

\[
\operatorname{Tr}
\left(
P_\alpha P_\beta
\right)
=
{1\over4}.
\]

In dimension three this is the SIC value

\[
{1\over d+1}={1\over4}.
\]

## Tight-frame identity

Fix one coordinate pair `i,j` and sum its three phase projectors. The
off-diagonal cube-root coefficients cancel:

\[
\sum_{k=0}^2P_{ij}^{(k)}
=
{3\over2}
(E_{ii}+E_{jj}).
\]

Each coordinate belongs to two of the three pairs. Hence the complete sum is

\[
\sum_{\alpha=1}^9P_\alpha=3I.
\]

The normalized effects

\[
E_\alpha={1\over3}P_\alpha
\]

therefore satisfy

\[
\sum_\alpha E_\alpha=I.
\]

They define a nine-outcome qutrit SIC POVM.

## Minimal informational completeness

The projector Gram matrix is

\[
G_{\alpha\beta}
=
\begin{cases}
1,&\alpha=\beta,\\
1/4,&\alpha\ne\beta.
\end{cases}
\]

Equivalently,

\[
G={3\over4}I_9+{1\over4}J_9.
\]

Its eigenvalue on the all-ones vector is

\[
3,
\]

and its eigenvalue on the eight-dimensional orthogonal complement is

\[
{3\over4}.
\]

The Gram matrix is invertible, so the nine projectors form a basis of the
nine-dimensional real Hermitian qutrit operator space.

No informationally complete POVM on a qutrit can have fewer than

\[
d^2=9
\]

outcomes. This orbit attains the lower bound.

## Exact state reconstruction

For a qutrit state `rho`, define the SIC probabilities

\[
p_\alpha
=
\operatorname{Tr}(\rho E_\alpha)
=
{1\over3}\operatorname{Tr}(\rho P_\alpha).
\]

The standard dual-frame calculation gives

\[
\rho
=
4\sum_{\alpha=1}^9p_\alpha P_\alpha-I.
\]

Thus the complete density matrix, including every imaginary coherence, is a
linear function of the nine outcome probabilities.

The cube-root phases are exactly what rotate the original real vacuum effect
into the missing complex quadratures.

## One POVM versus nine settings

The nine nonorthogonal effects cannot be outcomes of one ordinary projective
measurement on the qutrit alone. A genuine single-setting SIC instrument
requires a Naimark dilation or another generalized-measurement constructor
with a nine-valued pointer.

There is a weaker multi-setting implementation target:

1. choose one orbit unitary `g_alpha`;
2. apply its inverse to a prepared qutrit copy;
3. test the native vacuum effect `P_A`;
4. retain the setting label and binary outcome;
5. repeat for all nine settings.

The nine conditional yes-probabilities reconstruct the same expectations.
This is tomography across settings, not one nine-outcome POVM. Randomly
choosing a setting and hiding its label destroys informational completeness.

## Tester versus actuator boundary

The SIC frame is a tester capability on prepared copies. It does not imply
that an arbitrary unknown data qutrit can be measured nondestructively or that
the finite gate group can synthesize every qutrit unitary.

Conversely, the continuous vacuum corridor plus discrete braids is
algebraically universal for actuation, but universal control does not by
itself provide a calibrated SIC readout. Preparation, gates, vacuum effect,
and pointer response must be typed separately.

This gives an exact four-way separation:

- finite gate reachability: 54 projective unitaries;
- associative span: every qutrit matrix;
- state-tomography effects: nine SIC projectors;
- continuous actuation: conditional full `U(3)` from the vacuum corridor.

## Circularity boundary

The nine orbit effects use the magnetic cube-root gate to generate their
complex phases. They cannot be the sole evidence certifying that same gate's
physical corridor.

Valid uses include:

- testing another independently implemented qutrit constructor after the
  magnetic gate and vacuum effect are calibrated;
- cross-checking the continuous vacuum corridor;
- performing sacrificial state tomography;
- detecting drift away from the declared finite constructor model.

Self-tomography of the magnetic phase requires an additional reference or a
self-consistency theorem strong enough to exclude common-mode conjugate
models. Agreement with SIC algebraic relations alone is not sufficient.

## Frame faults

A fixed common conjugation of all nine effects preserves their SIC Gram matrix
and reconstructs states in the conjugated frame. Internal tomography remains
consistent while external logical labels are wrong.

Permuting outcome labels also preserves the unlabeled SIC geometry. Therefore
the apparatus must anchor:

- which line is the native vacuum effect;
- which braid word identifies each coordinate pair;
- which magnetic orientation is called `omega` rather than `omega^2`;
- which pointer label corresponds to each effect.

Purity and spectrum are invariant under a common unitary frame fault, while
signed logical matrix entries are not.

## Process tomography boundary

Informationally complete output effects do not alone reconstruct an unknown
channel. Process tomography additionally needs a spanning family of prepared
inputs, or an entangled faithful input and joint output measurement.

If both SIC preparations and effects are independently compiled, their
`9 by 9` transition table is process-informationally complete. The current
packet derives only the effect-frame algebra and its state reconstruction
formula.

## Exact falsifiers

- An orbit size other than nine.
- Two distinct orbit lines having overlap modulus other than one half.
- The projector sum differing from `3I`.
- The projector Gram matrix having a zero eigenvalue.
- Fewer than nine qutrit POVM outcomes claimed informationally complete.
- The displayed SIC probabilities failing the reconstruction formula.
- Nine sequential binary settings called one nine-outcome projective
  measurement.
- The setting label discarded while completeness is retained.
- SIC effect completeness promoted to unitary gate universality.
- The magnetic gate used as its own sole complex calibration reference.
- Internal SIC geometry claimed to fix an external logical frame.
- Output-effect completeness alone promoted to process tomography.

## Shared Carrier geometry and quantum coefficient lens

Shared Carrier geometry supplies group orbits, stabilizers, tight frames,
effect completeness, setting labels, Naimark dilation, reconstruction versus
actuation, and common-frame faults.

The quantum coefficient lens supplies the qutrit cube-root phases, electric
braid permutations, native vacuum effect, SIC overlap, and protected fusion
interpretation.

## Result

The finite magnetic-braid constructor group transports one native vacuum
effect into a minimal qutrit SIC tomography frame. The orbit is complete for
state reconstruction even though the same group is finite and nonuniversal
for actuation. Physical use remains conditional on independently compiled
orbit gates, vacuum readout, setting retention, and frame calibration.

No build or checker was run for this research-only packet.
