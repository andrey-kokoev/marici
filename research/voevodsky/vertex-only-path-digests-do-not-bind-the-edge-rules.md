# Vertex-only path digests do not bind the edge rules

Fresh `check_path_digest_edge_binding.py` compares synthetic paths with the same ordered source/middle/end occurrences but different edge labels: two weakening edges versus one comparison followed by weakening. Hashing only the vertices produces the same commitment; hashing the versioned ordered typed-edge sequence distinguishes them. A two-weakening replay rejects the comparison-labelled edge. This is a nonredundant successor to branching path selection: selecting occurrence IDs alone does not certify the inference rules used on the path.

These are synthetic graph fixtures, not signed observed events or owner-issued Farkas rows. No authorized row issuer/recipient is identified; no analytic S,A,R,C,G correspondence is licensed. Next examine whether path commitments also bind source-row manifest digest and exact target at EACH edge so identical typed edges on a changed source cannot replay.
