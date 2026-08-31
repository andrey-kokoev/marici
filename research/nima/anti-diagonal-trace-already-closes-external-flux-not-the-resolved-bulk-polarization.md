# Anti-diagonal trace already closes external flux, not the resolved bulk polarization

## Status

Frontier reconciliation. No G1.1 or RH claim.

## Existing closure

The repository already separates the complete Green problem into endpoint and bulk parts. The established anti-diagonal completed zero-trace theorem cancels the total typed endpoint contribution

\[
\mathfrak b_\partial^+-\mathfrak b_\partial^-+\mathfrak F_B=0,
\]

where the external five-cell controller carries the constant--delta and tail--principal-value boundary representation.

Therefore, after the moving-seam and resolved-graph covariance results, **external boundary-flux cancellation is not the next open gate**. Endpoint attachment is natural, and its anti-diagonal completed trace cancels the typed external flux.

## What survives cancellation

Green integration by parts has the split

\[
\langle DK,zK\rangle
=
\mathfrak b_\partial(K;z)+\mathfrak b_{\mathrm{bulk}}(K;z).
\]

Killing the first term does not kill or orient the second. The oriented face difference is

\[
\Delta_{\mathrm{face}}
=
\|x_+\|^2-\|x_-\|^2
=
4\operatorname{Re}\langle DK,zK\rangle.
\]

By contrast, the positive face sum erases this cross term. Hence the resolved positive graph

\[
(1+M_\Phi^2)I+B^*B
\]

and endpoint zero-trace cancellation still do not determine the ordered bulk polarization.

The hostile phase rotation

\[
DK\mapsto e^{i\varphi}DK
\]

preserves every diagonal norm and the endpoint packet while changing
\(\operatorname{Re}\langle DK,zK\rangle\). This proves that neither resolved-Gram preservation nor complete endpoint cancellation can close the bulk identity alone.

## Correct local frontier

The remaining Green mate is not the whole bulk-plus-external-port theorem. Its external-port summand is closed. The residual is exactly the source-authorized ordered cross-face polarization

\[
\mathcal C_z(K)=\langle DK,zK\rangle
\]

on the resolved completed source domain, together with its compatibility with the selected direct-sum graph before codiagonalization.

For G1.1 this means that diagonal positivity data must be supplemented by the ordered matrix-unit pairings. In finite two-column form, one must retain all four entries

\[
E_{11},\ E_{12},\ E_{21},\ E_{22},
\]

rather than only the two diagonal energies or their sum. The off-diagonal entries are where phase/orientation lives.

## Radical consequence

Endpoint radical compatibility is already protected: the retained endpoint metric is positive and the odd interaction vanishes on genuine zero-trace bulk directions. Remaining radicals can occur only in the even zero-trace bulk. To descend the ordered polarization, one must prove

\[
\mathcal C_z(r,v)=\mathcal C_z(v,r)=0
\]

for every radical vector \(r\) of that even bulk form and every admitted \(v\). Diagonal vanishing \(\mathcal C_z(r,r)=0\) is insufficient without polarization.

## Revised verdict

The sequence is now:

1. moving-seam covariance of the resolved three-port graph — closed;
2. endpoint naturality — closed;
3. anti-diagonal cancellation of typed external flux — closed;
4. ordered cross-face bulk polarization on the resolved completion — open;
5. radical descent and closed range of the full analytic--arithmetic pushout — open;
6. prime-uniform coercivity — open.

Thus the earliest local quadratic gate is the ordered bulk polarization, not another seam, endpoint-rank, or external-flux calculation.
