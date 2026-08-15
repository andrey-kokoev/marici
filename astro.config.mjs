import { defineConfig } from 'astro/config'
import { createMarkdownProcessor } from '@astrojs/markdown-remark'
import rehypeKatex from 'rehype-katex'
import remarkMath from 'remark-math'
import remarkNaradaMath from './src/lib/remark-narada-math.mjs'

const markdown = await createMarkdownProcessor({
  remarkPlugins: [remarkMath, remarkNaradaMath],
  rehypePlugins: [rehypeKatex],
})

export default defineConfig({
  markdown,
  output: 'static',
  site: process.env.PUBLIC_SITE_URL,
})
