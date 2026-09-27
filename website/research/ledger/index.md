<script setup>
import { ref, computed, onMounted } from 'vue'
const query = ref('')
const page = ref(1)
const pageSize = 50
const entries = ref([])
const loading = ref(true)
const matches = computed(() => {
  const q = query.value.trim().toLocaleLowerCase()
  return q ? entries.value.filter(e => `${e.title} ${e.description} ${e.authorLabel}`.toLocaleLowerCase().includes(q)) : entries.value
})
const visible = computed(() => matches.value.slice((page.value - 1) * pageSize, page.value * pageSize))
onMounted(async () => {
  entries.value = await (await fetch('/research/ledger/index.json')).json()
  loading.value = false
  if (location.hash === '#search') document.querySelector('[data-ledger-search]')?.focus()
})
</script>

# Research ledger

The dated public record is loaded from `src/ledger`. Draft entries are excluded. Search matches titles, summaries, and author names.

<PagefindSearch />

<label>Search entries <input data-ledger-search v-model="query" type="search" placeholder="Search the ledger…" @input="page = 1" /></label>
<p class="ledger-meta">{{ loading ? 'Loading the published ledger…' : `${matches.length.toLocaleString()} entries` }}</p>
<div class="ledger-list">
  <article v-for="entry in visible" :key="entry.slug" class="ledger-card">
    <p class="ledger-meta">Entry {{ entry.entry }} · {{ entry.date }} · {{ entry.authorLabel }} · {{ entry.kind }}</p>
    <h2><a :href="entry.url">{{ entry.title }}</a></h2>
    <p>{{ entry.description }}</p>
  </article>
</div>
<nav aria-label="Ledger pages" class="home-links"><button :disabled="page <= 1" @click="page--">Previous</button><span>Page {{ page }} / {{ Math.max(1, Math.ceil(matches.length / pageSize)) }}</span><button :disabled="page * pageSize >= matches.length" @click="page++">Next</button></nav>
