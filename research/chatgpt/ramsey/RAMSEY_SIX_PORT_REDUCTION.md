# Conditional six-port reduction for R(3,7)

## Input and scope

Let G be triangle-free on 23 vertices with independence number at most 6, assumed only for contradiction. The exact Ramsey value R(3,7)=23 is already known; the purpose is to isolate a direct, reproducible incidence obstruction, not to assert a new value.

External numerical inputs (published and independently checkable):

- R(3,6)=18; the seven admissible 17-vertex (3,6) graphs have 40, 41, 40, 41, 40, 42, 42 edges.
- e(3,6,16)=32, e(3,6,17)=40.
- e(3,5,10)=10, e(3,5,11)=15, e(3,5,12)=20, e(3,5,13)=26.

See https://arxiv.org/html/1210.5826, Table 3 and https://users.cecs.anu.edu.au/~bdm/data/ramsey.html.

## I. Regularity

For every vertex v, 5 <= deg_G(v) <= 6. Lower bound: G-N[v] has independence at most 5, so order at most 17. Upper bound: N(v) is independent. Put r=#{v:deg(v)=5}. The degree sum gives e(G)=69-r/2.

For degree-5 v, G-N[v] has 17 vertices and at least 40 edges. Since N(v) is independent, e(G)=e(G-N[v])+sum_{u in N(v)}deg(u). Put r_v=#{u in N(v):deg(u)=5}; then 69-r/2 >= 40 + (30-r_v), so r_v >= r/2+1. If r>0, the induced graph on the r degree-5 vertices would have minimum degree >r/2, contradicting Mantel's theorem. Hence r=0, and G would be 6-regular.

## II. 16-vertex core

For any v, A=N(v) has 6 independent vertices; B=V(G)-N[v] has 16. Since G is 6-regular, e(G)=69 and e(G[B])=69-6^2=33. Put H=G[B] and P_b=N(b) cap A. Every a in A occurs in exactly five P_b, every b satisfies deg_H(b)+|P_b|=6. Each port fiber Q_a={b:a in P_b} is independent of size five. Every independent T in H must touch at least |T| of these six fibers (Hall condition). Thus the remaining obstruction is existence of a 16-vertex (3,6) graph H of size 33 with a six-fiber incidence design satisfying these conditions.

## III. Singleton contraction

The total port incidence is 6*5=30. If s vertices have singleton ports, 30 >= s+2(16-s), giving s>=2. The singleton ports are necessarily distinct: two vertices with the same singleton label cannot be red-adjacent (triangle with the corresponding a), and then their independent pair would violate Hall.

Choose b with P_b={a}. Removing N_G[b] from G retains v and A' = A-{a}; its external part is B' = B-(N_H(b) union {b}). Since G is 6-regular, |B'|=10 and the resulting graph has 16 vertices and alpha exactly 5. The new port labels are P'_c=P_c-{a}, and for each independent T subset B', T union {b} is independent in B, proving |union P'_c|>=|T|. Also alpha(B')<=4. Hence the reduced five-port system is admissible.

## IV. Four ports are impossible

By R(3,5)=14 and alpha(H)<=5, every b in H has deg_H(b)>=2, hence |P_b|<=4. If |P_b|=4, then deg_H(b)=2; let c,d be its two neighbors in H. Their ports are disjoint from the four ports of b, so deg_H(c),deg_H(d)>=4. Since H-N_H[b] has 13 vertices, triangle-free with alpha<=4, it has at least 26 edges. Consequently 33=e(H-N_H[b])+deg_H(c)+deg_H(d)>=26+8=34, impossible. Thus |P_b| is 1, 2, or 3.

For h=#{b:|P_b|=3}, necessarily

    #{p=1}=2+h,  #{p=2}=14-2h,  #{p=3}=h,

with 0<=h<=4.

## V. Parity forces a triple-port contact

For v in G, a nonneighbor b has mu(v,b)=|P_b| common red neighbors with v. Since G has no independent seven-set, mu(v,b)>=1. If mu(v,b)<=2 for every nonadjacent pair, then each v has exactly two nonneighbors with mu=1 and fourteen with mu=2, by sum_b mu(v,b)=6*5=30. Each vertex v would then lie in precisely fourteen (not necessarily induced) red 4-cycles. Summing over 23 vertices would give 23*14/4 cycles, not an integer. Thus some nonadjacent pair has at least three common neighbors. Section IV rules out four or more; therefore some vertex v has h>=1, hence at least three singleton-port external vertices.

Among any three singleton-port external vertices, at least two are red-nonadjacent (triangle-free). Their singleton labels are distinct, and their independent pair has tight Hall coverage of two ports. This forces a genuine two-set tight composition in the canonical blue simplex complex.

## VI. Neighborhood redundancy

For b with p=|P_b|<=3, its neighborhood N_H(b) is independent of size 6-p. Because all its ports lie in the complement of P_b and Hall requires at least 6-p covered labels, their union is exactly [6]-P_b. Let S_b=sum_{c in N_H(b)}(|P_c|-1). By deleting N_H[b] from the 33-edge graph H, the remaining graph has 9+p vertices, independence at most 4, and

    e(H-N_H[b])=5*p+3+S_b.

The exact lower bounds e(3,5,10)=10, e(3,5,11)=15 and e(3,5,12)=20 give S_b>=2 for p=1,2,3. In particular there are at least two redundant incidence contacts among ports of the independent neighbors of b. These appear as (at least two) 4-cycle incidences through b with an opposite port vertex.

## VII. What is unproved

The statements above are necessary for any hypothetical 23-vertex (3,7) graph. They do **not** prove the final impossibility of the 6-regular case. The remaining target is to rule out a six-fiber design on a 16-vertex 33-edge (3,6) core with a degree-3 vertex (equivalently a triple-port b). The obstruction must use Hall compatibility beyond the edge counts and parity already established.

## VIII. Verification

Run `python ramsey_six_port_reduction.py` with `r37_22.g6` in the same directory. It checks the seven 17-vertex critical graphs, confirms the numerical algebra for the conditional core, and checks 15,364 exact singleton contractions across the 191 existing 22-vertex critical (3,7) graphs. These checks validate the formulas and the contraction on known graphs, not the existence of a 23-vertex graph.
