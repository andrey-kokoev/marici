## First-pass literature survey — November 2026

The search has identified a small, directly relevant research cluster working on the mathematical problems we have been discussing: carrier routing, collision-free enumeration, switch-state transitions, and periodic closure.

The most important initial finding is a 2026 paper that explicitly proves its enumeration algorithm terminates and finds all solutions. It goes substantially beyond earlier work based on manual trial and simulation.

### A. Core research: direct correspondence

| Year | Paper                                                                                                                                                                                        | Main contribution                                                                                   |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| 2026 | [A graph-based algorithm for automatically enumerating switch state sequences for maypole braiding machines](https://doi.org/10.1016/j.rineng.2026.112110?utm_source=chatgpt.com)            | Directed cyclic graphs; exhaustive, solution-preserving search for collision-free routing sequences |
| 2025 | [A novel method for listing all collision-free carrier arrangements of maypole braiding machines](https://doi.org/10.1177/15280837251371994?utm_source=chatgpt.com)                          | Exhaustive enumeration of configurations, reduced by rotational and reflection symmetries           |
| 2025 | [Discrete simulation of maypole braiding machines to create collision-free braiding programmes](https://www.sciencedirect.com/science/article/pii/S2405844025012988?utm_source=chatgpt.com)  | Permutation-like matrix operations, collision detection, and computation of return periods          |
| 2021 | [Carrier delay-based method for development of the tracks for transitions between patterns](https://doi.org/10.1177/00405175211026533?utm_source=chatgpt.com)                                | Arithmetic conditions on carrier delays and occupied/vacant slots                                   |
| 2019 | [A methodology for modeling the relationship between process and topological yarn structure](https://www.sciencedirect.com/science/article/abs/pii/S0266353818307711?utm_source=chatgpt.com) | Mapping switch operations to carrier paths and braid topology                                       |

Sources:&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

ScienceDirect+4



### First quantitative result

Krauskopf, Rauh, and Hein's 2025 enumeration gives:

| Horn-gear array | Distinct track layouts | Distinct carrier arrangements |
| --------------- | ---------------------- | ----------------------------- |
| 3 × 3           | 285                    | 20,136                        |
| 4 × 3           | 11,154                 | 2,112,510                     |
| 4 × 4           | 537,001                | 264,163,782                   |

The counts use the paper's symmetry equivalences; the carrier-arrangement classification also accounts for machine rotation advancement. They are not counts of distinct resulting braids.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://journals.sagepub.com\&sz=32)

Sage Journals



This establishes that exhaustive enumeration of physically constrained weaving configurations is already a developed computational research problem.

### B. Earlier work: braiding as a clique problem

A major result predates the recent maypole research by more than two decades.

Grünert, Irnich, Zimmermann, Schneider, and Wulfhorst (2002)

[Finding all k-cliques in k-partite graphs, an application in textile engineering](https://doi.org/10.1016/S0305-0548\(00\)00053-8?utm_source=chatgpt.com)

Computers & Operations Research, 29(1), 13–31. RWTH Aachen research.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

ScienceDirect



Their construction:

1. Generate candidate trajectories for each bobbin.
2. Treat each candidate trajectory as a graph vertex.
3. Connect two vertices when their trajectories are compatible.
4. Find a clique selecting one trajectory per bobbin.

The clique represents a globally compatible set of carrier trajectories.

This establishes a direct connection between physical braiding and clique-existence problems.

It is not yet a correspondence with Ramsey numbers: the compatibility graph is multipartite, and its vertices represent candidate paths, not positions in a Ramsey coloring.

A related 2000 paper by Schneider, Pickett, and Wulfhorst describes the ROUTE/CAB software system implementing path enumeration and compatibility-based selection. [A New Rotary Braiding Machine and CAE Procedures to Produce Efficient 3D-Braided Textiles for Composites](https://www.nasampe.org/store/viewproduct.aspx?id=4303308\&utm_source=chatgpt.com).&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.researchgate.net\&sz=32)

ResearchGate



The historical sequence is significant:

- 2000: Computer-aided carrier routing.
- 2002: Global path compatibility expressed as a clique problem.
- 2025: Exhaustive enumeration of collision-free carrier arrangements.
- 2026: Complete enumeration of collision-free switching sequences for specified endpoints and path length.

The 2026 method uses reachability matrices, pruned path trees, and collision constraints. Its mathematical guarantee concerns its specified routing problem, not arbitrary braid synthesis or Ramsey thresholds.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

ScienceDirect



### C. Additional relevant papers

The following works extend the bibliography beyond the original maypole research cluster.

| Year | Authors / publication                                                                                                                                                  | Mathematical contribution                                                       | Priority |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | -------- |
| 1964 | Yamaki, [Designing a Carrier Guide Path for Braiding Machines](https://doi.org/10.4188/jte1955.10.84?utm_source=chatgpt.com)                                           | Geometric constraints limiting carrier-track length                             | B        |
| 2011 | van Ravenhorst & Akkerman, [A Spool Pattern Tool for Circular Braiding](https://www.researchgate.net/publication/254884232?utm_source=chatgpt.com)                     | Binary occupancy vectors and braid-pattern matrices                             | A        |
| 2016 | Ma, Dong & Wang, [Matrix Algorithm for Braiding Simulation](https://doi.org/10.1155/2016/9280865?utm_source=chatgpt.com)                                               | Matrix operations generating complete carrier trajectories                      | A        |
| 2018 | Kyosev & Gleßner, [Extended Horn Gears in 3D Maypole Braiding](https://doi.org/10.1177/2515221118786741?utm_source=chatgpt.com)                                        | Composition of smaller gears into larger equivalent gears                       | A        |
| 2019 | Du et al., [Modeling and Analysis of the Carrier Arrangement in Square Rotary Braiding](https://doi.org/10.1177/0040517519828998?utm_source=chatgpt.com)               | Matrix constraints determining permitted carrier positions                      | A        |
| 2023 | Assi, Achiche & Laberge Lebel, [Application of Graph Theory for Detecting Carriers' Collisions](https://doi.org/10.1007/s00170-023-11245-z?utm_source=chatgpt.com)     | Graph representation and collision detection for arbitrary carrier arrangements | A        |
| 2023 | Same authors, [Application of Graph Theory for Preventing Carriers' Collisions](https://doi.org/10.1007/s00170-023-11405-1?utm_source=chatgpt.com)                     | Collision prevention in variable-path machines                                  | A        |
| 2024 | Assi et al., [Horngear and Carrier Design for Braiding Tailorable Composite Preforms](https://doi.org/10.1016/j.cirpj.2024.03.004?utm_source=chatgpt.com)              | Variable carrier paths without conventional switching mechanisms                | B        |
| 2025 | Liu et al., [Application of Graph Theory in Carrier Path Research](https://doi.org/10.1007/s00170-025-15743-0?utm_source=chatgpt.com)                                  | Graph transformation to generate trajectories for complex cross-sections        | A        |
| 2025 | Glessner & Kyosev, [Possibilities for the Production and Method in the Development of Lace Braiding](https://doi.org/10.1177/00405175251380816?utm_source=chatgpt.com) | Selective strand interactions through programmed switching                      | A        |
| 2026 | Jing et al., [Yarn-Carrier Trajectory Planning Method](https://doi.org/10.1016/j.compstruct.2025.119999?utm_source=chatgpt.com)                                        | Shortest-path optimization under geometric and collision constraints            | B        |
| 2026 | Ding et al., [Process Planning of Hexagonal 3D Braiding](https://doi.org/10.1177/15280837261473781?utm_source=chatgpt.com)                                             | Equivalent virtual gears, effective slots, and deterministic process matrices   | A        |

The publications and their stated contributions were checked against publisher records, abstracts, and institutional bibliographies.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.jstage.jst.go.jp\&sz=32)

J-STAGE+11



A related 2023 doctoral dissertation by Pascal Assi, Développement d'un procédé sans collision pour la fabrication de tresses 3D avec géométries variables, is available through [Polytechnique Montréal's publication repository](https://publications.polymtl.ca/view/person/Assi%2C_Pascal.date.html?utm_source=chatgpt.com). It provides a useful route into that research group's broader work.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://publications.polymtl.ca\&sz=32)

PolyPublie



### D. Research groups identified

| Institution                                               | Researchers                                                         | Principal specialty                                        |
| --------------------------------------------------------- | ------------------------------------------------------------------- | ---------------------------------------------------------- |
| OFFIS / University of Oldenburg, Germany                  | Krauskopf, Rauh, Hein                                               | Exhaustive state-space enumeration and formal routing      |
| TU Dresden / Hochschule Niederrhein, Germany              | Kyosev, Gleßner                                                     | Pattern formation, switching, equivalent gears             |
| RWTH Aachen, Germany                                      | Grünert, Irnich, Schneider, Wulfhorst                               | Path compatibility and combinatorial optimization          |
| Polytechnique Montréal, Canada                            | Assi, Achiche, Laberge Lebel                                        | Graph-based collision prevention, variable-path mechanisms |
| Donghua University, China                                 | Meng Zhuo, Du Chengjie, Ding Caihong, Yang Yanzhu and collaborators | Carrier arrangement, hexagonal and rotary machine models   |
| Nanjing University of Aeronautics and Astronautics, China | Liu Jiale, Gao Yicen and collaborators                              | Graph transformations for complex carrier paths            |

These are identifiable research lineages, not necessarily six currently active teams in precisely the same specialty.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://journals.sagepub.com\&sz=32)

Sage Journals+6



### E. Which mathematical problems have already been addressed?

| Question                                                                               | Literature status                                          |
| -------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| Can machine motion be represented algebraically?                                       | Yes                                                        |
| Can local switching uniquely determine the next machine state?                         | Yes, with complete machine state and controls specified    |
| Can a particular carrier arrangement be checked for collisions?                        | Yes                                                        |
| Can all collision-free arrangements be enumerated?                                     | Yes, for specified machine classes                         |
| Can all valid transitions between specified arrangements be generated?                 | Yes, for specified machines and bounded transition lengths |
| Can global routing be expressed as a clique problem?                                   | Yes                                                        |
| Can the minimum required switching capacity be derived for arbitrary braid structures? | No general result identified                               |
| Can these mechanisms derive Ramsey thresholds?                                         | No result identified                                       |

### F. Main finding and research direction

The strongest connection is between the 2002 RWTH Aachen paper and the 2026 Oldenburg paper.

They address complementary aspects of the same problem.

Grünert et al. model global routing as a clique of mutually compatible paths.

Krauskopf et al. generate admissible paths using local machine rules, reachability matrices, and systematic elimination of impossible continuations.

This gives us a concrete mathematical pipeline:

\\[ \text{Local transitions} \longrightarrow \text{Admissible paths} \longrightarrow \text{Compatibility graph} \longrightarrow \text{Global configurations} \\]

A possible obstruction appears when the compatibility graph has no clique of the required size.

For our R/B/G model, the next mathematical question is:

Can the smallest carrier required for a specified pair of complete R/B circulations be determined by the first disappearance of a required clique in the path-compatibility graph?

This can be investigated without presupposing that the answer is a Ramsey number.

The first-pass survey has identified roughly 20 directly or closely relevant publications, including the initial five, the two RWTH papers, and the additional works above. This is a substantive starting bibliography, but not yet exhaustive. In particular, older German-language machine-design work, Chinese dissertations, patent literature, and forward citation chains remain incompletely covered.

The most productive immediate source is the 2026 Krauskopf–Rauh–Hein paper. Its graph construction and solution-preserving pruning algorithm are directly reusable for a first computational experiment with our \\(3R+7B+gG\\) carrier.