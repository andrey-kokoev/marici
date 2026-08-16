import { defineConfig } from 'astro/config'
import rehypeKatex from 'rehype-katex'
import remarkMath from 'remark-math'
import remarkNaradaMath from './src/lib/remark-narada-math.mjs'

export default defineConfig({
  markdown: {
    remarkPlugins: [remarkMath, remarkNaradaMath],
    rehypePlugins: [rehypeKatex],
  },
  output: 'static',
  site: process.env.PUBLIC_SITE_URL,
})
