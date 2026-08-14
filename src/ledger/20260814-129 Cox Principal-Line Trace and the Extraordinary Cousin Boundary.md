# Cox Principal-Line Trace and the Extraordinary Cousin Boundary

## Record

Date: 2026-08-14

Status: proved integral occurrence-level theorem; falsified the bare coherent-Cousin interpretation; loaded PC promotion and the scalar-source lift remain open.

Scope: the occurrence variables of the fixed \(D=03\) road square. Monodromy/Kummer packets, reciprocal-standard versus original-Borel--Moore variance, the repeated-normal excess map, and the physical line \([dX_{03}]\) are not reconstructed here.

## Setup

Put

\[
R=\mathbb Z[x_0,x_1,x_3,x_4],
\qquad
U=\operatorname{Spec}R\setminus
\bigl(V(x_0,x_1)\cup V(x_3,x_4)\bigr).
\]

The fixed weighted road square of entry 97 is

\[
R\langle F\rangle\xrightarrow{d_2}
R\langle a,b,c,d\rangle\xrightarrow{d_1}
R\langle v_{00},v_{10},v_{01},v_{11}\rangle,
\]

with

\[
d_2F=x_3a-x_4b-x_0c+x_1d
\]

and

\[
\begin{aligned}
d_1a&=-x_0v_{00}+x_1v_{10},&
d_1b&=-x_0v_{01}+x_1v_{11},\\
d_1c&=-x_3v_{00}+x_4v_{01},&
d_1d&=-x_3v_{10}+x_4v_{11}.
\end{aligned}
\]

Define the principal-lcm generators

\[
\bar a=x_3a,
\quad \bar b=x_4b,
\quad \bar c=x_0c,
\quad \bar d=x_1d,
\]

\[
\bar v_{00}=x_0x_3v_{00},
\quad
\bar v_{10}=x_1x_3v_{10},
\quad
\bar v_{01}=x_0x_4v_{01},
\quad
\bar v_{11}=x_1x_4v_{11}.
\]

In these generators the differential is ordinary oriented square incidence:

\[
F\longmapsto \bar a-\bar b-\bar c+\bar d,
\]

\[
\begin{aligned}
\bar a&\longmapsto-\bar v_{00}+\bar v_{10},&
\bar b&\longmapsto-\bar v_{01}+\bar v_{11},\\
\bar c&\longmapsto-\bar v_{00}+\bar v_{01},&
\bar d&\longmapsto-\bar v_{10}+\bar v_{11}.
\end{aligned}
\]

Let

\[
M=x_0x_1x_3x_4.
\]

The weighted augmentation

\[
(v_{00},v_{10},v_{01},v_{11})
\longmapsto
(x_1x_4,x_0x_4,x_1x_3,x_0x_3)
\]

sends every \(\bar v_{ij}\) to \(M\).

## Theorem: the formal road trace is one principal-line functional

The principal-lcm subcomplex is an integral cellular resolution of the principal Cartier ideal

\[
(M)=\mathcal O_U(-D),
\qquad
D=D_0+D_1+D_3+D_4.
\]

Its normalized differential ranks are \(1\) and \(3\); every nonzero Smith factor is a unit. Consequently it is saturated and has no integral torsion. Duality gives the single coefficient line

\[
\mathcal O_U(D)=\operatorname{Hom}_{\mathcal O_U}
(\mathcal O_U(-D),\mathcal O_U),
\]

not four independently chosen Laurent coefficients.

The distinguished functional \(M\mapsto1\) has, in the original road bases, the four representatives

\[
\boxed{
\Theta_{03}^{\rm occ,formal}
=
\left(
\frac1{x_0x_3},
\frac1{x_1x_3},
\frac1{x_0x_4},
\frac1{x_1x_4}
\right).
}
\]

Thus the entry-97 occurrence coefficients are the four local expressions of one normalized dual principal-line functional. Once its dense-torus value is fixed to one, Laurent injectivity makes the solution unique.

The generic normalization is nevertheless independent information. The \(v_{10}\) residue alone permits

\[
f\in1+(x_1,x_3),
\]

and even all four corner residues permit

\[
f\in1+(x_0x_1,x_3x_4).
\]

This is the generic-unit obstruction of the D03 ledger entry
`Four-Corner Cellular Nerve and the Generic-Unit Obstruction` in its smallest
coefficient form.

## The occurrence-level \(x_3\) Gysin

The first extraordinary step can be constructed without fitting a fraction. On the \(x_3\) edge let

\[
S_3=(R/(x_3))|_U.
\]

For \(i=0,1\), the endpoint Cartier divisor is cut out by the non-zero-divisor \(x_i\), and

\[
R\!\operatorname{Hom}_{S_3}(S_3/(x_i),S_3)
\simeq[S_3\xrightarrow{x_i}S_3].
\]

Hence

\[
\operatorname{Ext}^0_{S_3}(S_3/(x_i),S_3)=0,
\qquad
\operatorname{Ext}^1_{S_3}(S_3/(x_i),S_3)=S_3/(x_i),
\]

with one primitive orientation generator and no integer torsion.

The canonical Koszul--Cech comparison for the ordered normals \((x_i,x_3)\) is

\[
1\longmapsto1,
\qquad
e_i\longmapsto(1/x_i,0),
\qquad
e_3\longmapsto(0,1/x_3),
\qquad
e_i\wedge e_3\longmapsto1/(x_ix_3).
\]

Equivalently, the degree-one extraordinary map from the \(x_3\) Cech object to the product Cech object is

\[
g_i^0(r)=(r/x_i,0),
\qquad
g_i^1(t)=t/x_i.
\]

The chain equation is exact. With cellular incidence \((-v_{00},+v_{10})\) and the retained endpoint orientation lines, the displayed corner coefficients are

\[
+\left[\frac1{x_0x_3}\right],
\qquad
+\left[\frac1{x_1x_3}\right].
\]

This proves the occurrence Koszul--Cech Gysin on one road edge. It does not yet identify that map with the loaded PC Gysin.

## Sharp blocker: coherent restriction is the wrong variance

The tempting simplification

\[
\text{generic regular Cox section}
\xrightarrow{\text{ordinary Cousin boundary}}
\text{corner simple pole}
\]

is false. In \(A[x^{-1}]/A\), the regular unit represents

\[
[1]=0.
\]

The same holds for a section regular in the invertible sheaf \(\mathcal O_U(D)\). The nonzero class \([1/x_i]\) is an extraordinary Cartier fundamental class, not an ordinary restriction of the generic line.

The occurrence calculation therefore does not supply any of the following:

- the reciprocal-standard/original-Borel--Moore comparison;
- the repeated-normal excess trace and its \(q\)-units;
- the physical orientation \([dX_{03}]=+1\);
- physical-Cut/Beck--Chevalley naturality;
- a nonzero scalar-specialization \(Q\)-leg; or
- the source differential \(d_{\rm sp,sc}\) and chain map \(G_{03}^{\rm Cousin}\).

The first unconstructed target arrow is the promotion

\[
\boxed{
g_{3}^{!,\rm occ}
\longrightarrow
g_{3}^{!,\rm PC},
}
\]

including both \(v_{00}\) and \(v_{10}\), all lower Cech terms, the independently established normal-excess packet, and \([dX_{03}]\). Only after this one-edge map is typed should the \(x_4\) edge or the complete four-edge coherence be attempted.

The first missing source arrow remains the independently normalized map into the generic road term with a genuinely nonzero \(Q\)-leg. The target coefficient theorem cannot create it.

## Cross-sector status

This is a \(D03\)-local occurrence theorem, not Marici-core machinery. Under the cross-sector promotion rule, a cosmological partial-energy analogue must construct its own extraordinary boundary class from independently fixed source geometry. Matching rational fractions or incidence patterns is insufficient.

## Evidence

Executable certificate:

`research/voevodsky/check_d03_toric_cox_cousin_trace.rs`

SHA-256:

`852652cbe3f8d20076c526e3adb493857e7859d6f33ad9cc2daede03750bfce4`

Reproduction:

```powershell
rustfmt --edition 2021 --check research\voevodsky\check_d03_toric_cox_cousin_trace.rs
rustc --edition 2021 -D warnings -O research\voevodsky\check_d03_toric_cox_cousin_trace.rs -o "$env:TEMP\check_d03_toric_cox_cousin_trace.exe"
& "$env:TEMP\check_d03_toric_cox_cousin_trace.exe"
```

The checker verifies the weighted and normalized chain identities, the principal ideal augmentation, Smith saturation, uniqueness of the formal trace, residue-only ambiguity ideals, the endpoint \(\operatorname{Ext}^1\) groups, the full Koszul--Cech lower terms and chain equations, the two \(x_3\)-edge corner coefficients, the coherent-residue zero control, and the torsion-free global Cox cohomology profile.

It must be read together with ledger entries 97 and 121 and the D03 ledger
entry `Four-Corner Cellular Nerve and the Generic-Unit Obstruction`. Entry 97
supplies the complete road trace, entry 121 supplies the independently loaded
\(v_{10}\) corner comparison, and the four-corner entry proves why supported
corners alone cannot recover the generic unit.

## Next experiment

Construct the loaded PC realization of the already-fixed occurrence map \(g_3^!\). Test both endpoint squares before any all-edge assembly:

\[
\operatorname{Res}_{v_{00}}^{\rm PC}g_3^!
\stackrel?=
\Theta_{03,v_{00}}^{\rm corner},
\qquad
\operatorname{Res}_{v_{10}}^{\rm PC}g_3^!
\stackrel?=
\Theta_{03,v_{10}}^{\rm corner}.
\]

The second target is entry 121. Require the same reciprocal/BM variance, ordered normal orientation, excess retraction, and positive physical line at both endpoints. Reject the promotion if either square needs a support change, a chosen splitting, a fitted sign, or deletion of lower Cech terms.

## Outcome contract

```json
{
  "claim": "The D03 principal-lcm road complex resolves one Cartier line, and the x3 edge carries a canonical occurrence-level Koszul-Cech Gysin with primitive v00 and v10 endpoint classes.",
  "status": "proved",
  "assumptions": [
    "The scope is the occurrence coefficient system on the fixed entry-97 road square.",
    "Endpoint and product-normal orientation lines are retained rather than scalarized.",
    "Previously established normal-excess and physical-normal data are frozen external factors, not outputs of this checker."
  ],
  "evidence_refs": [
    "research/voevodsky/check_d03_toric_cox_cousin_trace.rs sha256:852652cbe3f8d20076c526e3adb493857e7859d6f33ad9cc2daede03750bfce4",
    "ledger entry 97",
    "ledger entry 121",
    "D03 ledger entry Four-Corner Cellular Nerve and the Generic-Unit Obstruction"
  ],
  "factorization_test": {
    "principal_line_resolution": "passed integrally with unit Smith factors",
    "x3_Koszul_Cech_chain_map": "passed at both endpoints with all lower terms",
    "product_Cartier_provenance": "passed; one unit gives the diagonal endpoint pair and edge incidence supplies the relative signs",
    "loaded_PC_promotion": "open",
    "nonzero_source_Q_leg": "open"
  },
  "counterevidence": [
    "A regular section of O or O(D) has zero ordinary coherent Cousin boundary.",
    "The occurrence theorem does not construct reciprocal/BM variance, the repeated-normal PC comparison, physical-Cut naturality, or G03."
  ],
  "next_experiment": "Promote the same x3 occurrence Gysin to the loaded PC category and test both v00 and v10 endpoint squares before rotating to any other edge."
}
```
