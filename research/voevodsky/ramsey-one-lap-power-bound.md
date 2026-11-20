# Sharp repetition bound for a one-lap monotone bridge reader

Fix k≥3 labelled terminals on a circle. A mask gives the terminal positions permitted at one inner site. In one orientation and phase a site may advance h=0,...,k−1 edges through permitted terminals. Neighboring sites meet at a common permitted terminal. Accept a closed trace advancing exactly k edges. One may take the union over orientations and phases. We compare existence, not path counts.

**Claim.** In arbitrary prefix and suffix contexts, x repeated k times and x repeated k+1 times have the same verdict. The uniform exponent k cannot be decreased.

Deletion: across k+1 copies there are at most k advances. Remove an idle copy. The bridge at its ends is identical and still connects.

Insertion: given a witness on k copies, duplicate an idle copy if one exists. Otherwise all k copies advance exactly once, with consecutive starting terminals all the way around. Relabel the oriented circle j→j+1. The same word x thus supports every one-edge transfer j→j+1. Some terminal is allowed throughout x: otherwise define t_j to be the first site in x forbidding j. In a one-step traversal j→j+1, all sites forbidding j+1 must precede the advance, and all sites forbidding j must follow it. Thus t_(j+1)<t_j for every j, impossible around a circle. Insert an idle copy at that universally allowed terminal, which occurs at a copy boundary. The argument works within the selected orientation and phase and leaves the external context unchanged.

Sharpness: use a block that forbids each terminal once, in descending order k−1,...,0, with a full mask after each such exclusion. Append one extra full mask as suffix; the complementary phase cannot accept it. In k−1 blocks, advance from j to j+1 in block j+1 (j=0,...,k−2), on a full mask between the exclusions of j+1 and j. Close from k−1 to 0 on the suffix. With k blocks, no block can idle because every terminal is excluded somewhere. Each would have to advance exactly once, which by the insertion argument requires a universally allowed terminal, in either orientation. Hence rejection. The suffix distinguishes x^(k−1) from x^k, proving sharpness.

This is a finite transport-language theorem, not a Ramsey threshold statement. The independent reader test `checkers/ramsey_one_lap_power_bound.py` verifies the sharpness family for k=3..12.
