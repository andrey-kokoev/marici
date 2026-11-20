# Affine matching and triangle-free output

Normalize the nonzero generator step to a. For each finite label z, look at partitions in which the hub is paired with z. Exactly three partitions remain: the three pairings of the other four labels.

The formula produces them from three selected duads:
- selected {hub,z}: remaining coordinate offsets {1,3}|{2,4};
- selected {z-2a,z-a}: remaining offsets {1,2}|{3,4};
- selected {z-a,z+a}: remaining offsets {1,4}|{2,3}.
All offsets are relative to z and measured in units of a modulo five. These are distinct and exhaust the three partitions. There are five values of z. The fifteen selected duads also exhaust all duads (five hub pairs and two five-element finite-pair orbits). Thus the assignment is a bijective incident pair-partition matching.

For any such perfect matching, construct the 22-vertex red graph with root *, six label vertices, and fifteen duad vertices. Root-label edges and label-containing-duad edges are red. Start with red edges between disjoint duads; at each partition, delete the edge joining its two unselected duads.

A red triangle cannot contain the root, since its label neighbors are independent. A triangle containing a label would require two disjoint duads both containing that label, impossible. A triangle of duads is exactly a partition of the six labels, and its prescribed deletion breaks that triangle. Each disjoint-duad edge belongs to one partition, so deletions cannot be ambiguous.

Every duad appears in three partitions. It is selected in exactly one; in each of the other two, one incident duad edge is deleted. Its degree is therefore 2+(6-2)=6. Each label has degree 1+5=6, and the root degree is 6. The graph is 6-regular on 22 vertices, hence has 66 red edges. This proves bijectivity, incidence, triangle-freeness and regularity without a graph census. Excluding independent sevens requires a further argument.
