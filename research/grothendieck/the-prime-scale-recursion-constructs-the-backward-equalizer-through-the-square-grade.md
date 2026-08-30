# The prime-scale recursion constructs the backward equalizer through the square grade

## Source recursion

Fix a prime `p`, put `L=log(p)`, and use the exact theta-label decomposition

\[
\Phi(u)=\Phi_{p\nmid}(u)+p^{-1/2}\Phi(u+L).
\]

For the half-line Laplace character, define

\[
F(z)=\int_0^\infty\Phi(u)e^{zu}\,du,
\qquad
R_p(z)=\int_0^\infty\Phi_{p\nmid}(u)e^{zu}\,du,
\]

and put

\[
q=p^{-1/2-z}.
\]

Let the full seam integrals be

\[
B_j(z)=\int_0^{jL}\Phi(u)e^{zu}\,du,
\]

and let the one-cell primitive seam integral be

\[
A_1(z)=\int_0^L\Phi_{p\nmid}(u)e^{zu}\,du.
\]

## Primitive backward equalizer

Changing variables in the shifted source term gives

\[
F=R_p+q(F-B_1),
\]

or

\[
(1-q)F=R_p-qB_1.
\]

At a scalar zero, this becomes the typed balance

\[
R_p=qB_1.
\]

The prime-exclusion channel does not vanish. It equals the moving seam
current, exactly as required by the balanced-defect correction.

## Square-grade refinement

Apply the same source decomposition inside the first seam cell:

\[
B_1=A_1+q(B_2-B_1).
\]

Therefore

\[
(1+q)B_1=A_1+qB_2.
\]

Eliminating `B_1` from the two independently derived identities gives the
all-parameter relation

\[
(1+q)R_p-qA_1-q^2B_2=(1-q^2)F.
\]

On the scalar-null pullback,

\[
(1+q)R_p=qA_1+q^2B_2.
\]

This is an exact backward equalizer through the square grade. The terms are
typed before imposing a zero:

```text
R_p       primitive p-exclusion source channel
q A_1     primitive moving-seam current
q^2 B_2   square moving-seam current
F         completed scalar boundary readout
```

## Place in the `3+2+1` architecture

The forward witness is the source recursion integrated against the character.
The contravariant backward witness pulls endpoint nullity into the source
covector. The displayed identity is their first nontrivial mate/equalizer
cell: it transports scalar nullity into a typed primitive-square boundary
balance without demanding that either input current vanish.

It also explains why the square current appears as an independent boundary
coordinate. It is forced by the second seam cell when the primitive recursion
is made compositional.

## Remaining obstruction

This cell is linear in the character/source pairing. The arithmetic Ward port
used in the proposed positive conservation law is quadratic and
state-dependent. Therefore the identity does not yet supply RH orientation.
The next rung must lift this linear primitive-square equalizer to a
sesquilinear or exterior-square mate on the same dynamical null pullback.

That lift must preserve the displayed coefficients and seam incidences; it
cannot replace them with scalar Tate cumulants or define the boundary form
from the Ward projection it is meant to explain.

## Durable verification

- Checker: `checkers/check_prime_scale_backward_square_equalizer.py`
- The checker verifies the elimination identity exactly as a polynomial
  consequence of the two source-recursion relations.
