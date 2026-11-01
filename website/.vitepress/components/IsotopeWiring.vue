<script setup>
import { onBeforeUnmount, ref, watch } from 'vue'
import { useData } from 'vitepress'
import source from '../../../examples/isotope-wiring/index.html?raw'

const frame = ref(null)
const { isDark } = useData()
const tokens = ['--vp-c-text-1', '--vp-c-text-2', '--vp-c-divider', '--vp-c-bg',
  '--vp-c-bg-soft', '--vp-c-default-soft', '--vp-c-brand-1', '--vp-c-brand-2',
  '--vp-c-brand-soft', '--vp-font-family-base']
let pending
function syncTheme() {
  const root = frame.value?.contentDocument?.documentElement
  if (!root) return
  const theme = getComputedStyle(document.documentElement)
  for (const token of tokens) root.style.setProperty(token, theme.getPropertyValue(token))
  root.classList.toggle('dark', isDark.value)
}
watch(isDark, () => {
  cancelAnimationFrame(pending)
  pending = requestAnimationFrame(syncTheme)
}, { flush: 'post' })
onBeforeUnmount(() => cancelAnimationFrame(pending))
</script>

<template>
  <iframe ref="frame" class="isotope-wiring" title="Isotope wiring editor"
    :srcdoc="source" @load="syncTheme" />
</template>

<style scoped>
.isotope-wiring {
  display: block;
  width: 100%;
  height: max(640px, calc(100dvh - 200px));
  border: 1px solid var(--vp-c-divider);
  border-radius: 10px;
  background: var(--vp-c-bg);
}
@media (max-width: 600px) {
  .isotope-wiring { height: max(560px, calc(100dvh - 140px)); }
}
</style>
