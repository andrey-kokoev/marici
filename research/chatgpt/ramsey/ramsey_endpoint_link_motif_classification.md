# Fourteen endpoint-link motifs reduce to five kernel families

ramsey_single_link_motifs.py classifies ALL160 endpoint links of Hall191's80 candidate switches by exact graph isomorphism. There are14 types. Their independent-five families have57 representative sets total; transporting these through the checked isomorphisms reproduces all550 singleton defect occurrences exactly. An arbitrary choice of isomorphism is harmless because the whole independent-set family, not one preferred set, is transported.

After stripping trees and suppressing degree-two paths, ramsey_link_kernel_classification.py verifies five structural families:
- forests (2 motif types);
- a pentagon with attached trees or separate tree components (6 types);
- three internally disjoint paths between two branch vertices (3 types; path lengths2,2,3 or2,3,3);
- four such parallel paths (1 type; lengths2,2,3,3);
- subdivided K4 (2 types, with six recorded path lengths).
Every cyclic kernel has at most four branch vertices. Tree attachments and subdivisions distinguish the14 exact graphs. This is a classification for this Hall source, not a theorem for every regular witness's links.

Three especially transparent independent-five counts:
1. A pentagon with one leaf attached at each vertex has11 independent five-sets. Choose exactly one endpoint from each of the five leaf edges; the selected cycle vertices must form an independent subset of C5. There are1+5+5=11 choices.
2. A four-arm star with every edge subdivided once has ONE independent five-set: its center plus its four outer leaves. Omitting the center leaves four disjoint arm edges and allows at most four choices.
3. C5 disjoint union two isolated edges has NO independent five-set, since its independence number is2+1+1=4.

This already derives an important switch family's defect count without enumerating sevens. The one-defect family B (old cyclic orbit6), represented by removing(1,7),(14,15) and adding(1,14),(7,15), has precisely links2 and3 above. The first link gives its unique residue{4,5,16,17,18}, hence unique seven{1,4,5,7,16,17,18}; the second gives none. C5 transport derives the corresponding result for all five phases.

Thus the earlier one-defect repair orbit is now explained by a subdivided-star/pentagon obstruction pair, rather than only measured from switched outputs. The more complicated families still require tracking independent residues through their small kernels and preserving their actual vertex embedding to determine which helpers repair them. Unlabelled motif type/count alone cannot select compatible phases.

Files: ramsey_single_link_motifs.py/JSON (14 representatives,57 residue templates,160 embedding isomorphisms); ramsey_link_kernel_classification.py/JSON (cores, branch paths, family checks). Next derive the six-defect partner family's embedded residues and its phase-locking repair relation from these kernel motifs, completing a structural account of the simplest cooperative pair.
