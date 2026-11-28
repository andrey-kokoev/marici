# Why one installed repair leaves a branch, while a blue pair fixes it

Use square 258,259,358,359. Reflection covers the second square. On the two pentagons under comparison the red links common to both include 1–4,6–7,6–10. The remaining red links match 1 and 4 to 7 and 10. Thus 1–4 cannot be a missed blue flank. Only 7–10 can be missed, and the remaining outside triple is {1,4,6} with red inner edge 1–4.

For i in {8,9} let i' denote the other site. By the flanked-edge construction, a single-movable row uses 6 and one of {1,4}. Its matched double-movable partner uses the other outside endpoint and the opposite site i'. Its site from {2,3} is forced by separation: 1 forbids 2, and 4 forbids 3. Hence the possible matched pairs are

- L_i: {4,6,i} linked to {1,3,i'};
- R_i: {1,6,i} linked to {2,4,i'}.

No equal-outside-pair construction is possible: its repeated double-movable outside endpoint would have to avoid both 2 and 3. Thus one needs one L and one R. The same-site quartets L_i + R_i work on either cycle. For opposite sites, L_i + R_j with j=i' requires 4 red to the flank next to j and 1 red to the flank next to i, by the opposite-site construction. Each cycle admits exactly one of these two assignments.

The four matched pairs have no row in common. A blue pair of installed rows in a common quartet L_i + R_i therefore fixes both L_i and R_i, even without using the observed blue color. The only completion is the original. A red pair fixes just one of the two indices. Keep it; try the single-movable row of the other pair on the opposite site. On one cycle the opposite-site construction succeeds; on rejection the same-site construction is still available.

The third row itself detects the matching, not just failure of the eventual fourth. For instance, after L_i try {1,6,j}, j=i'. It shares j with the installed {1,3,j}. Both ports are blue to the two square ports through j. Those four ports can join site i, outside site 4, and the flank endpoint next to j if the latter is blue to 4: the three sites are mutually blue, and all four ports miss them. This seven forbids the probe regardless of the chosen new links. If the flank endpoint is red to 4, the opposite-site construction already gives a full legal quartet containing the probe. For a retained R_i exchange the roles of 1 and 4 (using the corresponding forced movable partners).
