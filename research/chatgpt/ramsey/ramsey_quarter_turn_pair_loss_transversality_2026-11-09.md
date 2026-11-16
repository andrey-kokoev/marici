# Quarter-turn incidence, pair-loss, and transverse projection: a Ramsey-generator obstruction

Date: 2026-11-09.  Status: exact matrix identities, a finite regression, and a general counterexample; no new Ramsey lower bound.

## Source being tested

Samuel Harris, Zion Hefty, Paul Horn, Dylan King, Florian Pfender, *A short proof that R(3,k) = Theta(k^2/log k)*, arXiv:2609.01782v1 (September 2026), especially Section 2 and Lemma 3.2 in Section 3. The paper constructs two random coordinate layers, overlays them, deletes edges from triangles, and establishes with high probability for all candidate sets I of size K=10pn:

    sum_{x in V_R disjoint_union V_B} binom(|X_x intersect I|, 2)
        < (1/20 + 5 eps) K^2.

The computation below asks whether the *deterministic quarter-turn-equivariant* two-layer model from `ramsey_two_bite_equivariant_matrix.py` admits an analogous bound. All adjacency and pair-loss quantities refer to the initial source layers, before mixed-triangle deletion, as in the paper's lemma.

## Exact matrix identity

Let two source graphs have adjacency matrices A_R and A_B of order m. Each final vertex v has coordinates pi_R(v), pi_B(v). For a K-set I of final vertices, define occupancy vectors

    r[a] = |{v in I : pi_R(v)=a}|,  b[a] = |{v in I : pi_B(v)=a}|.

The source-neighborhood intersection counts are A_R r and A_B b. Therefore, **for every source and every projection map**, with no probability or symmetry assumption,

    L(I) = sum_x binom((A_R r)[x], 2) + sum_y binom((A_B b)[y], 2)
         = 1/2 ( ||A_R r||^2 + ||A_B b||^2
                 - 1^T A_R r - 1^T A_B b ).

If both sources are d-regular, K=sum(r)=sum(b), r_0=r-(K/m)1 and b_0=b-(K/m)1, then

    L(I) = (d^2/m) K^2 - dK
           + 1/2 ( ||A_R r_0||^2 + ||A_B b_0||^2 ).              (1)

This exact mode decomposition separates the forced uniform-mode contribution from the nonuniform incidence concentration. Rotation can permute these modes but does not by itself bound their sizes.

In particular,

    L(I) >= (d^2/m) K^2 - dK.                                   (2)

For the original m=13, d=2, equation (2) becomes L(I)>=4K^2/13-2K. For every integer K>=8, this exceeds (1/20+5/1000)K^2. Hence no 13-coordinate, two-degree-2-layer overlay can satisfy the paper's pair-loss bound at any such K, regardless of the coordinate embedding or phase selection.

This comparison concerns the paper's pair-loss *certificate*, not a theorem that the finite overlay is Ramsey-inadmissible. In particular, the asymptotic K=10 sqrt(n log n) of the paper is greater than n when n=65.

## A general quarter-turn-equivariant counterexample

Suppose m has a unit u satisfying u^2=-1 mod m (e.g. m=101, u=10). Let D be a symmetric d-element subset of Z/mZ, defining the red circulant source; let uD define the blue source. Optionally choose D so that both sources are triangle-free; this is possible for large m by choosing a sparse symmetric subset of (m/3,m/2) modulo m.

For any positive integer s, build the final vertex set

    V = {(a,t): a in Z/mZ, 1<=t<=s}

with *identical* two projections pi_R(a,t)=pi_B(a,t)=a. The map tau(a,t)=(ua,t) has order four, tau^2(a,t)=(-a,t), and exchanges the two source edge layers exactly. Every coordinate fiber in either layer has size s.

Assume m >= 10d. Choose any U of 10d coordinate values and I=U x {1,...,s}, so K=10ds. Each of the two source layers counts every pair of vertices within one occupied fiber in exactly d neighborhoods, hence

    L(I) >= 2*(10d)*d*binom(s,2)
         = K*d*(s-1),
    L(I)/K^2 >= (s-1)/(10s).                                      (3)

For s>=3, this lower bound is at least 1/15, greater than 1/20+5/1000. Thus **quarter-turn symmetry, triangle-free source layers, and perfectly balanced fibers do not imply the paper's pair-loss bound**, even with a growing source-coordinate system. The missing property is how the two coordinate partitions are *transverse* to one another; in this counterexample they coincide.

A numerical exact test at m=101, u=10, d=2, s=6, |U|=20 gives K=120:

    L_R=1248, L_B=600, L=1848, L/K^2=0.1283333333,
    same-fiber lower bound ratio=1/12=0.0833333333,
    1/20 target=0.05.

The finite example is illustrative; inequality (3) is the all-scale theorem.

## Decomposing what must be controlled

For an undirected d-regular source, (A^2)[a,b] is the number of common source neighbors of positions a,b. Expanding the pair-loss gives

    L(I) = d W_pi(I) + E_pi(I),

where

    W_pi(I) = sum_a binom(r[a],2) + sum_b binom(b[b],2)

is the total number of same-coordinate vertex pairs across both projections, and

    E_pi(I) = sum_{v<w in I, pi_R(v)!=pi_R(w)} (A_R^2)[pi_R(v),pi_R(w)]
            + sum_{v<w in I, pi_B(v)!=pi_B(w)} (A_B^2)[pi_B(v),pi_B(w)]

is the distinct-coordinate overlap correction. Both terms are nonnegative. The paper's pair-loss lemma therefore demands, at a minimum,

    d W_pi(I) < (1/20+5 eps)K^2  for every K-set I,

and a small enough E_pi(I) to leave room for the full bound.

At the paper's natural scaling K=10ds, a set I that saturates 10d whole *red* fibers already contributes approximately K^2/20 through the red layer alone. This explains why the coefficient 1/20 appears: it is the cost of one fully concentrated coordinate layer. The second layer must not become equally concentrated on that same I. Rotation-equivariance alone does not enforce this.

For the 65-vertex quarter-turn construction with coordinate-difference set T={0,1,5,8,12}, direct exact integer optimization found a 16-element independent set with:

    L_R=60, L_B=52, L=112, L/K^2=0.4375.

The universal mode bound is 4*16^2/13-2*16=46.769..., hence L>=47 by integrality. This gives both a global impossibility bound for the source representation and an explicit stress-test witness.

## Implications for the symmetry-generator hypothesis

The first part of the mechanism survives unchanged:

    source circulants --(quarter-turn exchanges layers)--> overlay
       --(equivariant mixed-triangle deletion)--> triangle-free graph.

But the paper's high-probability independent-set argument cannot be imported from phase symmetry alone. It depends on transversality of the *two coordinate embeddings* and on small neighborhood-overlap losses for all candidate sets. A fixed 13-position carrier also cannot support a growing-coordinate asymptotic family; its uniform spectral mode already blocks the desired pair-loss certificate.

**Next discriminating construction:** grow m and d; choose m admitting an order-four multiplier u, a low-codegree triangle-free circulant source D of degree d roughly sqrt(m/log m), and an injective sparse bipartite coordinate-incidence set V subset Z_m x Z_m invariant under tau(a,b)=(u b,u a). Test the exact worst-case ratio max_{|I|=K} L(I)/K^2, rather than only independence numbers after deletion, against 1/20+5 eps. Crucially, test sets concentrated on coordinate fibers; sampling random I misses the difficult cases.

This identifies a precise missing primitive: **symmetry-compatible transverse coordinate incidence**. Its existence with the paper's full uniform overlap bounds is open in our current deterministic construction.

## Reproduction

    python /mnt/data/check_ramsey_pair_loss.py

The script imports the previous two-layer constructor, verifies the finite maximum independent set by integer optimization, checks the matrix trace identity, and gives the 101-coordinate diagonal counterexample. No asymptotic or exact Ramsey-number assertion depends on numerical optimization.
