# The thimble column is the algebraic remainder of one integral monodromy column

## Minimal computable object

A full geometric thimble mesh is sufficient but not necessary. The requested column can be extracted from one column of the integral monodromy on

\[
H^2(S_E\setminus D_\infty;\mathbb Z).
\]

Choose an integral basis

\[
(k_1,\ldots,k_7,\delta,\beta),
\]

where the \(k_i\) span the primitive infinity-Gysin kernel, \(\delta\) is the primitive invariant elliptic lift, and \(\beta\) projects to the transverse elliptic cycle. Normalize the quotient monodromy by

\[
T\delta=\delta,
\qquad T\beta\equiv\beta+2\delta\pmod{\mathcal T_7}.
\]

Then

\[
\boxed{
r=T\beta-\beta-2\delta\in\mathcal T_7.
}
\]

Projecting \(r\) to the final algebraic character plane gives

\[
r_{--}=a e_6+bv_{\rm alg}+2u,
\qquad u\in\mathcal A_{--},
\]

and the desired thimble/Gysin column is

\[
\boxed{(a,b)=r_{--}\bmod2.}
\]

## Lift invariance

Replacing \(\beta\) by \(\beta+k\), \(k\in\mathcal T_7\), changes

\[
r\mapsto r+(T-I)k.
\]

The algebraic monodromy is identity, so this does not change \(r\). Replacing \(\delta\) or the ambient representative by an algebraic lift changes the displayed \((e_6,v_{\rm alg})\) coefficients by an even vector. Hence \((a,b)\) is well defined.

## Concrete acquisition contract

Only the following data need be produced by a numerical or cellular Picard--Lefschetz continuation:

1. an integral primitive-Gysin-compatible basis;
2. the single column \(T\beta\);
3. the coordinates of \(\delta,e_6,v_{\rm alg}\) in that basis;
4. an exact check that the remaining algebraic-character coordinates of \(r\) vanish or are projected away.

There is no need to reconstruct all periods or the full \(9\times9\) matrix.

## Current absence

No current artifact contains an integral coordinate vector for \(T\beta\). The rational residue matrix determines its elliptic quotient \(\beta+2\delta\) but erases the algebraic remainder \(r\), exactly where the two parity bits live.

Verification:

- `research/voevodsky/checkers/check_thimble_column_extraction_contract.py`
- `research/voevodsky/results/thimble_column_extraction_contract.json`
