<script setup lang="ts">
import DefaultTheme from 'vitepress/theme'

function closeSectionDrawer(event: MouseEvent) {
  if (!(event.target instanceof Element)) return
  const link = event.target.closest<HTMLAnchorElement>('.VPSidebar.open a[href*="#"]')
  if (!link) return
  const url = new URL(link.href)
  if (url.origin !== location.origin || url.pathname !== location.pathname) return
  // VitePress closes on route changes, but section hashes are the same route.
  // Use its existing backdrop action so scroll locking is also cleaned up.
  document.querySelector<HTMLElement>('.VPBackdrop.backdrop')?.click()
}
</script>

<template>
  <DefaultTheme.Layout @click.capture="closeSectionDrawer" />
</template>
