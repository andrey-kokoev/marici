# Gauge quotient and observer quotient are different operations

## Decisive distinction

Two mechanisms can both make coordinates disappear:

1. a gauge quotient removes a common transformation that preserves the complete
   relational certificate;
2. an observer quotient applies a non-injective readout and may erase a
   physically nonzero component.

They must not be identified.

## Relational gauge criterion

Let source preparations have feature vectors (v_i) in an inner-product space,
and let their relational certificate be the Gram matrix

[
K_{ij}=langle v_i,v_jangle.
]

A common orthogonal or unitary action (U) is invisible because

[
langle Uv_i,Uv_jangle=langle v_i,v_jangle.
]

When the source theory authorizes this common action as a change of frame, the
Gram matrix is a complete frame-free certificate of span and conditioning.
No absolute coordinate orientation is required.

Aspect's pure-qubit rows provide the exact optical instance:

[
a_i=(1,r_i),qquad
K_{ij}=1+r_imathbin{cdot}r_j
      =2|langlepsi_i,psi_jangle|^2.
]

A common unitary is therefore gauge for the probe-frame certificate.

This inference is typed. Purity and indistinguishability are required to turn
measured two-copy overlaps into this pure-state Gram geometry. Without those
certificates, the same scalar overlap table need not describe the claimed
feature vectors.

## Character projection criterion

Let a two-sheet transport be

[
T:Xlongrightarrow Yoplus Y,
qquad
T(x)=(A(x),B(x)).
]

The symmetric and antisymmetric readouts are

[
E(x)=A(x)+B(x),qquad M(x)=A(x)-B(x).
]

If (M(x)=0), one may conclude only that (T(x)) lies in the diagonal
subspace. One may not conclude that (T(x)=0). The exact falsifier is

[
T(x)=(y,y),qquad y
e0,
]

for which (M(x)=0) but (E(x)=2y
e0).

Strominger's exceptional circuits realize precisely this witness. Their
magnetic projection vanishes because the two nonzero sheets agree, while the
complementary electric projection remains nonzero.

For a finite symmetry group, the same statement becomes representation
theoretic: a readout supported on one character sector cannot establish
vanishing in the omitted isotypic sectors. Faithful observation requires a
source-authorized family whose character projections jointly separate the
reachable transport image.

## Combined theorem

A discarded direction is certified as gauge only when both conditions hold:

1. the declared relational certificate is invariant under that direction;
2. source authority identifies points along the direction as presentations of
   the same physical preparation or process.

A kernel of one observer satisfies neither condition by itself.

Conversely, a family of character ports is observationally complete on a
reachable source locus (L) exactly when the intersection of their kernels
with (L) is zero. This is a locus-relative statement; global injectivity is
unnecessary.

Thus the correct sequence of gates is:

1. derive the source-reachable locus;
2. quotient only source-authorized common gauge;
3. decompose the remaining transport into symmetry characters;
4. prove the admitted ports jointly separate that quotient locus;
5. only then optimize conditioning.

## Cross-lane consequences

### Optics

Pairwise fidelities can replace an absolute Pauli frame, but only after purity,
indistinguishability, common-port typing, and loss calibration are certified.
The overlap instrument removes frame gauge; it does not create a missing
preparation latitude.

### Strominger

Magnetic invisibility is not transport absence. The symmetric electric port is
a required complementary character on the exceptional locus. The next test is
whether magnetic and electric ports are jointly available on the same source
packet, not merely separately definable.

### Flavor

A signed contrast can vanish through cancellation of two nonzero stage
responses. Before interpreting a flavor null as absence, decompose the
stage-exchange action and test both invariant and anti-invariant components.
Only source-authorized stage equivalence may be quotiented as gauge.

### Grothendieck

Reflection-even and reflection-odd theta channels must be treated as character
ports, while a common change of adelic presentation may be gauge only if it
preserves the full source-derived Gram or determinant certificate. A scalar
functional-equation projection cannot by itself certify disappearance of the
complementary channel.

### Kitaev

Simple-current, ribbon-reversal, and vacuum-frame actions require the same
separation. An invariant Wilson table may certify a presentation gauge only
for the complete admitted relational algebra. A single character readout may
annihilate a nonzero logical sector.

## Finite falsifier

For any claim that a vanishing readout proves absence:

1. construct the source transport vector before projection;
2. decompose it into the admitted symmetry-character components;
3. exhibit a nonzero component in the kernel of the claimed decisive port.

One such vector disproves the inference. For a gauge claim, additionally find
two source states with the same proposed certificate that are not identified
by any source-authorized frame action; that disproves completeness of the
certificate.

## Frontier

The next shared object is not simply an additional scalar probe. It is a typed
joint instrument carrying:

- a source-reachable preparation locus;
- a relational gauge certificate;
- a complete set of required character ports;
- a resource law proving those ports refer to the same preparation;
- a stability law for the resulting quotient observation map.
