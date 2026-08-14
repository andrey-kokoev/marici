# D03 Thom Endpoint Koszul Hull and the Missing Road Generizations

## Record

Date: 2026-08-14

Status: one proved integral occurrence theorem and one sharp falsifier. The
Thom-decorated D03 carrier has a unique minimal exact coefficient hull and a
precise Beck--Chevalley divisibility criterion. An external Thom line plus
the generic carrier does not construct the two extraordinary endpoint
pushforwards. Their actual road-generization morphisms remain the first
missing spatial data.

## The minimal exact occurrence hull

Work over

\[
R=\mathbb Z[x_1,x_5].
\]

Entry 116 established

\[
d e_3=-x_1q_0+x_5q_2,
\qquad
e_3=\{x_1,x_5\},
\quad q_0=\{x_5\},
\quad q_2=\{x_1\}.
\]

The smallest exact cellular completion is the augmented Koszul resolution

\[
\boxed{
R\langle e_3\rangle
\xrightarrow{(-x_1,x_5)^T}
R\langle q_0,q_2\rangle
\xrightarrow{(x_5,x_1)}
R\langle a\rangle
\longrightarrow R/(x_1,x_5).
}
\]

Indeed,

\[
d^2e_3=(-x_5x_1+x_1x_5)a=0.
\]

The row \((x_5,x_1)\) has primitive first syzygy
\((x_1,-x_5)\), so the displayed column is its oriented negative and the
complex is exact. No denominator or rational splitting occurs.

Tensoring with the external Rees conormal \(L_3=[t_3]\) preserves
exactness. It does not create an internal \(h_3\) on \(e_3,q_0,q_2\); entry
116 already proved that all three supports omit \(x_3\).

## Primitive lcm-line classification

Let an abstract target interval have

\[
dT=-\tau_0+\tau_2
\]

and consider

\[
e_3\mapsto\alpha T,
\qquad
q_0\mapsto b_0\tau_0,
\qquad
q_2\mapsto b_2\tau_2.
\]

The chain equation is

\[
\alpha=x_1b_0=x_5b_2.
\]

Since \(x_1,x_5\) are coprime,

\[
\boxed{
(\alpha,b_0,b_2)=c(x_1x_5,x_5,x_1).
}
\]

The primitive positive coefficient solution is therefore

\[
\alpha=x_1x_5,
\qquad b_0=x_5,
\qquad b_2=x_1.
\]

This is the canonical map among the principal occurrence lines

\[
I_{e_3}=(x_1x_5),
\qquad I_{q_0}=(x_5),
\qquad I_{q_2}=(x_1).
\]

It removes the coefficient obstruction. It does not create the spatial
target cells \(T,\tau_0,\tau_2\).

## Exact Beck--Chevalley criterion

Leave the actual road boundary unknown:

\[
d_{\rm road}F_{03}
=b_0\tau_{q_0}+b_2\tau_{q_2}.
\]

Let \(g\) be the generic coefficient of a putative correspondence and let
\(a_0,a_2\) be its endpoint coefficients. Equality of the two length-two
paths, equivalently vanishing of the mixed term in the total square, gives

\[
\boxed{
gb_0=-x_1a_0,
\qquad
gb_2=x_5a_2.
}
\]

With the established generic normalization \(g=1\), a diagonal lift exists
precisely when

\[
b_0\in(x_1),
\qquad
b_2\in(x_5),
\]

and is then uniquely

\[
a_0=-b_0/x_1,
\qquad
a_2=b_2/x_5.
\]

These quotients express divisibility in principal-line modules; they are
not coefficient-ring inversions. Any geometric candidate must independently
produce \(b_0,b_2\). The formulas above then decide existence and normalize
its endpoint maps.

## Why entries 86 and 97 do not supply the endpoints

Their marked trace lives inside the actual road square

\[
F_{03}=K_4\times K_4
\]

with occurrence vertices

\[
v_{00}=x_0x_3,
\quad v_{10}=x_1x_3,
\quad v_{01}=x_0x_4,
\quad v_{11}=x_1x_4.
\]

The entry-97 source is the marked V formed by two edges at \(v_{00}\), and
its trace evaluates the entire road-square costalk. By contrast,

\[
q_0=\{x_5\},
\qquad q_2=\{x_1\}
\]

are central Boolean dual-link cells. The variable \(x_5\) does not occur in
the entry-86/97 square. Even \(q_2\) is not \(v_{10}\): their coefficient
lines are respectively \((x_1)\) and \((x_1x_3)\).

Currying the entry-97 trace therefore maps into the Verdier dual of the
complete \(F_{03}\) boundary costalk. It does not define

\[
q_0\to\tau_{q_0},
\qquad q_2\to\tau_{q_2}.
\]

Identifying those cells from their common unloaded boundary pattern would
be the missing cross-support correspondence, not a consequence of the
marked counit.

## Sharp falsifier

The following sufficiency claim is false:

\[
\text{external }[t_3]
+\text{ generic }e_3\leftrightarrow F_{03}
\quad\Longrightarrow\quad
\text{canonical endpoint road pushforwards}.
\]

The tensor product supplies neither the road generizations \(b_0,b_2\) nor
an extraordinary identification with reciprocal-regular to
original-Borel--Moore \(\operatorname{Tor}_1\) costalks. Different endpoint
coefficients give different formally square-zero systems after one defines
the road boundary from those choices.

After central base change

\[
C=R/(x_1,x_5),
\]

each Cartier packet becomes

\[
[C\xrightarrow0 C].
\]

It retains separate \(H_0\) and \(\operatorname{Tor}_1\) lines, but the
scalar Beck--Chevalley equation degenerates to \(0=0\). Base change cannot
recover the lost ideal inclusions or normalize the endpoint map.

This is not a no-go for the extraordinary correspondence. It identifies
the first datum that correspondence must derive.

## Next executable target

Construct only the \(q_0\) endpoint first:

\[
\Gamma_{0}^{!,\rm mR}:
\operatorname{Th}_{x_3}^{\rm mR}\otimes I_{x_1}q_0
\longrightarrow
[t_3]\tau_{q_0}.
\]

It must have:

1. a nonzero generic \(Q\)-leg through the saturated roof
   \(e_3\leftrightarrow F_{03}\);
2. special boundary \(-x_1q_0\);
3. a reciprocal-standard to original-Borel--Moore extraordinary map onto
   the road \(\operatorname{Tor}_1\) line;
4. the repeated-normal image \([t_3]\mapsto\eta_{3,\rm mix}\);
5. the separate positive physical orientation \([dX_{03}]=+1\); and
6. equality of the two Cartier--PL composites before central base change.

If the correctly typed derived Hom group is zero, or its Beck--Chevalley
defect is nonzero, this endpoint fails locally. If it is a normalized
rank-one class, construct \(q_2\) and only afterward test a common thimble
and the \(D_3\) orbit.

## Evidence

New exact certificate:

- `research/voevodsky/check_d03_thom_endpoint_bc.rs`, SHA-256
  `8e5b72b62c5882ad3959ee15f2eeaed77e85bb53522ad3f06e98e0b6de0778fb`.

The certificate derives the occurrence differentials from the masks,
checks the augmented Koszul resolution, classifies the primitive lcm-line
map, proves the entry-86/97 label mismatch, derives the two-path equations,
tests divisibility, and verifies that central base change cannot select the
two \(\operatorname{Tor}_1\) maps.

## Outcome contract

```json
{
  "claim": "The D03 endpoint occurrence column has the canonical exact augmented Koszul hull, and any normalized road lift is governed by b0 in (x1), b2 in (x5), with uniquely induced endpoint coefficients. The primitive lcm coefficient map exists integrally. An external Thom line and the generic e3-to-F03 carrier do not supply the actual road generizations or extraordinary Tor1 endpoint maps.",
  "status": "falsified",
  "assumptions": [
    "Occurrence, Rees, monodromy, and physical-normal lines remain distinct.",
    "The falsifier concerns sufficiency of the external tensor and generic carrier, not existence of a new extraordinary correspondence.",
    "The central fibre is used only as a derived coefficient test, not as a spatial identification."
  ],
  "evidence_refs": [
    "research/voevodsky/check_d03_thom_endpoint_bc.rs",
    "ledger entries 86, 97, 100, 112, 115, and 116"
  ],
  "factorization_test": {
    "augmented_Koszul_hull": "proved",
    "primitive_lcm_line": "proved",
    "two_path_BC_equations": "proved",
    "entry_86_97_endpoint_identification": "falsified",
    "external_Thom_sufficiency": "falsified",
    "q0_extraordinary_endpoint": "unconstructed",
    "full_G03_Cousin": "unconstructed"
  },
  "counterevidence": [
    "The Boolean q cells are not occurrence vertices of the F03 road square.",
    "The external tensor does not determine the road-generization coefficients.",
    "Central base change turns the coefficient square into the vacuous equality 0=0."
  ],
  "next_experiment": "Construct one marked q0 extraordinary endpoint kernel with a nonzero generic Q leg, derive its road generization before central base change, and test the displayed divisibility and Beck-Chevalley equations."
}
```
