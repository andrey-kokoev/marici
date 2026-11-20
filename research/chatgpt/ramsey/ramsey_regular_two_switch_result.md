# Regular witnesses are not connected by valid two-edge switches

Move: remove disjoint red edges ab,cd and add either ac,bd or ad,bc, requiring added edges absent. Retain only triangle-free graphs with no independent seven. This preserves all degrees. Both orientations of every candidate pair were checked for each of ten regular catalogue representatives. Valid outputs were identified by exact backtracking isomorphism; each saved mapping is checked on every vertex pair.

Results: 21,918 legal switches, 685 triangle-free outcomes, 22 valid outcomes (counts are oriented local moves from representatives, not distinct graph classes). The unlabelled transition components are:
- {182,183,184,185,186}
- {187,188}
- {189}
- {190}
- {191}

Records 190 and 191, the two Hall-center types, have **zero valid switches**, including switches to their own isomorphism type. Their isolation does not depend on catalogue exhaustiveness: every local candidate was explicitly ruled out before classification. Thus neither can initiate any path of valid two-edge switches, even if other catalogue records were missing. Record 189 is also locally frozen.

Interpretation: pair signatures are not simply a convenient starting point from which all regular witnesses can be reached via this smallest regularity-preserving move. Some non-Hall witnesses are mutually deformable, but the Hall types are locally rigid at this move size. This does not prove rigidity under larger simultaneous switches, transitions through nonregular graphs, or other state spaces.

Files: ramsey_regular_two_switch.py; ramsey_regular_two_switch.json (counts, concrete removed/added edges, exact target isomorphisms). Next discriminator: determine the minimum simultaneous degree-preserving edge exchange that leaves each Hall type, especially whether a three-edge move suffices or a four-edge move is required. Distinguish preserving a particular Hall center from permitting the root structure to change.
