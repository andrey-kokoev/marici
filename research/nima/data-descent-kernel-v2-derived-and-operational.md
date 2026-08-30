# Data-descent kernel v2: derived and operational layers

Owner: `marici.Nima`

## Implemented layers

### Derived base change

Complexes, `Kernel`, `Cokernel`, `Cone`, and `Tor` are first-class types.
A nonflat base change is rejected unless it declares derived tensoring, its
Tor outputs, and comparison evidence.  The cosmology wall packet compiles as
a nonflat derived specialization with a rank-seven `Tor` grade.

This types the claim; it does not recompute the historical rank-seven theorem.
That theorem remains supplied by its referenced sector evidence.

### Correspondence variance

A correspondence is represented as a supported span with
contravariant-left/covariant-right variance.  Pushforward requires declared
properness or support.  Flattening it into an ordinary covariant map is
rejected.

### Evidence replay

Replay entries contain a site-local Python checker, output artifact, expected
SHA-256 digest, and expected result fields.  Replay is bounded, refuses paths
outside the site and non-Python checker entrypoints, executes the checker, and
then verifies both semantic fields and artifact bytes.  A forged digest fails.

### Executable capability fibers

A finite fiber declares:

- states and diagnostics;
- total operation action tables;
- a complete composition table and identity;
- policy sections from diagnostics to operations;
- optional recovery goals;
- transition maps between fibers.

The compiler executes the action tables, verifies the composition law and
policy goal, and requires capability transitions to be bijective functors.
The toric bit-syndrome packet compiles; a partial policy and a nonfunctorial
frame transition fail.

### Resource-relative capability status

A capability may be `Executable`, `Conditional`, or `Obstructed` relative to
an explicit resource theory. Executability requires admitted resources and a
scope-matched replay certificate. Conditionality names the missing resource
and an evidenced contract that the extension must preserve. Obstruction names
both the missing resource and evidenced witnesses. Circuit cost fields are
typed independently as `known`, `unknown`, or `undefined`: an absent circuit
has undefined cost, rather than a fabricated zero.

Resource extension is monotone and cannot rewrite the frozen judgement;
restriction must recover it. Resource-typed frame transitions remain
evidenced bijective functors and cannot silently change capability status.
The finite D(S3) packet exercises these constructors and hostile cases while
leaving the existing cosmology and toric packets unchanged.

## What the two packets establish

The cosmology packet exercises data descent, derived specialization,
supported correspondence, and replayed evidence.  It does not claim that its
coefficient classes are executable operations.

The toric packet exercises a genuinely executable finite capability fiber and
a decoder section.  It is the minimal bit-error model, not the full toric
decoder or a fault-tolerant constructor.

Keeping the packets separate prevents the type system from manufacturing the
missing operational lift in cosmology.

## Remaining boundary

The kernel still lacks dependent ranks, chain-level matrix verification,
higher homotopies, derived correspondence composition, infinite-dimensional
capabilities, quantitative resource optimization, and proof-assistant
certification. It types finite resource-relative claims; it does not turn a
proposed resource into an admitted physical instrument.
