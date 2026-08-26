# D5 cubic versus shaping generalized CP

Work package: WP601  
Owner: marici.Figueiredo

## Correction to the quartic window

WP600 proves that inequivalent faithful \(D_5\) doublets of weights one and
two share only a radial mixed quartic of bidegree \((2,2)\). The complete
renormalizable grammar nevertheless contains the cubic

\[
K=\operatorname{Re}(z_\phi z_\psi^2),
\]

because its rotation charge is \(1+2\cdot2=5\). Bare CP also preserves
\(K\). On the unit-radius slice,

\[
K=\cos(\alpha+2\beta).
\]

At the WP600 representative \((0,\pi/5)\), a coefficient \(\gamma\) gives

\[
\nabla(\gamma K)=
\begin{pmatrix}
-\gamma\sin(2\pi/5)\\
-2\gamma\sin(2\pi/5)
\end{pmatrix},
\]

which is nonzero for every \(\gamma\ne0\). The D5 representation is therefore
not a complete renormalizable selector by itself.

## Complete diagonal Z5 shaping audit

Assign an additional diagonal \(Z_5\) charge pair \((q_\phi,q_\psi)\).
The cubic is forbidden when

\[
q_\phi+2q_\psi\ne0\pmod5.
\]

The common \(D_5\) rotation has charge vector \((1,2)\). A shaping vector is
linearly independent of it precisely when

\[
q_\psi-2q_\phi\ne0\pmod5.
\]

Over \(\mathbb F_5\), the vanishing loci of these expressions coincide: the
five dependent charge pairs are exactly the five pairs that allow the cubic.
Consequently every one of the twenty charge pairs that forbids the cubic
combines with \((1,2)\) to generate the full independent rotation group
\(C_5\times C_5\).

Independent rotations restore componentwise generalized CP. For any pair of
quintic extrema \((m\pi/5,n\pi/5)\), bare CP composed with independent powers
\((m,n)\) fixes both components. Thus diagonal shaping repairs the cubic only
by destroying the intended physical CP breaking.

## Disposition

The WP600 quartic criterion remains useful, but its first D5 witness fails as
a complete renormalizable architecture. The smallest repair class is also
closed:

- without shaping, the allowed cubic moves the proposed vacuum;
- every diagonal Z5 shaping charge that forbids the cubic generates
  independent rotations and restores generalized CP.

A successor must use a non-diagonal non-abelian selection rule, gauge locality,
or collective breaking that forbids the cubic without factorizing the common
rotation group. It must then be audited against the complete invariant ring,
not only one bidegree.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp601_d5_cubic_shaping_cp_tradeoff.py

The generated result is
research/flavor/results/wp601_d5_cubic_shaping_cp_tradeoff.json.
