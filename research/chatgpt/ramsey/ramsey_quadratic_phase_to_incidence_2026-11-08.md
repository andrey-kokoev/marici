# Quadratic phase-to-incidence transport in the four-sector Ramsey construction

8 November 2026. Exact source-row phase calculation and exhaustive 13-to-17 orbit-attachment audit.

Companion: `check_ramsey_quadratic_phase_decoder.py` (standard-library Python). Run `python check_ramsey_quadratic_phase_decoder.py`.

## 1. Setting and result

The original symbolic row `RGRG...00`, encoded as `R=1`, `G=-1`, and two zeros, has a source-generated four-phase carrier. For even row length this is a 2D rotation plane. For odd length >=5 it is a fixed line plus a 2D rotation plane. The earlier `ramsey_original_matrix_sector_audit.py` checks these carriers for lengths 4 through 10; this note independently extracts their normalized phase coordinates

\[
q_0=(1,0),\quad q_1=(0,1),\quad q_2=(-1,0),\quad q_3=(0,-1),
\quad Q(c,s)=(-s,c).
\]

The actual 13-to-17 Ramsey witness starts with the 13-vertex graph \(G=C_{13}(\pm1,\pm5)\). Its automorphism \(\sigma(v)=5v\pmod {13}\) has order four. The independent set \(S_0=\{1,7,11\}\) generates four binary red-neighborhood columns \(n_t=\mathbf1_{\sigma^tS_0}\):

| Phase | Red neighborhood |
|---:|---|
| 0 | {1,7,11} |
| 1 | {3,5,9} |
| 2 | {2,6,12} |
| 3 | {4,8,10} |

These columns are disjoint and each contains three ones. Thus, writing \(X=[n_0\ n_1\ n_2\ n_3]\),

\[
X^TX=3I_4,\qquad \operatorname{rank}X=4,
\qquad \sigma X=X R_4,
\]

where \(R_4\) advances the four phase columns. The incidence span is therefore a scaled isometric copy of the real regular representation of the cyclic group \(C_4\).

**Linear obstruction:** No linear map from the 2D or 3D row carrier can produce four linearly independent columns. No affine map defined on the four planar phase points can do so, because \(q_0+q_2=q_1+q_3\), whereas \(n_0+n_2\ne n_1+n_3\). The latter discrepancy \(\Delta=n_0-n_1+n_2-n_3\) satisfies \(\|\Delta\|^2=12\).

In fact, the minimum squared Frobenius loss in approximating all four neighborhood columns by an affine map of \((c,s)\) is exactly \(\|\Delta\|^2/4=3\). The missing mode is the alternating character of \(C_4\), not another spatial rotation axis.

## 2. Exact quadratic phase decoder

Define the four scalar functions

\[
\ell_0(c,s)=\frac{c^2+c}{2},\quad
\ell_1(c,s)=\frac{s^2+s}{2},\quad
\ell_2(c,s)=\frac{c^2-c}{2},\quad
\ell_3(c,s)=\frac{s^2-s}{2}.
\]

They satisfy \(\ell_j(q_t)=\delta_{jt}\). Hence

\[
\boxed{\Phi(c,s)=\sum_{j=0}^3\ell_j(c,s)n_j}
\]

is a **degree-two, phase-equivariant decoder** obeying

\[
\Phi(q_t)=n_t,\qquad
\Phi(Q(c,s))=\sigma\Phi(c,s).
\]

It is polynomial (not a binary graph encoder at arbitrary intermediate angles): the output is 0/1 on the four quarter-turn states. The statement of equivariance holds on the full coefficient plane.

Alternatively, set

\[
M=(n_0+n_1+n_2+n_3)/4,\quad
C=(n_0-n_2)/2,\quad
D=(n_1-n_3)/2,\quad
E=(n_0-n_1+n_2-n_3)/4.
\]

Then

\[
\Phi(c,s)=(c^2+s^2)M+cC+sD+(c^2-s^2)E.
\]

On the unit circle the first factor becomes simply \(M\). Its four independent real cyclic modes are

| Mode | Dimension | Transformation under sigma |
|---|---:|---|
| Constant \(M\) | 1 | fixed |
| First harmonic \((C,D)\) | 2 | quarter-turn |
| Second harmonic \(E\) | 1 | changes sign |

Thus the exact decomposition is \(\mathbf1\oplus V_{90^\circ}\oplus\varepsilon\), dimensions \(1+2+1=4\). The original even-k carrier supplies the quarter-turn plane alone; the odd-k carrier additionally has a fixed direction, but neither supplies the alternating character by a linear map. The quadratic term creates it algebraically.

The checker recovers \(q_t\) from the original source row carrier for every \(k=4,\ldots,10\), then verifies that the quadratic decoder recovers all 52 binary column entries exactly for each \(k\). This is a *conditional adapter*: the 13-vertex graph and the 4-column incidence orbit supply its coefficients. It does not derive the 13-vertex graph from the short symbolic row.

## 3. Eliminate both attachment choices, within a fixed four-vertex orbit

Rather than require a three-element seed transversal, enumerate **all 183 independent sets** \(S\) of the 13-vertex graph, including the empty set, and form the four columns \(\mathbf1_{\sigma^tS}\).

A graph on the four new vertices preserved by the cyclic phase shift can use only two edge orbits: the four neighboring edges or the two opposite edges. Thus exactly four internal edge patterns are possible: empty, matching \(2K_2\), cycle \(C_4\), complete \(K_4\).

For each of these \(183\times4=732\) choices, the checker constructs the 17-vertex block adjacency matrix and tests (i) absence of red triangles and (ii) independence number at most five. The independence numbers come from a precomputed exact 13-vertex induced-subgraph table and the necessary-and-sufficient extension identity

\[
\alpha(H)=\max_{J\in\operatorname{Ind}(F)}
\left(|J|+\alpha\bigl(G-\bigcup_{j\in J}\sigma^jS\bigr)\right).
\]

Results (all seed subsets are independent; failed triangle checks excluded):

| Four-new-vertex internal red graph | Triangle-safe choices | Valid with alpha <= 5 |
|---|---:|---:|
| Empty | 183 | 0 |
| Matching \(2K_2\) | 113 | 0 |
| \(C_4\) | 87 | **4** |
| Complete \(K_4\) | 0 | 0 |

All four survivors are exactly the four cyclic translates of \(\{1,7,11\}\). They have seed size three, choose one vertex from each nonzero length-four orbit, and produce isomorphic 17-vertex witnesses. The final graph has 42 red edges, no red triangles, and independence number exactly five.

**Conditional selection theorem (fully enumerated):** Given the old graph \(C_{13}(\pm1,\pm5)\), the automorphism \(v\mapsto5v\), and a sector of four new vertices with cyclic equivariance, the Ramsey constraints uniquely determine the seed-orbit and the internal edge orbit, up to the cyclic action. The triple-transversal shape, red \(C_4\), and resulting 17-vertex graph are outputs of the constraints, not selection inputs.

The four actual seed representatives are still symmetry equivalent. No unmarked equivariant procedure can select **one** distinguished seed from this four-element orbit: such a seed would have to be fixed by the order-four action, and none is. The oriented empty pair in the source row is a possible *phase marker*; an actual identification of this marker with a particular 13-vertex neighborhood label has not been derived.

## 4. General algebraic degree bound for longer cyclic sectors

Suppose \(q\) equally spaced phase points lie on the unit circle, and their intended incidence columns \(n_0,\ldots,n_{q-1}\) are linearly independent (for example nonzero disjoint binary supports).

A real polynomial decoder of total degree \(d\) in \((c,s)=(\cos\theta,\sin\theta)\) restricts to a trigonometric polynomial with frequencies at most \(d\). For \(d<\lfloor q/2\rfloor\), its values at the \(q\) phases lie in a subspace of dimension at most \(2d+1<q\) (with the usual even-\(q\) adjustment). They cannot span the \(q\) independent columns.

Conversely, Fourier/Lagrange interpolation on the cyclic phases uses modes through \(\lfloor q/2\rfloor\), each representable by a real polynomial of that degree in \(c,s\). Therefore

\[
\boxed{d_{\min}=\lfloor q/2\rfloor}
\]

for a polynomial decoder of *arbitrary independent incidence columns* at those \(q\) phases. For \(q=4\), the required degree is exactly two. This is a theorem about cyclic incidence transport, **not** a formula for \(R(3,k)\).

## 5. Implications and remaining gate

- A 90° carrier can advance the four phases with only two rotating real dimensions.
- An exact **binary incidence** representation of the four phases requires four independent cyclic modes, including the second-harmonic parity contrast.
- Degree-two phase decoding gives the full four-column incidence orbit; together with a source graph and the derived internal \(C_4\), it produces a valid 17-vertex Ramsey witness.
- The Ramsey constraints determine that attachment uniquely within the four-vertex \(C_4\)-equivariant family, without supplying the desired output size as an input.
- This does **not** determine which order-four symmetry or sector length to use at arbitrary Ramsey parameters; it does **not** prove extremality or a general closed formula.

The next mathematically decisive gate is to produce the old graph, cyclic symmetry, and phase-labeled attachment carrier from the same original symbolic source rule, rather than supplying the graph first. It is also necessary to test larger cyclic orbit sizes if a prospective universal generator must have unbounded increment sizes.
