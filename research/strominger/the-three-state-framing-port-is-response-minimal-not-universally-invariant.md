# The Three-State Framing Port Is Smith-Profile-Minimal, Not Response-Faithful

## Question

Does the source incidence object force exactly three invariant states, or does
it merely supply a three-state quotient through which the reflection response
happens to factor?

## Exact orbit calculation

There are thirty-two legal signed Moore presentations. The nontrivial
automorphism of their typed deletion incidence is endpoint reversal. It acts
without fixed points, so its signed-presentation quotient has sixteen orbits.

The three source-defined framing classes contain these orbits with
multiplicities

\[
8,\qquad 4,\qquad 4.
\]

Consequently the three-state classifier is strictly coarser than the complete
invariant quotient. A concrete hostile invariant is the sign of the repeated
generator: endpoint reversal preserves it, while the three-state classifier
forgets it. Two presentations can therefore have the same framing class and
different invariant orbits.

## Correct factorization theorem

Let \(X\) be the set of legal signed presentations, \(G\cong C_2\) its exact
typed-incidence automorphism group, \(F:X\to\{A,B,C\}\) the framing classifier,
and \(R\) the computed reflection-response profile. Then

\[
X\longrightarrow X/G\longrightarrow\{A,B,C\}\longrightarrow
\{R_A,R_B,R_C\}
\]

is a well-defined factorization. The first quotient has sixteen elements, the
second has three, and the last map is injective because the three response
profiles are distinct.

## Stratified construction of the number three

After forgetting signs, all six generator permutations are legal. Endpoint
reversal pairs them into three unsigned orbits. Two have an endpoint generator
repeated; one has the unique through-going generator repeated. Thus even the
endpoint-versus-through map is a coarse type map: it merges two unsigned
orbits into the endpoint stratum.

The polarity character is defined only over the through-going stratum and has
the two values \(-1\) and \(+1\). The response port consequently has the
stratified form

\[
\{\text{endpoint}\}\;\sqcup\;
\{\text{through}\}\times\{-1,+1\}.
\]

Its cardinality three is therefore not a homogeneous three-fold symmetry. It
is one collapsed endpoint state plus a two-sheet orientation cover over the
through-going state. This construction explains why the exceptional generator
is the only locus at which polarity matters.

## Local-constructor falsifier

The evident typed presentation changes are endpoint reversal, exchange of the
two nonrepeated slots, reversal of the repeated-generator sign, independent
tail-sign changes where legal on the endpoint stratum, and simultaneous
tail-sign reversal on the through stratum. Each is admitted only where it
preserves Moore legality and the framing type.

Without coupled tail inversion, their unary-factorized action groupoid has
four connected components, all of size eight:

\[
E_0,\qquad E_1,\qquad T_+,\qquad T_-.
\]

The missing constructor is simultaneous inversion of both nonrepeated
generators. On the endpoint stratum either individual inversion is
Moore-illegal, while their simultaneous inversion is Moore-legal and connects
\(E_0\) to \(E_1\). After adjoining this atomic coupled move, the groupoid has
exactly the three Smith-depth-profile fibers of sizes sixteen, eight, and
eight.

Thus the endpoint merge is source-generated, but only by a constructor whose
legal action cannot be factored through legal unary intermediates.

Hence two different minimality statements must be separated:

- Source universality is false: not every incidence-invariant observable
  factors through \(F\).
- Profile minimality is true: the computed Smith-depth profile factors through
  \(F\), and no two of \(A,B,C\) can be merged without losing profile
  information.

The source constructs the admissible three-state port. The Smith-depth
observation selects it as the minimal sufficient port for that compressed
observation, not for the full response matrix.

## Explanatory consequence

This locates the first nonfaithful arrow precisely. It is not endpoint
reversal itself. It is the deliberate coarse-graining

\[
X/G\longrightarrow\{A,B,C\}.
\]

That coarse-graining is lawful because the response is constant on its fibers,
but it is not forced as the universal invariant semantics of the source.

## Replay

```powershell
python research/strominger/checkers/eta_squared_faithful_artin_action_checks.py
```

The checker verifies sixty-five exact gates and emits the sixteen-orbit census, the
eight-four-four fiber sizes, and an explicit same-framing/different-orbit
witness.
