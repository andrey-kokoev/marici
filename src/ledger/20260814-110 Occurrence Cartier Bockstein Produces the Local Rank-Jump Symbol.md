# Occurrence Cartier Bockstein Produces the Local Rank-Jump Symbol

## Record

Date: 2026-08-14

Status: proved for the canonical barycentric pullback of the absolute
occurrence complex, its spectator-factor obstruction, and the resulting
relative Cartier/Bockstein class. No global Yoneda specialization or CHY
identification is claimed.

## Claim

Let \(\mathcal P_{\rm abs}\) be the integral unlocalized absolute
support/occurrence complex of entry 105, pulled to the barycentric
subdivision of the corrected \(D03\) blowup. For a flag

\[
S_0<S_1<\cdots<S_k,
\]

the coefficient stalk is the stalk on \(S_0\). Deleting the initial flag
vertex applies the actual primal lcm corestriction, while deleting any other
vertex uses the identity. Together with the internal normal differential and
the tensor-totalization sign, this gives an integral complex with

\[
1169\text{ generators},
\qquad
\operatorname{rk}C_*=(51,303,521,282,12),
\qquad d^2=0.
\]

On the marked seven-triangle carrier, the exact loaded identity is not the
naive formula proposed in entry 109. It is

\[
\boxed{
dH_{\rm Morse}^{\rm abs}
=q_J^{\rm abs}-x_3\widetilde\xi^{\rm abs}.
}
\]

The common nonunit factor \(x_3\) is forced because every special gallery
edge lies in the short facet \(x_3\). Reducing modulo \((x_3)\) is an exact
falsifier for any claimed ordinary pullback producing
\(\widetilde\xi\) directly.

The principal-ideal evaluation

\[
(x_3)^\vee\otimes(x_3)\longrightarrow R,
\qquad x_3^\vee(x_3)=1,
\]

is valid on the special ideal-valued term. It cannot extend to an absolute
chain map on the whole carrier: the generic chain contains coefficients
\(-1,+1,X_{03}\), none divisible by \(x_3\). Such an extension would be an
\(R\)-linear division map \(R\to R\), which is impossible without
inverting \(x_3\).

The correct operation is relative. Let \(E=\{a,c\}\) be the endpoint cap,
let \(J\) be the generic side, and form the endpoint-and-generic-relative
complex

\[
B
=
\operatorname{Cone}\!\left(
C_*^{\rm BM}(J,E;\mathcal P_{\rm abs})
\longrightarrow
C_*^{\rm BM}(T,E;\mathcal P_{\rm abs})
\right).
\]

Equivalently, in the finite certificate,

\[
B=(C_{\rm carrier}/E)/(R\,q_J).
\]

The generic term is now killed with its correct relative variance, and the
loaded identity becomes

\[
\boxed{
d_B[H_{\rm Morse}]
=-x_3[\widetilde\xi].
}
\]

Apply the Cartier triangle for \(I_3=(x_3)\):

\[
I_3\otimes_R^L B
\longrightarrow B
\longrightarrow (R/I_3)\otimes_R^L B
\xrightarrow{\delta_{I_3}}
(I_3\otimes_R^L B)[1].
\]

Then \([H_{\rm Morse}\bmod x_3]\) is a cycle and

\[
\delta_{I_3}[H_{\rm Morse}\bmod x_3]
=[-x_3\widetilde\xi].
\]

Pairing only after this connecting morphism gives the integral occurrence
Bockstein/Gysin class

\[
\boxed{
\beta_{x_3}[H_{\rm Morse}\bmod x_3]
=-[\widetilde\xi].
}
\]

The sign is fixed jointly by the thimble and positive \(x_3\)-normal
orientations. Reversing either reverses the sign; it cannot be reset
independently.

Finally, \([\widetilde\xi]\) is not merely a formal output. In the smallest
relative carrier,

\[
x_3[\widetilde\xi]=0,
\qquad
[\widetilde\xi]\ne0.
\]

At the specialization to \(\mathbf F_{101}\), \(x_3\mapsto0\) and all other
occurrence variables map to one. The boundary/relation matrix on 15
degree-one generators has rank seven; adjoining
\(\widetilde\xi\) raises the rank to eight. Thus
\([\widetilde\xi]\) is a certified nonzero \(x_3\)-torsion class.

## Interpretation

This is the first intrinsic chain-level realization of the local
rank-jump/QTDS symbol. The associated-grade operation is not coefficientwise
division and not a rational projector. It is a Cartier connecting operation
on a relative scalar occurrence complex:

\[
\boxed{
\operatorname{gr}_{x_3}^{\rm local}
\simeq
\beta_{x_3}^{\rm Cartier}.
}
\]

This statement is local and carrier-level. It does not yet show that the
class is representation-independent, factorization-natural, the global
half-object \(\mathsf J\), or equal to \((\operatorname{Pf}'A)^2\) in CHY
cohomology.

The result nevertheless changes the frontier. The scalar first-normal
symbol now has an exact chain mechanism, and the missing global problem is
to compare this local occurrence Bockstein with the
normalization--conductor tag object and with physical-cut specialization.

## Evidence

Exact certificate:

- `research/voevodsky/check_d03_pabs_morse_pullback.rs`

SHA-256:

```text
647120e3c82f5b51c825e710a2444132d2e2da71a045cc083b7f182df5c4a50b
```

It reconstructs the 215-generator absolute complex, constructs the full
1169-generator barycentric pullback, verifies every weighted mixed square in
\(d^2\), derives the seven-triangle boundary and common \(x_3\) factor,
checks the ordered \(D03\) carrier sign, proves the global ideal-dual map is
mistyped, constructs the relative occurrence Koszul/Cartier identity, and
certifies nonvanishing of \([\widetilde\xi]\).

## Boundary

- The common \(x_3\) factor is required by the ordinary occurrence cosheaf.
  Removing it before passing to the relative Cartier triangle is an invalid
  division rule.
- The occurrence ideal \((x_3)\) and the monodromy normal \((u_3)\) are
  distinct. No identification between them is made.
- The principal ideal dual is applied only to the ideal-valued output of the
  connecting morphism. It is not extended to the generic \(R\)-valued
  chain.
- The Bockstein class is proved in the minimal relative carrier \(B\). Its
  image in a larger scalar PC/Cousin complex and its survival under physical
  factorization remain open.
- The current construction does not provide \(H_{\rm cond}\), identify two
  trivializations of the global Yoneda class, or construct
  \(\operatorname{sp}_G\).
- Nonvanishing over one finite-field specialization proves the integral
  polynomial class is not a boundary in the certified finite complex. It
  does not prove a global twisted-cohomology comparison theorem.

## Next experiment

Construct the conductor comparison for one sheet before attempting the full
six-tag object. The exact target is a variance-correct map

\[
\boxed{
\kappa_{+,03}^{\rm cond}:
B_{+,03}^{\rm Cart}
\longrightarrow
P_{\rm tag,+}[s]
}
\]

from the local Cartier/Bockstein complex to the positive-sheet conductor
tag complex, with a derived—not assigned—shift \(s\). It must send the
Bockstein class to the corresponding three-tag first normal symbol, commute
with the triangle incidence, retain occurrence and monodromy lines
separately, and reproduce the already-fixed \(D03\) orientation.

Then construct its polarity conjugate. Only after the two maps exist may one
test whether their alternating sum is \(K_{\rm alt}\), whether
\(\Delta^\vee\) gives the primitive unit, and whether physical Gysin
specialization agrees with entry 100.

## Outcome contract

```json
{
  "claim": "The canonical P_abs-loaded seven-triangle Morse carrier has boundary q_J-x3*xi_tilde. In the endpoint-and-generic-relative Cartier complex, the x3-Bockstein of H_Morse mod x3 is the nonzero torsion class -xi_tilde. Thus the local scalar rank-jump symbol is intrinsically realized as a Cartier connecting operation, not division by x3.",
  "status": "proved",
  "assumptions": [
    "The corrected D03 blowup, absolute complex, gallery, and orientations are those of entries 105-109.",
    "The claim is scoped to the finite relative occurrence complex B; no global PC or CHY comparison is inferred.",
    "Occurrence x3 and monodromy u3 remain independent coefficient layers."
  ],
  "evidence_refs": [
    "research/voevodsky/check_d03_pabs_morse_pullback.rs",
    "ledger entries 105-109"
  ],
  "factorization_test": {
    "absolute_P_abs_d2": "passed",
    "barycentric_pullback_d2": "passed on 1169 generators",
    "naive_boundary_without_x3": "falsified",
    "absolute_ideal_dual_chain_map": "falsified as untyped",
    "relative_Cartier_Bockstein": "passed",
    "xi_tilde_nonboundary": "passed over F_101 rank certificate",
    "global_Yoneda_or_CHY_identification": "unconstructed"
  },
  "counterevidence": [
    "Every special gallery edge contains x3.",
    "The generic q_J chain is not I3-valued.",
    "The proved Bockstein is local to the endpoint-and-generic-relative complex."
  ],
  "next_experiment": "Construct the one-sheet conductor comparison kappa_{+,03}^{cond}; test whether the local Cartier class maps to the positive three-tag normal symbol before forming K_alt."
}
```
