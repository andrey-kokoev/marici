# Whole-Gallery Cartier--Tag Gysin and the Primitive Three-Top Obstruction

## Record

Date: 2026-08-14

Status: proved for the supported associated-grade \(D03\) whole-gallery map
and for the failure of the three rotated tops to glue in the existing
absolute/barycentric scalar carrier. No full PC extraordinary-costalk lift,
positive-sheet totalization, or factorization-natural half-object is claimed.

## Claim

Let \(B_{+,03}^{\rm Cart}\) be entry 110's endpoint-and-generic-relative
Cartier complex. After the natural lcm-line cap, its expanded gallery is

\[
C_2=R\langle H\rangle
\xrightarrow{-x_3(1,1,1)}
C_1=R\langle e_c,h_E,e_r\rangle
\xrightarrow{
\left(\begin{smallmatrix}1&-1&0\\0&1&-1\end{smallmatrix}\right)}
C_0=R\langle b_1,b_D\rangle .
\]

Hence

\[
H_1(B_{+,03}^{\rm Cart})
=R/(x_3)\langle[n]\rangle,
\qquad n=e_c+h_E+e_r,
\]

and the positive Cartier normal applied to the negative Morse thimble gives
entry 110's class \(-[\widetilde\xi]=-[n]\).

The marked \(D03\) road meets the gallery on \(e_r\). Its positive costalk
orientation is \(c\to b_D\), opposite to the gallery orientation
\(b_D\to c\). Therefore the strict representative \(-e_r^\vee\) satisfies

\[
(-e_r^\vee)(-[n])=1.
\]

The three negative edge cochains are cohomologous modulo the two internal
vertex coboundaries. This is a single whole-gallery Borel--Moore integration,
not a segmentwise assignment of three source edges to three tags.

With \(C=R/(x_1,x_3,x_5)\), the canonical quotient
\(R/(x_3)\to C\), entry 93's conormal map
\([x_3]\mapsto dx_3\), and entry 94's label \(dx_3\mapsto t_3=d_1\)
give the intrinsic supported associated-grade map

\[
\boxed{
\kappa^{\rm gr}_{+,03}:
\beta_{x_3}^{\rm Cart}(B_{+,03})
\longrightarrow C\,t_3,
\qquad
\kappa^{\rm gr}_{+,03}(-[\widetilde\xi])=+t_3 .
}
\]

No occurrence variable and no integer is inverted. A free target is
impossible:

\[
\operatorname{Hom}_R(R/(x_3),R)=0,
\qquad (-e_r^\vee)dH=x_3\ne0.
\]

The next hoped-for step does not exist inside the current source carrier.
Rotating the three Morse identities gives

\[
d(H_{14}+H_{03}+H_{25})
=q_\Sigma-
(x_1\widetilde\xi_1+x_3\widetilde\xi_3+x_5\widetilde\xi_5),
\]

where

\[
\partial q_\Sigma
=c_{14}+c_{03}+c_{25}-3v_+.
\]

For

\[
E=\{v_+,c_{14},c_{03},c_{25}\},
\]

the class is

\[
[q_\Sigma]=(1,1,1)
\in H_1(sd(K_6),E;\mathbb Z)
\simeq\ker\!\left(H_0(E)\to H_0(K_6)\right)
\simeq\mathbb Z^3.
\]

It is primitive, nonzero, and \(D_3\)-invariant. Thus no integral polynomial
higher chain in the existing endpoint-relative carrier cancels the generic
terms while retaining the three special galleries. Quotienting by the full
short boundary \(B_{\rm short}\) makes \(q_\Sigma\) bound, but kills all three
special galleries at the same time.

The target norm map itself is unobstructed:

\[
N:Rf_+\longrightarrow R\langle t_1,t_3,t_5\rangle,
\qquad N(f_+)=(1,1,1).
\]

If a common source top existed, its map to \(f_+\) would be unique and
integral. The obstruction is therefore on the scalar source side, not a need
to divide by three.

## Evidence

Exact certificates:

- `research/voevodsky/check_d03_whole_gallery_tag_gysin.rs`
- `research/voevodsky/check_three_rotated_gallery_top_gluing.rs`

SHA-256:

```text
971df4192b644a408193551b8bb02cc6c0036c93c4e2c7037824b97e450a2e20
b1fd94f004e97226c55bfc3b943c398773434eda9dee44adf1f03b3673b907d5
```

The first certificate checks the actual blown-up gallery supports, lcm-line
naturality, relative homology, road/costalk orientation, internal-coboundary
independence, supported base change, conormal label, and free-target no-go.

The second reconstructs the full \(K_6\) face poset and barycentric
differential. At unit occurrence coefficients over \(\mathbf F_{101}\),

\[
\operatorname{rk}\operatorname{im}d_2=126,
\qquad
\operatorname{rk}\langle\operatorname{im}d_2,q_\Sigma\rangle=127.
\]

Any unlocalized polynomial filler would specialize to a filler here, so the
rank jump is a valid no-go. Relative to \(B_{\rm short}\), both ranks are
\(64\), while the special galleries vanish.

Reproduce with `rustfmt --check`, `rustc --edition 2021 -D warnings -O`, and
execution of each certificate. Both JSON outputs and `git diff --check` pass.

## Boundary

- The local theorem is an ordinary supported associated-grade statement. The
  derived base change contains an excess copy:
  \[
  R/(x_3)\otimes_R^L C\simeq[C\xrightarrow0 C].
  \]
  Its \(\operatorname{Tor}_1\) line, reciprocal twist, normal shifts, and full
  PC extraordinary costalk have not been identified.
- Principal occurrence ideals are retained as labelled dualizable lines and
  evaluated before base change. Replacing them by their image ideals in \(C\)
  would wrongly kill the \((x_1)\) and \((X_{03}x_1)\) factors.
- The global calculation falsifies only gluing in the current
  absolute/barycentric carrier and its two natural relative quotients. It is
  not a no-go for a new normalization--conductor, multi-Rees, or bivariant
  specialization correspondence.
- The coefficient \(-3v_+\) does not license averaging by \(1/3\). The class
  \((1,1,1)\) is primitive, and the target norm attachment is integral.
- No negative-sheet assembly, full \(K_{\rm alt}\), physical-cut
  Beck--Chevalley theorem, CHY comparison, or higher-multiplicity conclusion
  follows.

## Consequence

The first stage proposed in entry 111 is complete: the whole \(D03\) Cartier
gallery has a canonical map to its single conductor tag. The failure is now
one level higher and has an exact address.

The smallest missing arrow is a positive-sheet normalization--conductor
comparison

\[
\boxed{
\alpha_+:
\mathcal S_+^{\rm cond}
\longrightarrow R\Gamma_{v_+}^{F}(\mathcal P_{\rm abs})
}
\]

or an equivalent bivariant/multi-Rees kernel whose differential supplies a
common top \(H_+\) with

\[
dH_+=-
(x_1\widetilde\xi_1+x_3\widetilde\xi_3+x_5\widetilde\xi_5),
\]

while retaining the three special galleries and the excess
\(\operatorname{Tor}_1\) data. Its associated-grade image must be
\(df_+=t_1+t_3+t_5\). Constructing this arrow, rather than another local sign
or a rational projector, is the next discriminating experiment.

## Outcome contract

```json
{
  "claim": "The whole D03 Cartier gallery has a canonical supported associated-grade map sending the intrinsic Bockstein class -xi_tilde to the positive tag t3. The three rotated source tops do not glue in the current absolute/barycentric carrier: their generic sum is the primitive D3-invariant class (1,1,1) in H1(sd(K6),E;Z), and the only existing quotient that bounds it also kills all three special galleries.",
  "status": "proved",
  "assumptions": [
    "The absolute occurrence complex, expanded gallery, Cartier class, and orientations are those of entries 93, 94, and 105-111.",
    "The local map is scoped to the supported ordinary associated grade C*t3, not the full derived PC costalk.",
    "Occurrence variables, normal monodromies, and integers remain uninverted."
  ],
  "evidence_refs": [
    "research/voevodsky/check_d03_whole_gallery_tag_gysin.rs",
    "research/voevodsky/check_three_rotated_gallery_top_gluing.rs",
    "ledger entries 93, 94, and 105-111"
  ],
  "factorization_test": {
    "whole_gallery_relative_homology": "passed integrally",
    "D03_costalk_orientation_and_sign": "passed",
    "supported_conormal_tag_map": "passed",
    "free_target_map": "falsified",
    "rotated_generic_sum_endpoint_relative": "nonzero primitive class; rank 126 to 127",
    "short_boundary_quotient": "generic class bounded but all special galleries killed",
    "full_PC_extraordinary_costalk": "unconstructed",
    "physical_Cut_Beck_Chevalley": "unconstructed"
  },
  "counterevidence": [
    "Derived base change has a nonzero Tor1 excess copy.",
    "No current relative quotient both kills the generic sum and retains the three special galleries.",
    "The target norm map is integral; division by three would solve the wrong problem."
  ],
  "next_experiment": "Construct alpha_+ or an equivalent bivariant multi-Rees kernel that retains a nonzero generic/source leg, cancels q_Sigma, and maps the three local Cartier galleries to the integral conductor norm boundary."
}
```
