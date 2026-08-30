# Quartic arithmetic-circuit completion (WP388)

## Bounded question

Can auxiliary multiplication gates turn WP387's high-degree invariant portal
into a local potential of degree at most four without changing its projected
zero set?

## Exact gate construction

For a representative product relation $t=xyr$, introduce auxiliary variables
$z,w$ and positive gate weights $a,b,c$:

\[
V=a(z-xy)^2+b(w-zr)^2+c(w-t)^2.
\]

Every term has polynomial degree at most four. Because every coefficient is
positive, $V=0$ holds exactly when all three gate equations hold. Eliminating
the auxiliaries gives

\[
z=xy,\qquad w=xyr,\qquad t=xyr.
\]

The auxiliary Hessian at the compiled solution is positive definite. Thus an
acyclic arithmetic circuit can replace a high-degree polynomial relation by
a collection of stable quartic gate penalties while preserving its projected
zero set.

Iterating the construction can in principle compile determinants,
discriminants, and the WP387 mixed invariant from fundamental matrix entries.
The operator-degree obstruction is therefore not an absolute algebraic
no-go.

## Authority obstruction

The compiler does not explain which circuit nature uses. Replacing the final
gate $(w-t)^2$ by $(w+t)^2$ preserves positivity, locality, degree, and
auxiliary stability but changes the selected relation from $t=xyr$ to
$t=-xyr$. Deleting the final gate makes the target $t$ completely invisible.

Hence the gate graph, signs, weights, and terminal relation carry the same
selector information as the original polynomial. Compiling the desired shell
after seeing it is a presentation rigidification, not a source derivation.

## Weak-basis descent

A circuit written directly in invariant inputs descends formally but retains
their high-degree input interface. A microscopic circuit from fundamental
flavor fields must assign transformation representations to every
intermediate variable and make every gate equivariant. Algebraic existence of
an untyped scalar circuit does not establish such a physical source.

The positive gate weights also require normalization authority. Rescaling an
intermediate variable changes adjacent weights and couplings while preserving
the projected zero set, producing an auxiliary-presentation groupoid that an
instrument must quotient or calibrate.

## Disposition

WP388 removes high polynomial degree as a decisive mathematical obstruction:
a stable quartic auxiliary presentation exists in principle. It strengthens
the source-authority gate. The circuit is a conditional selector only after
its topology, representations, coefficients, and terminal relation are
derived independently from flavor dynamics.

The smallest falsifier is the correct versus sign-flipped final gate: both are
healthy quartic circuits and select different shells. The next gate is an
equivariant microscopic circuit grammar frozen before the desired flavor
relation is supplied.

Run `uv run --with sympy python
research/flavor/checkers/wp388_quartic_arithmetic_circuit.py` to regenerate
the result.
