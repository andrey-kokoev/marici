# Phase-I connected-sewing unit obstruction

Author: `marici.Grothendieck`  
Date: 2026-08-20  
Status: unbounded boundary-pushout theorem with exact all-even framed controls

## The strongest apparent unit

The later Voevodsky-sector results give a substantially stronger candidate
than the earlier regional-product inventory:

- entry 628 says the oriented four-point interval supplies a primitive unit;
- entry 537 tensors fixed four-point units with the six-point physical line;
- entries 540--541 prove framed Cut gluing through arities ten and twelve;
- entry 542 promotes the construction to every even arity by
  quadrangulation induction.

All four source checkers, including the general even-arity induction, pass.
The positive result must therefore be retained: primitive framed coefficient
lines have coherent external products, and the four-point generator carries
coefficient `+1`.

The Phase-I question is whether that primitive unit is also a **Carrier
object unit** for the connected product.

## The Carrier sewing law is a boundary pushout

Sew two marked polygons along one boundary edge.  Their boundary sites are
tagged before sewing, and the two endpoints of the chosen left edge are
identified with the two endpoints of the chosen right edge.  Thus the output
boundary is the finite pushout

\[
B_L\mathop{\sqcup}_{E}B_R,
\qquad |E|=2.
\]

The arity readout is consequently

\[
\boxed{n_L\star n_R=n_L+n_R-2.}
\]

This is not inferred from one example.  It simultaneously gives every exact
profile used by the framed Cut results:

\[
\begin{aligned}
4\star4&=6,\\
6\star4&=8,\\
4\star8=6\star6&=10,\\
4\star10=6\star8&=12.
\end{aligned}
\]

The checker constructs the pushouts from tagged boundary sets and verifies
these profiles independently.

## The object-level unit would have arity two

An object `E` is a unit for connected sewing only if

\[
n\star e=n
\]

for every admitted `n`.  The pushout law forces

\[
n+e-2=n
\quad\Longrightarrow\quad
\boxed{e=2.}
\]

Geometrically this is exactly the interface edge regarded as an object: it
has no external boundary beyond the two endpoints already identified in the
pushout.

The established stable even-polygon family begins at arity four.  Entry 27
states `n=2m >= 4`, and the framed induction uses four- and six-point base
objects.  No interface-only two-point Carrier is admitted.

The four-point factor cannot substitute for it.  For every tested and every
formal even arity,

\[
n\star4=n+2,
\]

so the proposed unit law has the exact nonzero residual

\[
\boxed{(n\star4)-n=2.}
\]

Mapping classes preserve boundary arity, so the higher-arity target cannot be
isomorphic to the original marked Carrier object.

## Why the primitive-unit terminology remains correct

The source theorems call the four-point object a primitive unit at a different
type.  They fix an oriented rank-one framed coefficient line and its chosen
generator `+1`.  Under the external product,

\[
z_6\boxtimes z_4=z_{8,\partial},
\]

with the four-point coefficient contributing multiplicative scalar `+1` and
no additional deformation.  Higher Cut strata similarly receive products of
primitive `+1` generators.

That statement is fully compatible with the arity obstruction.  The product
lands in a new higher-arity boundary line.  It does not give a natural
Carrier isomorphism

\[
\Sigma_n\star\Sigma_4\cong\Sigma_n.
\]

Thus there are two valid but noninterchangeable units:

1. a chosen generator in a framed coefficient line; and
2. a missing object unit for the Carrier sewing bifunctor.

## The intrinsic law visible in arity

Remove the two interface endpoints and define boundary excess by

\[
\epsilon(n)=n-2.
\]

Then

\[
\epsilon(n_L\star n_R)
=
\epsilon(n_L)+\epsilon(n_R).
\]

Connected edge sewing therefore carries an intrinsic **additive** law on
boundary excess.  Calling its coefficient external product “tensor” does not
turn this Carrier arity law into the multiplication needed for the initial
semiring.

In the conditional monoidal-additive branch, a distributive multiplication
would require a tensor unit equal to the connected additive generator `U`.
The only unit compatible with edge sewing is the absent interface-only
two-point object, while the admitted four-point generator is not a unit.

## Exact checker

The companion checker:

- reruns the exact framed rigidity certificates at arities 8, 10, and 12 and
  the general even-arity induction;
- constructs edge-sewing pushouts from tagged finite boundary sets;
- verifies all published Cut profiles;
- solves the unit equation exactly;
- records the persistent four-point arity residual `2`.

Artifacts:

- `research/grothendieck/checkers/phase_i_connected_sewing_unit_obstruction.py`;
- `research/grothendieck/results/phase-i-connected-sewing-unit-obstruction.json`.

All arities are readouts of source boundary sets.  No coefficient ring,
prime, degree, Frobenius action, or arithmetic multiplication is used as a
Carrier input.

## Phase-I verdict

The all-even framed coefficient product is real and coherent.  It does not
supply the missing Phase-I product:

\[
\boxed{
\text{the four-point primitive coefficient unit is not a Carrier unit;
connected edge sewing has no unit in the admitted stable family.}
}
\]

Accordingly, neither the literal-coproduct branch nor the conditional
monoidal-additive branch has a total unital distributive Carrier tensor.  The
initial semiring, intrinsic multiplication, irreducibles, primes, and Phase-II
Burnside--Witt structure remain unavailable.

The result does not forbid adjoining an unstable two-point interface object
or constructing a genuinely different tensor.  Either move is additional
Carrier structure and requires its own source authorization and coherence
proof.

No ledger entry is claimed by this packet.
