# Why every disjoint port pair repairs a failed square

**Scope.** A red path; four distinct parent ports whose supports are the four choices `{f,x_i,y_j}`, where `x_0,x_1` and `y_0,y_1` are disjoint adjacent path pairs and `f` is fixed. The parent and each new port on its own are legal (no red triangle or blue seven), with all port links blue. Add two ports S,T. The claim is about repairing the joint attachment, not selecting this path realization from the table.

**Lemma.** Every blue seven in the joint all-blue-port graph contains *all six ports*.

Both newcomers are necessary by single-attachment legality. Write U for the union of the four corner supports. Sites outside U that are blue to S contain no mutually blue pair: such a pair, all four parent ports and S would already form a seven. Hence any proposed seven with S and T uses at most one site outside U.

Inside U the largest mutually blue set has at most three sites: at most f and one site from each adjacent pair. If the seven uses h parent ports, it must avoid their supports. For h=1 there are at most two remaining sites inside U (the other two choices); for h=2 there is at most one, since distinct corners differ in at least one choice; for h=3 all sites of U are covered. Thus for h=0,1,2,3 the inside-U capacities are at most 3,2,1,0 respectively. With at most one outside site there are at most 4-h available path sites, whereas the seven requires 5-h. This proves the lemma. For h=4 one outside site suffices exactly when all six supports miss it.

**Repair.** Every surviving seven uses both endpoints of any proposed port link. Turning a single link red therefore destroys every seven and cannot create a new blue one. It creates a red triangle exactly when its endpoints share a support site: only one port link is red. Thus every disjoint pair is a sufficient single repair. No disjoint pairs means no port edge may legally become red. Exactly one means it is forced in any repair. With multiple eligible edges any one works; the proof does not license every simultaneous recoloring. The argument has no width bound and does not require the new supports to be distinct from each other. It uses the literal independent swaps and single-attachment legality.

**Finite cross-check.** [Minimal repair census](results/ramsey_square_port_repairs.json) · [checker](checkers/ramsey_square_port_repairs.py).
