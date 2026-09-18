# Many-many ordered bulk-polarization gate

For a finite two-column realization, retain the full ordered matrix

$$
\mathbf E_z(K)=
\begin{pmatrix}
\langle DK_1,zK_1\rangle&\langle DK_1,zK_2\rangle\\
\langle DK_2,zK_1\rangle&\langle DK_2,zK_2\rangle
\end{pmatrix}.
$$

The diagonal entries encode observer energies. The off-diagonal entries encode phase and orientation. The relative readout is the ordered form

$$
\mathcal C_z(K_i,K_j)=\langle DK_i,zK_j\rangle.
$$

A valid many-many quotient requires radical descent:

$$
 r\in\operatorname{Rad}(Q_{\rm bulk})
\Longrightarrow
\mathcal C_z(r,v)=\mathcal C_z(v,r)=0
$$

for every admitted `v`.

The gate is checked first on the common analytic source core, then extended by joint graph closure. Endpoint and external-flux coordinates are carried by the already closed boundary sector.

Status: ordered bulk-polarization gate implemented as the next analytic interface; radical descent and closed-range extension remain open.
