# The A1z correspondence: why the unique partnerless channel carries the unique odd determinant line

Companion to `checkers/a1z_jacobian_correspondence_checks.py` (groups
J1–J6, 29/29, exit 0; results in
`results/a1z_jacobian_correspondence.json`). This packet answers the
question left open by the rung-3 cocycle arc (`rung3-cocycle.md`, K5): the
rational square-root gate fails on exactly one of the six rung-3 channels,
\(A^{(1)}_z\), whose determinant line is \(uX\) — and that channel is
precisely the one whose electric partner vanishes identically,
\(A^{(1)}_E=0\). Coincidence or correspondence? Correspondence — and the
mechanism is sharper than expected: the oddness is located entirely in the
Jacobian of the soft map.

## 1. The operator is a pure square (J1)

The five grounded \(S^{(2)-}\) channels of R1.2/R1.3 are exactly the pure
square of a single leg vector field. With
\(V=c_{z_k}\partial_{z_k}+c_{E_k}\partial_{E_k}\) and the common denominator

\[
\mathrm{den}=-\frac{4E_k\omega^2\,(z-z_k)(\bar z-\bar z_k)}{(1+u)(1+z_k\bar z_k)},
\]

every channel is a coefficient of \(V^2/\mathrm{den}\), certified exactly:

\[
A^{(2)}_z=\frac{c_{z_k}^2}{\mathrm{den}},\quad
A_{zE}=\frac{2c_{z_k}c_{E_k}}{\mathrm{den}},\quad
A^{(2)}_E=\frac{c_{E_k}^2}{\mathrm{den}},\quad
A^{(1)}_z=\frac{V(c_{z_k})}{\mathrm{den}},\quad
A^{(1)}_E=\frac{V(c_{E_k})}{\mathrm{den}}=0 .
\]

So rung 3 is the first "squared-vector-field rung": the principal symbol is
the rank-1 symmetric square \(c\otimes c\), and the first-order sector is
the vector \(V(c)\).

## 2. The partner-vanishing is a Hamiltonian collapse (J2)

The grounding \(A^{(1)}_E=0\) says \(V(c_{E_k})=0\): the vector field
annihilates its own second component. In two leg dimensions a vector field
annihilating a function is Hamiltonian with respect to it, and here the
multiplier is explicit:

\[
\mu=\frac{E_k\,c_{z_k}}{c_{E_k}}=\frac{(z-z_k)(1+z_k\bar z_k)}{1+z\bar z_k},
\qquad
c_{z_k}=\mu\,\partial_{E_k}c_{E_k},\qquad
c_{E_k}=-\mu\,\partial_{z_k}c_{E_k}.
\]

Both flow identities are certified exactly (J2.flow.a/b). So "the partner
vanishes" *is* "V is Hamiltonian with respect to \(c_{E_k}\)" — the two
statements are the same statement.

## 3. The surviving channel is a Jacobian (J3)

A Hamiltonian vector field applied to any function gives a Poisson bracket.
Certified exactly:

\[
V(c_{z_k})=\mu\;\mathrm{Jac}(c_{z_k},c_{E_k}),\qquad
\mathrm{Jac}(c_{z_k},c_{E_k})
=-\frac{4\omega^2(z-z_k)^2(1+z\bar z_k)}{(1+u)^2(1+z_k\bar z_k)},
\]

with Jac not identically zero (the soft map
\((z_k,E_k)\mapsto(c_{z_k},c_{E_k})\) is a local diffeomorphism). Hence

\[
A^{(1)}_z=\frac{\mu\;\mathrm{Jac}(c_{z_k},c_{E_k})}{\mathrm{den}}
\]

is an *area form* — an antisymmetric object — while every other channel is
a *symmetric product* of soft-factor lines. This is the structural
asymmetry behind the gate.

## 4. Square-norm bookkeeping (J4)

The determinant line is a multiplicative norm character:
\(\det(K)=F_2\sigma(F_2)=D(K)\) with
\(D(f)=Q(\alpha f)/Q(f)\), \(Q(f)=f\,\sigma(f)\), and \(D(fg)=D(f)D(g)\)
(certified). Every product-side input has a **square** character:

\[
D(c_{z_k})=X^2,\qquad D(c_{E_k})=1,\qquad D(\mathrm{den})=X^2,\qquad
D(\mu)=X^2,
\qquad X=\frac{(1+z\bar z_k)(1+\bar z z_k)}{(z-z_k)(\bar z-\bar z_k)} .
\]

Even the Hamiltonian multiplier is square-protected. Multiplicativity then
*forces* the even determinant lines of every product channel —
\(\det(A^{(2)}_z)=X^2\), \(\det(A_{zE})=1\), \(\det(A^{(2)}_E)=X^{-2}\) —
with no case-by-case computation.

## 5. The Jacobian carries the unique odd character (J5)

The single non-square input in the entire construction is the soft-map
Jacobian:

\[
\boxed{\;D\big(\mathrm{Jac}(c_{z_k},c_{E_k})\big)=uX\;}
\]

certified exactly (J5.char). Everything else — both c-lines, the
denominator, the multiplier — is square. The K3 determinant line is then
*derived*, not observed:

\[
\det(A^{(1)}_z)=\frac{D(\mu)\,D(\mathrm{Jac})}{D(\mathrm{den})}
=\frac{X^2\cdot uX}{X^2}=uX,
\]

with odd \(\mathrm{val}_z=1\), so no rational square root exists: the
square-root gate failure is located exactly in the Jacobian of the soft
map.

## 6. The correspondence (J6)

- **Necessity (forced).** Every symmetrized c-product channel has even
  determinant by J4 multiplicativity — a theorem about the family, not a
  per-channel fact.
- **The collapse.** Partner-vanishing \(\Leftrightarrow\) Hamiltonian \(V\)
  \(\Leftrightarrow\) the first-order sector is a pure Jacobian area form —
  the only channel not protected by the square bookkeeping.
- **Pinning identities (exact).** The odd line is pinned by the even lines
  up to the diagonal monomial \(u^2\):

\[
\det(A^{(1)}_z)^2=u^2\,\det(A^{(2)}_z)\,\det(A_{zE}),\qquad
F_2(A^{(1)}_z)^2=-\bar z^{2}\,F_2(A_{zE})\,F_2(A^{(2)}_z) .
\]

**Verdict.** "Vanishing partner" does not numerically force oddness — it
removes the square protection. When \(A^{(1)}_E\) vanishes, the surviving
magnetic first-order channel is necessarily a Jacobian, the unique object
in the construction whose norm character is not automatically a square;
and the soft map's Jacobian is computed to carry \(uX\), odd. The unique
partnerless channel carries the unique odd determinant line — a
correspondence, with the mechanism fully exhibited.

A cross-arc note: this is the second time an odd \(u\)-object has turned
out to be born at a specific structural locus rather than in the datum —
the readout-parity arc (`readout-parity-mechanism.md`) located the odd
\(u^7\) of \(P(M_3)\) at the readout projection grade, and here the odd
\(uX\) is located at the soft-map Jacobian. In both cases the datum itself
is even throughout.
