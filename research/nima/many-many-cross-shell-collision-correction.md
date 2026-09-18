# Many-many cross-shell collision correction

For an ordered-pair shell history,

$$
\rho_{nm}^{[a,b]}(t)
=(nm)^{-1/2}
K_{[a+\log n,b+\log n]}\left(t+\log\frac mn\right).
$$

The unlabelled codiagonal sees only

$$
(a+\log n,\ b-a,\ \log(m/n),\ (nm)^{-1/2}).
$$

Consequently distinct source tuples can produce proportional histories. The many-many wall carrier must retain the labels `(a,b,n,m)` through the codiagonal, or explicitly adjoin the collision-cycle sector.

The corrected global object is therefore a labelled relative carrier with a codiagonal map

$$
C_{\rm lab}:\mathcal V_{\rm lab}\to\mathcal W_{\rm pair},
$$

followed by a scalar output map only after the collision quotient is specified.

Status: mixed cross-shell collision obstruction incorporated into the architecture.
