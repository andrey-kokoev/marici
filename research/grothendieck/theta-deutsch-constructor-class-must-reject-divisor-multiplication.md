# Theta Deutsch constructor class must reject divisor multiplication

## Impossible-task formulation

Let `A` be a proposed class of completed theta/Tate bulk--boundary objects,
and let `sigma_R(s)` be the scalar relative section read from an object
`R in A`. The desired theorem is

\[
 \sigma_R(s)=0\quad\Longrightarrow\quad\Re s={1\over2}
\]

for the distinguished arithmetic object.

Deutsch asks which authorized construction makes an off-seam null state
impossible. This gives a necessary gate before searching for an invariant.

## Divisor-multiplication no-go

Suppose the proposed admissible class is closed under multiplication by every
entire scalar `H` satisfying

\[
 H(1-s)=H(s),
 \qquad
 \overline{H(\bar s)}=H(s),
\]

and the readout is natural:

\[
 \sigma_{H R}(s)=H(s)\sigma_R(s).
\]

For `a,b>0`, take

\[
 H_{a,b}(s)=
 \left((s-\tfrac12-a)^2+b^2\right)
 \left((s-\tfrac12+a)^2+b^2\right).
\]

It obeys both symmetries and has an off-seam zero quartet. Therefore `H R`
is admissible by closure but its scalar section has off-seam zeros.
Symmetry-compatible scalar closure of the constructor class consequently
rules out a zero-confinement theorem from those axioms alone.

## What the source invariant must do

A successful constructor repertoire must fail closure under `H_{a,b}` for a
reason visible before locating its zeros. It must expose the first violated
source law, for example:

1. positive prime-power Fock coefficients;
2. labelled scale-translation recursion;
3. Poisson incidence between primal and dual lattices;
4. the primitive and square boundary-current signature; or
5. completion compatibility of the full relative state.

Merely preserving the functional equation, conjugation, regulator covariance,
and the bulk--boundary type is insufficient.

## Minimal counterfactual test

Given any proposed relational invariant `I`, evaluate it on `R` and on the
formally multiplied object `H_{a,b}R` without consulting either divisor.

- If both objects satisfy the same constructor axioms and `I`, the invariant
  has no RH force.
- If the hostile object fails, report the first failed constructor equation.
- If rejection occurs only because `H` has zeros, the definition is circular.

The target is therefore not an invariant of completed scalar presentations.
It is an invariant of source provenance whose scalar consequence is divisor
rigidity.

## Current sharp conjecture

The conjecture is that the labelled theta/Tate constructor groupoid is not
closed under any nonconstant symmetry-compatible divisor multiplier. Its
complete bulk--boundary sewing invariant detects this failure before scalar
compression.

This conjecture is Popperian: one source lift of an off-seam
divisor-bearing `H` that preserves every declared constructor law falsifies
it.

## Scope

Rejecting hostile divisor multiplication establishes canonical-section
rigidity, not RH by itself. A further theorem must still show that the genuine
source section cannot vanish off the seam. The point is to demand the exact
counterfactual discriminator before investing in that theorem.
