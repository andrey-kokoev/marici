# Faithful ports can compose to a blind net

## Conjecture under attack

After separating invariant construction from instrument authority, the next
natural claim is:

> A family of source-authorized ports, each proved faithful on the invariant
> object, remains faithful when composed through an authorized observation
> interface.

This claim is false.  Local faithfulness is not preserved by arbitrary
downstream pairing.

## Minimal hostile network

Let the invariant carrier be

\[
C=\mathbb F_7.
\]

Use two faithful ports

\[
r_+(x)=x,
\qquad
r_-(x)=-x.
\]

The route packet

\[
R(x)=(r_+(x),r_-(x))=(x,-x)
\]

is faithful.  Now apply the sum interface

\[
S(a,b)=a+b.
\]

The composite is

\[
(S\circ R)(x)=x-x=0
\]

for every \(x\).  Both routes are individually faithful and the pair is
jointly faithful before aggregation, but the exposed network readout is
completely blind.

The same ports wired to the difference interface

\[
D(a,b)=a-b
\]

give

\[
(D\circ R)(x)=2x,
\]

which is faithful over \(\mathbb F_7\).

## Verdict

Instrument authority and network-composition authority are separate.  A
kernel theorem for every local port does not imply a kernel theorem for the
assembled readout.

The missing constructor is:

```text
ObservationNet
  route_ports
  wiring_map
  route_labels
  pairing_signs
  composite_domain
  composite_kernel
  retained_complementary_ports
  source_authority
```

The route packet retains the distinction.  Blindness begins at the sum
interface.  Keeping both the sum and difference ports restores faithfulness,
since they reconstruct the two route values when two is invertible.

## Deutschian significance

An explanation must locate the first nonfaithful arrow.  It is insufficient
to say that every component was valid or that the final zero was required by
symmetry.  The source must explain why this particular pairing is the admitted
record interface and which complementary distinction it discards.

## Revised conjecture

> Invariant construction, local instrument authority, and observation-net
> wiring are independently typed.  Faithfulness of the exposed system is a
> theorem about their full composite, not a property inherited from its local
> factors.

The next falsifier asks whether even a faithful complete net can lose its
distinctions after lawful composition with another independently faithful net.
