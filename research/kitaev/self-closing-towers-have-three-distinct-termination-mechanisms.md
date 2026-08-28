# Self-closing towers have three distinct termination mechanisms

Owner: \`marici.Kitaev\`

## Question

When is a proposed next coherence rung genuinely new, and when is it already
forced by lower data?

## Claim boundary

This packet classifies three finite termination mechanisms already present in
Marici. It does not claim every sector has a finite closure degree or that
algebraic closure supplies physical implementation.

## General termination test

A tower self-closes at depth \(r\) when every admissible continuation above
depth \(r\) is uniquely determined, or at least forced to exist with no new
independent invariant, by the frozen data through depth \(r\).

The hostile test is always the same:

> Can two source-admissible objects agree on every cell through depth \(r\) but
> disagree at depth \(r+1\)?

If yes, the tower has not self-closed. If no, and the nonexistence of such a
pair follows from the governing law rather than finite sampling, the tower
terminates at \(r\).

Three different mechanisms can make this happen.

## Mechanism one: categorical coskeletality

Strominger's strict metaplectic result is the clean categorical instance. A
section of an ordinary group extension gives a two-cocycle
\(\omega(g,h)\). The cocycle identity

\[
\omega(h,k)\omega(g,hk)
=
\omega(g,h)\omega(gh,k)
\]

makes all longer parenthesizations agree.

The nerve of an ordinary category is 2-coskeletal: binary composition and the
associativity cell determine every higher simplex. There is no independent
infinite associator tower.

The termination gate is not merely a table of pair phases. The pair phases
must satisfy the triple cocycle identity. A hostile non-cocycle agrees with the
same binary typing but fails at length three.

Thus this tower closes after a finite coherence law is verified.

## Mechanism two: flag or Gram closure

Knill–Laflamme correctability is a different self-closure. For errors \(E_i\)
on code projector \(P\), every higher correctable span is determined by the
pair equations

\[
P E_i^\dagger E_jP=\alpha_{ij}P.
\]

A subset is correctable exactly when all of its pairs satisfy these equations.
The correctability complex is therefore the flag complex of the compatibility
graph.

No independent triple condition remains. Positivity of \(\alpha\) is automatic
because the scalars come from actual operator overlaps.

This is not 2-coskeletality of a composition nerve. It is pair-generation of a
quadratic admissibility law. The shape is a clique complex rather than a nerve
of composable arrows.

If scalar overlaps are fitted without source operators, positivity becomes new
data and the self-closure claim fails.

## Mechanism three: functional saturation

Figueiredo's three-route moment result is observational rather than
compositional. Route weights \((p_-,p_0,p_+)\) are reconstructed from
normalization and

\[
m_1=p_+-p_-,
\qquad
m_2=p_++p_-.
\]

The coordinate map is injective, so every further exact route statistic is a
function of the reconstructed weights. The observation family has reached
functional saturation on the frozen finite domain.

This is neither a categorical nerve nor a flag complex. It is finite
reconstruction closure.

The first moment alone does not close: two different mixtures share \(m_1=0\)
and differ in \(m_2\). The second moment supplies the missing coordinate.
Instrument authority remains separate because \(m_2\) requires repeated
branch-resolved preparations or a two-copy instrument.

## One word, three meanings

“Self-closing” should therefore be replaced by a typed termination claim:

- coskeletal closure: higher coherence cells are forced by lower composition
  laws;
- flag closure: higher admissible subsets are forced by bounded-arity
  compatibility;
- saturation closure: further observations are functions of a faithful
  coordinate packet.

These mechanisms have different falsifiers and different implementation gates.

## Closure depth by minimal obstructions

For a finite downward-closed admissibility family \(\mathcal K\), a minimal
nonface is a forbidden set all of whose proper subsets are admitted.

If every minimal nonface has size at most \(r+1\), then admissibility is
determined by faces of size at most \(r+1\). The maximum minimal-nonface size is
the exact finite arity needed to detect every obstruction.

A flag complex is the case in which every minimal nonface has size two. All
failure is already visible pairwise.

A hollow triangle has one minimal nonface of size three. Its edges pass, but a
genuine ternary implementation obstruction remains.

This gives a finite diagnostic for executable recovery complexes: compute or
bound the support size of minimal forbidden recovery families.

## Why polynomial degree is not enough

A quadratic source law often suggests pair closure, but degree alone does not
prove it. Determinants, positivity regions, shared-resource constraints, and
elimination can create higher-support obstructions even when local formulas are
low degree.

KL self-closure follows from the exact pair-indexed theorem, not from the word
“quadratic.” Figueiredo's closure follows from explicit injectivity, not merely
from having two moments. Strominger's closure follows from a cocycle identity,
not merely from binary multiplication.

The termination proof must name the forcing theorem.

## Observation and constructor sides

An observation tower can self-close while its constructor tower remains open.

- Figueiredo: moments reconstruct the finite mixture, but the required
  repeatable instrument is separate.
- Kitaev: pair overlaps determine algebraic correctability, but one authorized
  common recovery may be absent.
- Strominger: a genuine strict extension forces higher associativity, but an
  implementation can still have domain, path, noise, or authority defects.

Thus self-closure means “no new invariant of this declared type.” It does not
mean “the whole system is finished.”

## Decision procedure

For any proposed next rung:

1. Freeze the object type and source-authorized lower data.
2. State the proposed higher cell.
3. Search for two admissible models with identical lower truncation and
   different higher cells.
4. If found, retain the next rung as independent.
5. If not, prove one of:
   - a coskeletality or coherence theorem;
   - a bounded-arity or flag theorem;
   - a faithful-coordinate saturation theorem.
6. Re-run the test at the physical constructor and completion layers.

Failure to find a counterexample is not a termination theorem.

## Strominger's new 3-adic question

The magnetic jet tower should ask whether higher jets are recursively
determined by frozen lower jets and source equations.

- If two admissible magnetic objects share the same lower jet and differ at the
  next lift, there is new obstruction data.
- If a source-derived recursion uniquely determines every higher jet, the jet
  tower functionally or coskeletally closes.
- Equality of terminal valuation does not prove jet closure; it can hide
  different filtered profiles.

This is exactly the hostile-pair test above.

## Deutschian explanation

A tower terminates for a reason only when a generative law makes further
variation impossible. “We checked many levels” is not such a reason.

The explanation must say why every proposed higher variation either violates
the lower law, is already a function of faithful coordinates, or is merely a
new implementation choice rather than a new mathematical invariant.

## Falsifiers

- Finite checking is promoted to coskeletality.
- A pair table is called coherent without its cocycle identity.
- A compatibility graph is transitively quotiented rather than flag-completed.
- Low polynomial degree is treated as a bounded-arity theorem.
- Coordinate injectivity is claimed without reconstructing the frozen domain.
- Algebraic termination is promoted to instrument or actuator completion.
- Two models with identical lower truncation and different next cells are
  ignored.

## Disposition

The phenomenon the operator recalled is real and occurs in at least three
typed forms. Strominger's metaplectic tower is coskeletal, Kitaev's algebraic
correctability tower is flag, and Figueiredo's finite moment tower is
functionally saturated. Their shared principle is forced continuation; their
forcing theorems and physical boundaries are different.

No checker, build, or Git operation was run for this research-only packet.
