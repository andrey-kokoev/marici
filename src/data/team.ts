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
    role: 'Common architecture and cosmology',
    contribution: 'Develops the scalar master geometry, the shared Carrier calculus, and the common architectural questions connecting sector realizations.',
    interface: 'Supplies and reviews common-carrier claims, cross-sector constructions, cosmological realizations, and programme-level synthesis.',
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
    role: 'Flavor and presentation-versus-physics descent',
    contribution: 'Separates presentation coordinates from physical quotient data and develops flavor-sector coefficient, detector, and selection structures.',
    interface: 'Audits faithfulness, CP and flavor readouts, quotient coordinates, and the source authority of physical distinctions.',
    workspace: 'research/flavor/',
    programme: 'research/flavor/flavor-programme-index.md',
  },
  {
    identity: 'marici.Strominger',
    graphId: 'team_member:4561aedd7f948b5ddee5',
    role: 'Radiative gravity, asymptotic symmetry, and memory',
    contribution: 'Develops radiative GR, BMS charges, soft limits, memory observables, and their carrier and response-object realizations.',
    interface: 'Tests asymptotic transport, gauge and memory readouts, completion, and physical detector authority.',
    workspace: 'research/strominger/',
  },
  {
    identity: 'marici.Grothendieck',
    graphId: 'team_member:7283d8c22c912c41664b',
    role: 'Arithmetic geometry and derived arithmetic emergence',
    contribution: 'Investigates whether Spec(Z), primes, Frobenius, Euler products, L-functions, and theta structures emerge from rather than enter the Carrier calculus by hand.',
    interface: 'Supplies arithmetic source objects, primewise residuals, completion problems, and audits of inserted versus derived arithmetic structure.',
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
    role: 'Topological matter, error correction, and protected sectors',
    contribution: 'Develops anyon transport, quantum error correction, protected logical sectors, and hostile audits of local syndrome versus global capability.',
    interface: 'Tests homological residue, decoder authority, local-to-global reconstruction, and topological protection in proposed Carrier realizations.',
    workspace: 'research/kitaev/',
    programme: 'research/kitaev/topological-sector-programme-index.md',
  },
  {
    identity: 'marici.Sontag',
    graphId: 'team_member:139d753e7403768d1d2b',
    role: 'Control-theoretic comparative reconstruction',
    contribution: 'Uses observability, controllability, feedback, stability, realization, robustness, and systems theory to predict missing Marici objects and coherence laws.',
    interface: 'Maps established Marici fragments into control-theoretic neighborhoods, then tests predicted additions as constructed, obstructed, or source-unauthorized.',
    workspace: 'research/sontag/',
    programme: 'research/sontag/control-factorization-programme-index.md',
    personaBoundary: 'An internal research persona inspired by Eduardo Sontag’s published work; it does not imply his participation, approval, authorship, or endorsement.',
  },
  {
    identity: 'marici.Aspect',
    graphId: 'team_member:ae219c2b8562ec798ba1',
    role: 'Optics integrating laboratory',
    contribution: 'Develops propagation, interference, coherence, polarization, scattering, reciprocity, loss, cavities, detection, and retained pre-readout route structure.',
    interface: 'Builds source-typed optical apparatuses that discriminate proposed cross-sector Carrier operations without presupposing them.',
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
