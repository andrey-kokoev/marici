# Erratum: enhanced Rees columns are not ambient thimble/Gysin columns

## Tempting calculation

The four enhanced-point realization is explicit:

\[
\Phi_{\rm exc}=
\begin{pmatrix}
1&-1&1&-1\\
1&1&-1&-1\\
1&-1&-1&1
\end{pmatrix}
\]

in point order \((++,+-,-+,--)\). Its columns sum to zero, so

\[
\Phi_{\rm exc}(1,1,1,1)^T=0.
\]

Combining this with the strict-transform congruence

\[
\widetilde C\equiv
E_{++}+E_{+-}+E_{-+}+E_{--}\pmod2
\]

would appear to force a zero thimble column.

## Type obstruction

Ledger entry 300 explicitly forbids this inference. The four enhanced germs are higher-Rees/Cut--nearby functionals with

\[
T_{\rm exc}=1,
\qquad N_{\rm exc}=0,
\]

whereas the desired object is an integral ambient lift of the elliptic vanishing cycle through the infinity-Gysin sequence. The entry states that no map from the four enhanced-point lattice to the nilpotent image is inferred from their matching ranks.

Likewise, entry 312 identifies the enhanced occurrence quotient with the **conductor algebraic layer** through \(\Phi_{\rm exc}=JK\), but explicitly leaves the elliptic vanishing line separate by infinity-Gysin type.

Thus the exceptional symbols in the blowup geometry cannot be identified with the higher-Rees generators \(h_{\epsilon\delta}\) without constructing the very ambient comparison being sought.

## Withdrawn reduction

The formula

\[
(a,b)=\pi_{\rm alg}
(E_{++}+E_{+-}+E_{-+}+E_{--})\pmod2
\]

is only a prospective geometric reduction. Existing \(\Phi_{\rm exc}\) columns do not instantiate \(\pi_{\rm alg}\). Consequently neither the zero column from their diagonal relation nor the conductor gluing label \((1,1)\) is the elliptic thimble/Gysin column.

## Exact separation of the three two-bit objects

1. **Enhanced/conductor saturation:** \((\mathbb Z/2)^2\), explicitly realized by \(J\) and \(\Phi_{\rm exc}\).
2. **Conductor quotient gluing:** recorded as \((1,1)\) in the marked rank-twelve nilpotent packet.
3. **Elliptic cusp lift:** \((a,b)\in\mathcal A_{--}/2\mathcal A_{--}\), still uncomputed.

Equal Smith type does not identify these objects.

## Remaining constructor

A valid computation must map a geometric exceptional curve or thimble chain directly into

\[
H^2(S_E\setminus D_\infty;\mathbb Z)
\]

and then evaluate its coordinates in the primitive kernel basis \((e_6,v_{\rm alg})\). The enhanced higher-Rees realization terminates in \((ye_3,xe_5,e_6)\) and does not provide this map.

Verification:

- `research/voevodsky/checkers/check_enhanced_thimble_type_separation.py`
- `research/voevodsky/results/enhanced_thimble_type_separation.json`
