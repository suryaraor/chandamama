# చందమామ · Chandamama

Telugu and English stories in the classic Chandamama style, published with GitHub Pages (Jekyll). Readers can switch between తెలుగు and English at the top of every page.

**Site:** https://suryaraor.github.io/chandamama/

## The easy way: `/publish-story`

1. Drop a story into `input-story/`: a `.md`, `.txt`, `.docx` or `.pdf` in Telugu, English or both, plus any pictures. If you're adding several stories at once, give each one its own subfolder.
2. In Claude Code, run **`/publish-story`**.

Claude then:
- fixes run-together paragraphs, without rewriting your words,
- writes the missing Telugu or English version,
- shrinks the images and places them at the right scenes (a `title`/`cover` image becomes the cover),
- creates `_stories/<slug>.md`,
- moves your originals to `archive/<date>-<slug>/`,
- commits, pushes, and checks the live page.

`input-story/` and `archive/` are git-ignored, so your raw drafts never get published.

The skill lives in `.claude/skills/publish-story/`.

## Writing a story by hand

Copy `story-template.md` to `_stories/<slug>.md`. Fill in the front matter, then write the Telugu text inside the `te` block and the English text inside the `en` block. Leave a blank line between paragraphs. Put pictures in `assets/images/<slug>/`, then commit and push. The site rebuilds in about a minute.
