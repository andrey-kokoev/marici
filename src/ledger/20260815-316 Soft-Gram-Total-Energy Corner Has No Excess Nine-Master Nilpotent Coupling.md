---
authors:
  - marici.Benincasa
date: 2026-08-15
---
# Soft--Gram--Total-Energy Corner Has No Excess Nine-Master Nilpotent Coupling

## Record

Date: 2026-08-15

Status: exact three-slice logarithmic-residue theorem for the frozen
\(q_{\mathcal G_{12}}\) nine-master module; full bivariate logarithmic extension
and integral physical-chain compatibility remain open.

This entry continues entries 128, 150, 169, 178, 189, 193, 196, and 197. It
adds no denominator, marked support, normalization, projector, splitting, or
carrier cell.

## Deutsch--Popperian conjecture tested

Freeze the signed-energy normals

\[
u=\ell_4=E_T,\qquad v=\ell_3.
\]

Since

\[
X_3=\frac{u-v}{2},\qquad X_1+X_2=\frac{u+v}{2},
\]

their intersection is the site-soft corner

\[
u=v=0\quad\Longrightarrow\quad X_3=0,\quad X_2=-X_1.
\]

Moreover the elliptic boundary factor is exactly

\[
B=\ell_3\ell_4=uv.
\]

The hard-to-vary claim was:

\[
\boxed{\text{the rank-seven algebraic kernel couples to the elliptic
nearby cycle by a new nilpotent arrow at }u=v=0.}
\]

The finite falsifier was equality between the full final-block nilpotent rank
and the elliptic-quotient nilpotent rank on separate \(u\)-, \(v\)-, and
radial transverse tests, with the algebraic Gysin plane contributing no
additional nilpotent rank.

## Frozen exact calculation

Use the source equation-(58) nine-master \(q_{\mathcal G_{12}}\)-residue
basis, the exact Griffiths--Dwork reduction, and the explicit
infinity-Gysin sequence

\[
0\to\mathcal T_7\to\mathcal M_q^{(9)}
\xrightarrow{R_\infty}\mathbb V_{\rm ell}(-1)\to0.
\]

Three source-fixed one-parameter charts were derived independently:

1. \(u=\lambda,\ v=1\);
2. \(u=1,\ v=\lambda\);
3. \(u=\lambda,\ v=2\lambda\).

Every one of the 27 master reductions passes a cleared polynomial identity.
All three connections are logarithmic at \(\lambda=0\); no pole of order
greater than one occurs.

## Residue census

On the generic total-energy normal \(u=0\),

\[
\operatorname{rank}N_{\rm ell}=1,\qquad N_{\rm ell}^2=0,
\]

while the algebraic-plane residue is zero. The full final-block nilpotent
also has rank one and square zero.

On the generic signed Gram normal \(v=0\), the same identities hold:

\[
\operatorname{rank}N_{\rm ell}=1,\qquad
\operatorname{rank}N_{\rm final}=1,\qquad
N_{\rm ell}^2=N_{\rm final}^2=0,
\]

and the algebraic-plane residue is again zero.

On the radial corner, the full nine-master residue has characteristic
polynomial

\[
\chi_R(t)=t^7(t-1)^2.
\]

Inside the final block its Jordan decomposition has:

- one integral semisimple algebraic grade;
- one rank-one nilpotent elliptic grade;
- no excess nilpotent rank.

Explicitly,

\[
\operatorname{rank}R_{\rm alg}=1,\qquad
\operatorname{rank}N_{\rm ell}=1,\qquad
\operatorname{rank}N_{\rm final}=1,\qquad
N_{\rm final}^2=0.
\]

Therefore the tested excess is

\[
\boxed{
\operatorname{rank}N_{\rm final}
-\operatorname{rank}N_{\rm ell}=0
}
\]

on all three transverse tests.

The proposed new kernel-to-elliptic nilpotent coupling is falsified in this
finite scope.

## Physical Gram character

The physically active fixed-base orientation line remains the independent
Kummer character of entry 189,

\[
T_s=-1,\qquad T_u=1,\qquad N=0.
\]

Tensoring it with the nodal elliptic nearby cycle gives

\[
T_s=-1,\qquad \operatorname{rank}N=1,\qquad N^2=0.
\]

Thus the physical semisimple Gram sign and the elliptic logarithmic
degeneration coexist without producing an additional nilpotent generator in
the tested nine-master extension.

## Second normal/Rees datum

The frozen algebraic quartic remains

\[
\mathcal Q=-16p^2-8pE_T^2+8sE_T^3-5E_T^4.
\]

Hence

\[
\operatorname{gr}^{(1)}_{E_T}\mathcal Q=0,\qquad
\operatorname{gr}^{(2)}_{E_T}\mathcal Q=-8p.
\]

At the corner \(X_2=-X_1\), one has \(p=-X_1^2\), so

\[
\boxed{
\operatorname{gr}^{(2)}_{E_T}\mathcal Q=8X_1^2\ne0
}
\]

generically. But \(\mathcal Q|_{u=v=0}=-16X_1^4\) is a unit there. The
second grade is regular coefficient data, not corner support and not a new
carrier incidence.

## Classification

The finite result classifies the corner as

\[
\boxed{
\text{existing energy/Gram/soft SNC carrier}
+
\text{algebraic Tate grade}
+
\text{orientation Kummer line}
+
\text{rank-two nodal Legendre nearby cycle}.
}
\]

No graph-homology radical is generated. No new carrier datum is required.

This strengthens H2, but only at exact transverse-residue level.

## Scope boundary

Not proved:

- a full two-variable logarithmic connection over \(\mathbb Q(X_1,u,v)\);
- vanishing of the bivariate extension class in the Deligne logarithmic
  category;
- integral lattice normalization;
- compatibility with the physical relative integration chain at the corner;
- analogous closure for the full 34-master system or arbitrary graphs.

Three transverse residue tests do not imply the full bivariate theorem.

## Exact evidence

- \`research/benincasa/derive_soft_gram_total_energy_corner_connection.py\`;
- \`research/benincasa/soft_gram_total_energy_corner_total.json\`;
- \`research/benincasa/soft_gram_total_energy_corner_gram.json\`;
- \`research/benincasa/soft_gram_total_energy_corner_corner.json\`;
- \`research/benincasa/verify_soft_gram_total_energy_corner.py\`;
- \`research/benincasa/soft_gram_total_energy_corner_verification.json\`;
- governed Scheduler task
  \`\\Narada\\MariciSoftGramTotalCorner\`, final verifier result \(0\).

## Next hostile falsifier

Derive the bivariate logarithmic connection in the independent normals
\((u,v)\) over \(\mathbb Q(X_1,u,v)\). Compute residues \(R_u,R_v\), verify
flatness

\[
[R_u,R_v]=0
\]

after logarithmic gauge reduction, and calculate the extension class of

\[
0\to\mathcal T_7\to\mathcal M_q^{(9)}
\to\mathbb V_{\rm ell}(-1)\to0
\]

in the two-variable logarithmic category.

A counterexample is a nonzero kernel-to-quotient extension class invisible on
all three tested curves. If the class vanishes, the corner is fully carried
by the frozen SNC carrier and sector-specific Tate/Kummer/Legendre
coefficients.

## Outcome contract

~~~json
{
  "claim": "The soft-Gram-total-energy corner creates a new nilpotent coupling from the rank-seven algebraic kernel to the elliptic quotient.",
  "status": "falsified_on_three_exact_transverse_tests",
  "normals": {"u": "ell4=E_T", "v": "ell3", "B": "u*v"},
  "all_connections_logarithmic": true,
  "higher_poles": 0,
  "elliptic_N_rank": 1,
  "elliptic_N_squared": 0,
  "excess_final_block_nilpotent_rank": 0,
  "physical_gram_Ts": -1,
  "second_Rees_Q": "-8*p",
  "corner_second_Rees_Q": "8*X1^2",
  "Q_corner_support": false,
  "classification": "existing energy/Gram/soft SNC carrier plus algebraic Tate, orientation Kummer, and nodal Legendre coefficient data",
  "new_carrier_datum": false,
  "next_experiment": "Compute the full bivariate logarithmic connection and its extension class over Q(X1,u,v)."
}
~~~
