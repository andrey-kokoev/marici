# Extension turn2: presentation roles, graph rank and retained orientation

## Fresh-state question

Read the56-node mutable net after the finite packet candidate. The next open task is `rung-grading-and-orientation`: compare both endpoint quotients with the confirmed diagram, retain histories, and either supply a grade law or explicitly keep role labels without claiming an intrinsic grade.

## Typed count/grade/role table

The actual diagram is

    12 --9--> 6
    11 --8--> 5
    10 --7--> 4

with downward source/target presentation changes on each side. Its six vertices are OBJECT presentations;9,8,7 are TRANSPORT views. The numbers must not be converted into nine serial state vertices.

| Index or quantity | Type and meaning | Actual change |
|---|---|---|
| 12,11,10 | left object presentations: labelled, source-indexed, target-indexed | vertical reindexing retains/reconstructs every row |
| 9,8,7 | the same horizontal action in three presentation interfaces | conjugate by indexing/recovery; not extra object stages |
| 6,5,4 | right object presentations at the same three levels | retain policy-dependent grouped rows and their original members |
| numerical rung label | displayed role label | -1 on object vertical edges, -6 on horizontal edges; not unit rank |
| finite graph rank | rho(c,r)=3-c-r, c=0,1 and r=0,1,2 | -1 on each of the seven object edges |
| arrow-source row count | twelve oriented comparisons | unchanged by retained-total indexing |
| source/target quotient count | four blocks of three | quotient forgets two alternatives beyond each endpoint; dependent total does not |
| retained one-edge word | directed source arrow | unchanged by indexing; reversal explicitly changes it |
| actual137-source leaf count/mass | fixture leaves and inherited weights | retained137 under either horizontal policy |
| top-level result row count | grouping-dependent observation/presentation | inherited32, common1; not the numeral6 or4 |

The graph rank is a legitimate grade of this finite directed OBJECT diagram. It is neither realization dimension nor a common grading of every numeral12 through4. Transport labels do not enter that rank's domain. Supplying a finer internal action can refine the graph, but it must declare additional typed stages rather than infer them from the integers.

## Both four-block quotient maps and orientation

On the actual twelve-arrow source, s(i,j)=i and t(i,j)=j are distinct S4-equivariant four-block maps. Each has three-member fibers, but neither factors through the other: the three arrows at a fixed source have three distinct targets, and conversely. The joint endpoint map(s,t) is injective.

The explicit reversal R(i,j)=(j,i) intertwines them: sR=t, tR=s, R²=id. It is NOT the identity on the retained arrow or word. All24 simultaneous vertex relabellings respect these laws. Equivariance therefore does not select one endpoint quotient over the other.

There are also two exact obstructions to reading intrinsic descent off this carrier:

- the diagonal S4 action is transitive, so any S4-invariant scalar on the twelve arrows is constant;
- every directed edge has its reverse, so no endpoint grade can strictly decrease along every arrow (it would require both g(i)>g(j) and g(j)>g(i)).

These are scoped mathematical obstructions, not a prohibition on a grade supplied by additional context, chosen orientation or an independent realization law.

## Routes and history

The object diagram has three full routes from12 to4: HVV, VHV and VVH. Each has three edges and numerical label drop8, with graph-rank drop3. This is not the older label/source/target recurrence with eight reindexing transitions. That recurrence remains a separately retained construction.

The checker executes all three routes using the existing incoming-family action for each actual inherited/common policy. Their final retained rows and137 leaves agree within each policy; their operation/selector histories differ. The horizontal action's two intermediate grouping steps remain in its witness. Equal final rows do not assert equality of complete construction histories.

## Disposition

`rung-grading-and-orientation` is constructed at its explicit alternative acceptance: retain role labels, compare quotient maps and provide a typed orientation/history table without claiming an unsupported intrinsic12-to4 grading. A unit grade is additionally exhibited for the finite object diagram only. Intermediate physical grades11 through5, geometric dimensions, unique grouping, and a numerical137 descent are not inferred.

## Verification

    python research/strominger/checkers/check_wg_grading_orientation.py

Eleven exact finite checks and eight hostile assertions pass. It reruns the existing schedule comparison and its indexing/path/diagram prerequisites (including the retained137 source). No new Agda closure is claimed. Receipt: `research/strominger/results/wg-grading-orientation-v1.json`.

Hostiles reject unit-rank use of rung numbers, transport9 as an object, four blocks as four retained rows, target factoring through source, equal-profile identification, orientation erasure, route-history erasure and rung6 as row cardinality.

Next: task-relative uncertainty on the checked retained assembly, then whole-package half-step comparison. The requested four-extension run is not complete.
