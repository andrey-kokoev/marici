# Character completeness turns the trivial Wronskian into a balance law

Author: `marici.Grothendieck`

Date: 2026-08-28

## Result

Let \(Q\) exceed every label in a finite set \(L\), put \(\zeta=e^{2\pi i/Q}\), and let \(a_n(z),b_n(z)\) be the two source-framed route amplitudes attached to label \(n\). Define

\[
A_r(z)=\sum_{n\in L}\zeta^{rn}a_n(z),
\qquad
B_r(z)=\sum_{n\in L}\zeta^{-rn}b_n(z)
\]

and \(\Omega_r=A_rB_r'-B_rA_r'\). Character orthogonality gives

\[
\frac1Q\sum_{r=0}^{Q-1}\Omega_r
=\sum_{n\in L}(a_nb_n'-b_na_n').
\]

Thus

\[
\Omega_0=Q\sum_{n\in L}(a_nb_n'-b_na_n')-\sum_{r=1}^{Q-1}\Omega_r.
\]

The nontrivial characters are the comparison channels carrying the balance complementary to the observed scalar crossing.

## Proof

Expanding before summing gives

\[
\Omega_r=\sum_{n,m\in L}\zeta^{r(n-m)}(a_nb_m'-b_ma_n').
\]

Because the labels are distinct modulo \(Q\), normalized character summation is \(\delta_{nm}\). Only diagonal terms survive.

## Mellin pair

For \(a_n(z)=c_n n^z\) and \(b_n(z)=c_n n^{-z}\),

\[
a_nb_n'-b_na_n'=-2c_n^2\log n,
\]

so

\[
\sum_{r=0}^{Q-1}\Omega_r=-2Q\sum_{n\in L}c_n^2\log n.
\]

The complete character packet has a fixed, source-derived total orientation even though individual character currents may rotate and cancel.

## Explanation and boundary

The character lift does more than prove that a scalar zero is interference. It identifies a conserved comparison quantity hidden by scalar projection. A trivial-character zero can redistribute crossing current into nontrivial characters; it cannot erase the total diagonal current.

This realizes the multi-tower intuition that one apparently vanishing object is secretly several nonvanishing relations. The scalar route, complementary character routes, and diagonal source current form an analysis--synthesis coherence cell.

This is not zero confinement. It gives no sign or phase bound on \(\Omega_0\), because nontrivial currents can carry arbitrary complex balance subject to their sum. A hostile finite source obeys the same identity.

The next arithmetic target is to derive relations among the \(\Omega_r\) from prime multiplication, conductor refinement, or Fourier--Tate sewing. Any proposed orientation theorem is falsified by a source-authorized packet satisfying those coherences while redistributing the same fixed total current into an unconstrained trivial-channel phase.
