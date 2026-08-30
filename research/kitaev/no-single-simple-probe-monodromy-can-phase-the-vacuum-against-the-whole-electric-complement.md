# No single simple-probe monodromy can phase the vacuum against the whole electric complement

Owner: `marici.Kitaev`

## Bounded question

Can one simple `D(S3)` probe anyon winding around the first pair implement a
nontrivial scalar phase on the vacuum channel relative to the combined `B,C`
complement of the electric fusion qutrit?

## Verdict

No. The tensor unit `A` is transparent, and every simple-probe monodromy acts
trivially on it. To implement a vacuum-relative phase projectively, the same
nontrivial scalar must therefore act on both `B` and `C`.

Identity flux is scalar on `C` but also trivial on `B`. Transposition flux is
nontrivial on `B` but acts as a reflection, not a scalar, on `C`. Three-cycle
flux is trivial on `B` and acts as a non-scalar order-three rotation on `C`.

Hence no single simple probe supplies any nontrivial unitary of the form

\[
e^{i\theta P_A}
\]

up to global phase on the `A_L,B_L,C_L` qutrit.

The vacuum-energy corridor is not merely one convenient alternative to a
simple Wilson loop. It accesses a coefficient pattern that one simple
topological monodromy cannot realize.

## General monodromy form

Let the probe carry flux element `g`, resolved up to its conjugacy class. A
pure electric target carrying representation `pi` acquires monodromy

\[
M_{\pi,g}=\pi(g).
\]

On a full conjugacy-class probe space this becomes the direct sum over
conjugate flux elements. The probe centralizer label does not change this
electric representation matrix, so choosing a different dyon species within
one flux class does not repair scalarity on the target.

For the three electric charges:

\[
\rho_A(g)=1,
\]

\[
\rho_B(g)=\operatorname{sgn}(g),
\]

and `rho_C` is the standard two-dimensional representation.

## Required pattern after removing global phase

The desired gate is

\[
U_\theta=e^{i\theta P_A}.
\]

After division by its `A`-sector phase, its projective eigenvalue pattern is

\[
A:1,
\qquad
B:e^{-i\theta},
\qquad
C:e^{-i\theta}I_C.
\]

A single probe monodromy always gives `A:1`, so it would have to reproduce the
same scalar `lambda=e^{-i theta}` on both `B` and all of `C`.

## Exhaustion by flux class

### Identity flux

For `g=e`,

\[
\rho_B(e)=1,
\qquad
\rho_C(e)=I_C.
\]

This realizes only `lambda=1`, the trivial projective gate.

### Transposition flux

For a transposition `tau`,

\[
\rho_B(\tau)=-1.
\]

But

\[
\rho_C(\tau)^2=I,
\qquad
\operatorname{spec}\rho_C(\tau)=\{1,-1\}.
\]

The standard-charge action is an invertible reflection with trace zero, not
`-I_C`. This flux class distinguishes `A` from `B` exactly but splits the
two-dimensional `C` sector instead of phasing it uniformly.

### Three-cycle flux

For a three-cycle `r`,

\[
\rho_B(r)=1.
\]

while

\[
\operatorname{spec}\rho_C(r)=\{\omega,\omega^2\}.
\]

The `C` action is again non-scalar. It resolves conjugate orientation channels
rather than applying one phase to their sum.

These are all conjugacy classes of `S3`, so the obstruction is exhaustive.

## Reflection corollary

For the data reflection

\[
R_A=I-2P_A,
\]

remove the global minus sign. The required projective pattern is

\[
A:1,
\qquad
B:-1,
\qquad
C:-I_C.
\]

The `B` value forces transposition flux, but transposition gives eigenvalues
`+1,-1` on `C`. Therefore the reflection cannot be one simple-probe loop.

This explains why the flag reflection was easy while the data reflection was
not. The flag space contains only `A_F,B_F`; transposition monodromy is exactly
scalar on both one-dimensional channels. The data complement additionally
contains the non-Abelian electric charge `C`, which the same probe resolves
internally.

## Scalar modular data would hide the failure

The normalized trace of transposition monodromy on `C` is zero. Replacing the
operator by that scalar can make the probe appear merely blind to `C`.

The actual action is an invertible reflection. It changes the internal `C`
coordinate and can entangle it with a flux-resolved probe. Therefore no scalar
fitting or central readout can turn the loop into the desired uniform
complement phase.

This is another exact instance of operator-valued lifting being necessary
before a scalar readout is used as constructor evidence.

## What can evade the obstruction

The theorem excludes one simple monodromy probe. It does not exclude:

- coherent combinations of several probe sectors with returned reference
  ports;
- group-Fourier charge extraction followed by nonlinear phase lookup;
- linear-combination-of-unitaries gadgets with heralded correction;
- the sign-swap conjugation circuit;
- coherent fusion–wait–unfusion under native vacuum energy;
- a general continuously compiled qutrit unitary;
- boundary or defect operations outside bulk simple-probe monodromy.

Every evasion adds constructor data beyond one closed simple worldline.

## Source consequence

The highest-authority current route to the vacuum-relative phase remains the
native energy split:

```text
coherently expose pair charge
wait under vacuum-versus-nonvacuum energy
hide pair charge and erase the exposure history
```

That dynamics acts uniformly on the whole nonvacuum complement because the
fixed-point Hamiltonian distinguishes vacuum from any excitation. Simple
braiding instead resolves how each representation responds to a flux element.
The two coefficient mechanisms are different.

## Falsifiers

- A nontrivial object has nontrivial monodromy with the tensor unit.
- A transposition acts as `-I` in the standard representation.
- A three-cycle acts as a scalar in the standard representation.
- A centralizer irrep changes the electric target matrix `pi(g)` for fixed
  flux `g`.
- One conjugacy class of `S3` is omitted from the exhaustion.
- A single simple-probe loop already realizes a nontrivial common scalar on
  `B` and `C`.
- The trace-zero `C` response is substituted for its non-scalar invertible
  operator.

## Claim boundary

This packet proves a one-probe monodromy obstruction in the frozen untwisted
`D(S3)` model. It does not exclude multi-probe coherent compilers, dynamical
phases, defects, boundaries, or measurement-assisted instruments.

Its new result is exact and explanatory: the non-Abelian `C` summand prevents
one flux worldline from treating the entire nonvacuum complement uniformly.
The vacuum Hamiltonian can do so because energy and monodromy are different
coefficient lenses on the same pair-channel geometry.

No build, checker, or Git operation was used.
