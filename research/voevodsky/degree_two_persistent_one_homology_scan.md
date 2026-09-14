# Degree-two persistent one-homology scan

## Question

Does the degree-two filtration contain genuine positive-length one-dimensional persistence intervals, and how sparse are they relative to edge arrivals?

## Claim boundary

The scan covers the distinct-shell multiplicative-degree-two sector through grade 20000 over two prime fields. It does not infer integral torsion, behavior in higher multiplicative degree, or physical meaning.

## Bold conjecture

Some noncanonical edges close already connected routes before their square fillers arrive, producing positive-length one-dimensional bars. Such births should be a minority of edge arrivals because many edges instead merge components, as at grade 70.

## Rivals

1. Every edge either merges components or arrives simultaneously with its filler; there are no positive-length one-bars.
2. One-bars are common rather than sparse, so canonical coherence does not control typical filtration behavior.
3. Field-dependent pairings reveal torsion or an implementation defect.

## Test

Enumerate all vertices, edges, and distinct-shell squares in multiplicative degree two through grade 20000. Order cells by grade, then dimension, direction tuple, and base. Reduce the full filtered boundary matrix independently over two large prime fields.

An edge with zero reduced boundary births a one-class. If a later square has that edge as its persistence pivot, record the half-open interval from edge grade to square grade. Record unpaired edge births as right-censored intervals. Require identical intervals over both fields.

Measure sparsity by the preregistered ratio

\[
\frac{\text{positive-length one-bar births}}{\text{all edge arrivals}}.
\]

Call the births sparse on this bounded sector only if this ratio is below 5 percent. Record zero-length same-grade pairs separately.

## Falsifiers

The existence prediction fails if no positive-length one-bar occurs. The bounded sparsity prediction fails if the ratio is at least 5 percent. Field disagreement or a boundary-composition failure is an execution defect.

## Computed result

The sector contains 1372 vertices, 1000 edges, and 73 squares through grade 20000. Exactly 73 edges have zero reduced boundary and therefore qualify as one-class births before grade ties are resolved. Every one is paired with a square at the same grade. There are no positive-length or right-censored one-bars. Both fields give identical pairings, and every square boundary composes to zero.

## Disposition

The existence prediction is falsified on this bounded sector. Persistent one-homology is not merely sparse: it is absent. Every edge that closes a route arrives in the same grade as a square filler. The 5-percent sparsity criterion is therefore vacuous rather than confirmed. The surviving stronger conjecture is a gradewise coherence law in multiplicative degree two; higher multiplicative degrees remain untested.
