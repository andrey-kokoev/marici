# Two permitted pairings would already fail a pair test

Assume four distinct, individually legal row ports on the width-ten square and pentagon. If two different pairings repair the graph, their union is a four-cycle of permitted links. Opposite ports on that cycle stay blue in both pairings. We show that some opposite pair alone then makes a blue seven with old vertices.

A legal row avoids the fixed site and uses one or two movable sites. If a row A on the cycle uses one movable site, the two square ports missing A are red to port A. Its two cycle neighbors B and C are disjoint from A's support. Because links AB and AC are permitted, neither B nor C is red to either square port. The three support sites of A and the two square ports are mutually blue and blue to both B and C. Thus B,C fail as a blue pair. This argument uses permission, not simultaneous activation of AB and AC.

Otherwise all four rows use two movable sites: one from each adjacent pair. Record the two choices as bits. A permitted link requires disjoint supports, so moving along an edge of the four-cycle flips both bits. Opposite rows consequently have the same two movable sites. They meet the same three square rows. They also miss at least three outside sites between them, since each row has just one outside site. Two of those missed sites are blue to each other (the red pentagon has no triangle). These two sites and the three square ports give a blue five common to the opposite ports. Again the pair fails.

Therefore two pairings cannot both work. Combined with the disjoint-endpoint result, any four-port attachment that needs exactly two links has one minimum repair. This does not assert that a four-cycle of permitted links is impossible before pair tests, nor that every attachment has a repair.
