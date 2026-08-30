# 1751 — The Physical Cut Pairing Does Not Resolve the Integral Cusp Extension

## Reconciliation

The corrected Entry 1750 identifies the source-normalized width-two
monodromy

\[
T_{\rm src}=
\begin{pmatrix}1&2\\0&1\end{pmatrix}.
\]

Its elliptic coinvariants contain \(\mathbb Z/2\). Entry 1152 separately
shows that gluing this coinvariant into the full rank-nine integral lattice
is controlled by

\[
\operatorname{Ext}^1_{\mathbb Z}
(\mathbb Z/2,\mathcal A_{--})
\simeq(\mathbb Z/2)^2.
\]

## Existing physical comparison

The physical Cut--nearby comparison need not be recomputed. Entry 1149
derives its source-normalized class in the master basis:

\[
(0,0,-2\pi^2/x,0,-2\pi^2/y,-2\pi^2/(xy),0,0,0).
\]

Every nonzero component lies in the algebraic infinity-Gysin kernel:

\[
R_\infty(e_3)=R_\infty(e_5)=R_\infty(e_6)=0.
\]

Therefore

\[
\boxed{
\mathcal C_{\rm phys}
\longrightarrow
\operatorname{coker}(T_{\rm src}-I)_{\rm ell}
\quad\text{is zero}.
}
\]

The vanishing occurs before taking coinvariants and is termwise, not a
rational cancellation. Hence the physical Cut commutator cannot choose
among Entry 1152's four integral gluing classes.

## Narrow result

The two unresolved parity bits are internal extension data of the complete
integral coefficient lattice. They are not a hidden activation by the known
physical Cut--nearby current.

No rational connection calculation, complex period, or repetition of the
Cut pairing can resolve them. The remaining finite construction is the
integral Picard--Lefschetz action on

\[
0\to\mathcal T_{7,\mathbb Z}
\to H^2(S\setminus D_\infty;\mathbb Z)
\to H^1(D_\infty;\mathbb Z)(-1)\to0,
\]

retaining the primitive infinity-Gysin lattice.

This is coefficient gluing over the existing total-energy carrier. No new
carrier stratum is implicated.

## Evidence

- Entries 1147, 1149, 1151, 1152, 1750;
- research/benincasa/results/cusp-physical-pairing-frontier.json.

## Next falsifier

Construct the local integral Lefschetz thimble of the nodal anticanonical
boundary inside the degree-two del Pezzo surface. Compute the parity of twice
an elliptic coinvariant lift along the integral algebraic plane
\(\langle e_6,v_{\rm alg}\rangle\). Any answer must be one of the four
predeclared classes in \((\mathbb Z/2)^2\).
