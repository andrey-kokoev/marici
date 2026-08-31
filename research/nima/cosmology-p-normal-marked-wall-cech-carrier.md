# The minimal marked-wall Čech carrier kills the nearby quotient at p=0

For ordered walls \((q_1,q_2,q_3)\) and ordered pairs
\((12,13,23)\), the source sewing data determine

\[
R^3\xrightarrow{d_0}R^3\xrightarrow{d_1}R/(p),
\]

with

\[
d_0=\begin{pmatrix}-1&1&0\\-1&0&1\\0&-1&1\end{pmatrix},
\qquad d_1=\begin{pmatrix}1&-1&1\end{pmatrix}.
\]

The circuit identity gives \(d_1d_0=0\). On the generic
\(K_{\rm CM}\)-invertible stratum, \(E_{\rm CM}=0\). The sewing subcomplex
\(J_{\rm sew}=\operatorname{im}d_0\) has rank two and is differential-stable
without imposing \(p\eta=0\) by definition.

For \(p\ne0\), the triple term is absent and the pair quotient has rank one.
At \(p=0\), \(d_1\) has rank one. Over both \(\mathbf F_{101}\) and
\(\mathbf F_{103}\),

\[
\dim H^1=3-2-1=0,
\qquad
\dim H^2=1-1=0.
\]

Thus the special triple Čech term kills the generic rank-one nearby quotient.
The minimal sewn carrier has no surviving \(\Xi_p\) and no nonzero relative
\(p\)-normal Bockstein. This is a no-go only for the minimal marked-wall Čech
carrier. A separately source-derived bulk/face augmentation could add the
required lift and must be checked afresh.

Artifact:

- `research/nima/checkers/check_cosmology_p_normal_marked_wall_cech_carrier.py`
- `research/nima/results/cosmology_p_normal_marked_wall_cech_carrier.json`
