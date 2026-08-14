# Mistyped Pairwise Coherence and the Filtered Three-Road Star

## Record

Date: 2026-08-14

Status: falsified the pairwise \(q_2\) formula of entry 100 as a canonically
typed next objective; proved the exact weighted three-road coefficient
identity; identified the remaining intrinsic map as a filtered
absolute-to-relative dual-block assembly.  The full PC map remains open.

This entry corrects only entry 100's proposed next experiment.  Its
support-directed can--var theorem and three labelled local excess traces are
unchanged.

## Why the pairwise road comparison is mistyped

Put

\[
A=(u_1,u_3,u_5),\qquad
Q_{03}=A+(u_0),\qquad Q_{25}=A+(u_2).
\]

The two local traces have different source complexes, occurrence bases,
physical normal lines, and targets:

\[
K(I_+^\vee)\otimes K(u_0,u_3)\longrightarrow C_{Q_{03}},
\qquad
K(I_+^\vee)\otimes K(u_2,u_5)\longrightarrow C_{Q_{25}}.
\]

The long-diagonal facets \(F_{03}\) and \(F_{25}\) are disjoint.  Their
common \(q_2\) in the source augmented triangle is a dual-normal-link cell,
not an intersection stratum of the scalar associahedron.  Entries 93--100
therefore define no maps

\[
\rho_{q_2}^{03},\qquad \rho_{q_2}^{25}
\]

to a common physical PC object.  The displayed difference in entry 100 was
not a morphism in the established correspondence category.

The functorial common support of the coefficient ideals is the union

\[
W=V(Q_{03})\cup V(Q_{25})=V(A,u_0u_2),
\]

with conductor

\[
U=V(A,u_0,u_2)
\]

and Mayer--Vietoris triangle

\[
C_U\longrightarrow C_{Q_{03}}\oplus C_{Q_{25}}
\longrightarrow C_W\longrightarrow C_U[1].
\]

In \(H_W^4\), writing

\[
t_W=\left[\frac1{u_0u_1u_2u_3u_5}\right],
\]

the coefficient-only difference is

\[
\delta_{q_2}=(u_2-u_0)t_W\ne0.
\]

Sending the two terms instead to the deeper conductor \(C_U[1]\) requires
new oriented Gysin maps.  Once those maps are adjoined, the same expression
is a Cech boundary because each term lifts from a codimension-four face.
Thus the old test had only two outcomes: a nonzero class in the canonical
union target, or a tautological null-homotopy after adding precisely the
unproved conductor correspondence.  Neither tests the intrinsic scalar
half-object.

## The corrected weighted source packet

The relative target of entry 98 has one top cell and three road cells, with
no lower groups:

\[
dK_{\rm rel}=T_0+T_1+T_2.
\]

Consequently the source \(q\)-cells and augmentation may map to zero.  No
pairwise road transition is required.  The smallest coefficient skeleton is
the raw, unlocalized Koszul complex

\[
K_E=K(u_4,u_0,u_2).
\]

Choose the based generators

\[
\begin{aligned}
f&=h_4h_0h_2,\\
e_1&=p_4h_0h_2,&
e_3&=-h_4p_0h_2,&
e_5&=h_4h_0p_2,\\
q_0&=p_4p_0h_2,&
q_1&=p_4h_0p_2,&
q_2&=h_4p_0p_2,\\
a&=p_4p_0p_2.
\end{aligned}
\]

Its differential is

\[
df=u_4e_1+u_0e_3+u_2e_5,
\]

\[
de_1=u_0q_0-u_2q_1,
\quad
de_3=-u_4q_0+u_2q_2,
\quad
de_5=u_4q_1-u_0q_2,
\]

\[
dq_0=u_2a,
\qquad dq_1=u_0a,
\qquad dq_2=u_4a.
\]

The checker proves \(d^2=0\) on all eight generators.  The unit augmented
triangle of entry 99 is only its localized diagonal normalization; it must
not replace this weighted integral object.

## Exact formal star identity

Let

\[
\tau_A=\left[\frac1{u_1u_3u_5}\right]
\]

denote the plus-branch Cech residue.  There is an exact, \(D_3\)-covariant
coefficient map

\[
\boxed{
\begin{aligned}
f&\longmapsto \tau_AK_{\rm rel},\\
e_1&\longmapsto \frac{\tau_A}{u_4}T_2,\\
e_3&\longmapsto \frac{\tau_A}{u_0}T_1,\\
e_5&\longmapsto \frac{\tau_A}{u_2}T_0,\\
q_0,q_1,q_2,a&\longmapsto0.
\end{aligned}}
\]

No \(u_j\) is inverted in the base ring.  Each negative power occurs only
inside the Cech localization summand named by that support.  The top chain
identity is

\[
\begin{aligned}
G(df)
&=u_4\frac{\tau_A}{u_4}T_2
 +u_0\frac{\tau_A}{u_0}T_1
 +u_2\frac{\tau_A}{u_2}T_0\\
&=\tau_A(T_0+T_1+T_2)
=d(\tau_AK_{\rm rel}).
\end{aligned}
\]

All lower squares commute because the relative target vanishes below road
degree.  The exact certificate also verifies the \(D_3\) group relations,
orientation signs, differential covariance, map covariance, and legality of
every localization denominator.

This is a conditional coefficient theorem, not yet an intrinsic PC map.
The value \(f\mapsto\tau_AK_{\rm rel}\) is the desired supported top value;
the calculation does not derive it from scalar specialization.  Nor does it
attach the three road values to entry 100's repeated-normal excess lines,
occurrence transitions, and distinct physical normal orientations.

## Canonical formulation of the missing map

The preceding boundary can be simplified conceptually.  Let

\[
X=K_6,
\qquad B=B_{\rm short},
\qquad U=X\setminus B,
\]

and let \(v_+\) be the all-odd central vertex.  Start with the **absolute**
loaded object \(P_{\rm abs}\), not the relative object.  The latter removes
\(v_+\), since \(v_+\subset B\).

For the closed inclusion \(i_+:\{v_+\}\hookrightarrow X\), the canonical
local-cohomology counit is

\[
\epsilon_+:
R\Gamma_{v_+}(P_{\rm abs})
=i_{+!}Ri_+^!P_{\rm abs}
\longrightarrow P_{\rm abs}.
\]

If \(P_{\rm abs}=\mathbb D F_{\rm abs}\), the open localization map has the
correct variance

\[
P_{\rm abs}\longrightarrow
Rj_*j^*P_{\rm abs}
\simeq\mathbb D(j_!j^*F_{\rm abs}).
\]

At the variance-neutral cellular/Borel--Moore level, the desired composite
is simply

\[
\boxed{
\mathcal S_+^{\rm cond}
\xrightarrow{\alpha_+}
C_{\rm abs}^{v_+}
\xrightarrow{\epsilon_{\rm cell}}
C_*^{\rm BM}(X)
\xrightarrow{q_{m cell}}
C_*^{\rm BM}(X)/C_*^{\rm BM}(B).
}
\]

Here \(C_{\rm abs}^{v_+}\) is the filtered dual-block complex.  The last two
arrows are canonical.  The only new construction is the comparison

\[
\boxed{
\alpha_+:
\mathcal S_+^{\rm cond}
\xrightarrow{\sim}
R\Gamma_{v_+}^{F}(P_{\rm abs}).
}
\]

The superscript \(F\) is essential.  In the ordinary derived category the
composite is zero because its support lies in the removed boundary.  Entry
99's carrier is likewise ordinary-null-homotopic.  The desired information
is a secondary filtered class.

The filtration must be bounded, exhaustive, separated, and \(D_3\)-stable,
and must retain:

- dual-block/Cousin depth \(f\to e\to q\to a\);
- unlocalized normal-support/Koszul degree;
- normalization--conductor occurrence degree;
- reciprocal versus Borel--Moore support direction;
- physical normal and \(\chi_N\) orientation lines.

Equivalently its Rees object must remain over \(R_0[t]\), without inverting
\(t\), any \(u_j\), or \(3\), with

\[
\operatorname{Rees}_F(M)/(t-1)=M,
\qquad
\operatorname{Rees}_F(M)/(t)=\operatorname{gr}_F M.
\]

The defining tests for \(\alpha_+\) are

\[
\operatorname{gr}(q_{\rm cell}\epsilon_{\rm cell}\alpha_+)
=A_+^{\rm car},
\]

and that its three codimension-one Cousin residues equal the established
\(\Theta_{14}^{\rm loc},\Theta_{03}^{\rm loc},\Theta_{25}^{\rm loc}\),
including all excess, twist, occurrence, and orientation data.  Their total
road restrictions must cancel, as support at \(v_+\) requires.

This formulation does not solve the problem by renaming it.  It removes the
arbitrary top arrow: the counit and localization are canonical, while
\(\alpha_+\) is the single geometric comparison theorem that remains.

## Evidence

Exact certificate:

- `research/voevodsky/check_weighted_three_road_star.rs`

SHA-256:

```text
7d56e062439e3bc0f50c26dbc6dfbb5847b381e2d37608e29e0815de37f7092f
```

It verifies the full raw Koszul differential, \(d^2=0\), all four displayed
Koszul--Cech values, the top and lower chain identities, denominator support,
and complete \(D_3\) covariance.  It deliberately reports
`status: inconclusive` because the intrinsic \(\alpha_+\) is not constructed.

Reproduce with:

```powershell
$src = "research/voevodsky/check_weighted_three_road_star.rs"
$exe = Join-Path $env:TEMP "check_weighted_three_road_star.exe"
rustfmt --edition 2021 --check $src
rustc --edition=2021 -D warnings -O $src -o $exe
& $exe | ConvertFrom-Json | Out-Null
```

## Consequence and next formula

The immediate objective is no longer a pairwise lower-vertex homotopy.  It is
the single filtered comparison

\[
\boxed{
A_+^{\rm Cous,PC}
:=
q_{\rm cell}\circ\epsilon_{\rm cell}\circ\alpha_+,
\qquad
\alpha_+:
\mathcal S_+^{\rm cond}
\xrightarrow{\sim}C_{\rm abs}^{v_+}.
}
\]

Its associated grade must be the exact weighted star above.  Polarity then
supplies the minus map.  Only after this filtered absolute-to-relative
assembly is proved should the construction return to eight-point Cut
naturality.

## Outcome contract

```json
{
  "claim": "The pairwise q2 objective is not canonically typed; the exact replacement is a D3-covariant weighted three-road star, whose intrinsic realization reduces to one filtered conductor-to-dual-block comparison followed by canonical absolute counit and relative localization maps.",
  "status": "conditional",
  "assumptions": [
    "Negative u powers occur only in named Cech localization summands, never in the base ring.",
    "The relative target is the entry-98 complex with one top cell, three road cells, and zero lower groups.",
    "The nonzero carrier is retained in a filtered/Rees, integral, D3-equivariant category rather than the ordinary derived category."
  ],
  "evidence_refs": [
    "research/voevodsky/check_weighted_three_road_star.rs",
    "ledger entries 98-100"
  ],
  "factorization_test": {
    "pairwise_q2_formula": "falsified as untyped",
    "raw_weighted_Koszul_complex": "passed",
    "formal_three_road_star": "passed exactly",
    "D3_covariance": "passed",
    "intrinsic_filtered_comparison_alpha_plus": "unconstructed"
  },
  "counterevidence": [
    "In the canonical union-support target the coefficient-only q2 difference is nonzero.",
    "Making it zero in the conductor requires new Gysin maps and is therefore tautological as a test.",
    "The absolute-to-relative composite is zero after forgetting the filtration.",
    "Entry 99 supplies only the associated carrier grade, not alpha_plus."
  ],
  "next_experiment": "Construct the filtered/Rees comparison alpha_plus from the actual normalization-conductor and loaded absolute dual-block complex; verify that its associated grade is the weighted star and that its three Cousin residues are exactly the established local traces."
}
```
