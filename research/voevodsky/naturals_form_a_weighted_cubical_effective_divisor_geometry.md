# Naturals form a weighted cubical effective-divisor geometry

## Question

What geometric object contains primes as sites, natural numbers as points, adjacent-prime replacements as directions, and the observed Boolean cubes as genuine cells?

## Claim boundary

Unique factorization identifies positive integers with finite effective divisors on the ordered set of primes. Adjacent-prime replacement defines a cubical state complex inside each fixed-degree divisor sector. Multiplication supplies a commutative monoidal operation between sectors, and prime magnitude supplies an edge-height filtration. This constructs source-derived cube fillers from commuting divisor moves; it does not assign physical spatial meaning to the complex.

## Naturals as effective prime divisors

Let \(P\) be the prime-index path with vertices \(1,2,3,\ldots\), where vertex \(i\) represents \(p_i\). Define

\[
D(N)=\sum_i\nu_{p_i}(N)[i].
\]

Unique factorization gives a bijection

\[
\mathbb N_{>0}\cong
\operatorname{Div}_{\mathrm{eff}}(P),
\]

and multiplication becomes divisor addition:

\[
D(MN)=D(M)+D(N).
\]

The degree is

\[
\deg D(N)=\sum_i\nu_{p_i}(N)=\Omega(N).
\]

Hence adjacent-prime moves preserve \(\Omega\), and the route graph decomposes into fixed-degree sectors.

## Root moves

The shell-\(i\) edge

\[
k p_i\longrightarrow k p_{i+1}
\]

becomes

\[
D\longmapsto D+\alpha_i,
\qquad
\alpha_i=[i+1]-[i],
\]

whenever the coefficient of \([i]\) in \(D\) is positive. This is one chip move along the prime-index path.

For a finite set \(I\) of distinct shell directions and a divisor \(D\), suppose

\[
D+\sum_{i\in S}\alpha_i
\]

is effective for every \(S\subseteq I\). The resulting \(2^{|I|}\) divisors form a Boolean cube. Its square faces commute because divisor addition is commutative:

\[
(D+\alpha_i)+\alpha_j
=(D+\alpha_j)+\alpha_i.
\]

This supplies an independently defined cubical filler, rather than only observing its boundary in the edge complex.

## Relation to symmetric powers

The degree-\(d\) sector is the set of effective divisors of degree \(d\), equivalently the discrete symmetric power

\[
\operatorname{Sym}^d(P).
\]

Enhancing every jointly admissible set of distinct chip moves to a cube gives a cubical effective-divisor state complex \(X_d(P)\). Its vertices are degree-\(d\) naturals, its edges are adjacent-prime replacements, and its higher cells encode independent commuting replacements.

The disjoint union

\[
X(P)=\coprod_{d\geq0}X_d(P)
\]

is commutative monoidal under divisor addition. On vertices this is ordinary multiplication of natural numbers. Products of cubical chains increase cubical degree, matching the earlier conclusion that two blind one-directions naturally produce a two-dimensional class rather than another edge route.

## Arithmetic filtration

If an edge has source \(N=k p_i\), its admission grade is

\[
g(N,i)=k p_i p_{i+1}=N p_{i+1}.
\]

In height notation,

\[
\log g(N,i)=\ell_p(D(N))+\ell_p([i+1]).
\]

A cube enters the filtered complex when every one of its edges is admitted; its filtration grade is the maximum edge grade. The canonical \(n\)-cube begins in degree \(n\) with one chip at each of the first \(n\) prime sites, and its maximal edge recovers \(L_n\).

## Geometric synthesis

The emerging object has four layers:

- effective-divisor points encode natural numbers;
- the type-\(A\) root metric encodes overlap of adjacent chip moves;
- cubical cells encode commuting families of moves;
- arithmetic height filters those cells by multiplicative cost.

Character probes add an apparatus-conditioned Hankel metric on the shell-direction space. Probe blindness means that a cubically realized direction or higher volume lies in the radical of that metric.

## Strongest falsification attempt

For all arithmetic edges through a finite cutoff, factor source and target and verify that their divisor difference is exactly one simple root and that degree is preserved. Exhaustively test multiplication-to-divisor addition on a bounded product domain. Enumerate admissible shell subsets through dimension five, verify every subset vertex is effective and every square commutes, and compare maximum edge cost with direct arithmetic grade enumeration.

## Disposition

The relationship between primes, naturals, and cubes is an effective-divisor state geometry on the prime-index path. It upgrades the current edge graph to a source-defined higher-dimensional cubical complex and gives the Clifford exterior degrees a matching cubical-chain interpretation.
