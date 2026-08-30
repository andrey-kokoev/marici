# A destructive charge measurement cannot become an unknown-state gate without an expanded workspace

Owner: `marici.Kitaev`

## Bounded question

Can the native vacuum-versus-nonvacuum measurement on the three-`C`-anyon
fusion qutrit, combined with the finite braid and magnetic gate group,
implement new deterministic unitaries by adaptive repetition on the same
qutrit?

No. Every selective vacuum-measurement branch has rank one or two on the
three-dimensional logical space. Rank cannot increase under later linear
composition. A deterministic unitary channel has Kraus rank one and requires
every nonzero history operator to be proportional to one full-rank unitary.
Therefore no history that directly projects the unknown data qutrit can be a
successful branch of a deterministic unitary implementation.

Measurement-assisted universality requires a larger quantum workspace. The
logical state must first be embedded or teleported so that every accepted
measurement branch remains a full-rank map from the input qutrit to an output
qutrit, even though a projector acts on the larger carrier.

## Claim boundary

The theorem concerns deterministic unitary action on an arbitrary unknown
state. Rank-deficient measurements remain useful for readout, state
preparation, filtering, error detection, and heralded nonunitary maps.

The obstruction assumes that the projector acts directly on the complete
current logical carrier and that no quantum subsystem outside that carrier
already holds an injective copy of its unknown state. Classical records and
merely adjoined unentangled ancillas do not change the conclusion. An
entangling encoding into a larger fusion space can.

## Same-space adaptive protocol

Let the unknown logical input lie in a `d`-dimensional space `H`. A complete
adaptive history `r` has a branch operator

\[
M_r
=
U_{r,k}A_{r,k}\cdots U_{r,1}A_{r,1}U_{r,0},
\]

where the `U` factors are unitary gates and each `A` factor is a selective
measurement Kraus operator chosen by the preceding classical record.

The resulting channel, after retaining or forgetting the classical history,
has Kraus family

\[
\{M_r\}_r.
\]

Adaptive choice changes which product belongs to each history. It does not
change the rank inequality for that product.

## Branch-rank monotonicity

For finite-dimensional linear maps,

\[
\operatorname{rank}(XY)
\leq
\min
\left{
\operatorname{rank}X,
\operatorname{rank}Y
\right}.
\]

Consequently,

\[
\operatorname{rank}M_r
\leq
\min_j\operatorname{rank}A_{r,j}.
\]

Unitary gates before or after a measurement preserve rank. Later
postselection, feed-forward, and repetition cannot restore a dimension
discarded by an earlier branch projector.

This is an information-capacity statement, not a probability statement. A
rank-deficient branch may occur with probability approaching one under
repetition and still fail to carry an arbitrary `d`-dimensional unknown state.

## Deterministic-unitary branch theorem

Suppose the complete adaptive instrument implements the unitary channel

\[
\Phi(\rho)=U\rho U^*.
\]

A unitary channel has Choi rank one. Hence every Kraus representation of it
has all nonzero Kraus operators proportional to `U`:

\[
M_r=c_rU.
\]

Every nonzero `M_r` must therefore have rank `d`.

Combining this with branch-rank monotonicity gives the exact criterion:

> No successful history of a deterministic unknown-state unitary may contain
> a same-space selective measurement operator of rank below `d`.

If such a history has nonzero probability for any input, the claimed unitary
channel is false. If the history is declared a failure and discarded, the
remaining operation is not deterministic unless the total failure
probability is exactly zero for every input.

## Application to the native vacuum PVM

On the pinned qutrit, let

\[
P_A=|A_L\rangle\langle A_L|
\]

be the first-pair vacuum projector. The binary charge measurement has branch
operators

\[
P_A,
\qquad
I-P_A.
\]

Their ranks are one and two. Therefore every same-qutrit history containing
either selective branch has rank below three.

No sequence of finite monomial gates, repeated vacuum tests, outcome-dependent
braids, or later magnetic cube-root phases can turn that history into a
full-rank unitary on the original unknown qutrit.

The nine SIC effects sharpen tomography but are rank one. Applying one as a
selective data measurement is even more destructive. Informational
completeness across an ensemble does not imply reversible gate action on one
unknown copy.

## Repeat-until-success does not evade rank loss

Suppose a protocol measures, applies a conditioned gate, and repeats after an
unwanted result. If the first measurement acted directly on the data qutrit,
every later history contains its rank-deficient branch factor. Its rank never
returns to three.

The probability of seeing a preferred label may converge to one, but the
conditional map can at most prepare or transform a lower-dimensional image.
It cannot converge to a unitary channel on all qutrit inputs.

This distinguishes two exponential claims:

- success probability approaches one;
- conditional logical map approaches the desired unknown-state unitary.

The first does not imply the second.

## Why classical records cannot hold the lost dimension

A measurement outcome records which branch occurred. For a binary PVM, it
stores at most a classical label distinguishing the rank-one and rank-two
subspaces. It does not store the quantum amplitudes removed by the projection.

Conditioned control can act on the surviving state and the label. It cannot
reconstruct arbitrary phase coherence between the two measured sectors. Such
reconstruction would invert a noninjective branch map.

Thus an objective record is not a quantum backup of the premeasurement state.
It records the event created by the instrument while the future Carrier has
already changed.

## Expanded-workspace escape

Let the logical input still have dimension `d`, but introduce a larger
workspace `W` and an isometric encoding

\[
E:\mathcal H_{\rm in}\longrightarrow\mathcal W.
\]

Let a selective measurement on `W` have Kraus operator `A_r`, followed by an
outcome-dependent decoding

\[
D_r:\mathcal W\longrightarrow\mathcal H_{\rm out}.
\]

The logical branch map is

\[
M_r=D_rA_rE.
\]

A physical projector `A_r` may be rank deficient on `W` while `M_r` remains
full rank `d`, provided its accepted image contains all encoded logical
dimensions and `D_r` is injective on that image.

This is the exact escape. The measurement may discard workspace dimensions,
but it must not discard a logical dimension.

## Minimal branchwise gate certificate

For a repeat-until-success measurement gadget that claims to implement a
unitary `U`, every accepted outcome history must report

\[
D_rA_rE=c_rU,
\qquad
c_r\neq0.
\]

It must also report:

1. the workspace and its anyon or ancillary typing;
2. the encoding isometry `E`;
3. every physical measurement branch `A_r`;
4. the record-conditioned decoder or continuation `D_r`;
5. failure branches and their retained state;
6. leakage outside all declared computational sectors;
7. the probability and expected cost of eventual success;
8. the fault spread through repeated trials.

Checking only the final success probability or selected fusion label is
insufficient.

## Sector hopping in known `D(S3)` universality

The known `U` and `V` qutrit protocols do not merely apply a rank-deficient
projector to one isolated qutrit and recover its state. They operate in a
larger fusion space containing distinct three-dimensional computational
sectors. Braiding and measurement can move the unknown logical vector between
those sectors. Successful branches act as full-rank transformations such as a
generalized Hadamard or an isomorphism between `U` and `V`.

Their exponential repeat-until-success claim is therefore compatible with
the rank theorem: the measurement is rank deficient on the ambient fusion
space while each accepted logical branch can remain rank three between typed
qutrit sectors.

This workspace structure is exactly what must be reconstructed natively for
the three-`C`-anyon qutrit. Copying only the charge-effect matrix omits the
mechanism that preserves the unknown state.

## Smallest native extension target

The first useful search is for a fusion workspace with at least two typed
qutrit sectors,

\[
\mathcal W
\supset
\mathcal H_C^{(0)}
\oplus
\mathcal H_C^{(1)},
\]

and a source-authorized braid or dyon-assisted map that mixes them. A charge
measurement should then select branches whose restrictions are full-rank maps

\[
\mathcal H_C^{(0)}\longrightarrow
\mathcal H_C^{(0)},
\qquad
\mathcal H_C^{(0)}\longrightarrow
\mathcal H_C^{(1)}.
\]

The second sector need not literally be another three-`C` fusion tree. It may
use a flux, dyon, boundary, or ancillary charge configuration. What matters is
that every accepted branch retains three logical dimensions and that the
sector label is recorded for feed-forward.

## Dimension lower bound on a nontrivial projective split

Suppose one measurement has at least two outcomes that can both occur while
preserving the entire unknown qutrit. Each corresponding physical outcome
subspace must contain an injective image of a three-dimensional logical
space. If the outcome subspaces are orthogonal, the ambient workspace must
have dimension at least six.

Thus a binary orthogonal sector-hopping gadget with two full-qutrit branches
requires

\[
\dim\mathcal W\geq6.
\]

This is attained by the abstract architecture

\[
\mathcal H_C\oplus\mathcal H_C.
\]

The bound does not apply when only one branch preserves the input and all
others are destructive failures, or when nonorthogonal generalized
measurement effects are used. Those cases require their own success and
restart contract.

## Fault consequence of repeated sector hopping

An expanded workspace avoids logical rank loss but introduces new physical
fault surfaces:

- the sector label may be misrecorded;
- a fault may mix accepted and leakage sectors;
- repeated trials may let one mobile ancilla fault revisit the data;
- a common calibration error may affect every attempt;
- the stopping time may correlate with an uncontrolled environment;
- decoding may restore the qutrit in the wrong semantic frame.

Exponential ideal success probability does not bound these accumulated fault
channels. The expected number and tail distribution of attempts must enter
the filtered constructor certificate.

## Exact falsifiers

- A rank-one or rank-two same-qutrit measurement branch is claimed to become
  a rank-three unitary after later gates.
- Repeat-until-success probability is substituted for branchwise logical rank.
- A classical outcome label is treated as retaining discarded quantum
  coherence.
- A SIC measurement on one unknown copy is called a reversible gate.
- A physical projector is judged only by its ambient rank rather than the rank
  of `D_r A_r E` on the logical input.
- A unitary channel is represented by nonproportional nonzero Kraus operators.
- A larger fusion space is invoked without specifying encoding, sector
  projectors, and decoding.
- Two orthogonal full-qutrit outcome sectors are placed in an ambient space of
  dimension below six.
- Exponentially small ideal nontermination is promoted to a fault threshold.
- The literature's charge effect is copied while its sector-hopping workspace
  is omitted.

## Shared Carrier geometry and quantum coefficient lens

Shared Carrier geometry supplies branch histories, rank monotonicity under
composition, typed workspaces, sector records, adaptive stopping, and the
distinction between event probability and retained state capacity.

The quantum coefficient lens supplies Kraus rank, unitary-channel rigidity,
fusion-sector projectors, coherent encoding and decoding, leakage, and
unknown-state preservation.

## Disposition

Direct charge measurement on the pinned three-`C`-anyon qutrit cannot be the
missing universal gate constructor. Every selective branch loses logical
rank, and no later same-space operation can restore it. The native vacuum PVM
and SIC effects are testers and state-preparation resources, not reversible
unknown-state actuators.

The smallest viable measurement-assisted architecture must enlarge the fusion
workspace so that every accepted branch remains rank three between typed
qutrit sectors. For a binary orthogonal split with two information-preserving
outcomes, the ambient dimension is at least six. Finding such a sector pair
and a complex bridge between it and the current `C` qutrit is now the precise
native constructor target.

No build, checker, or Git operation was run for this research-only packet.
