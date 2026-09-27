<script setup>
import { teamMembers, teamRegistryAuthority } from '../../../src/data/team'
</script>

# Research team

Marici uses qualified research identities so claims retain accountable authorship while cross-sector work remains part of one shared programme. Roles state responsibility and interface; they do not make one researcher's results authoritative in another's domain.

**Registry authority:** {{ teamRegistryAuthority.humanPolicy }}. Durable identities are recorded on `{{ teamRegistryAuthority.graphSurface }}` as `{{ teamRegistryAuthority.graphKind }}` entities.

<div class="ledger-list">
  <article v-for="member in teamMembers" :key="member.identity" class="ledger-card">
    <p class="ledger-meta">{{ member.role }}</p>
    <h2>{{ member.identity }}</h2>
    <p>{{ member.contribution }}</p>
    <p><strong>Team interface:</strong> {{ member.interface }}</p>
    <p><strong>Workspace:</strong> <code>{{ member.workspace }}</code></p>
    <p v-if="member.programme"><strong>Programme:</strong> <code>{{ member.programme }}</code></p>
    <p v-if="member.personaBoundary">{{ member.personaBoundary }}</p>
    <a :href="`/explore/graph/?entity=${encodeURIComponent(member.graphId)}`">Graph record</a>
  </article>
</div>

## Interpretation boundary

Roles organize inquiry; they do not certify conclusions. Mathematical or physical authority comes from the stated source, exact verification, review boundary, and—where applicable—an independently established carrier operation.
