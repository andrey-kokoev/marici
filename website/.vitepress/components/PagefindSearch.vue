<script setup lang="ts">
import { ref, onMounted } from 'vue'
const term = ref('')
const results = ref<any[]>([])
const searching = ref(false)
let pagefind: any
let timer: ReturnType<typeof setTimeout>
onMounted(async () => { pagefind = await import(/* @vite-ignore */ new URL('/pagefind/pagefind.js', location.origin).href); await pagefind.init() })
async function search() {
  clearTimeout(timer)
  const query = term.value.trim()
  if (!query || !pagefind) { results.value = []; return }
  searching.value = true
  const response = await pagefind.search(query)
  results.value = await Promise.all(response.results.slice(0,8).map((item: any) => item.data()))
  searching.value = false
}
function schedule() { timer = setTimeout(search, 180) }
</script>

<template>
  <section class="pagefind-search" aria-label="Search all published pages and ledger entries">
    <label>Search all public entries <input v-model="term" type="search" placeholder="Search full text…" @input="schedule" /></label>
    <p v-if="searching">Searching…</p>
    <ul v-else-if="results.length"><li v-for="item in results" :key="item.url"><a :href="item.url">{{item.meta?.title || item.url}}</a><div v-html="item.excerpt"></div></li></ul>
  </section>
</template>

<style scoped>
.pagefind-search{margin:1rem 0;padding:1rem;border:1px solid var(--vp-c-divider);border-radius:8px}.pagefind-search label{display:grid;gap:.35rem}.pagefind-search input{padding:.6rem}.pagefind-search li{margin:.8rem 0}.pagefind-search :deep(mark){background:var(--vp-c-brand-soft);color:inherit}
</style>
