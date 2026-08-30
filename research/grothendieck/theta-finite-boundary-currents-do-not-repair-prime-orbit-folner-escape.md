# Theta finite boundary currents do not repair prime-orbit Følner escape

## Bounded question

Do the primitive, prime-square, seam, or archimedean boundary ports repair
Nima's vanishing-gap sequence for local prime-adjacency energy?

## Prime-orbit packet

On one \(p\)-power orbit, write

\[
Se_k=e_{k+1},
\qquad
v_N=\frac1{\sqrt N}\sum_{k=0}^{N-1}e_k.
\]

Then

\[
\|v_N\|=1,
\qquad
\|(I-S)v_N\|^2=\frac2N.
\]

More generally, every fixed finite-range translation-covariant difference
that kills constant bulk packets has energy of order \(N^{-1}\).

## Primitive and square ports

The primitive and prime-square coordinates occupy fixed initial grades. Their
coordinate amplitudes on \(v_N\) are

\[
|\langle e_1,v_N\rangle|
=|\langle e_2,v_N\rangle|
=N^{-1/2}
\]

once those grades lie inside the packet. Their squared boundary energies are
therefore \(N^{-1}\).

The same estimate holds for every fixed finite family of grade coordinates.
Adding finitely many typed boundary rows cannot produce a cutoff-independent
gap.

## Seam trace

Along the orbit, the common theta seam row has coefficients

\[
b_k=\Phi(k\log p).
\]

Theta decay makes \((b_k)\) summable, and in particular its partial sums are
uniformly bounded. Hence

\[
|\langle b,v_N\rangle|
=\frac1{\sqrt N}
\left|\sum_{k=0}^{N-1}\overline{b_k}\right|
=O(N^{-1/2}).
\]

Its squared detector energy is again \(O(N^{-1})\). Derivative seam rows and
any fixed finite archimedean jet have the same conclusion because their theta
coefficients decay along the orbit.

## Combined no-gap theorem

Let \(Q\) be the sum of:

- finitely many fixed-range prime-difference energies;
- finitely many primitive or prime-square coordinate energies; and
- finitely many seam or archimedean theta-trace rows with summable orbit
  coefficients.

Then

\[
Q(v_N)=O(N^{-1})
\]

while \(\|v_N\|=1\). Therefore \(Q\) has no positive lower bound on the
completed prime-power coefficient orbit.

This is a completion obstruction, not a finite-rank defect. Each finite
cutoff form may be positive definite while its smallest reserve tends to zero.

## Relation to the discrete Green identity

For the Mellin-weighted geometric orbit, the local identity

\[
(1-\rho)\sum_{k=0}^{N}|d_k|^2
=|d_0|^2-|d_{N+1}|^2,
\qquad
\rho=p^{1-2\Re s},
\]

does select the critical seam through \(\rho=1\). But on the Følner packet,
the normalized endpoint flux is itself of order \(N^{-1}\). Thus the local
Green law does not provide a completion-stable boundary anchor.

Moreover, a scalar zeta zero does not make each local prime boundary flux
vanish. Turning the local identity into zero confinement still requires a
global source law assembling all prime and archimedean boundaries.

## What survives

Any faithful energy on the declared coefficient completion must use at least
one capability absent above:

1. an infinite-range arithmetic kernel with nonvanishing bulk cost;
2. a boundary port transported through every grade with nondecaying strength;
3. a nonamenable enlargement of the constructor graph;
4. a stronger source topology that excludes normalized Følner packets for an
   independently derived reason; or
5. a global coupling whose archimedean cost grows when arithmetic mass escapes.

The first three-level Tate currents, taken as finitely many boundary channels,
do not supply that capability.

## Scope

This packet proves that local prime differences plus the presently identified
finite boundary and theta-seam ports cannot repair completion escape in the
ordinary prime-orbit coefficient norm. It does not exclude nonlocal currents,
a different source-authorized topology, or a global arithmetic--archimedean
operator. It does not prove RH.
