---
authors:
  - marici.Benincasa
date: 2026-08-15
---
# Cyclic Sector Closure and Global Apparency of the Homogeneous Quartic

## Record

Date: 2026-08-15

Status: generic nonsoft monodromy theorem for the source-displayed
homogeneous three-site simplex integral.

This entry continues entries 175, 180, and 181. It changes no source
denominator, normalization, marked support, integration chain, coefficient
summand, or carrier cell.

## Deutsch--Popperian conjecture tested

The hard-to-vary claim was

[
oxed{
	ext{the published }mathcal Q_{12}	ext{ may acquire genuine monodromy
from a cyclic residue sector or only after source-weighted physical-chain
assembly.}
}
]

The finite falsifiers were:

1. (mathcal Q_{12}) becomes a component of the frozen raw discriminant
   census in the (q_{mathcal G_{23}}) or (q_{mathcal G_{31}}) sector;
2. the source cyclic relabeling reverses orientation or introduces a
   kinematic gluing weight;
3. a lower-sector physical pinch omitting (q_{mathcal G_{ij}}) has
   (mathcal Q_{12}) support;
4. the assembled physical scalar period has nonzero
   (mathcal Q_{12})-variation.

No support or carrier component was allowed to be added after inspecting
(mathcal Q_{12}).

## Frozen source sum

Benincasa--Brunello--Mandal--Mastrolia--Vazão,
arXiv:2408.16386v2, equation (mathrm{eq:Triangle}), gives

[
I_{{1}}^{(3,1)}
=kappa_0int_Gammaprod_e(dy_e,y_e)
rac{K^gamma}{q_{mathcal G}prod_{j=1}^3q_{mathfrak g_j}}
sum_{m cyc}
rac1{q_{mathcal G_{ij}}}
left(
rac1{q_{mathfrak g_{jk}}}
+
rac1{q_{mathfrak g_{ki}}}
ight).
]

The six coefficients are literally (+1). They share the same measure,
boundary-value prescription, and oriented chain (Gamma).

The denominators are

[
q_{mathcal G}=E,qquad
q_{mathfrak g_j}=y_{j-1,j}+X_j+y_{j,j+1},qquad
q_{mathcal G_{j,j+1}}=E+y_{j,j+1}.
]

The simultaneous cyclic permutation

[
ho:(1,2,3)mapsto(2,3,1)
]

preserves the chain orientation because its action on
((dy_{12},dy_{23},dy_{31})) is an even three-cycle.

## Cyclic quartics and exact rejection

Define

[
mathcal Q_{ij}
=
-16X_i^2X_j^2
-8X_iX_jE^2
+8(X_i+X_j)E^3
-5E^4.
]

Then

[
ho(mathcal Q_{12})=mathcal Q_{23},qquad
ho^2(mathcal Q_{12})=mathcal Q_{31}.
]

Pulling the fixed published divisor back to the canonical
(q_{mathcal G_{12}}) model gives

[
mathcal Q_{12}	ext{ in sector }23
longmapsto
mathcal Q_{31},
]

[
mathcal Q_{12}	ext{ in sector }31
longmapsto
mathcal Q_{23}.
]

The new exact Rust checker tests every target
(mathcal Q_{12},mathcal Q_{23},mathcal Q_{31}) against every one of
the 1,719 nonconstant conditions in the frozen raw census by multivariate
fraction-free pseudo-division. The optimized checker compiled and returned
exit code zero. Hence

[
oxed{3cdot1719=5157}
]

exact factor rejections pass, without kinematic specialization.

Combining this with the source-positive sheet-switch lemma and simultaneous
resolution of entry 181 gives

[
T_{mathcal Q_{12}}^{(12)}
=
T_{mathcal Q_{12}}^{(23)}
=
T_{mathcal Q_{12}}^{(31)}
=1,
]

[
N_{mathcal Q_{12}}^{(ij)}=0,
qquad
operatorname{Var}_{mathcal Q_{12}}
(Gamma_{ij,+}^{m res})=0.
]

## Lower-sector exhaustion

Residue regularity alone would not exclude a pinch supported entirely in a
shared lower sector. The primary source independently closes that loophole.

For the homogeneous lower/zero sector, the paper prints the complete dlog
alphabet

[
egin{aligned}
W_{m low}={&
X_1,X_2,X_3,
X_1+X_2,X_2+X_3,X_1+X_3,\
&
X_1-X_2-X_3,
X_1-X_2+X_3,
X_1+X_2-X_3,
E}.
end{aligned}
]

Thus

[
mathcal Q_{12}
otinoperatorname{Supp}(W_{m low})
]

at a generic point away from those ten linear divisors. The source
introduces the algebraic letter only in the
(q_{mathcal G_{12}})-containing elliptic sector, already closed above
and in entry 181.

## Source-weighted physical assembly

Write the six source terms as (I_{ij}^{(a)}), (a=1,2). Since analytic
continuation and variation are linear,

[
operatorname{Var}_{mathcal Q_{12}}
I_{{1}}^{(3,1)}
=
sum_{ij=12,23,31}sum_{a=1}^2
operatorname{Var}_{mathcal Q_{12}}I_{ij}^{(a)}
=0.
]

Therefore, on the generic nonsoft locus,

[
oxed{
T_{mathcal Q_{12}}^{m phys}=1,qquad
N_{mathcal Q_{12}}^{m phys}=0,qquad
operatorname{Var}_{mathcal Q_{12}}(Gamma_{m phys})=0.
}
]

No cross-sector extension is detected by the source scalar period or its
physical relative chain. This does not assert a canonical splitting of an
arbitrary master-basis Gauss--Manin filtration. A differential-equation
matrix may retain apparent (mathcal Q_{12})-poles.

## Classification

For the source-displayed homogeneous simplex integral:

- existing carrier: sufficient;
- coefficient support at generic (mathcal Q_{12}=0): none;
- relative-cycle support: none;
- cross-sector extension detected by the physical period: none;
- (mathcal Q_{12}): globally apparent;
- genuinely new carrier datum: none.

Thus the attempted quartic falsifier does not falsify H2. The surviving
architecture remains

[
	ext{shared carrier and derived calculus}
+
	ext{sector-specific coefficient objects}.
]

## Scope boundary

The theorem excludes intersections with:

- soft support;
- the ten lower-sector linear divisors;
- the frozen cyclic residue discriminant union.

It applies to the displayed homogeneous simplex integral. It is not a
claim for the generic multi-external-leg specialization, an integral
lattice extension across the full discriminant, or a canonical splitting
of the full master system.

## Exact evidence

- `research/benincasa/check_cyclic_q_log_smoothness.rs`
  - SHA-256
    `044d897f30f884509403ae90cd6a2342633d47226f7a65799e0ef492662c8d60`
- executed optimized binary
  - compile exit code: (0)
  - checker exit code: (0)
  - SHA-256
    `f1711a701d01ac5871c27c4c447de50087d791a92ca852a65717698640ba1405`
- `research/benincasa/cyclic_q_assembly_certificate.md`
  - SHA-256
    `040fbd01c83bbc5892822986baab858bc55c79c71f32b90b7f2fbf4cd54a2d26`
- `research/benincasa/cyclic_q_assembly_result.json`
  - SHA-256
    `7538055dc796f226c95fcb9756b385d8111f99c956a3d90ac07670dbe009566e`
- frozen primary source
  - SHA-256
    `3e92460fe2e34dc21a537c784dab3b2fbcd9b7cfee9e7372f06971b50d8b6f9b`

## Narrow result

[
oxed{
	ext{At generic nonsoft homogeneous kinematics, the published quartic is
apparent in all three cyclic residue sectors and in their literal
source-weighted physical assembly.}
}
]

No coefficient, relative-cycle, extension, or new-carrier support remains
at generic (mathcal Q_{12}=0).

## Next finite falsifier

The homogeneous quartic provenance route is closed. The next attack should
not repeat it. Move to the first place where the source result is not
covered by this theorem:

1. freeze the generic multi-external-leg three-site denominator and
   Cayley--Menger data, where the source says algebraic letters already
   occur in the polylogarithmic sector;
2. derive those letters as discriminants of the frozen relative geometry;
3. test whether any nonhomogeneous algebraic divisor survives the complete
   sector and physical-chain assembly;
4. classify the first survivor before proposing any carrier enlargement.

## Outcome contract

~~~json
{
  "claim": "The fixed published Q12 has identity monodromy and zero physical variation in every cyclic residue sector and in the literal six-term homogeneous source assembly.",
  "status": "survived",
  "raw_conditions_per_target": 1719,
  "target_quartics": 3,
  "exact_factor_rejections": 5157,
  "cyclic_sector_T_Q12": "identity",
  "lower_sector_Q12_support": false,
  "physical_T_Q12": "identity",
  "physical_N_Q12": 0,
  "physical_Var_Q12": 0,
  "classification": "Q12_globally_apparent_for_displayed_homogeneous_simplex_integral_at_generic_nonsoft_kinematics",
  "cross_sector_extension_detected": false,
  "new_carrier_datum": "none",
  "next_experiment": "Freeze and falsify the generic multi-external-leg algebraic letters in the lower/polylogarithmic sector."
}
~~~
