import { defineConfig } from 'vitepress'
import { katex } from '@mdit/plugin-katex'

export default defineConfig({
  title: 'Marici',
  description: 'Research from the relational carrier.',
  cleanUrls: true,
  ignoreDeadLinks: true,
  sitemap: { hostname: 'https://marici.andrei-kokoev.workers.dev' },
  markdown: {
    config(md) { md.use(katex, { throwOnError: false, strict: 'error' }) },
  },
  themeConfig: {
    nav: [
      { text: 'Theory', link: '/research/theory/' },
      { text: 'System', link: '/research/system-characteristics/' },
      { text: 'Results', link: '/research/results/' },
      { text: 'Predictions', link: '/research/predictions/' },
      { text: 'Ledger', link: '/research/ledger/' },
      { text: 'Graph', link: '/explore/graph/' },
      { text: 'Team', link: '/about/team/' },
    ],
    socialLinks: [{ icon: 'github', link: 'https://github.com/andrey-kokoev/marici' }],
    search: { provider: 'local' },
  },
})
