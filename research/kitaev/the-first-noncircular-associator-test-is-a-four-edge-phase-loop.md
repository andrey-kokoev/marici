# The first noncircular associator test is a four-edge phase loop

Owner: `marici.Kitaev`

## Question

Can the electric `D(S3)` associator be tested coherently without pretending
that an absolute trivalent phase frame is physical or calibrating the
preparation mixer from the associator one intends to test?

Yes at the algebraic level. Open route phases transform under independent
left- and right-tree gauge choices, but phase products around cycles of the
left--right overlap graph are invariant. Because that graph is bipartite, its
smallest possible phase-bearing cycle has four edges. The frozen
`C,C,C`-to-`C` recoupling matrix has a four-edge cycle with exact normalized
holonomy `-1`.

The remaining physical question is whether the source supplies a coherent
ordered-product instrument that can measure this loop without collapsing it
into four separate transition probabilities.

## Claim boundary

This packet identifies and evaluates the smallest gauge-invariant associator
phase witness in the existing pure-electric fragment. It does not construct a
laboratory interferometer, prove mixed-sector coherence, or establish a
fault-tolerant implementation.

The loop is invariant under trivalent basis phases. It is not asserted to be a
complete invariant of a fusion category or a gapped phase.

## Two fusion-tree frames

Let

\[
P_e=|e_L\rangle\langle e_L|,
\qquad
Q_f=|f_R\rangle\langle f_R|
\]

for intermediate charges

\[
e,f\in\{A,B,C\}.
\]

The overlap matrix is

\[
F_{ef}=\langle e_L|f_R\rangle.
\]

In the established microscopic gauge,

\[
F=
\begin{pmatrix}
\frac12&\frac12&\frac1{\sqrt2}\\
-\frac12&-\frac12&\frac1{\sqrt2}\\
\frac1{\sqrt2}&-\frac1{\sqrt2}&0
\end{pmatrix}.
\]

Separate fusion-channel experiments measure

\[
\operatorname{Tr}(P_eQ_f)=|F_{ef}|^2.
\]

They therefore see only edge magnitudes in the bipartite graph joining left
vertices `e` to right vertices `f` whenever `F_ef` is nonzero.

## Trivalent gauge acts at graph vertices

Change the phases of the fusion-tree basis vectors by

\[
|e_L\rangle\longmapsto e^{i\alpha_e}|e_L\rangle,
\qquad
|f_R\rangle\longmapsto e^{i\beta_f}|f_R\rangle.
\]

Then

\[
F_{ef}\longmapsto
e^{-i\alpha_e}e^{i\beta_f}F_{ef}.
\]

An individual overlap phase is therefore not gauge invariant. Neither is the
designation of the open `A/B` superposition that appears bright at one right
port. That open fringe becomes operational only after a preparation phase
frame is independently attached.

## Internal experiments cannot self-calibrate the frame

The same obstruction appears in the general preparation--constructor--readout
model. Let `rho_a` be prepared states, `U` a coherent constructor, and `E_b`
readout effects. The observed probabilities are

\[
p(b|a)=\operatorname{Tr}(E_bU\rho_aU^*).
\]

For arbitrary input and output unitaries `G_L` and `G_R`, define

\[
\rho'_a=G_L\rho_aG_L^*,
\qquad
U'=G_RUG_L^*,
\qquad
E'_b=G_RE_bG_R^*.
\]

Then

\[
\operatorname{Tr}(E'_bU'\rho'_aU'^*)
=
\operatorname{Tr}(E_bU\rho_aU^*).
\]

No collection of probabilities generated wholly inside this jointly
transformed apparatus can select its attachment to an external source frame.
Longer internal sequences may identify a realization up to the same gauge;
they do not create an absolute reference.

When the labelled rank-one channel projectors are independently trusted, the
full unitary freedom shrinks to diagonal phase transformations. The remaining
phase ambiguity is still invisible to basis-channel probabilities.

## Coherence-anchor graph theorem

Suppose `n` labelled rank-one ports are fixed and the remaining gauge is

\[
D=\operatorname{diag}(e^{i\theta_1},\ldots,e^{i\theta_n}).
\]

An oriented coherence anchor on an edge `(i,j)` fixes the operator

\[
K_{ij}=|i\rangle\langle j|.
\]

Preserving this anchor requires

\[
\theta_i=\theta_j
\pmod{2\pi}.
\]

Let the admitted anchor edges form a graph with `c` connected components.
The residual phase stabilizer is constant on each component. After removing
the physically irrelevant global phase, it is

\[
U(1)^{c-1}.
\]

For real sign frames, the corresponding residual group is

\[
C_2^{c-1}.
\]

Consequently, all relative port phases are fixed exactly when the anchor graph
is connected. A minimal complete anchor on `n` ports has `n-1` edges.

For the open electric bright-dark witness, only the support `{A,B}` matters.
One independently calibrated `A--B` coherence edge fixes its relative sign.
For a fully calibrated three-channel input frame, two independent coherence
edges are necessary and sufficient. A separately calibrated three-channel
output frame requires two more unless source geometry identifies the two
phase references by an independently proved transport.

## Gauge-invariant cycle theorem

An alternative to fixing every vertex phase is to close the route. For two
left vertices `e,e'` and two right vertices `f,f'`, define

\[
\Omega_{ee';ff'}
=
F_{ef}F_{e'f'}
\overline{F_{ef'}}
\overline{F_{e'f}}.
\]

Every vertex phase occurs once with each orientation, so

\[
\Omega_{ee';ff'}
\longmapsto
\Omega_{ee';ff'}.
\]

The same number has the basis-free ordered-projector expression

\[
\Omega_{ee';ff'}
=
\operatorname{Tr}
\left(
P_eQ_fP_{e'}Q_{f'}
\right).
\]

This is a four-state Bargmann invariant. Its magnitude is fixed by the four
edge probabilities:

\[
|\Omega_{ee';ff'}|
=
\sqrt{
P_{ef}P_{e'f'}P_{ef'}P_{e'f}
}.
\]

Its complex phase is not contained in those probabilities.

More generally, gauge-invariant overlap monomials correspond to cycles in the
nonzero bipartite support graph. If that graph has `V` vertices, `E` edges,
and `c` connected components, its cycle-space rank is

\[
E-V+c.
\]

Before imposing unitarity or other source equations, this is the number of
independent cycle-phase coordinates. A support forest has no such coordinate;
all of its edge phases can be absorbed into vertex gauges.

For the displayed electric matrix, only the `C--C` edge is absent. Hence

\[
V=6,
\qquad
E=8,
\qquad
c=1,
\qquad
E-V+c=3.
\]

The raw overlap support therefore carries three cycle-phase coordinates before
orthogonality and the remaining source equations relate them.

## Exact electric loop

Choose

\[
e=A,
\qquad
e'=B,
\qquad
f=A,
\qquad
f'=C.
\]

The four overlaps are

\[
F_{AA}=\frac12,
\qquad
F_{BC}=\frac1{\sqrt2},
\qquad
F_{AC}=\frac1{\sqrt2},
\qquad
F_{BA}=-\frac12.
\]

Therefore

\[
\Omega_{AB;AC}
=
F_{AA}F_{BC}\overline{F_{AC}}\overline{F_{BA}}
=
-\frac18.
\]

The basis probability table determines only

\[
|\Omega_{AB;AC}|=\frac18.
\]

The normalized phase holonomy is

\[
\omega_{AB;AC}
=
\frac{\Omega_{AB;AC}}{|\Omega_{AB;AC}|}
=
-1.
\]

This sign survives every independent rephasing of the four participating
trivalent vertices. Unlike the open bright-dark designation, it does not need
an absolute choice of which `A/B` superposition is called plus.

## Why four edges are first

The overlap graph has two vertex types: left fusion channels and right fusion
channels. A route alternates between them. It therefore has no odd cycle.

A two-edge return merely gives

\[
F_{ef}\overline{F_{ef}}=|F_{ef}|^2.
\]

The first closed route capable of retaining phase has length four. This is not
an arbitrary experimental preference; it follows from the bipartite Carrier
geometry of two fusion-tree frames.

The coefficient lens determines the value transported around that cycle. For
ordinary positive transition data it is a magnitude. For the quantum lens it
is an ordered complex Bargmann invariant.

## Hostile realization with identical basis statistics

Let the coherent frame change be represented by a unitary `U` with transition
probabilities `P_ef`. Define the measure-and-prepare channel

\[
\mathcal M(\rho)
=
\sum_{e,f}
P_{ef}
\langle e_L|\rho|e_L\rangle
|f_R\rangle\langle f_R|.
\]

For every basis input `e` and basis output `f`, `U` and `M` give the same
probability `P_ef`. The channel `M` first destroys all coherence between left
routes, so it cannot preserve the four-amplitude phase loop.

This is the smallest realization-level hostile model. It does not need a
second unitary associator with the same moduli. It shows that the scalar table
cannot distinguish coherent reassociation from classical stochastic routing.

## Minimal noncircular instrument

To test the loop rather than its four edges separately, an admitted apparatus
must provide:

1. coherent access to the four rank-one ports `P_A`, `P_B`, `Q_A`, and `Q_C`;
2. an ordered product or equivalent coherent path superposition preserving the
   order `P_A Q_A P_B Q_C`;
3. a control reference that reads both real and imaginary loop quadratures;
4. a null test showing that replacing one coherent link by dephasing destroys
   the phase signal while preserving the edge probabilities;
5. a locality and nondisturbance statement for every port operation;
6. an error model separating loss of visibility from a changed loop phase.

Controlled cyclic permutations, sequential weak-measurement dilations, and
ancilla interferometry are possible mathematical realizations of an ordered
trace. None is yet source-authorized in the `D(S3)` lattice compiler.

## What the loop would establish

A successful loop measurement would establish more than agreement with the
fusion probability table: it would distinguish a coherent fusion-tree
realization from the measure-and-prepare shadow and verify one
gauge-invariant phase of the associator attachment.

It would establish less than full constructor equivalence. One loop does not
reconstruct all associator entries, prove pentagon coherence, determine mixed
flux braiding, or show fault-tolerant controllability.

## Falsifiers

- An individual overlap phase is called gauge invariant.
- An open bright-dark sign is claimed without a phase anchor.
- A simultaneous preparation, constructor, and readout gauge is said to be
  removed by more internal data alone.
- A product of four transition probabilities is substituted for the ordered
  four-projector trace.
- The normalized electric loop is reported with sign `+1` in the frozen
  microscopic gauge.
- A row or column rephasing changes the claimed loop value.
- The stochastic measure-and-prepare realization is said to preserve route
  coherence because its basis statistics agree.
- An ancilla or controlled ordered product is treated as source-authorized
  merely because it exists abstractly.
- One electric loop is promoted to a complete `D(S3)` coherence theorem.

## Disposition

The noncircular content of the electric associator is now separated from its
open-port calibration. Absolute trivalent phases require a connected trusted
anchor graph. Gauge-invariant associator phase can instead be tested by a
closed overlap cycle.

The smallest such cycle has four edges, and the established electric matrix
predicts exact normalized holonomy `-1`. The next physical constructor problem
is correspondingly sharp: realize the ordered four-projector trace without
reducing it to four independent probabilities and without importing an
unauthorized coherent control primitive.

No checker, build, or Git operation was run for this research-only packet.
