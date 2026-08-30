# The marked germ must be congruence-closed under source constructors

## Present visibility is insufficient

A target-relative quotient must support composition with admitted transformations. If
\(v\) and \(w\) have identical current target readouts but an authorized
constructor \(C\) makes some readout distinguish \(Cv\) from \(Cw\), then
identifying \(v\) with \(w\) destroys composition.

Therefore the full-fiber relation must be a congruence:

\[
v\sim w
\Longrightarrow
Cv\sim Cw
\]

for every admitted source constructor \(C\).

## Linear formula

Let \(\mathcal T\) be the declared linear target family and
\(\mathcal M_{\mathrm{src}}\) the authorized constructor monoid. The largest
discardable subspace is

\[
K_*
=
\bigcap_{F\in\mathcal T}
\bigcap_{C\in\mathcal M_{\mathrm{src}}}
\ker(F\circ C).
\]

Equivalently, \(K_*\) is the largest constructor-invariant subspace contained
in the kernel of every immediate target readout. The marked germ is

\[
G_*=V/K_*.
\]

This is the linear form of Aspect's retained-port requirement. A currently
silent direction remains in the germ when an authorized composed operation can
activate it.

## Finite shift witness

Let the immediate target read only the first coordinate of \((x,y,z)\), and
let an admitted constructor shift

\[
C(x,y,z)=(y,z,0).
\]

The immediate kernel contains both \(y\) and \(z\). After one constructor
application, \(y\) becomes visible. After two, \(z\) becomes visible. The
constructor-closed common kernel is zero. Quotienting either silent coordinate
before closing the constructor orbit would make the shift ill-defined on the
quotient.

## RH consequence

Primitive and square incidence cannot be treated as a static finite list of
readouts. Prime multiplication, valuation-depth operations, reciprocal
transport, inverse-frequency transport, and cutoff inclusions enlarge their
observable orbit. The RH germ must be formed from that closed orbit.

This gives a disciplined answer to whether the full valuation/Fock carrier is
over-retained. Finite valuation cylinders separate every finite packet by
unique factorization, so the constructor-closed germ may equal the full finite
packet module. If so, that is a theorem of the target orbit rather than an
assumption. At completion, a nonzero common pro-kernel may reappear and must be
tested separately.

## Native-arity and authority gates remain

Congruence closure only makes source constructors descend. It does not prove
that the nonlinear relative determinant is constant on the resulting full
fibers, and it does not select the determinant-line trivialization. Aspect's
arity and authority gates remain independent.

## Falsifiers

Reject a proposed germ when:

1. an admitted constructor sends two identified representatives to distinct
   target fibers;
2. a discarded direction becomes visible after a finite constructor word;
3. constructor closure is asserted only at each cutoff but fails for the
   completed monoid action;
4. congruence descent is mistaken for source authority.

## DPC verdict

The faithful marked germ is the quotient by the constructor-closed full-fiber
relation. Target relativity removes permanently irrelevant distinctions;
congruence closure retains every distinction that an authorized transformation
can make relevant after algebraic composition.

## Verification

`check_rh_constructor_closed_marked_germ.py` verifies immediate, one-step, and
two-step visibility in the shift witness, proves that the closed common kernel
is zero, and rejects the premature immediate-kernel quotient.
