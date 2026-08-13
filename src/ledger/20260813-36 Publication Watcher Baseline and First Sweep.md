# Publication Watcher Baseline and First Sweep

## Record

Date: 2026-08-13

Status: first primary-source sweep complete. The watcher is represented as a typed paper/claim
DAG, with conjectural Marici links kept separate from claims established in the publications.

The sweep covers:

1. new Nima Arkani-Hamed authored arXiv submissions;
2. revisions and journal publications of existing authored work;
3. papers that substantively use, extend, test, or delimit an Arkani-Hamed result;
4. graph changes relevant to the Nima scalar-master program.

A bibliographic citation alone is not an alert. The unit of interest is a claim-level DAG delta.

## Watcher data model

Use three kinds of nodes:

- P: publication or version-of-record;
- C: claim established in a publication;
- L: latent synthesis or missing theorem inferred by Marici.

Use typed edges:

- establishes;
- extends;
- uses-formalism;
- rederives;
- reverse-recovers;
- tests;
- delimits;
- contradicts;
- specializes;
- suggests;
- requires.

The following event types are alert-worthy:

- NEW_NODE;
- NEW_EDGE;
- MERGE;
- REVERSE_EDGE;
- CLOSURE;
- FALSIFIER;
- STRICTIFY;
- LIFT;
- UNIQUENESS;
- VERSION_DELTA.

## Nima-authored 2026 submissions

The arXiv author record has four new 2026 submissions through 2026-08-13 and no August
submission.

### P-N26-01: The Very Nearly Right Theory of Flavor

Source: https://arxiv.org/abs/2607.27315

Submitted 2026-07-29. Nine-link sparse Yukawa textures with one CP phase exhibit fitted phases
clustered near multiples of pi/8 and produce testable CKM-angle deviations. This is outside the
active amplitude branch, but it is an example of sparse combinatorial structure controlling
apparently complicated phenomenology.

### P-N26-02: Surface Water Wave Scattering and the Hydrotope

Source: https://arxiv.org/abs/2606.28280

Submitted 2026-06-26. In a restricted deep-water-wave sector, an all-multiplicity classical
scattering amplitude is, up to a kinematic factor, the volume of a sliced-box polytope called
the hydrotope. This is a NEW_GEOMETRY node adjacent to Marici's theme of compact geometry
organizing dynamics, but no scalar-surface operator link is established.

### P-N26-03: Combinatorics of the Cosmohedron

Source: https://arxiv.org/abs/2603.03425

Submitted 2026-03-03 and revised 2026-03-20. It proves the Matryoshka face description of the
cosmohedron, develops X-in-Y chiseled polytopes, and sketches an application to ultraviolet
divergences of loop-integrated amplitudes. This is a NEW_GEOMETRY and possible LIFT-supporting
node for nested boundary operations.

### P-N26-04: Generating the fermion mass hierarchy at the TeV scale

Source: https://arxiv.org/abs/2602.17754

Submitted 2026-02-19. Vector-like fermion chains use chain locality to generate Yukawa
hierarchies while suppressing flavor and CP violation. This belongs to the flavor branch.

## Authored version events missed by the inherited sweep

### V-N26-01: Correlators are simpler than wavefunctions, v4

Source: https://arxiv.org/abs/2512.23795

Originally submitted 2025-12-29; revised four times through 2026-07-09. The current paper
shows that full-spacetime correlator integrals have fewer singularities and simpler
factorization than half-spacetime wavefunctions, with a vanishing first subleading Laurent
term and a differential operator generating the next total-energy terms from amplitudes.

This is a VERSION_DELTA signal. A source diff is still required before assigning a new
claim relative to v1.

### V-N26-02: The Cut Equation, v2

Source: https://arxiv.org/abs/2412.21027

Originally submitted 2024-12-30; revised 2026-04-06. The abstract-level claims are unchanged:
surface functions generate inequivalent triangulations and satisfy an all-genus cut recursion.
This revision is metadata-only until a v1-v2 claim diff is performed.

## Highest-information external nodes

### P-X01: On differential operators for scalar-scaffolded gluons

Source: https://arxiv.org/abs/2512.15882

Version 2 appeared 2026-07-18 and the paper was published as JHEP 07 (2026) 167.

Established claims:

- differential operators in 2n-scalar scaffold variables can extract a single planar cubic
  scalar diagram from an n-gluon amplitude;
- generalized operators produce mixed scalar/gluon amplitudes;
- the independent mixed-amplitude space with r scalars has Catalan dimension C_(r-2);
- the resulting natural basis gives a planar gauge-invariant universal expansion;
- some naive generalizations fail.

DAG event: NEW_OPERATOR.

Marici inference, not a paper result:

\[
\partial_\Gamma \circ J^1 \stackrel{?}{=} \pi_\Gamma .
\]

The paper does not show that these operators invert scaffolding, are adjoints of the first
normal jet, act on the scalar chain complex, or commute with Cut/sewing.

### P-X02: How gluon leading singularities discover curves on surfaces

Sources:

- https://arxiv.org/abs/2512.17019
- https://doi.org/10.1007/JHEP07(2026)101

Published 2026-07-10.

Established claims:

- on-shell gluing of pure-gluon three-point amplitudes produces a curve-covering
  combinatorics;
- the allowed coverings are non-overlapping curves covering each graph edge exactly once;
- this precisely matches maximal residues from linearized surfaceology u variables;
- loop spin-sum corrections admit the same graphical encoding;
- matching fixes closed-curve exponents at arbitrary loop order.

DAG event: REVERSE_EDGE at the level of leading singularities:

\[
\text{on-shell gluon gluing}
\longrightarrow
\text{surface curve coverings}.
\]

Important perimeter: this is not yet a theorem that full YM sewing reconstructs the complete
surface function, Cut Equation, or scalar master object. The reverse recovery is established
for leading singularities/maximal residues.

### P-X03: Can Locality, Unitarity, and Hidden Zeros Completely Determine Tree-Level Amplitudes?

Source: https://arxiv.org/abs/2604.07195

The paper derives known soft behavior of tree YM and NLSM from locality, unitarity, and hidden
zeros, but explicitly states that the method does not logically guarantee completeness for an
unknown theory.

DAG event: UNIQUENESS_CONDITIONAL.

### P-X04: Five-point partial waves, splitting constraints and hidden zeros

Source: https://arxiv.org/abs/2601.15088

Published as JHEP 06 (2026) 092.

Established claims:

- two five-point splitting loci become linear relations in partial-wave space;
- at low mass levels, with spin truncation, they can fix the five-point data and force the
  hidden zero at the intersection;
- once both channels allow spin-2 exchange, a genuine kernel remains.

DAG event: FALSIFIER of an unqualified hidden-zero uniqueness claim.

### P-X05: Analytic Boundaries of Infinite-Spin-Tower Amplitudes from Hidden Zero

Source: https://arxiv.org/abs/2607.27300

Submitted 2026-07-29.

Established claims:

- hidden-zero and splitting constraints admit families of unitary meromorphic
  infinite-spin-tower amplitudes;
- evenly spaced poles reduce the construction to Veneziano amplitudes;
- in the crossing-symmetric meromorphic class studied, the amplitudes have a constrained
  product form and populate analytic boundaries.

DAG event: DELIMITS/REFINES uniqueness. Zeros and splits need a typed admissibility class,
including spectral and spin assumptions, before they can be a recognition theorem.

### P-X06: A field-inspired derivation of open string amplitudes

Source: https://arxiv.org/abs/2608.02754

Submitted 2026-08-03. A weak-associativity condition on point-split on-shell string vertices
gives a binary-tree recursion with physical channels manifest and matches the recent
Arkani-Hamed--Figueiredo--Remmen five-point representation. It explicitly cites Binary
Geometries, On unitarity of tree-level string amplitudes, hidden zeros, multiparticle
factorization, and all-order splits.

DAG event: REDERIVES/TESTS the open-string branch. A map from weak associativity to binary
geometry is not supplied; this is a candidate merge, not a closed merge.

### P-X07: Partial Waves for Multipositivity

Source: https://arxiv.org/abs/2608.02719

Submitted 2026-08-03. It develops spin-resolved partial waves for multipositivity at four,
five, and six points and cites the Nima-authored multiparticle-factorization, string-unitarity,
and EFT-Hedron lines.

DAG event: EXTENDS the positivity/rigidity branch, adjacent to but not yet joined with the
scalar-surface operator algebra.

### P-X08: The CKM sector of the exceptional-Jordan programme

Source: https://arxiv.org/abs/2608.01445

Submitted 2026-08-02. It proposes a candidate exceptional-Jordan skeleton for the nine-link
texture of P-N26-01 and explicitly states that this is not a derivation.

DAG event: FAST_RESPONSE and SUGGESTS, not PROVES.

## First graph delta

The high-information amplitudes subgraph is

\[
\begin{array}{ccccc}
\text{scalar surface master}
&\xrightarrow{\text{scaffolding}}
&\text{YM}
&\xrightarrow{\text{physical gluing}}
&\text{curve coverings at maximal residues}
\\
&&\downarrow \partial_\Gamma
\\
&&\text{mixed/scalar Catalan modules}
\end{array}
\]

with the separate recognition branch

\[
\text{hidden zeros + splits}
\longrightarrow
\begin{cases}
\text{conditional rigidity under restricted spin/spectrum},\\
\text{nontrivial spin-2 kernels},\\
\text{infinite-spin-tower solution families}.
\end{cases}
\]

The strongest defensible synthesis is therefore:

> Surface curve combinatorics is independently recovered by physical gluon composition at
> maximal residues, while scalar-scaffolding variables carry differential lowering operations
> into Catalan scalar/mixed modules.

The stronger statement remains conjectural:

> The scalar surface theory carries a closed raising/lowering/sewing/pairing operator algebra
> whose representations are interacting field theories.

## Updated latent nodes

### L0: intrinsic surface operator algebra

Candidate generators:

\[
\operatorname{gr},\quad
J^1,\quad
\partial_\Gamma,\quad
I_{\rm scalar}^{-1},\quad
\operatorname{Cut/Sew},\quad
\operatorname{PrimSym}^2.
\]

Confidence increases because two reverse-directed observations now exist:

- physical YM gluing recovers curve coverings at leading singularities;
- differential operations on scaffold variables recover individual scalar diagrams and
  Catalan mixed modules.

L0 is not closed until adjunction and cut-naturalness are proved.

### L1: typed recognition principle

Replace the unqualified proposal

\[
\text{cuts + zeros + boundary behavior}
\Rightarrow
\text{unique amplitude}
\]

by

\[
\text{cuts + zeros + boundary behavior + admissibility class}
\Rightarrow
\text{candidate uniqueness}.
\]

The admissibility class must state at least allowed analytic structure, pole spectrum, spin
growth/truncation, boundedness, and multiplicity compatibility.

## Highest-value research tests produced by this sweep

1. Pairing adjunction:

\[
\langle J^1 f,g\rangle
\stackrel{?}{=}
\langle f,J^{1\dagger}g\rangle,
\qquad
J^{1\dagger}\in\operatorname{span}\{\partial_\Gamma\}.
\]

2. Cut compatibility:

\[
\operatorname{Cut}\,\partial_\Gamma
\stackrel{?}{=}
(\partial_{\Gamma_L}\otimes\partial_{\Gamma_R})\operatorname{Cut},
\]

with the sum over compatible channel restrictions made explicit.

3. Scope extension of reverse recovery: determine whether the gluon-gluing/curve-covering
equivalence extends from maximal residues to a chain-level or surface-function sewing map.

4. Recognition theorem: classify the smallest admissibility hypotheses that remove the
spin-2 kernel and infinite-spin-tower alternatives without inserting the answer.

5. Open-string merge: compare weak associativity of point-split vertices with binary
u-equations/factorization and test whether they define the same operadic composition.

## Corrections to the inherited ChatGPT sweep

- The four new 2026 Nima submissions were correctly identified.
- There is no August 2026 Nima-authored arXiv submission in the author record through
  2026-08-13.
- The July 10 JHEP publication of the gluon-leading-singularity paper is verified.
- The July 18 revision and JHEP publication of the differential-operator paper are verified.
- The inherited sweep missed 2026 revision events for Correlators are simpler than
  wavefunctions and The Cut Equation.
- It also missed the spin-2 kernel and infinite-spin-tower results, which materially weaken
  an unqualified hidden-zero uniqueness interpretation.
- The equations involving J^1, adjoints, scalar pairing, and Cut naturality are Marici
  conjectures, not claims of the cited papers.

## Watcher operational status

The old chat's statement that a daily watcher was already running is not evidence of a
scheduled task. On 2026-08-13 the task-lifecycle recurrence listing failed with

    sqlite_error: no such column: definition_json

The MCP process reports itself live/current, so this is a lifecycle data/schema problem rather
than proof that a recurrence exists. No configuration or database file was edited. Until the
lifecycle surface is repaired, this ledger and the machine-readable DAG are the durable
baseline, but daily automation is not verified.
