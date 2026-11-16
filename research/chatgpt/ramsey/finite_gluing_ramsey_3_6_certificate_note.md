# Finite gluing certificate for R(3,6) = 18

## Result and scope

An exact rational certificate excludes every five-regular, 18-vertex graph with no triangle and no independent set of six vertices. The certificate uses induced patterns on at most seven vertices, restriction identities, degree identities, and eleven nonnegative mean squares of rooted-pattern counts.

Together with the elementary five-regularity reduction below and the explicitly checked 17-vertex witness, this proves the known value R(3,6)=18. This is a computational reconstruction of a known Ramsey result, not a new Ramsey bound. The five-regularity reduction was supplied; it was not discovered automatically by the optimizer.

## Files and execution

Keep these two files in the same directory:

- `verify_ramsey_overlap_certificate.py`
- `ramsey_3_6_overlap_certificate.json`

Run:

```sh
python -m pip install networkx
python verify_ramsey_overlap_certificate.py
```

The verifier does not use a linear-programming solver, semidefinite-programming solver, or floating-point arithmetic. It recomputes the coefficients from finite colored graphs and checks the final inequality using Python's exact rational arithmetic. It also checks completeness of the small-pattern catalogue by independently enumerating allowed labeled graphs and comparing their count with the sum of their isomorphism-orbit sizes.

This is a programmatically checked combinatorial certificate, not a proof formalized in a proof assistant.

## What is being glued

Choose an ordered triple of root vertices. A witness consists of two additional, unordered vertices together with all edge colors on these five vertices. Vertices may be relabeled only while preserving the three root labels.

For a rational-valued function f on these rooted five-vertex records, put

    Z_f(root) = average of f(root, A) over all two-element witness sets A.

Every actual graph satisfies

    average_root Z_f(root)^2 >= 0.

Multiplication glues two records along their three root vertices. Their additional witness sets can share zero, one, or two vertices. Consequently, the product expands into induced-pattern frequencies on seven, six, and five vertices, respectively. This finite overlap calculation retains witness collisions; it does not use a limit as the graph order tends to infinity.

For n=18, there are 15 non-root vertices and 105 two-element witness sets. For two independent choices A,B of such sets, the probabilities of |A intersection B|=0,1,2 are respectively

    78/105, 26/105, 1/105.

The same collision formula, with n as a parameter, works for every graph order.

## Variables and identities

Let p_H be the probability that a uniformly chosen vertex subset induces the unlabelled graph H. Red edges are present graph edges; white edges are absent edges. Patterns containing a red triangle or a white six-clique are omitted.

The catalogue has:

| Order | Allowed unlabelled patterns |
|---|---:|
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 7 |
| 5 | 14 |
| 6 | 37 |
| 7 | 100 |

There are 164 probability variables in total. They obey nonnegativity, normalization at each order, and exact restriction identities obtained by deleting one uniformly selected vertex.

Five-regularity supplies rooted extension identities. If a root has d neighbors in its k-vertex induced record, it has exactly 5-d neighbors outside that record. Averaging this equality gives linear identities among k- and (k+1)-vertex pattern frequencies. These identities retain the root's orbit within its pattern, not just its unrooted degree sequence.

## Exact contradiction

The JSON supplies 142 rational equality multipliers and 11 nonnegative rational multipliers of squared rooted-pattern expressions. All eleven square expressions use three roots and two witness vertices.

Let S be their weighted sum of mean squares. The exact checker derives coefficients c_H such that

    S + sum_H c_H p_H = B,       B = -1.

At each pattern order k, let m_k be the smallest c_H among patterns of that order. Since the probabilities at each order sum to one, put

    L = sum_k m_k
      = -12278293 / 135475200000000.

Then

    S + sum_H (c_H - m_|H|) p_H = B - L
                               = -1 + 12278293/135475200000000
                               < -1/2.

Every term on the left is nonnegative. This is the exact contradiction. The strict bound is checked using rational arithmetic, not numerical eigenvalue tolerances.

## How the certificate was found

A linear relaxation using only pattern frequencies, restriction identities, and degree identities remained feasible. Mean-square inequalities were added by constructing finite rooted-flag moment matrices. Negative numerical eigenvectors supplied candidate separating squares; their coefficients were rounded to integers and their gluing coefficients computed exactly. A linear dual calculation selected a nonnegative combination.

Floating-point optimization was used only to find the certificate. The delivered verifier reconstructs and proves the final contradiction independently. Its validity does not depend on the search algorithm or optimizer status.

The full initial search generated 139 candidate square cuts. Eleven have nonzero multipliers in the checked certificate.

## Five-regularity reduction

Assume G has 18 vertices, no triangle, and no independent six-set. Use the previously established values R(3,4)=9 and R(3,5)=14.

Every neighborhood is independent, so every degree is at most five. A vertex of degree at most three would leave at least 14 nonneighbors; those contain an independent five-set, which together with the vertex is forbidden. Hence every degree is four or five.

Suppose v has degree four. Its 13 nonneighbors induce a graph H with no triangle and no independent five-set. Each vertex of H has degree at most four in H. Degree at most three in H would leave at least nine nonneighbors in H; these contain an independent four-set, which together with that vertex would be an independent five-set. Thus H is four-regular.

Choose t in N(v). It has at least three neighbors h1,h2,h3 in H: its degree in G is at least four, one neighbor is v, and it cannot be adjacent to any other member of N(v). Each hi has four neighbors in H and already has the additional neighbor t, so it has no neighbors in N(v) other than t. The three hi are mutually nonadjacent, since they are neighbors of t in a triangle-free graph.

Therefore {h1,h2,h3} together with N(v) minus {t} is an independent six-set. This contradiction excludes degree four. Every degree is five.

This is the familiar structural reduction; no uniqueness classification of the 13-vertex graph is needed for the argument above.

## Lower-bound witness

The checker decodes the following 17-vertex graph6 string:

    P??GaOo`XMGsIcT?pSLaGuA?

It verifies all triples and all six-element vertex subsets. There is no red triangle and no white six-clique. Its 41 red edges therefore establish R(3,6)>17.

## What this does and does not establish

This demonstrates an actual obstruction-producing use of the retained-overlap algebra. The multiplication rule, finite collision corrections, and positivity are fixed independently of the desired threshold. The target forbidden patterns and graph order enter as inputs.

It does not establish a short formula for Ramsey numbers, a fixed overlap depth that suffices for every pair (r,s), or any new bound for R(3,18). Nor does it derive the supplied five-regularity reduction automatically.

The relevant general mathematical framework is finite flag-algebra/moment positivity, not merely the spectrum of a single adjacency or transport operator.

## Primary references

David Cariolaro, “On the Ramsey number R(3,6),” Australasian Journal of Combinatorics 37 (2007), 301–304. In particular, Claim 1 gives the five-regularity reduction.
https://ajc.maths.uq.edu.au/pdf/37/ajc_v37_p301.pdf

Bernard Lidický and Florian Pfender, “Semidefinite Programming and Ramsey Numbers,” arXiv:1704.03592. This develops the use of flag-algebra methods for finite Ramsey problems.
https://arxiv.org/abs/1704.03592

Brendan McKay's catalogue of (3,6)-Ramsey graphs on 17 vertices supplies the graph6 witness used in the previous stages of this investigation.
https://users.cecs.anu.edu.au/~bdm/data/r36_17.g6
