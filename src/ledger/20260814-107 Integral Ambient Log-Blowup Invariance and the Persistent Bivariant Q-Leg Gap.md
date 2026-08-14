# Integral Ambient Log-Blowup Invariance and the Persistent Bivariant Q-Leg Gap

## Record

Date: 2026-08-14

Status: proved for the integral loaded stellar subdivision, its filtered
strong deformation retract, literal invariance of the relative road quotient,
and transport of the global Yoneda extension. Falsified as a construction of
the missing marked Beck--Chevalley map.

## The ambient modification

Let

\[
p:\widetilde K_6=\operatorname{Bl}_{C}K_6\longrightarrow K_6,
\qquad C=\{D03,x_1\}.
\]

The center is an actual codimension-two face of the labelled hexagon
associahedron. It is contained in the short-diagonal boundary
\(B_{\rm short}\) and is disjoint from the positive central vertex

\[
v_+=\{x_1,x_3,x_5\}.
\]

Use the full inverse-image filtration

\[
\widetilde F_0=F_0,
\qquad
\widetilde F_1=PC_{\rm supp}(p^{-1}B_{\rm short}),
\qquad
\widetilde F_2=PC_{\rm supp}(\widetilde K_6).
\]

The ordinary and blown-up face censuses are

\[
(1,9,21,14)
\quad\longrightarrow\quad
(1,10,24,16),
\]

and the loaded degree ranks are

\[
(14,63,93,45)
\quad\longrightarrow\quad
(16,72,106,51).
\]

Thus the absolute loaded complex grows from 215 to 245 generators, with

\[
\operatorname{rk}(\widetilde F_0,\widetilde F_1,\widetilde F_2)
=(8,238,245).
\]

## Occurrence and monodromy are different layers

The blowup exposed a necessary correction. The exceptional monodromy
character is multiplicative:

\[
q_E=q_{03}q_1,
\qquad
u_E=u_{03}+q_{03}u_1
=u_{03}+u_1+u_{03}u_1.
\]

There is no corresponding additive occurrence variable
\(X_E=X_{03}+x_1\). Occurrence coefficients come from the lcm-labelled
cellular resolution.

Over the marked point

\[
b=\{D03,x_1,x_3\},
\]

the exceptional interval separates vertices \(b_1,b_D\). The occurrence
boundaries are

\[
de_c'=X_{03}b_1-x_5a,
\qquad
dh_E=b_D-b_1,
\qquad
de_r'=x_0c-x_1b_D.
\]

The exceptional edge therefore has unit cellular boundary. The unique
primitive expanded chain is

\[
\boxed{
\widetilde\xi
=x_1e_c'+X_{03}x_1h_E+X_{03}e_r'
}
\]

and it obeys

\[
\boxed{
d\widetilde\xi=X_{03}x_0c-x_1x_5a.
}
\]

The blowdown and section are

\[
\begin{aligned}
r(b_1)=r(b_D)&=b,& r(h_E)&=0,&
r(e_c')&=e_c,&r(e_r')&=e_r,\\
s(b)&=b_1,&s(e_c)&=e_c',&
s(e_r)&=e_r'+x_1h_E.
\end{aligned}
\]

They satisfy \(rs=1\), carry \(\xi\leftrightarrow\widetilde\xi\), and the
unit exceptional edge gives an integral chain homotopy between \(sr\) and
the identity.

The independent normal subdivision is the saturated complex

\[
L_0=R\langle p\rangle,
\qquad
L_1=R\langle h_{03},h_E,h_1\rangle,
\qquad
L_2=R\langle A,B\rangle,
\]

with

\[
dA=h_E-h_{03}-q_{03}h_1,
\qquad
dB=u_1h_{03}-u_{03}h_1.
\]

It retracts integrally to \(K(u_{03},u_1)\) by

\[
r(h_E)=h_{03}+q_{03}h_1,
\qquad r(A)=0,
\qquad r(B)=h_{03}\wedge h_1,
\qquad H(h_E)=A.
\]

Tensoring this local contraction with every spectator packet preserves it:
the two totalization cross terms cancel with opposite Koszul signs. No Rees
parameter, normal variable, occurrence coefficient, or integer is inverted.

## Filtered invariance and the literal road quotient

The occurrence and normal contractions are supported entirely over the
center, hence entirely inside \(\widetilde F_1\). Extending them by the
identity gives an integral filtered strong deformation retract

\[
(\widetilde F_0\subset\widetilde F_1\subset\widetilde F_2)
\simeq
(F_0\subset F_1\subset F_2)
\]

which is the identity on \(F_0\) and on

\[
Q=F_2/F_1.
\]

More strongly, the blown-up quotient is literally the same seven-generator
chain complex:

\[
\widetilde Q=\widetilde F_2/\widetilde F_1=Q,
\qquad
(\operatorname{rk}Q_i)_i=(0,0,3,4).
\]

Its three long-facet occurrence attachments and three normal-circle
boundaries retain their original coefficients and signs.

Consequently the global Yoneda two-extension

\[
e_F=
[0\to F_0\to F_1\to F_2/F_0\to Q\to0]
\in\operatorname{Ext}^2(Q,F_0)
\]

transports canonically through the filtered subdivision equivalence. This is
an actual invariance theorem, not merely equality of associated grades.

## The surviving obstruction

The same support calculation prevents an overclaim. Since
\(C\subset B_{\rm short}\), the complete exceptional divisor and every cell
of the expanded gallery lie in \(\widetilde F_1\). Therefore

\[
q_{\widetilde Q}\circ\widetilde\gamma=0.
\]

The literal marked restriction of the transported Yoneda class remains the
entry-105 zero:

\[
\operatorname{pb}_{03}^{\rm lit}(p^*e_F)=0.
\]

The nonzero chain \(\widetilde\xi\) is a canonical secondary trivialization
inside \(\widetilde F_1\). It is not itself a representative of a map from
\(Q\) to \(F_0[2]\). Blowup invariance transports the already known gallery
class; it does not create the missing extraordinary-pullback leg.

The first unconstructed arrow is therefore

\[
\boxed{
\operatorname{BC}^{\log}_{+;03}:
R\!\operatorname{Hom}(\widetilde Q,\widetilde F_0[2])
\longrightarrow
\mathcal H^{\rm loc}_{+;03},
}
\]

where \(\mathcal H^{\rm loc}_{+;03}\) is the normalized local bivariant Hom
complex of entries 97 and 100. It must be constructed independently and
satisfy

\[
\operatorname{BC}^{\log}_{+;03}(p^*e_F)=\Theta_{03}^{\rm loc}.
\]

Its associated-grade carrier must be \(\widetilde\xi\); its excess component
must be the labelled two-copy class \(\eta_{3,\rm mix}\); and its endpoint,
physical-normal, determinant, and support variances must all be visible.
Entry 97 proves uniqueness only after such a closed, correctly typed,
unit-normalized cocycle exists. It cannot supply existence.

## Rejected shortcut

If one incorrectly introduces an additive occurrence coefficient
\(X_E=X_{03}+x_1\), the subdivision quotient contains \(K(X_E)\), with

\[
H_0=R/(X_E),
\]

and a blowdown contraction would require \(X_E^{-1}\). This is a useful
negative control: it detects precisely the forbidden conflation of lcm
occurrence weights with Kummer-character multiplication.

## Evidence

Exact certificate:

- `research/voevodsky/check_d03_global_log_blowup_relative_q.rs`

SHA-256:

```text
07b2fb9eae2390c779140ce1e37542ebc83c475cb7747c5af9c31a152869da2d
```

It verifies the full face and loaded-generator censuses, exceptional square,
occurrence contraction, saturated normal contraction, spectator signs,
filtered ranks, literal relative quotient, transported extension, and zero
exceptional \(Q\)-image. The entry-105 and entry-106 certificates were also
rerun.

## Consequence

The ambient log blowup is now understood exactly:

\[
\boxed{
\text{canonical integral resolution and invariance theorem,}
\quad
\text{not the missing bivariant comparison.}
}
\]

The scalar master already contains the local secondary carrier and the
global two-extension, and the blowup relates each to its own transform. The
remaining mathematics is the extraordinary operation relating those two
categorical degrees.

## Outcome contract

```json
{
  "claim": "The ambient toroidal blowup along C={D03,x1} gives an integral filtered stellar-subdivision equivalence, preserves the global Yoneda two-extension, and canonically expands the marked gallery, but its exceptional/gallery support has zero relative-Q image and therefore does not construct the missing Beck--Chevalley map.",
  "status": "proved",
  "assumptions": [
    "The blowup filtration uses the full inverse image of the short-diagonal boundary.",
    "Occurrence coefficients use the lcm-labelled cellular resolution and remain independent of monodromy parameters.",
    "The ordered center normals are (D03,x1), fixing q_E=q_D03 q_1 and the positive exceptional orientation."
  ],
  "evidence_refs": [
    "research/voevodsky/check_d03_global_log_blowup_relative_q.rs",
    "ledger entries 97, 100, 105, and 106"
  ],
  "factorization_test": {
    "absolute_filtered_SDR": "passed integrally",
    "relative_Q": "literal seven-generator identity",
    "global_Yoneda_transport": "passed",
    "expanded_gallery": "passed",
    "ordinary_exceptional_Q_leg": "falsified; identically zero",
    "global_to_local_Beck_Chevalley": "unconstructed"
  },
  "counterevidence": [
    "The exceptional divisor and expanded gallery lie wholly in F1.",
    "The local secondary trivialization and global Ext2 class inhabit different functorial types.",
    "Rank-one local uniqueness does not construct a bivariant source map.",
    "An additive exceptional occurrence variable produces a noncontractible K(X_E) quotient and is rejected."
  ],
  "next_experiment": "Construct BC_log_{+;03} as an independently typed extraordinary pull--push kernel with a nonzero Q leg, then test its carrier, repeated-normal excess class, endpoints, and physical normal before invoking local uniqueness."
}
```
