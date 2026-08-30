# Deutsch--Popperian conjecture: gauge equivalence versus rival explanation

## Status

This packet classifies the nonuniqueness left by a successful explanatory
realization. It asks when two realizations are merely different presentations
of one explanation and when they make genuinely different source claims.

## 1. Typed realizations

Let a realization be

\[
\mathfrak R=(S,I,\{C_w\}_{w\in\mathcal W},\{O_r\}_{r\in\mathcal R},\Sigma),
\]

where:

- \(S\) is the internal state object;
- \(I\) initializes source histories in \(S\);
- \(C_w\) realizes intervention \(w\);
- \(O_r\) realizes readout \(r\);
- \(\Sigma\) is the declared source decomposition, coefficient lens, and typing
  data.

The observable response to a word \(u=w_k\cdots w_1\) is

\[
O_r C_{w_k}\cdots C_{w_1}I(h).
\]

## 2. Three levels of agreement

Two realizations may agree at three different strengths.

### Behavioural equivalence

They produce identical results for all admitted histories, intervention words,
and readouts.

### Constructor equivalence

There is an invertible typed map \(\eta:S\to S'\) satisfying

\[
\eta I=I',
\qquad
\eta C_w=C'_w\eta,
\qquad
O'_r\eta=O_r
\]

for every admitted \(w,r\).

### Source equivalence

The same \(\eta\) also preserves the authorized source structure \(\Sigma\): its
atoms, module boundaries, coefficient lens, distinguished unit, sheet character,
and admitted incidence maps.

Behavioural equivalence alone is observational underdetermination. Constructor
equivalence identifies presentations of one dynamical system. Source equivalence
identifies presentations of one typed explanation.

## 3. Authorized gauge group

For a fixed realization, define

\[
\operatorname{Gauge}(\mathfrak R)
=
\{\eta\in\operatorname{Aut}(S):
\eta I=I,
\ \eta C_w=C_w\eta,
\ O_r\eta=O_r,
\ \eta\Sigma=\Sigma\}.
\]

The last condition is essential. Without it, a state-coordinate transformation
may mix primitive and square currents, exchange sheets, move the tensor unit, or
erase a declared subsystem boundary while leaving a scalar response unchanged.
That is not automatically an authorized gauge transformation.

## 4. Linear-control baseline

For finite-dimensional linear systems

\[
x_{t+1}=Ax_t+Bu_t,
\qquad
y_t=Cx_t,
\]

the response is determined by the Markov parameters

\[
CA^kB.
\]

If two realizations have the same Markov parameters and are both reachable and
observable, then they have the same dimension and are related by an invertible
similarity \(T\):

\[
A'=TAT^{-1},
\qquad
B'=TB,
\qquad
C'=CT^{-1}.
\]

Thus minimality converts behavioural equivalence into constructor equivalence
for the untyped linear system.

It does not prove source equivalence. The similarity may fail to preserve a
declared decomposition

\[
S=S_P\oplus S_Q\oplus S_{\mathrm{seam}},
\]

or may mix components carrying different coefficient lenses. Source typing
therefore cuts the ordinary similarity orbit into smaller authorized orbits.

## 5. Rival-explanation criterion

Two successful realizations are rival explanations when:

1. they are behaviourally equivalent on the current interface;
2. no authorized source equivalence intertwines them;
3. some admissible source intervention, conservative interface extension, or
   module-local replacement distinguishes them.

If condition 3 has not yet been supplied, they are unresolved explanatory
alternatives rather than experimentally separated rivals.

If no possible authorized extension can distinguish them, the proposed source
distinction is idle relative to the programme and should be quotiented as gauge.

## 6. The nonuniqueness trichotomy

Given an evidence interface, explanatory nonuniqueness has three forms.

### Gauge orbit

All surviving models are related by authorized source equivalences. The
explanation is unique up to gauge.

### Reference torsor

The models differ by a free transitive action, but no admissible datum chooses an
origin. Examples include an unframed sign sheet or phase convention. One trusted
source reference selects a frame without adding amplitude coordinates.

### Genuine moduli

The models contain invariant parameters not removable by authorized gauge and
not fixed by current evidence. New interventions are required. Calling one
member the explanation would exceed the evidence.

## 7. Three-lens consequence

The authorized equivalence depends on the coefficient lens.

- For additive currents, it is typically a linear change of basis preserving
  distinguished rows and grading.
- For determinant-line phases, it is a line-bundle gauge preserving the chosen
  unit or orientation data.
- For ordered holonomy, it is conjugation or a typed natural equivalence that
  preserves ordered composition.

Equality after scalarization is weaker than all three. In particular,

\[
\operatorname{tr}(UV)=\operatorname{tr}(VU)
\]

does not authorize identifying the ordered realizations \(UV\) and \(VU\).

## 8. Toric-code witness

Changing the representatives of logical cycles by plaquette boundaries is an
authorized gauge change: the homology class and all logical intersection
pairings are preserved.

Exchanging the two fundamental cycles may be an authorized lattice symmetry if
the frozen geometry admits it. It is not a gauge change if the source interface
labels the two ports independently.

Choosing different decoders with identical syndrome and logical outputs is not
mere gauge when their repair locality or fault response differs under an
admitted noise intervention. The enlargement exposes a genuine explanatory
modulus.

## 9. Finite audit

For two finite linear typed realizations, perform the following tests in order.

1. Compare all response words up to a completeness bound.
2. Remove unreachable and unobservable state.
3. Solve the intertwining equations for invertible \(T\).
4. Impose the source-preservation constraints on \(T\).
5. Classify the solution set as empty, an authorized gauge orbit, a torsor, or a
   positive-dimensional moduli family.
6. Search for the smallest typed extension whose response separates distinct
   authorized orbits.

The first-invalid witness is either a response word, a failed intertwining
equation, or a source invariant changed by every available intertwiner.

## 10. Strengthened DPC

An explanatory claim is warranted only up to the largest equivalence relation
that preserves all admitted constructor compositions, modular interventions,
source types, and conservative extensions.

Equivalently, explanation is not an internal state presentation. It is an
authorized equivalence class of reusable realizations together with a critic
capable of detecting changes outside that class.

## 11. Critic

The source-preservation condition can be abused: one can declare arbitrary
internal labels sacred and thereby manufacture inequivalent explanations.

The repair is an authority condition. A source distinction enters \(\Sigma\) only
if it is independently derived from the source construction or is tied to an
admitted intervention. Typing does not create ontology by stipulation.

## 12. Bottom line

Minimal prediction removes redundant state. Authorized gauge removes redundant
presentation. Neither removes genuine source ambiguity.

The programme should therefore report explanatory conclusions in one of three
forms:

\[
\text{unique up to authorized gauge},
\qquad
\text{a reference torsor},
\qquad
\text{an unresolved moduli family}.
\]

Anything sharper requires a new source-derived discriminator.
