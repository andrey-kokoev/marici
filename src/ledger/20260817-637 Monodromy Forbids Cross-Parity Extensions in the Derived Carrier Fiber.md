# Entry 470 — Monodromy Forbids Cross-Parity Extensions in the Derived Carrier Fiber

Entry 469 left one apparent alternative for the full chain-level lift: either
the derived carrier fiber is the blockwise sum of its even Koszul cell and odd
matrix factorization, or the quartic tail creates an extension between those
parity blocks.  The physical finite pushforward of Benincasa Entry 463 rules
out the second possibility once the map is constructed geometrically.

## Involutive constraint

After the quadratic normalization of

\[
a^2=u\,g(u,b),
\]

the deck transformation is an involution \(T\).  Its nearby-cycle characters
are

\[
T|_{\mathcal R_+}=+1,
\qquad T|_{\mathcal L_-}=-1.
\]

Every map obtained functorially from the normalized exact complex—including
the map to the Koszul resolution of \(z^2\), its chosen geometric
nullhomotopy, and its homotopy fiber—commutes with \(T\).  In the eigenbasis,
an arbitrary map is

\[
F=\begin{pmatrix}F_{++}&F_{+-}\\F_{-+}&F_{--}\end{pmatrix}.
\]

The equation \(TF=FT\) gives

\[
2F_{+-}=0,\qquad 2F_{-+}=0.
\]

Over \(\mathbb Q\), both cross-character blocks vanish.  Equivalently, the
canonical idempotents

\[
e_+=\frac{1+T}{2},\qquad e_-=\frac{1-T}{2}
\]

split the entire diagram, and cones and homotopy fibers preserve this split.
Thus there can be no derived extension between the even Koszul block and the
odd matrix-factorization block.

## What the quartic-tail mixing can mean

This does not erase Entry 450's first-order mixing.  The quartic carrier
basis has characters

\[
(1,a,a^2,a^3)=(+,-,+,-).
\]

Hence the tail itself has an even rank-two and an odd rank-two part.  The
complete exact complex may mix \(\mathcal R_+\) with the even tail and
\(\mathcal L_-\) with the odd tail.  It cannot mix the two monodromy
characters with each other.

Accordingly the full remaining calculation is not one large extension
problem but two independent same-character calculations:

\[
\operatorname{Fib}(F)
\simeq
\operatorname{Fib}(F_+)\oplus\operatorname{Fib}(F_-).
\]

The plus calculation must determine whether the even quartic tail contributes
anything beyond the Koszul length-two cell.  The minus calculation must
determine whether the odd tail contributes anything beyond the globally
extended twisted matrix-factorization line.

## Logical boundary

The splitting is unconditional for a deck-equivariant derived
specialization morphism.  It does **not** construct that morphism.  A map
assembled from chart formulas without proving deck equivariance cannot invoke
this theorem; such a failure would expose a non-geometric choice, not a new
extension class.  The next executable gate is therefore to construct the
normalized map character by character and compute its residual kernel and
cokernel within each eigenspace.

The checker verifies the commutator equations, the two idempotents, and the
\(2+2\) character split of the quartic tail using exact rational arithmetic.
