# The retained four-chart graph has an explicit order-four twistor rotation

## Question

Does the larger retained common graph construct the fourth presentation turn without inverting a scalar trace?

## Claim boundary

Yes algebraically, and continuously for the topology transported from the common graph. This does not identify the transported chart topology with every independently prescribed unanchored output topology.

Let \(M_k\) be the retained common graph at fixed parameter \(k\). For each presentation index \(i\in\mathbb Z/4\), let

$$
e_{i,k}:M_k\xrightarrow{\simeq}\widetilde V_{i,k}
$$

be its complete graph chart. Define the graded twistor carrier

$$
\mathfrak T_k
=
\coprod_{i\in\mathbb Z/4}\widetilde V_{i,k}.
$$

The quarter-rotation is

$$
\tau_k(e_{i,k}(m))=e_{i+1,k}(m).
$$

It preserves the retained common datum \(m\) and cyclically changes only its presentation chart. Its inverse is

$$
\tau_k^{-1}(e_{i,k}(m))=e_{i-1,k}(m).
$$

Four applications give

$$
\tau_k^4(e_{i,k}(m))=e_{i,k}(m),
$$

so

$$
\tau_k^4=\operatorname{id}_{\mathfrak T_k}.
$$

The four adjacent presentation constructors are restrictions of one operator:

$$
\tau_k\vert_{\widetilde V_{i,k}}
=e_{i+1,k}e_{i,k}^{-1}.
$$

In particular, the last quarter turn is

$$
\tau_k\vert_{\widetilde V_{4,k}}
=e_{1,k}e_{4,k}^{-1}:
\widetilde V_{4,k}\longrightarrow\widetilde V_{1,k}.
$$

This is reconstruction from the retained common graph followed by the source chart. It is not inversion of the scalar Weil functional.

If every chart carries the topology transported from \(M_k\), then \(\tau_k\) is a homeomorphism because each restriction is a chart transition. Comparison with unanchored product-subspace or regulator topology remains a separate map.

## Source-derived order-four candidate

The bilateral additive-Tate boundary construction already carries a Fourier operator satisfying

$$
\mathcal F_k^4=\operatorname{id}.
$$

For a retained datum \(m\) in that common carrier, define four orbit presentations

$$
D_{i,k}(m)=\mathcal F_k^{i-1}m,
\qquad i=1,2,3,4.
$$

Then the same operator gives every quarter turn:

$$
\mathcal F_kD_{i,k}(m)=D_{i+1,k}(m)
$$

with indices modulo four. In particular,

$$
\mathcal F_kD_{4,k}(m)=D_{1,k}(m).
$$

The four character projectors

$$
P_\lambda=\frac14\sum_{a=0}^3\lambda^{-a}\mathcal F_k^a,
\qquad \lambda\in\{1,-1,i,-i\},
$$

diagonalize this order-four action. This supplies a source-derived candidate for the abstract chart rotation.

## Orbit-to-presentation typing test

The orbit elements \(D_{i,k}(m)\) are vectors in the additive-Tate boundary carrier, whereas the semilocal vertices \(\widetilde V_{i,k}\) are complete presentation objects. They cannot be identified directly. For a Hermitian form \(Q_k\) on the common carrier, the correctly typed orbit presentations would be

$$
\mathcal D_{i,k}(x,y)
=
Q_k(\mathcal F_k^{i-1}x,\mathcal F_k^{i-1}y).
$$

Identification with the semilocal charts requires four natural isometries

$$
\chi_{i,k}:\mathcal D_{i,k}\xRightarrow{\simeq}\widetilde V_{i,k}
$$

intertwining the Fourier action with the adjacent presentation maps. No such four-map interface was located. Even equality of the orbit forms requires the invariance equation

$$
Q_k(\mathcal F_kx,\mathcal F_ky)=Q_k(x,y),
$$

which is established for the boundary Hilbert product by unitarity but not for the completed endpoint--gamma--prime Weil form. Thus \(\mathcal F_k^4=1\) supplies the rotation operator, while the orbit-to-semilocal presentation identification remains the first missing typed interface.

## Port-versus-presentation test

No prior packet identifies the four Fourier ports with the four semilocal vertices. Their types disagree:

- \(P_r,C_{-r},P_{-r},C_r\) are support/character states in one additive distributional boundary carrier;
- \(V_1,V_2,V_3,V_4\) are source, geometric, spectral, and trace presentations of a semilocal functional.

In particular, \(V_4\) is not a conjugate-character line, and \(V_1\) is not a shifted-support comb. Equal cardinality four does not construct an identification.

The source-derived conclusion is therefore a vertical order-four fiber

$$
P_r\longrightarrow C_{-r}\longrightarrow P_{-r}\longrightarrow C_r\longrightarrow P_r
$$

carried by the larger retained boundary graph. Relating this fiber to the semilocal presentation tetrahedron requires a separate functor assigning a Fourier-saturated boundary fiber to each presentation and intertwining the six presentation maps. The notation \(D_1,\ldots,D_4\) should denote these four Fourier ports, not be silently replaced by \(V_1,\ldots,V_4\).

## Projection-square test

Parameterize the retained graph by the complete source datum \(h\) and set

$$
q_1(h)=h,
\quad q_2(h)=U_S(h),
\quad q_3(h)=(\Omega_S^+h,\Omega_S^-h),
\quad q_4(h)=\mathcal O_S(h).
$$

The four adjacent presentation maps on the corresponding essential images are

$$
C_{12}=U_S,
\qquad
C_{23}=q_3C_{21},
\qquad
C_{34}=\mathcal O_SC_{31},
\qquad
C_{41}=\mathcal O_S^{-1}.
$$

Therefore the four projection squares are

$$
q_2=C_{12}q_1,
\quad q_3=C_{23}q_2,
\quad q_4=C_{34}q_3,
\quad q_1=C_{41}q_4.
$$

Each equation follows by substitution and the inverse equations already proved on the observer-generated images. Thus the chart rotation projects to the twelve complete presentation maps, not merely to a relabeling. The first three projected maps are continuous in their declared essential-image topologies. The fourth is continuous in the topology transported from the retained graph; continuity in an independently inherited product-subspace topology remains equivalent to the missing inverse estimate for \(\mathcal O_S\).

## Disposition

The larger retained common graph formally constructs a cyclic chart rotation and fourth-power identity, and the additive-Tate Fourier operator supplies an independent source-derived order-four candidate. The chart projection squares commute by construction on observer-generated images. Identifying that chart rotation with the Fourier operator requires the four orbit-to-presentation isometries \(\chi_{i,k}\); these are not constructed. The fourth chart turn is continuous in transported graph topology, while independent unanchored observer-image continuity still requires an inverse estimate.