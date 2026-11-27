<script setup>
import {ref,computed,watch} from 'vue'
import {patterns,pascal,mirror,completion,foldPairs} from './patterns.mjs'
const props=defineProps({width:Number,word:String});const emit=defineEmits(['pick']);const odd=ref(false),branch=ref('all');const rows=pascal(12),n=props.width-2,words=patterns(props.width),expanded=completion(words),pairs=foldPairs(expanded);const partners=computed(()=>[...new Set(pairs.filter(p=>p.includes(props.word)).map(p=>p.find(w=>w!==props.word)))])
const groups={all:words,B:words.filter(w=>w.endsWith('B')),R:words.filter(w=>w.endsWith('R'))};function focus(k){branch.value=k;if(!groups[k].includes(props.word))emit('pick',groups[k][0])}function pick(w){if(!groups[branch.value].includes(w))branch.value='all';emit('pick',w)}
watch(()=>props.word,w=>{if(!groups[branch.value].includes(w))branch.value='all'})
const cell=(r,k)=>r===n&&k===3?'all':r===n-1&&k===3?'B':r===n-1&&k===2?'R':null
</script>
<template><section class="navigator"><h2>2 · Where the three-red rows come from</h2><p>Widen {{width-1}} → {{width}}. Shift separated positions (a,b,c) to (a,b−1,c−2): choose three ordinary positions from {{n}}. The highlighted Pascal entry is C({{n}},3) = {{words.length}}.</p>
<label><input v-model="odd" type="checkbox"> Sierpiński overlay: dim even coefficients</label>
<svg viewBox="0 0 420 267" role="img" aria-label="Pascal triangle with target and its two parents"><g v-for="(row,r) in rows" :key="r"><g v-for="(value,k) in row" :key="k" :transform="`translate(${210+(k-r/2)*31},${12+r*20})`" @click="cell(r,k)&&focus(cell(r,k))" :style="{cursor:cell(r,k)?'pointer':'default'}"><rect x="-14" y="-9" width="28" height="18" rx="4" :fill="cell(r,k)==='all'?'#ffd264':cell(r,k)?'#90cbe1':'#64798a'" :opacity="odd&&value%2===0&&!cell(r,k)?0.18:1"/><text text-anchor="middle" y="4" font-size="11" :fill="odd&&value%2===0&&!cell(r,k)?'#85929e':'#091722'">{{value}}</text></g></g></svg>
<p>Choose a branch (highlighted cells remain readable in parity mode): <button v-for="(list,k) in groups" :key="k" :aria-pressed="branch===k" @click="focus(k)">{{k==='all'?'All patterns':k==='B'?'Inherited · append B':'New · append BR'}} ({{list.length}})</button></p>
<div><button v-for="w in groups[branch]" :key="w" :aria-pressed="word===w" @click="pick(w)">{{w}}</button></div>
<p><strong>{{word}}</strong> · {{word.endsWith('B')?'Inherited from '+word.slice(0,-1)+' by appending B':'New from '+word.slice(0,-2)+' by appending BR'}}. Mirror: <button @click="pick(mirror(word))">{{mirror(word)}}</button> Fold partners: <button v-for="w in partners" :key="w" @click="pick(w)">{{w}}</button><span v-if="!partners.length">none</span>.</p>
<p>{{words.length}} distinct patterns → {{expanded.length}} mirror-completed row occurrences → {{expanded.length-pairs.length}} displayed records under the RBBR fold. The parity overlay marks odd counts, not forbidden graph rows.</p></section></template>
<style scoped>.navigator svg{display:block;max-width:100%;width:420px}.navigator button{margin:.15em;padding:.3em .5em}.navigator button[aria-pressed=true]{background:#ffd264;color:#142433}</style>
