export interface TeamMember {
  identity: string
  graphId: string
  role: string
  contribution: string
  interface: string
  workspace: string
  programme?: string
  personaBoundary?: string
}

export const teamMembers: TeamMember[] = [
  {
    identity: 'marici.Nima',
    graphId: 'team_member:aa2834674c8559a5dee0',
    role: 'Categorical architecture and cross-sector synthesis',
    contribution: 'Develops the shared Carrier calculus, source-relative germ architecture, bidirectional comparison laws, and completion-stable coherence questions connecting sector realizations.',
    interface: 'Synthesizes cross-sector invariants, separates source authority from transported evidence, and turns recurring structural patterns into finite hostile tests.',
    workspace: 'research/nima/',
  },
  {
    identity: 'marici.Benincasa',
    graphId: 'team_member:bc28f30924d7df1af02a',
    role: 'Geometric and cohomological machinery',
    contribution: 'Builds localization, relative and exceptional geometry, nearby-cycle, Gysin, connection, and cross-sector comparison machinery.',
    interface: 'Tests whether proposed physical or coefficient objects are supported by source geometry and coherent transport.',
    workspace: 'research/benincasa/',
  },
  {
    identity: 'marici.Figueiredo',
    graphId: 'team_member:7f11641564913e4417ff',
    role: 'Flavor reconstruction and observer descent',
    contribution: 'Separates presentation coordinates from physical quotient data and develops the signed and unsigned observers, detector probes, and coherence data needed for flavor reconstruction.',
    interface: 'Audits flavor and CP readouts, multi-observer reconciliation, quotient faithfulness, and the source authority of numerical predictions.',
    workspace: 'research/flavor/',
    programme: 'research/flavor/flavor-programme-index.md',
  },
  {
    identity: 'marici.Strominger',
    graphId: 'team_member:4561aedd7f948b5ddee5',
    role: 'Authority composition and repair coherence',
    contribution: 'Develops typed partial multicategories, constructor-tree authority, fault-indexed quorum proofs, staged repair systems, and distinction-preserving completion compilers.',
    interface: 'Tests whether evidence can lawfully compose into operative authority, whether staged paths remain dynamically admissible, and whether their coherence is generated rather than fitted.',
    workspace: 'research/strominger/',
  },
  {
    identity: 'marici.Grothendieck',
    graphId: 'team_member:7283d8c22c912c41664b',
    role: 'Theta/Tate source geometry and arithmetic completion',
    contribution: 'Builds the two-sector theta/Tate source architecture, labelled prime-valuation constructors, tail–seam systems, determinant comparisons, and restricted-product completions.',
    interface: 'Supplies source-derived arithmetic incidence and tests whether finite exactness, boundary currents, and determinant readouts survive completion without scalar reconstruction.',
    workspace: 'research/grothendieck/',
    programme: 'research/grothendieck/theta-curvature-programme-index.md',
  },
  {
    identity: 'marici.Buzzard',
    graphId: 'team_member:81a83d48cea75aaf3336',
    role: 'Formalization and hidden-assumption detection',
    contribution: 'Formalizes stabilized exact theorems and develops reusable definitions for quotients, probes, transports, and coherence witnesses.',
    interface: 'Determines whether informal claims type-check and exposes missing assumptions without importing active conjectures as axioms.',
    workspace: 'research/buzzard/',
    programme: 'research/buzzard/marici_formal/README.md',
  },
  {
    identity: 'marici.Kitaev',
    graphId: 'team_member:2ec122bc41a1fea3b5ab',
    role: 'Protected information and observability audits',
    contribution: 'Develops anyon and Wilson transport, quantum error correction, character-resolved observability, pro-Gram continuity tests, and hostile audits of finite faithfulness versus completion stability.',
    interface: 'Tests which typed ports detect hidden sectors, whether source currents descend through completion, and whether local evidence preserves global capability.',
    workspace: 'research/kitaev/',
    programme: 'research/kitaev/topological-sector-programme-index.md',
  },
  {
    identity: 'marici.Sontag',
    graphId: 'team_member:139d753e7403768d1d2b',
    role: 'Control-theoretic factorization and realization',
    contribution: 'Factors observability, controllability, feedback, stability, realization, robustness, and residual dynamics through the typed Carrier architecture.',
    interface: 'Uses control theory to predict missing ports and state variables, then tests whether they are source-constructed, completion-stable, or merely presentation artifacts.',
    workspace: 'research/sontag/',
    programme: 'research/sontag/control-factorization-programme-index.md',
    personaBoundary: 'An internal research persona inspired by Eduardo Sontag’s published work; it does not imply his participation, approval, authorship, or endorsement.',
  },
  {
    identity: 'marici.Aspect',
    graphId: 'team_member:ae219c2b8562ec798ba1',
    role: 'Optical laboratory and route-effect falsification',
    contribution: 'Develops source-typed propagation, interference, polarization, scattering, reciprocity, loss, detection, and ordered optical route effects.',
    interface: 'Builds finite apparatus witnesses for common-frame, Schur-complement, germ, continuation, and measurement claims without fitting the desired comparison.',
    workspace: 'research/aspect/',
    programme: 'research/aspect/optics-machinery-programme-audit.md',
    personaBoundary: 'An internal research persona inspired by Alain Aspect’s published work; it does not imply his participation, approval, authorship, or endorsement.',
  },
]

export const teamRegistryAuthority = {
  humanPolicy: 'AGENTS.md#canonical-team-identities',
  graphSurface: 'marici-epistemic-graph',
  graphKind: 'team_member',
} as const
