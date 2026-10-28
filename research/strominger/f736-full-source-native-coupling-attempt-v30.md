# Full-source/native coupling: explicit update and native-admission test

## Frozen requirements

Attempt the new coupling on the existing finite native fixture, retaining full compact observer functions. Use the established coefficient encoder L_c:C^5->F_c and decoder D_c:F_c->C^5 with D_c L_c=I. Keep the actual native transfer U:c->d and its two established comparison equations

    D_d U=D_c,
    U L_c=L_d.

These are hypotheses on the admitted fixture transfers, not claims about every future native operation. In particular they hold for the frozen source-preserving NE comparison. The candidate native field metric on encoded vectors satisfies

    ||L_c v||^2=||T v||^2,

where T is the actual five-observation matrix. The native field transfers in the tested metric-unitary class preserve field norm.

Source inputs: the finite encoder note/contract, strict native comparison, full-five joint-field candidate, v25 grid, and the existing observer-closure audit's exact product observations. No new physical law or operator-admission rule is introduced.

## 1. Extend the observation, not the finite source decoder

For f in D=C_c^infinity(R), set

    O(f)=(ell_plus(f),ell_minus(f),A f(0),A f(delta),A f(2delta)),
    r(f)=T^(-1) O(f).

These functionals are defined on the full source. On the frozen packet E_packet(v), O(E_packet(v))=Tv and r(E_packet(v))=v. The map r is a finite observation map, not a faithful source representation.

Define the joint carrier by the compatibility equation

    X_c={(x,f) in F_c x D : D_c x=r(f)}.

It contains the exact frozen embedding

    x -> (x,E_packet(D_c x)).

Every element has a unique decomposition

    x=z+L_c r(f),   z in ker D_c.

Thus X_c is isomorphic to ker(D_c) x D. It retains the native complement and the entire observer, rather than trying to put convolution closure into five or 44 scalar coordinates. Its product/graph topology uses the LF topology of D.

This compatibility equation is a proposed extension of the original readout contract. The bare existence conjecture only specified frozen-packet agreement. If this all-source readout agreement is not required, the verdict below must be restricted accordingly.

## 2. An explicit source-active joint update

For fixed a in D let M_a f=a*f. Define

    tildeM_a(x,f)=(x+L_c[r(a*f)-r(f)], a*f).

In split coordinates this is simply

    (z,f) -> (z,a*f).

It preserves X_c because

    D_c(x+L_c[r(a*f)-r(f)])=r(a*f).

Its native field update uses full-source information, including distinctions invisible in r(f). It is linear and continuous for each fixed a on the declared carrier.

Composition is exact:

    tildeM_a tildeM_b=tildeM_(a*b).

This follows either by cancellation of the two readout increments or by source convolution associativity. D is nonunital; an identity operation is included separately as the identity multiplier, not by claiming that a delta distribution belongs to C_c^infinity.

For an admitted native U set

    tildeU(x,f)=(Ux,f).

Then tildeU maps X_c to X_d, and

    tildeU tildeM_a^c=tildeM_a^d tildeU

follows from U L_c=L_d. In split coordinates it acts by (z,f)->(Uz,f). This constructs a full-source-active coupling compatible with the existing NE square at the linear algebra level.

## 3. Native admission fails for this update

Compatibility with U does not make tildeM_a a native operation. The unchanged native rules provide marked-context transfers and coefficient permutations, with their prescribed field maps; they do not admit arbitrary additive field updates.

There are two exact diagnostics.

### A. Decoded-source invariant

Every word made from the admitted source-preserving transfers satisfies

    D_target U_word x=D_source x.

The proposed update instead satisfies

    D_c x'=r(a*f).

Take f=p0 and a=2p0. Multiplicativity of the endpoint observations gives

    ell_plus(f)=ell_minus(f)=1,
    ell_plus(a*f)=ell_minus(a*f)=2.

Thus r(a*f) differs from r(f). The update cannot be any word of the admitted source-preserving transfers. Adding an idle transition also leaves the invariant unchanged.

### B. Norm obstruction for the prepared input

Take x=L_c e0, f=p0, so z=0. The actual packet has

    O(p0)=(1,1,1,0,0),
    ||x||^2=3.

The existing product calculation gives

    O(p0*p0)=(1,1,rho,0,0),
    rho=A integral p0(u)^2 du >0.

For a=2p0, the proposed update therefore has

    O(a*f)=(2,2,2rho,0,0),
    ||x'||^2=8+4rho^2>3.

It cannot be implemented by a norm-preserving native field word. More strongly, any joint update obeying the same full-source readout equation D_d x'=r(a*f) in this orthogonal five-frame metric must have

    ||x'||^2 >= ||T r(a*f)||^2=8+4rho^2.

Changing its undecoded complement cannot repair the norm inequality: that complement is orthogonal to the encoded five-frame. This stronger statement uses the documented orthogonal encoder/readout construction, not merely an arbitrary right inverse.

The source test a=2p0 is a nonzero admitted compact smooth convolution observer. This is an analytical observer action; the calculation exposes why requiring every such action to be a native metric-unitary execution is a stronger and generally incompatible demand.

## 4. Verdict and scope

The explicit full-source joint update exists and commutes with the source-preserving native crossing. It fails admission as an operation in the unchanged source-preserving/metric-unitary native transfer class.

Under the additional natural requirement that the original five observations continue to agree with the native decoder on the full source, the universal claim that every source convolution is realized by such native transfers is rejected. The endpoint invariant and norm calculation give separate exact obstructions.

The bare broader conjecture only requires agreement on the frozen packet. It could evade this test by changing the observation semantics after leaving that packet, by authorizing nonunitary source-driven native updates, or by separating analytical observer action from native execution. None of these is established here. In particular, independent source action with an idle native field would not implement the full-source readout compatibility tested above.

The source convolution action and NE are therefore separate operation types in this attempt. A useful next contract must say whether convolution is an analytical indexing action, a native execution, or a source/native coupled operation with a newly admitted rule. Calling all three 'whiskering' would hide the failed equation.

No H736 or dependent filler was constructed, and the net was not changed. The attached checker verifies exact observation-matrix arithmetic and the norm polynomial; domain continuity, convolution identities and native rule scope are the explicit mathematical/source premises above.
