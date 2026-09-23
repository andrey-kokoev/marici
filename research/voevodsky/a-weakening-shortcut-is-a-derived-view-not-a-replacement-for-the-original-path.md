# A weakening shortcut is a derived view, not a replacement for the original path

Fresh `check_nondestructive_weakening_shortcut.py` models a FICTIONAL two-edge weakening audit chain x<=1 -> x<=2 -> x<=3. A validated arithmetic shortcut x<=1 -> x<=3 adds a separate DERIVED VIEW referencing the original chain digest and all three occurrence IDs, marked `observed_direct_edge=False`. The chain, middle event, both old edges and old digest remain unchanged. Changing the middle bound to 4 invalidates replay, and the prior shortcut's source-path digest no longer matches.

The fixture is neither an observed audit log nor a grant to mutate graph history. A shortcut cannot erase historical occurrences just because endpoint mathematics composes. All issuer, publication and analytic S,A,R,C,G role questions remain open.

Next test a BRANCHING audit path with two distinct intermediate weakening occurrences giving identical x<=3 endpoints: a derived shortcut must specify WHICH validated path it compresses by path digest; endpoint pair alone cannot select an audit trail.
