# A common minimum repair can be read in either direction

Fix the square and a nonempty family of its legal pentagons. Forced means the same color on every pentagon in that family. There is a common labeled minimum two-link quartet if and only if there exists an eligible forced-blue flank edge uv and the remaining outside triple K satisfies one of the following conditions:

1. An edge in K is forced red.
2. A pair S in K is forced blue, the remaining site in K is adjacent to neither member of the other movable pair, and the fixed site is adjacent to neither u nor v.

For sufficiency use the same-movable-site construction in case 1 and the opposite-site, equal-outside-pair construction in case 2. All labels in the chosen construction depend only on the certificate, not the unresolved cycle.

For necessity read the labels of the common quartet. Its union misses exactly u,v outside the square. They flank a movable pair, pass the clearance test, and must be blue on every cycle. Two rows each have two outside sites. Their outside pairs A,B lie in K and are blue because the rows attach. If A and B differ, these are two of the three pairs of K. Deleting a nonadjacent pair of vertices from a pentagon leaves exactly one red edge. It must be the pair of nonshared endpoints of A and B; its color is therefore forced. If A=B, the repeated pair is forced blue. The single-movable rows must occupy opposite sites (otherwise they coincide). The opposite-site witness requires the fixed site clear of u,v, and the remaining outside site occurs in both double-movable rows, once with each site of the other axis. Separation forces both corresponding path nonadjacencies. This proves the usability conditions, not just the color claim.

The criterion concerns existence of at least one common quartet, not constancy of the count or uniqueness of the common witness. Its two sufficient cases need not be exclusive.

## Why a third pentagon is impossible

Once the red edge inside K is fixed, the fifth site of the path description (the isolated site in K) must join both u and v in red. Each end of the inner red edge needs one more neighbor, so only the two matchings to u and v remain. This settles the forced-red case.

For the repeated blue pair S={s,t}, write K={s,t,a}. The inner red edge is either a–s or a–t. For each choice the other member of S is the common red neighbor of u,v. One required red edge from an end of the inner red edge to u or v fixes the matching completely.

Look just beyond the consecutive block u,x,z,v, with u<v. Each existing exterior neighbor (u−1 or v+1) belongs to K: clearance excludes the fixed site and both members of the other movable pair Y. If such a neighbor is a, its required red link to the adjacent flank fixes the matching for either inner red edge. If the block is interior and neither exterior neighbor is a, those neighbors are s and t. Whichever is on the inner red edge has a required flank link, again fixing the matching. In both cases there are at most two pentagons.

It remains to treat a block at the boundary whose only exterior neighbor belongs to S. Reflect if necessary: the block occupies 1–4 and column 5 belongs to S. All of K, the fixed site, and Y occupy columns 5–10. If a is distance one or two from either s or t, that inner edge is forced red or blue respectively; this fixes which of a–s and a–t is red. There are then at most two matchings. Otherwise a is at least three columns from both. The two members of S cannot lie on opposite sides of a in a six-column block. They are at least two apart (they form a separated row pair of sites). On the same side they therefore span at least six columns together with a. Equality forces S={5,7}, a=10 since column 5 belongs to S. The other labels are 6,8,9, so Y, an adjacent pair, must be 8,9. But a is next to 9 and occurs with each member of Y in one of the double-movable rows. This violates separation. Thus the last possible route to a third cycle is excluded.
