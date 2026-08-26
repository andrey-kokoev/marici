# Crossed-polarizer context insertion theorem

## Bounded question

What does a third polarizer establish when it makes light pass through two
crossed endpoint polarizers, and which parts of the ordered optical realization
can be reconstructed from endpoint intensity?

## Frozen conventions

Work in the real Jones plane with normalized linear-polarization vectors

\[
|\theta\rangle=
\begin{pmatrix}
\cos\theta\\
\sin\theta
\end{pmatrix},
\qquad
P_\theta=|\theta\rangle\langle\theta|.
\]

Angles are identified modulo \(\pi\). Polarizers are ideal rank-one filters.
There is no birefringent phase, loss beyond ideal filtering, depolarization,
detector threshold, or multiple reflection. Intensities are normalized to the
intensity \(I_1\) after preparation by the first polarizer.

## Ordered-word theorem

For an ordered word with input angle \(\theta_0\), output angle \(\theta_q\),
and \(q-1\) intermediate polarizers,

\[
W=P_{\theta_q}P_{\theta_{q-1}}\cdots P_{\theta_1}P_{\theta_0},
\]

the transmitted amplitude from the prepared input ray to the output ray is

\[
A(W)
=
\langle\theta_q|
P_{\theta_{q-1}}\cdots P_{\theta_1}
|\theta_0\rangle
=
\prod_{j=0}^{q-1}
\cos(\theta_{j+1}-\theta_j).
\]

Hence

\[
\frac{I_{\mathrm{out}}}{I_1}
=
\prod_{j=0}^{q-1}
\cos^2(\theta_{j+1}-\theta_j).
\]

The proof is repeated use of

\[
P_\beta|\alpha\rangle
=
\langle\beta|\alpha\rangle|\beta\rangle
=
\cos(\beta-\alpha)|\beta\rangle.
\]

The word transmits nonzero amplitude exactly when no adjacent pair is
orthogonal.

## Crossed endpoints and one insertion

Take

\[
\theta_0=0,
\qquad
\theta_2=\frac{\pi}{2}.
\]

Without an intermediate polarizer,

\[
P_{\pi/2}P_0=0.
\]

Insert \(P_\theta\). Then

\[
A(\theta)=\cos\theta\sin\theta
=
\frac12\sin2\theta,
\]

and

\[
\frac{I_{\mathrm{out}}(\theta)}{I_1}
=
\cos^2\theta\sin^2\theta
=
\frac14\sin^22\theta.
\]

At \(\theta=\pi/4\), the transmitted fraction is \(1/4\).

## Creation versus revelation

The comparison is between two different constructor words:

\[
P_{\pi/2}P_0
\]

and

\[
P_{\pi/2}P_\theta P_0.
\]

The inserted polarizer does not passively reveal intensity transmitted by the
first word. It changes the channel by creating an allowed sequence of nonzero
adjacent overlaps.

What the experiment tests is the shared composition law. The same projector
model that predicts extinction for the two-factor word predicts transmission
for the three-factor word without independently fitting a new endpoint value.

This is explanatory evidence through relation-locked counterfactuals, not a
measurement of a hidden pre-insertion output.

## Optimal monotone chain theorem

Fix crossed endpoints and \(q-1\) intermediate polarizers on the monotone
shortest angular route. Define increments

\[
\Delta_j=\theta_{j+1}-\theta_j,
\qquad
\Delta_j\ge0,
\qquad
\sum_{j=0}^{q-1}\Delta_j=\frac{\pi}{2}.
\]

Then

\[
\frac{I_{\mathrm{out}}}{I_1}
\le
\cos^{2q}\left(\frac{\pi}{2q}\right),
\]

with equality exactly when

\[
\Delta_0=\cdots=\Delta_{q-1}=\frac{\pi}{2q}.
\]

For nonzero transmission, every increment lies in \([0,\pi/2)\). The function

\[
f(x)=\log\cos x
\]

is strictly concave there because

\[
f''(x)=-\sec^2x<0.
\]

Jensen's inequality gives

\[
\sum_{j=0}^{q-1}\log\cos\Delta_j
\le
q\log\cos\left(\frac{\pi}{2q}\right).
\]

Exponentiation and squaring prove the bound and its equality condition.

As \(q\to\infty\),

\[
\cos^{2q}\left(\frac{\pi}{2q}\right)
\longrightarrow1.
\]

Thus increasingly fine, evenly spaced filtering can transport the polarization
between crossed endpoints with asymptotically unit conditional transmission.
This is the finite projector-chain form of polarization Zeno transport.

The theorem is restricted to the declared monotone shortest route. It does not
optimize arbitrary winding angle lists or account for per-element insertion
loss.

## Endpoint-intensity fibre for one unknown insertion

On the declared interval

\[
0\le\theta\le\frac{\pi}{2},
\]

endpoint intensity is

\[
r(\theta)=\frac14\sin^22\theta.
\]

It satisfies

\[
r(\theta)=r\left(\frac{\pi}{2}-\theta\right).
\]

For every \(0<r<1/4\), the fibre contains exactly two angles:

\[
\left\{\theta,\frac{\pi}{2}-\theta\right\}.
\]

At \(r=1/4\), the fibre is the singleton \(\{\pi/4\}\). At \(r=0\), it contains
the two endpoint insertions \(\{0,\pi/2\}\).

The coherent real amplitude

\[
A(\theta)=\frac12\sin2\theta
\]

has the same reflection symmetry. Measuring that amplitude without an internal
context does not resolve the two-angle fibre.

## Minimal internal separator

Place one intensity tap immediately after the unknown middle polarizer. Its
normalized value is

\[
s(\theta)=\cos^2\theta.
\]

On \([0,\pi/2]\), \(s\) is strictly decreasing and therefore injective. The pair

\[
(r(\theta),s(\theta))
\]

reconstructs \(\theta\) uniquely on the declared interval.

Endpoint intensity alone is not injective, while one additional scalar internal
tap is sufficient. Therefore one internal scalar context is cardinal-minimal
for this one-parameter packet when no half-interval prior is authorized.

The tap changes the instrument architecture and can disturb a physical beam.
The statement is an algebraic interface theorem, not a claim of nondisturbing
laboratory access.

## Ordered lens versus scalar lens

The scalar lens retains

\[
|A(W)|^2.
\]

The coherent lens retains \(A(W)\), once a phase reference is fixed. The ordered
lens retains the word

\[
(P_{\theta_q},\ldots,P_{\theta_0}).
\]

Neither intensity nor one total amplitude generally reconstructs the word.
Factorizations of the same scalar transition are nonunique.

The noncommutativity is explicit:

\[
P_\beta P_\alpha
=
\cos(\beta-\alpha)|\beta\rangle\langle\alpha|,
\]

whereas

\[
P_\alpha P_\beta
=
\cos(\beta-\alpha)|\alpha\rangle\langle\beta|.
\]

They are generally different operators even when a reciprocal endpoint
intensity experiment assigns them the same scalar transmission.

## Obstruction classification

For the one-insertion crossed packet:

- the source object is the labelled angle \(\theta\in[0,\pi/2]\);
- the endpoint record is \(r(\theta)\);
- the reflection \(\theta\leftrightarrow\pi/2-\theta\) is not gauge when the
  middle polarizer orientation is source-labelled;
- endpoint intensity therefore fails by global multiplicity;
- the internal tap kills that two-point fibre;
- arbitrary word reconstruction remains unresolved and is not claimed.

This is a Gate 2 repair in the unified obstruction register. No completion
claim is involved in the fixed finite packet.

## Hostile extensions

The ideal theorem should next be attacked by adding one effect at a time.

1. **Insertion loss:** multiply each stage by an independently measured
   efficiency and test whether equal-step angular optimality survives.
2. **Birefringent phase:** replace real rays by complex Jones vectors and test
   which phase contexts recover Pancharatnam-type cycle data.
3. **Depolarization:** replace Jones operators by Mueller matrices or quantum
   channels and test when one coherent word model ceases to exist.
4. **Finite extinction:** replace rank-one projectors by full-rank diattenuators
   and measure how the exact zero becomes a small but nonzero baseline.
5. **Detector threshold:** test whether a mathematically nonzero route becomes
   operationally invisible and compute the criticism margin.
6. **Tap disturbance:** model the separator as an instrument rather than a free
   readout and price the information gained against transmission changed.

Each extension changes one source type. They should not be combined before the
first residual is isolated.

## Exact falsifiers

- Any ideal word whose measured intensity differs from the adjacent-overlap
  product falsifies the frozen model.
- A non-equal monotone angle partition exceeding the equal-step bound falsifies
  the optimization theorem.
- Two distinct angles in \([0,\pi/2]\) with equal endpoint and internal-tap
  intensities falsify the minimal separator theorem.
- Treating the inserted polarizer as a passive observation of the original
  two-factor output falsifies the constructor typing.
- Claiming arbitrary word reconstruction from one endpoint intensity exceeds
  the proved fibre result.

## Shared Carrier geometry versus optical coefficient lens

The shared Carrier contribution is the labelled ordered route, insertion site,
endpoint structure, and refinement of one route into several adjacent steps.

The optical coefficient lens supplies Jones rays, inner products, rank-one
projectors, and Malus-law intensity. A different lens could place stochastic,
noncommutative, or lossy coefficients on the same route while retaining the
Carrier factorization.

## Claim boundary

This is an exact finite theorem for ideal real Jones projectors. It establishes
ordered contextuality, the optimal monotone crossed-polarizer chain, a complete
one-insertion endpoint fibre, and a cardinal-minimal internal scalar separator.

It does not establish a laboratory apparatus, nondisturbing tap, coherent phase
protocol, Mueller-channel extension, or physical Zeno limit with per-polarizer
loss. Those require Aspect's optical source and instrument authority.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
9/10. The frozen optionality test was whether the system produced a genuine
ordered-context and minimal-separator theorem rather than only a Malus-law
example. The main confound was ideal-projector physics.

Post-objective: excitement 10/10, confidence 9.5/10, realized information gain
9.5/10. The ordered-context branch survived: insertion changes the constructor
word; equal angular subdivision is uniquely optimal on the monotone route; and
endpoint intensity has an exact two-point fibre killed by one internal scalar
tap. Laboratory loss, depolarization, and tap disturbance remain unresolved.
