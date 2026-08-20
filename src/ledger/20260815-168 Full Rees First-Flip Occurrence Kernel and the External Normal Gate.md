# Full Rees First-Flip Occurrence Kernel and the External Normal Gate

## Record

Date: 2026-08-15

Status: theorem proved for the regular two-generator occurrence/Rees layer.
The full blowup realizes the universal first-flip occurrence packet, not only
its exceptional associated grade. Endpoint reciprocal-to-BM normal/Cech
counits, the external entry-100 normal kernel, and the nonzero generic-(Q\)
gluing remain unconstructed. No graph admission is claimed.

## Ordered occurrence ideal and Rees blowup

Let

\[
A=\mathbb Z[x_5,X_{D03},\ldots]
\]

be the unlocalized occurrence ring, with \(x_5,X_{D03}\) independent
polynomial parameters, and put

\[
I=(x_5,X_{D03}).
\]

The full first-flip occurrence space is

\[
Y=\operatorname{Bl}_I(\operatorname{Spec}A)
=\operatorname{Proj}\operatorname{Rees}_A(I),
\qquad
\pi:Y\longrightarrow\operatorname{Spec}A.
\]

With homogeneous coordinates \([G:H]\), its Rees equation is

\[
X_{D03}G-x_5H=0.
\]

The two standard affine charts are

\[
U_G=\operatorname{Spec}A[t]/(X_{D03}-x_5t),
\qquad t=H/G,
\]

and

\[
U_H=\operatorname{Spec}A[s]/(x_5-X_{D03}s),
\qquad s=G/H.
\]

On their common locus \(s=t^{-1}\). Away from \(V(x_5,X_{D03})\),
\(\pi\) is an isomorphism. Over the center the exceptional fibre is

\[
E\simeq\mathbb P^1.
\]

No occurrence variable has been inverted on the base; the ratios occur only
in their named blowup charts.

## Tautological convention and exact sheaf sequence

Fix the quotient convention

\[
\mathcal O_Y(1)=\mathcal O_Y(-E),
\qquad
\pi_*\mathcal O_Y(1)=I.
\]

Thus \(\mathcal O_Y(1)|_E\simeq\mathcal O_{\mathbb P^1}(1)\), while
\(\mathcal O_Y(-1)=\mathcal O_Y(E)\). With this convention the canonical
labelled sequence is

\[
\boxed{
0\longrightarrow
\mathcal O_Y(E)
\xrightarrow{\ (X_{D03},-x_5)\ }
\mathcal O_Y^{\oplus2}
\xrightarrow{\ (x_5,X_{D03})\ }
\mathcal O_Y(-E)
\longrightarrow0.
}
\]

The composite vanishes strictly:

\[
x_5X_{D03}-X_{D03}x_5=0.
\]

The first arrow is the primitive relation from entry 167 and the last arrow
is the tautological quotient. The relation is unique up to one global scalar;
the marked orientation selects \((X_{D03},-x_5)\).

## Derived pushforward and the universal edge complex

On the exceptional fibre,

\[
h^0(\mathcal O_E(1))=2,
\qquad
h^1(\mathcal O_E(1))=0.
\]

Cohomology and base change, together with the isomorphism away from the
center, give

\[
R\pi_*\mathcal O_Y(-E)=I,
\qquad
R^{>0}\pi_*\mathcal O_Y(-E)=0.
\]

For the other two terms,

\[
R\pi_*\mathcal O_Y(E)=A,
\qquad
R\pi_*\mathcal O_Y^{\oplus2}=A^{\oplus2},
\]

with no higher terms in this regular two-generator case. Therefore the
derived pushforward of the sheaf sequence is the exact Koszul presentation

\[
\boxed{
0\longrightarrow A
\xrightarrow{\ (X_{D03},-x_5)\ }
A^2
\xrightarrow{\ (x_5,X_{D03})\ }
I
\longrightarrow0.
}
\]

This is the universal \(A\)-linear first-flip occurrence complex isolated in
entry 106 and refined by entry 167. The full Rees blowup constructs it before
specializing to the exceptional fibre.

## The exceptional interval is only associated grade

The oriented exceptional \(\mathbb P^1\), or its real interval shadow with
two labelled ends, records the associated-grade direction

\[
[x_5:X_{D03}].
\]

It recovers the primitive relation and endpoint orientation after passage to
the exceptional grade. It is not the whole construction: retaining only the
interval forgets the two affine Rees charts, their transition, the ideal
pushforward \(I\), and the universal off-exceptional occurrence family.

Thus entry 106's exceptional interval is a correct associated-grade shadow,
while \(Y\) is the full occurrence kernel.

## Free endpoint lines are not divisor sheaves

The middle term after pushforward has two free presentation generators,

\[
A\langle m_+\rangle\oplus A\langle v_+\rangle.
\]

They are not structure sheaves of the coordinate divisors. The latter push
forward to

\[
A/(x_5),
\qquad
A/(X_{D03}).
\]

Hence

\[
A\langle m_+\rangle\ne A/(x_5),
\qquad
A\langle v_+\rangle\ne A/(X_{D03}).
\]

The free generators present the ideal \(I\); they do not assert that either
endpoint is supported only on a coordinate divisor. Confusing these types
would destroy the line-valued counit and replace a syzygy resolution by two
torsion quotient modules.

## External entry-100 normal kernel

The entry-100 reciprocal normal packet is external to the occurrence Rees
construction. Its exclusive line \(u_5^\vee\), shared normals \(u_1,u_3\),
and repeated-\(u_3\) excess packet can be tensored with the exact occurrence
resolution. At the coefficient level this retains

\[
\operatorname{Tor}_0=R/J,
\qquad
\operatorname{Tor}_1=R/J
\]

and the abstract \(\eta_{3,\rm mix}\) evaluation with the established signs.
It uses neither \(x_5^{-1}\) nor \(X_{D03}^{-1}\) on the source.

This external compatibility does not construct:

- the reciprocal-to-original-BM endpoint counits;
- the lower Cech terms on the two half-corridor charts;
- the normal-cone map for the external \(x_3\) Thom/excess packet;
- the second central flip; or
- a spatial comparison with the literal entry-143 states.

In particular, tensor compatibility is not a claim that the entry-100 normal
kernel is already geometrically attached to \(Y\).

## Relative carrier and star boundary

The two endpoint branches of the first flip give the expected primitive
relative carrier line after forgetting coefficients. This is compatible with
the Rees relation and with the entry-167 line-valued counit. Ordinary
restriction to a single scalar star, however, cannot supply the required
cross-support normal comparison: it either retains only one endpoint branch
or lands in the familiar augmentation-zero submodule.

The Rees construction repairs the occurrence syzygy, not the spatial star
map. No new two-branch support pullback or extraordinary normal map follows
from the existence of the blowup.

## Generic-Q boundary

The literal first flip, both labelled endpoints, and its edge lie in the
short-boundary support \(F_B\). Therefore their projection to

\[
Q=F_K/F_B
\]

is zero. Equivalently, the full occurrence Rees kernel has

\[
\pi_Q(Y_{\rm first\ flip})=0.
\]

This does not contradict its nonzero ideal pushforward: \(I\) is an
occurrence coefficient object, whereas \(Q\) is the spatial long-facet
quotient. The two types must not be identified.

Consequently the Rees kernel does not provide the retained generic
\(q_J\) component, attachment to the \(F03\) peripheral cone roof, or the
entry-160 Beck--Chevalley cell. Those require a second-flip/long-chart
correspondence leaving \(F_B\) in a controlled support-graded sense.

## Anti-circularity controls

- Do not replace the full Rees blowup by its exceptional interval.
- Do not identify \(\mathcal O_Y(-E)\) with \(\mathcal O_Y(E)\); the fixed
  convention is \(\mathcal O_Y(1)=\mathcal O_Y(-E)\) and
  \(\pi_*\mathcal O_Y(-E)=I\).
- Do not identify free endpoint presentation lines with coordinate-divisor
  quotient sheaves.
- Do not infer endpoint BM counits or lower Cech maps from an external tensor
  product.
- Do not infer a nonzero \(Q\) leg from the nonzero ideal \(I\).
- Do not infer graph admission, a spatial normal enhancement,
  Beck--Chevalley, endpoint pointing, or parity from the occurrence blowup.
- Do not invert an occurrence variable, normal parameter, or integer.

## Falsifiers and scope

The Rees theorem would be falsified by failure of either affine chart,
failure of the sheaf sequence, a nonzero higher direct image of the positive
tautological line in this regular case, failure of its pushforward to be
\(I\), or an additional independent relation in the two-generator ideal.

The geometric boundary would be crossed by an independently constructed
spatial normal-cone comparison attaching the entry-100 reciprocal packet to
the literal first-flip charts, including both endpoint counits and every
lower Cech term, followed by a nonzero attachment to the filtered
\(U_{03}/Q\) leg.

No no-go is claimed for such an enlarged correspondence. The theorem is
scoped to the occurrence/Rees layer and its derived pushforward.

## Exact certificate

The exact checker is

- `research/voevodsky/check_d03_rees_first_flip_occurrence.rs`.

Its SHA-256 hash is

`be53ad19db433239ed6892c526d005e6aeb0a288d2afb8fa9849d7e2d7675b50`.

It verifies the Rees equation and both charts, exceptional
\(\mathbb P^1\) cohomology, vanishing higher pushforward, tautological ideal
pushforward, primitive unique syzygy, free resolution, separation of endpoint
free lines from divisor quotients, and zero generic-\(Q\) projection.

## Next experiment

Tensor the full occurrence Rees resolution with the entry-100 reciprocal
normal kernel and construct the actual spatial normal-cone map on both Rees
charts. Derive, rather than assign, the two endpoint reciprocal-to-BM
counits and every lower Cech term, retaining both repeated-\(u_3\) Tor grades.
Then attach the second central flip and test whether the enlarged
correspondence reaches the \(F03\) peripheral roof with a retained nonzero
\(q_J\) leg. Only afterward test Beck--Chevalley or endpoint parity.

## Outcome contract

~~~json
{
  "claim": "For I=(x5,X_D03), the full Rees blowup Y has charts X_D03=x5*t and x5=X_D03*s, and the positive tautological line O_Y(1)=O_Y(-E) pushes to I with no higher term; its canonical sheaf sequence pushes to the universal exact first-flip occurrence complex 0 -> A -> A^2 -> I -> 0.",
  "status": "proved",
  "scope": "regular two-generator occurrence/Rees layer and derived pushforward only; no spatial normal enhancement, endpoint BM-Cech counits, U03/Q gluing, or graph admission",
  "assumptions": [
    "x5 and X_D03 are an ordered regular sequence of independent occurrence variables.",
    "Proj uses the quotient convention O_Y(1)=O_Y(-E).",
    "The entry-100 reciprocal normal kernel remains an external typed factor.",
    "The literal first flip remains inside entry-143 short-boundary support F_B."
  ],
  "factorization": {
    "Rees_equation": "X_D03*G-x5*H=0",
    "G_chart": "A[t]/(X_D03-x5*t)",
    "H_chart": "A[s]/(x5-X_D03*s)",
    "exceptional_fibre": "P1",
    "tautological_convention": "O_Y(1)=O_Y(-E)",
    "sheaf_sequence": "0 -> O_Y(E) --(X_D03,-x5)--> O_Y^2 --(x5,X_D03)--> O_Y(-E) -> 0",
    "pushforwards": ["A", "A^2", "I=(x5,X_D03)"],
    "higher_pushforwards": "zero",
    "universal_occurrence_complex": "0 -> A -> A^2 -> I -> 0",
    "primitive_syzygy": "(X_D03,-x5), unique up to scalar",
    "exceptional_interval": "associated grade only",
    "endpoint_free_lines": ["A*m_plus", "A*v_plus"],
    "coordinate_divisor_modules": ["A/(x5)", "A/(X_D03)"],
    "external_entry100_normal_kernel": "coefficient-compatible; spatial attachment unconstructed",
    "repeated_u3": "Tor0 and Tor1 retained",
    "endpoint_BM_Cech_counits": "unconstructed",
    "lower_Cech_terms": "unconstructed",
    "generic_Q_projection": "zero"
  },
  "evidence_refs": [
    "research/voevodsky/check_d03_rees_first_flip_occurrence.rs",
    "src/ledger/20260814-100 Support-Directed Can-Var Packet and Three Local Cousin Traces.md",
    "src/ledger/20260814-106 Marked Log Gallery Secondary Class and the Global Yoneda Gap.md",
    "src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md",
    "src/ledger/20260815-166 Two-Support MV Excess and the Missing D03 Chart-Generic Leg.md",
    "src/ledger/20260815-167 First Central-Flip Line-Valued Counit and the Next-Flip Generic Gate.md"
  ],
  "checker_sha256": "be53ad19db433239ed6892c526d005e6aeb0a288d2afb8fa9849d7e2d7675b50",
  "counterevidence": [
    "The exceptional interval forgets the full two-chart Rees family and ideal pushforward.",
    "Free presentation lines are not coordinate-divisor quotient modules.",
    "External coefficient compatibility does not construct endpoint BM-Cech counits or spatial normal maps.",
    "The entire literal first flip lies in F_B and has zero projection to Q."
  ],
  "next_experiment": "Tensor the full occurrence Rees resolution with the entry-100 reciprocal normal kernel, construct the spatial normal-cone map and both endpoint BM-Cech counits with all lower Cech terms, then attach the second flip and test a retained nonzero q_J leg before Beck-Chevalley or parity."
}
~~~
