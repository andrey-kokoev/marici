# Four-phase rotation, quotient and cone: Ramsey comparison at k = 3–10

Date: 2026-11-08  
Status: working mathematical note; distinguishes derived identities, source results and exploratory interpretations.  
Scope: configurations R/G/0; cyclic index reversal; Fourier four-phase action; three-packet rotation/quotient; a five-dimensional cone cutting two antipodal four-cube vertices.

## 1. The initial records

For each integer k from 3 to 10, use a row of k cells. Its last two entries are empty; its first k-2 entries alternate R,G, beginning with R:

| k | Input row | Reference R(3,k) |
|---:|---|---:|
| 3 | `R00` | 6 |
| 4 | `RG00` | 9 |
| 5 | `RGR00` | 14 |
| 6 | `RGRG00` | 18 |
| 7 | `RGRGR00` | 23 |
| 8 | `RGRGRG00` | 28 |
| 9 | `RGRGRGR00` | 36 |
| 10 | `RGRGRGRG00` | 40–41 (bounds) |

These are symbolic input configurations. The letters R and G have not been assigned values necessary for the linear-algebra calculations below. A prior proposal B = i√a, R = √a, G = a remains a proposed separate encoding. Index operations and symbol algebra are distinct.

## 2. Exact four-phase Fourier operation

Fix n = k and zero-based indices j,l in Z/nZ. On complex row/column coefficients define the normalized discrete Fourier matrix (positive-sign convention)

\[
(F_n)_{jl}=n^{-1/2}\exp(2\pi i jl/n).
\]

Define the cyclic point-reversal permutation P_n by `(P_n x)_j = x_{-j mod n}`. The standard geometric-sum identity gives

\[
F_n^2=P_n, \qquad F_n^4=I_n.
\]

Thus the sequence `x, F_n x, P_n x, F_n^3 x, x` closes exactly for every n. The second step preserves index 0 and reverses indices 1..n-1. Fourier steps act on coefficients and generally produce complex linear combinations; they are not merely red/green cell permutations.

The four phase projectors for eigenvalues λ in {1,-1,i,-i} are

\[
E_{\lambda,n}=\frac14\sum_{s=0}^3\lambda^{-s}F_n^s,
\qquad E_{\lambda,n}^2=E_{\lambda,n},
\qquad\sum_\lambda E_{\lambda,n}=I_n.
\]

Their ranks (confirmed by numerical matrix checks of idempotence at tolerance 1e-12; exact values also follow from traces of F_n, F_n² and conjugate F_n) are:

| n | rank E_1 | rank E_-1 | rank E_i | rank E_-i | Sum |
|---:|---:|---:|---:|---:|---:|
| 3 | 1 | 1 | 1 | 0 | 3 |
| 4 | 2 | 1 | 1 | 0 | 4 |
| 5 | 2 | 1 | 1 | 1 | 5 |
| 6 | 2 | 2 | 1 | 1 | 6 |
| 7 | 2 | 2 | 2 | 1 | 7 |
| 8 | 3 | 2 | 2 | 1 | 8 |
| 9 | 3 | 2 | 2 | 2 | 9 |
| 10 | 3 | 3 | 2 | 2 | 10 |

One phase dimension is added at each n. This identity alone is not a count of Ramsey vertices; a correspondence from phase objects to Ramsey-admissible configuration objects would have to be explicitly constructed.

## 3. Independent three-packet primitive: six oriented rays and four quarter-turns

The existing Marici construction begins with three consecutive directed two-endpoint packets and its source-defined cyclic successor

\[
C=\begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix},\quad C^3=I.
\]

Let

\[
Q=(I+C+C^2)/3,\quad P=I-Q,\quad J=(C-C^T)/\sqrt 3.
\]

The source establishes `rank(Q)=1`, `rank(P)=2`, `J²=-P`, and `QJ=JQ=0`. The images `P e_1, P e_2, P e_3` define three equally spaced unoriented axes in the contrast plane `x+y+z=0`; their two orientations give six rays. Define the derived operator

\[
U=Q+J.
\]

On the contrast plane U is a 90° rotation, and on the common line it is the identity. Directly,

\[
U^2=Q-P,\qquad U^3=Q-J,\qquad U^4=I,
\]

and its four-phase average is the rank-one common-line projector:

\[
\boxed{(I+U+U^2+U^3)/4=Q.}
\]

The derived U belongs to the three-packet coefficient space R³, not the n-cell Fourier space C^n. An adapter relating them has not been specified. The three axes in this construction are coefficient-plane axes, rather than three independently derived spatial rotation axes in three dimensions.

Source: [Three consecutive two-packets generate a complex plane and half-phase lift](https://github.com/andrey-kokoev/marici/blob/7afcae687310b5db324ebfab4fbfe26444c73758/research/nima/triangle-half-phase-primitive.md).

## 4. Retained return versus erased history: established precedents

Several Marici constructions distinguish an ordinary closed orbit from a retained-state return.

- [Four-port Fourier orbit](https://github.com/andrey-kokoev/marici/blob/7afcae687310b5db324ebfab4fbfe26444c73758/research/grothendieck/generic-rational-cosets-form-an-exact-four-port-fourier-orbit.md) gives `support -> character -> reflected support -> reflected character -> support`. A one-port special case exists at a fixed point.
- [Four-chart convolution/Fourier realization](https://github.com/andrey-kokoev/marici/blob/7afcae687310b5db324ebfab4fbfe26444c73758/research/nima/four-chart-fourier-convolution-realization.md) alternates the product, with exact chart-typed Fourier squares and four-step closure.
- [Two-polarity four-chart successor seam](https://github.com/andrey-kokoev/marici/blob/7afcae687310b5db324ebfab4fbfe26444c73758/research/nima/a-source-cycle-selector-makes-the-two-polarity-four-chart-seam-faithful.md) constructs a source-defined fourth-to-first seam; a return in the displayed Fourier chart need not restore the original source record.
- [Four-chart suspension helix](https://github.com/andrey-kokoev/marici/blob/7afcae687310b5db324ebfab4fbfe26444c73758/research/voevodsky/a-clean-universal-category-for-the-eight-lattice-four-chart-suspension-system.md) defines `q⁴=Σ`, returning to the chart phase with a shift in retained grade.

These are concrete alternative descriptions of four-stage structure, with different source spaces and different meanings of quotient and return. Equality of the stage count does not provide a map between them.

## 5. Exact cone section cutting two opposite vertices of a 4-cube

Let the four-dimensional cube be `[-1,1]^4`, with 16 vertices. The full cone over it is the five-dimensional cone

\[
K_0=\{(x,t)\in\mathbb R^4\times\mathbb R:\ t\ge0,\ |x_i|\le t\}.
\]

Consider the subcone obtained by imposing

\[
-2t\le\sum_{i=1}^4 x_i\le2t.
\]

At height t=1, the 16 original cube corners are classified by the number h of negative coordinates. Their sums are `4−2h`:

| h | Sum | Number of original corners retained |
|---:|---:|---:|
| 0 | 4 | 0 |
| 1 | 2 | 4 |
| 2 | 0 | 6 |
| 3 | -2 | 4 |
| 4 | -4 | 0 |

The section has exactly 14 vertices: 4+6+4. No new vertices are introduced by these particular cuts, because every original cube edge connects corners whose sums differ by exactly 2; each cutting hyperplane meets a crossing edge at its original endpoint. The two removed corners are `(1,1,1,1)` and `(-1,-1,-1,-1)`.

Thus `16−2=14` is a genuine incidence result. It numerically equals `R(3,5)`. The thresholds ±2t are specified as part of this cone construction, rather than derived from the four-phase Fourier action.

## 6. Status of the Ramsey comparison

Exact mathematical results assembled here:

1. Fourier four-step law `F_n²=P_n`, `F_n⁴=I` for every n.
2. Phase-projector ranks at n=3..10.
3. The source-derived three-packet quarter-turn `U=Q+J` and the rank-one averaging identity.
4. A five-dimensional cone with a 14-vertex four-dimensional section obtained by removing two opposite cube corners.

Active proposed connection: derive a single source-defined transformation of the R/G/0 records which induces the relevant Fourier or contrast-plane operators, retains the history/quotient rules, and selects the same geometric completion operation. The previous `4×7=28` or `4×9=36` raw cell counts arose from an alternative permutation-based counting convention, not from Fourier phase-projector ranks; they are exploratory observations rather than deductions from this four-phase Fourier model.

The next discriminator can be local: explicitly compute the image of the initial `RGR00` or `RGRGRG00` source record under a proposed common operation and compare all retained states, then calculate its quotient. Do not tune the quotient using the known Ramsey number.
