# Recursive relational architecture

## Question

What is the unit beneath `3+2+1` and `2(2+1)+1`, and how does the construction
scale to Marici sectors?

## Unit

The unit is a marked carrier germ: a type, an identity token, a provenance
interface, and an unconsumed comparison port. It is not an event, occurrence,
instant, or scalar measurement. It is the smallest object on which identity
transport and later sewing remain defined.

Consuming the port maps the germ to a completed quotient. Retaining it keeps
the carrier available for a later relational mate.

An event arises only after a separate realization map binds a carrier germ to
a record in an ordered experimental history. Temporal order is another
relation on realized records. Neither realization nor order belongs to the
unit itself.

## Elementary cell

The elementary dynamical cell is `2+1`:

```text
forward witness + backward witness + mate
```

The witnesses construct and probe a record. The mate states how their fibers
totalize or close. Input, output, and control are types of this cell, not
necessarily three additional dynamical stages.

## Recursive grafting

Several elementary cells may be grafted along retained comparison ports. Each
graft adds a relational mate:

```text
two cells:    2(2+1)+1
n cells:      n(2+1)+ relational mates required by the gluing tree
```

The count is controlled by topology, not arithmetic expansion. A binary tree
with `n` leaves has `n-1` possible relational mates, but a mate is required
only where the target relation fails to descend through the proposed local
quotients.

## Exact selection theorem

For local completion maps `q_i` and an `n`-argument target relation `beta`,
local-first completion is valid exactly when inserting any vector from
`ker(q_i)` into the corresponding argument makes `beta` vanish.

For two sectors this says

\[
\beta(\ker q_A,V_B)=0,
\qquad
\beta(V_A,\ker q_B)=0.
\]

If either condition fails, no downstream operation on the completed local
objects can recover the relation. The relational mate must run first.

This is the general form of the optical parity obstruction. The hyperbolic
pairing can be globally nondegenerate while both local quotient completions
erase its decisive directions.

## Sector architectures

### Optics

Two path-marker cells retain the pair-herald key. The outer parity mate acts
before local marginalization. Bell analysis adds independently controlled
local probe families but uses the same retained carrier.

### Theta and arithmetic

The retained cutoff sector and a new prime-labelled block are local cells. The
outer mate is the complete Schur first jet, including both incidence directions
and retained-state transport. A diagonal new-block trace fails when the mixed
pairing does not descend through the separate completions.

### Signed Clark and passive systems

Positive and negative character sectors are local cells. Mixed Green terms
must be evaluated on their trace radicals before separate radical quotients.
One nonzero mixed value forces relational-first topology.

### Geometric and elliptic/Kummer sectors

The compact elliptic quotient and marked kernel have distinct local
completions. The surviving extension direction is an outer relational mate.
A horizontal forget-marks map determines which incidence direction descends
and which must remain in the extension carrier.

### Flavor

Source dynamics and calibrated measurement are separate cells. Their outer
mate identifies which realization occurred. It cannot become a selector unless
a source-derived relation survives as an independently authorized constructor.
This explains structurally why more measurement rank does not choose the
source scale.

### Radiative gravity

Early and late boundary cuts are local charge-flux cells. Memory is the outer
mate pairing them through retained generator and flux provenance. Completing
each cut to charges before forming the flux relation can erase the radiative
direction.

### Error correction

Physical regions or syndrome patches are local witness/mate cells. Logical
operators supported only in cross-region correlations require outer sewing;
local recovery quotients must not consume their shared syndrome instance keys
first.

## Architecture compiler

For any proposed sector decomposition:

1. name the marked carrier germs and their retained comparison ports;
2. name every local `2+1` cell and completion map;
3. write the target multilinear relation;
4. contract it against every local kernel;
5. complete locally where all contractions vanish;
6. insert a relational mate before every quotient where one survives;
7. repeat recursively on the resulting gluing tree.

The output is not one universal tower. It is the minimal relational tree that
preserves exactly the target constructors.

## Disposition

`3+2+1` and `2(2+1)+1` are presentations of a more primitive calculus:
marked carrier germs, `2+1` witness cells, and relational mates inserted according
to kernel-descent obstructions.

## Verification

Run:

```text
python research/aspect/checkers/check_recursive_relational_architecture.py
```
