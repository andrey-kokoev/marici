# The Bunch--Davies marked-top discontinuity is the physical parity readout

Use the source-normalized marked form

\[
\Omega_{111}=\frac{da\wedge db}{L_1L_2\sqrt K}
\]

and the continued physical relative current \(\Gamma_{\rm BD}(E)\) selected by

\[
E\longmapsto E-i0.
\]

Define the cusp readout by

\[
\mathcal R_{\rm BD}(\Omega_{111})
:=\frac{1}{2\pi i}
\operatorname{Disc}_{E=0}
\int_{\Gamma_{\rm BD}(E)}\Omega_{111},
\]

with its value taken in the integral algebraic nearby-cycle quotient and then reduced modulo two.

The source residue map places \(\Omega_{111}\) on the top quotient generator \(g_{111}^{\rm top}\). Its total-energy specialization kernel is primitive. The Bunch--Davies continuation supplies the conductor boundary

\[
(2,-2,2,-2)
\]

and primitive half-boundary

\[
(1,-1,1,-1).
\]

The two-node cellular boundary sends this half-boundary with coefficient one to

\[
e_{6,\mathrm B}=C_--C_+
=3H-E_1-\cdots-E_6-3E_7.
\]

The typed marked extension column is

\[
g_{111}^{\rm top}\longmapsto
\begin{pmatrix}
0\\0\\1/[8(x+y)]\\0
\end{pmatrix}_{(e_2,e_4,e_6,v_0)}.
\]

Accordingly, the two-channel physical readout is

\[
\left(
\langle\mathcal R_{\rm BD},e_6^\vee\rangle,
\langle\mathcal R_{\rm BD},v_{\rm alg}^\vee\rangle
\right)
\equiv(1,0)\pmod2.
\]

The coefficient \(1/[8(x+y)]\) belongs to the de Rham normalization, while the cellular coefficient one belongs to the integral Betti normalization.

One comparison statement carries the remaining verification burden: the continued source current \(\Gamma_{\rm BD}\) specializes to the derived oriented conductor chain with multiplicity one. The explicit \(i0\) arc calculation geometrically specifies this statement; Grothendieck has received the task of realizing it independently inside an integral Mayer--Vietoris or Clemens--Schmid diagram.

Certificate:

- `research/voevodsky/checkers/assemble_BD_marked_top_physical_readout.py`;
- `research/voevodsky/results/BD_marked_top_physical_readout.json`.
