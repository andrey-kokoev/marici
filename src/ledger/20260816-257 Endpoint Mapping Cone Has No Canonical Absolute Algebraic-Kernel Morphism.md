---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Endpoint Mapping Cone Has No Canonical Absolute Algebraic-Kernel Morphism

## Record

The next comparison proposed in entry 255 is finitely falsified before
coordinates are chosen. In the frozen coefficient calculus, the canonical
sewn endpoint mapping cone has no morphism into

\[
\mathcal A_{--}=\langle e_6,v_{\rm alg}\rangle\subset H^2(S).
\]

The endpoint extension remains marked relative coefficient data. This
requires no new carrier incidence.

## Deutsch--Popperian conjecture

The hard-to-vary claim was

\[
\boxed{
\text{the source endpoint mapping cone canonically and horizontally maps
to }\mathcal A_{--}.
}
\]

Before computing a matrix, freeze the source objects and every available
nonzero canonical arrow. Let \(W\subset S\) be the finite marked wall and
\(U=S\setminus W\). The relevant localization sequence is

\[
H^2(S)\longrightarrow H^2(U)
\longrightarrow H^1(W)(-1)
\longrightarrow H^3(S).
\]

The endpoint cone realizes in \(H^1(W)(-1)\). The algebraic Gysin kernel
is a subobject of \(H^2(S)\), so its canonical arrow has the opposite
variance:

\[
\mathcal A_{--}\hookrightarrow H^2(S).
\]

Consequently the frozen arrow closure contains

\[
\text{EndpointCone}\longrightarrow H^1(W)(-1)
\longrightarrow H^3(S),
\]

and

\[
\mathcal A_{--}\longrightarrow H^2(S)
\longrightarrow H^2(U)
\longrightarrow H^1(W)(-1),
\]

but contains neither

\[
\text{EndpointCone}\longrightarrow H^2(S)
\]

nor

\[
\boxed{\text{EndpointCone}\longrightarrow\mathcal A_{--}.}
\]

This is the finite falsifier.

## Why the apparent shortcuts fail

The parent label \(e_6\) records integrand ancestry. Residue changes
support and cohomological degree, so ancestry is not a morphism back to the
absolute master.

Disjointness from the infinity divisor gives zero direct elliptic boundary
image. A zero image does not select a lift into the kernel of the infinity
map.

Finally, the generic algebraic kernel already splits without
\(\mathcal Q\) support (entry 211). Even a post hoc localization splitting
would therefore not provide a source-derived home for \(\mathcal Q\).

Any nonzero endpoint-to-\(\mathcal A_{--}\) map would require one of:

- a localization splitting or contracting homotopy;
- a separately derived physical relative-realization correspondence.

Neither datum is present in the frozen construction. Adding one after
seeing \(e_6\), \(v_{\rm alg}\), or \(\mathcal Q\) is prohibited.

## Classification

- endpoint mapping cone: marked relative coefficient data;
- finite wall: existing marked carrier;
- \(\mathcal A_{--}\): absolute algebraic coefficient subobject;
- \(e_6\) relation: ancestry only;
- direct Legendre image: zero;
- canonical endpoint-to-algebraic-kernel morphism: absent;
- genuinely new carrier datum: none.

Thus the source frame failure of entry 255 cannot be repaired by replacing
the frame with an absolute algebraic-kernel target. The two objects are
compatible outputs of the same carrier calculus, not canonically identified
coefficient objects.

## Consistency with the completed home of \(\mathcal Q\)

This type gate does not reopen the provenance question already closed by
entries 181, 183, and 212. Those entries froze the positive physical sheet,
resolved every cyclic residue sector, rejected \(\mathcal Q\) from
\(3\cdot1719=5157\) raw discriminant tests, and proved

\[
T_{\mathcal Q}=1,
\qquad
N_{\mathcal Q}=0,
\qquad
\operatorname{Var}_{\mathcal Q}(\Gamma_{\rm phys})=0
\]

at generic nonsoft homogeneous kinematics. Entry 211 independently excludes
\(\mathcal Q\) from the generic algebraic kernel and its internal
extension.

The present result adds one consistency statement:

\[
\boxed{
\text{the endpoint mapping cone supplies no hidden lift of }\mathcal Q
\text{ into }\mathcal A_{--}.
}
\]

Combining the prior provenance theorem with this gate leaves the completed
classification

\[
\boxed{
\mathcal Q
\text{ is apparent cyclic/master-presentation alphabet data in the frozen
homogeneous system.}
}
\]

It is neither carrier support, coefficient support, algebraic-extension
support, nor physical relative-chain support on the generic locus. The
shared carrier remains unchanged.

## Exact evidence

- research/benincasa/marici-gm/src/bin/endpoint_to_algebraic_kernel_type_gate.rs;
- research/benincasa/endpoint-to-algebraic-kernel-type-gate.json;
- entries 181, 183, 211, 212, 237, 245, 254, and 255;
- warning-denied Rust compilation and execution.

## Next hostile falsifier

Do not repeat the generic \(\mathcal Q\)-monodromy test. Instead construct
the maximal generic-open decomposition of the complete homogeneous
three-site coefficient system, including:

1. the lower Tate/Kummer sector;
2. the three cyclic nine-master residue sectors;
3. each rank-seven algebraic kernel;
4. each rank-two elliptic infinity-Gysin quotient;
5. the marked relative endpoint/wall objects;
6. every source-defined sewing and extension arrow.

The hard-to-vary claim is

\[
\boxed{
\text{over the maximal generic open base, every non-elliptic constituent is
Tate/Kummer or marked-relative data, and all cross-layer arrows are generated
by the frozen localization/Gysin/sewing calculus.}
}
\]

A finite falsifier is any source master, singular divisor, or extension arrow
that cannot be placed in that inventory without a new carrier stratum or an
unmotivated splitting.

## Outcome contract

~~~json
{
  "claim": "The canonical endpoint mapping cone admits a source-defined horizontal morphism into A_--.",
  "status": "falsified_by_type_and_variance",
  "endpoint_object": "marked wall relative coefficient object",
  "target_object": "A_-- subset H2(S)",
  "canonical_endpoint_to_H2_arrow": false,
  "canonical_endpoint_to_A_--_arrow": false,
  "e6_ancestry_is_coordinate": false,
  "zero_infinity_image_selects_kernel_lift": false,
  "new_carrier_incidence": false,
  "prior_Q_verdict": "apparent_cyclic_master_presentation_alphabet_data",
  "T_Q": "identity",
  "N_Q": 0,
  "endpoint_gate_adds_hidden_Q_lift": false,
  "next_experiment": "Construct or finitely falsify the maximal generic-open decomposition of the complete homogeneous three-site coefficient system."
}
~~~
