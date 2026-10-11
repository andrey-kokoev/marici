<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'

type Node = {id:string;label:string;name:string;kind:string;generation?:number;charge:string;spin:string;x:number;y:number}
type Relation = {id:string;label:string;kind:string;mediators:string[];members:string[];color:string}
const graph = ref<{scope:string;nodes:Node[];relations:Relation[];notes:string[]}>({scope:'',nodes:[],relations:[],notes:[]})
const selected = ref('')
const enabled = ref(new Set<string>())
const selectedNode = computed(() => graph.value.nodes.find(node => node.id === selected.value))
const activeRelations = computed(() => graph.value.relations.filter(relation => enabled.value.has(relation.id)))
const incident = computed(() => activeRelations.value.filter(relation => relation.members.includes(selected.value) || relation.mediators.includes(selected.value)))
function toggle(id:string) { const next = new Set(enabled.value); next.has(id) ? next.delete(id) : next.add(id); enabled.value = next }
function edgePath(source:Node,target:Node,index:number) { const bend = (index % 5 - 2) * 9; return `M ${source.x} ${source.y} Q ${(source.x+target.x)/2} ${(source.y+target.y)/2+bend} ${target.x} ${target.y}` }
onMounted(async () => {
  const response = await fetch('/standard-model-graph.json')
  const data = await response.json()
  if (data.schema !== 'marici.matter.standard-model-graph.v1') throw new Error('Unexpected Standard Model graph schema')
  graph.value = data
  enabled.value = new Set(data.relations.map((relation:Relation) => relation.id))
})
</script>

<template>
  <section class="sm-app">
    <p class="scope">{{ graph.scope }}</p>
    <div class="controls" aria-label="Interaction filters">
      <strong>Show interactions</strong>
      <button v-for="relation in graph.relations" :key="relation.id" :aria-pressed="enabled.has(relation.id)" :style="{'--relation':relation.color}" @click="toggle(relation.id)">{{ relation.label }}</button>
    </div>
    <div class="layout">
      <div class="canvas">
        <svg viewBox="40 35 900 535" role="img" aria-label="Interactive graph of Standard Model particles and their interactions">
          <g class="guides">
            <text x="150" y="62">Generation I</text><text x="310" y="62">Generation II</text><text x="470" y="62">Generation III</text><text x="775" y="62">Bosons</text>
            <text x="55" y="175">Quarks</text><text x="55" y="405">Leptons</text>
          </g>
          <g class="edges">
            <template v-for="relation in activeRelations" :key="relation.id">
              <template v-for="mediatorId in relation.mediators" :key="mediatorId">
                <path v-for="(memberId,index) in relation.members" :key="`${relation.id}-${mediatorId}-${memberId}`" :d="edgePath(graph.nodes.find(n=>n.id===mediatorId)!,graph.nodes.find(n=>n.id===memberId)!,index)" :stroke="relation.color" :class="{muted:selected && memberId!==selected && mediatorId!==selected}" />
              </template>
            </template>
          </g>
          <g v-for="node in graph.nodes" :key="node.id" class="node" :class="[node.kind,{selected:selected===node.id}]" :transform="`translate(${node.x},${node.y})`" tabindex="0" role="button" :aria-label="node.name" @click="selected=selected===node.id?'':node.id" @keydown.enter="selected=node.id" @keydown.space.prevent="selected=node.id">
            <circle r="27"/><text text-anchor="middle" dominant-baseline="central">{{node.label}}</text><title>{{node.name}}</title>
          </g>
        </svg>
        <p>Click a particle for details. Colored links mean that the species participates in that interaction; they are not individual Feynman vertices.</p>
      </div>
      <aside aria-live="polite">
        <template v-if="selectedNode">
          <p class="eyebrow">{{selectedNode.kind.replace('-', ' ')}}</p>
          <h2>{{selectedNode.name}}</h2>
          <dl><dt>Symbol</dt><dd>{{selectedNode.label}}</dd><dt>Spin</dt><dd>{{selectedNode.spin}}</dd><dt>Electric charge</dt><dd>{{selectedNode.charge}} e</dd><template v-if="selectedNode.generation"><dt>Generation</dt><dd>{{selectedNode.generation}}</dd></template></dl>
          <h3>Visible interactions</h3><ul><li v-for="relation in incident" :key="relation.id"><span :style="{background:relation.color}"></span>{{relation.label}}</li></ul>
          <button @click="selected=''">Clear selection</button>
        </template>
        <template v-else><h2>Standard Model field content</h2><p>Select a node to inspect its quantum numbers and interaction families.</p></template>
      </aside>
    </div>
    <details><summary>Scope and interpretation</summary><ul><li v-for="note in graph.notes" :key="note">{{note}}</li></ul><p><a href="https://github.com/andrey-kokoev/marici/blob/main/research/matter/standard-model-graph.json">View the machine-readable source data</a>.</p></details>
  </section>
</template>

<style scoped>
.sm-app{display:grid;gap:1rem}.scope{padding:.8rem 1rem;border-left:4px solid var(--vp-c-brand-1);background:var(--vp-c-bg-soft)}.controls{display:flex;align-items:center;gap:.55rem;flex-wrap:wrap}.controls button,.sm-app aside button{padding:.45rem .7rem;border:2px solid var(--vp-c-divider);border-radius:999px;background:var(--vp-c-bg);color:var(--vp-c-text-1)}.controls button[aria-pressed=true]{border-color:var(--relation);box-shadow:inset 0 -3px 0 var(--relation)}.layout{display:grid;grid-template-columns:minmax(0,3fr) minmax(230px,1fr);gap:1rem}.canvas,aside{border:1px solid var(--vp-c-divider);border-radius:10px;background:var(--vp-c-bg-soft)}.canvas{overflow:auto}.canvas svg{display:block;width:100%;min-width:650px}.canvas>p{margin:.5rem 1rem 1rem;color:var(--vp-c-text-2);font-size:.86rem}.guides text{fill:var(--vp-c-text-2);font-size:14px;text-anchor:middle}.guides text:nth-of-type(5),.guides text:nth-of-type(6){text-anchor:start}.edges path{fill:none;stroke-width:1.5;opacity:.34;transition:opacity .2s}.edges path.muted{opacity:.06}.node{cursor:pointer;outline:none}.node circle{stroke:var(--vp-c-bg);stroke-width:3}.node text{fill:white;font-size:17px;font-weight:700;pointer-events:none}.node.quark circle{fill:#b95749}.node.lepton circle{fill:#4b86a8}.node.gauge-boson circle{fill:#b28a37}.node.scalar circle{fill:#8265a5}.node:hover circle,.node:focus circle,.node.selected circle{stroke:var(--vp-c-text-1);stroke-width:5}.node.selected circle{r:33px}aside{padding:1rem}aside h2{font-size:1.2rem}.eyebrow{text-transform:uppercase;letter-spacing:.1em;font-size:.72rem;color:var(--vp-c-text-2)}dl{display:grid;grid-template-columns:1fr 1fr;gap:.35rem}dt{font-weight:600}dd{margin:0}aside ul{list-style:none;padding:0}aside li span{display:inline-block;width:.75rem;height:.75rem;border-radius:50%;margin-right:.5rem}details{padding:.8rem 1rem;border:1px solid var(--vp-c-divider);border-radius:8px}@media(max-width:800px){.layout{grid-template-columns:1fr}.canvas svg{min-width:600px}}
</style>
