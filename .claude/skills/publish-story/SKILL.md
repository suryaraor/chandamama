---
name: publish-story
description: Turn the raw stories dropped into input-story/ into bilingual (Telugu + English) Chandamama-style pages for the GitHub Pages site, with their illustrations placed through the story, then archive the originals and publish. Use when the user says "publish the story", "convert input-story", "add the new story", runs /publish-story, or has put a new story file or images into input-story/.
---

# Publish a story from input-story/

The repo is a Jekyll site published from the `gh-pages` branch to https://suryaraor.github.io/chandamama/. Every story is one Markdown file in `_stories/` that holds **both** a Telugu and an English version; a switch in the masthead flips between them. Your job is to take whatever the user dropped into `input-story/`, produce that file plus its images, archive the originals, and publish.

Repo root: `C:\Surya\GitHub\chandamama` (Bash: `/c/Surya/GitHub/chandamama`).

## 1. Find the stories

List `input-story/` recursively, ignoring `input-story/archive/` if it exists. Work out which files make up each story:

- **A subfolder is one story.** All text and images inside it belong together.
- **Loose files at the top level:** if there is one text file, it and every loose image form one story. If there are several text files, match images to stories by file-name prefix (`foo.md` ↔ `foo-1.jpg`). If that doesn't settle it, look at the images and match them by content. If you still can't tell, ask the user.
- Text can be `.md`, `.txt`, `.docx` (`pandoc -t gfm file.docx`), `.pdf` (Read tool) or `.rtf`/`.odt` (pandoc). Images can be `.jpg/.jpeg/.png/.webp/.gif`. Skip anything else and say so.
- If `input-story/` holds nothing to convert, say so and stop.

Before you write anything, check `_stories/` for a story with the same title. If you find one, ask whether to replace it or skip it. Never overwrite one silently.

## 2. Read the story and look at every image

Read the text in full. Open **every** image with the Read tool, because you need to know what each one shows in order to place it.

Find out which language the text is in. Telugu script is U+0C00–U+0C7F. The input may be Telugu only, English only, or both. If both languages are present, take each version as given.

Pull out:
- **Title.** Often it's the first line, may be prefixed by `తెలుగు పేరు:` / `Title:`, or may appear with the English source title in brackets. Drop that prefix.
- **Moral.** A trailing `నీతి:` / `Moral:` line. If there isn't one, leave `moral` out rather than inventing one.
- **Source.** If the story is a retelling of a known tale (e.g. "The Legend of Sleepy Hollow"), put it in `original`.
- **Author.** Use the name the user gives. Otherwise use the `author` from the most recent file in `_stories/` and mention that you did.

**Paragraph repair.** Drafts often arrive with their paragraphs run together (`...నమ్మకం.ఆ పల్లెలో...`) or with the title glued to the first sentence. Restore the breaks at sentence ends where the scene or speaker changes, and strip any duplicated title. **Do not otherwise edit the author's words.** Fixing breaks is fine; rewriting sentences is not. If you spot an obvious typo, mention it in your summary instead of silently "fixing" it.

## 3. Write the missing language

Translate the story into whichever language is missing, so both versions tell the same story paragraph by paragraph.

- **Telugu:** the classic Chandamama voice. Open with అనగనగా…, keep sentences simple and warm, use spoken-literary Telugu a child can read aloud, and keep foreign names transliterated the same way throughout (ఇకాబోడ్ క్రేన్).
- **English:** a classic storybook voice ("Once upon a time…") in plain, vivid sentences suitable for children. Don't make it more ornate than the Telugu.
- Keep the same number of paragraphs in the same order, so an illustration sits at the same point in both versions.
- Translate the title, moral, category and summary too. Use a transliterated name for `author_en` (సూర్య → Surya).

## 4. Prepare the images

Choose a slug: a short, lowercase, hyphenated romanisation of the Telugu title (తలలేని రౌతు → `talaleni-rauthu`). It becomes both the URL and the image folder.

Run the optimizer. It scales images down to a 1600px maximum and compresses them; raw uploads are often 4 MB or more:

```bash
python .claude/skills/publish-story/scripts/optimize_images.py assets/images/<slug> input-story/<files...>
```

It prints each output path, its size in pixels and its file size. Then decide where each image goes:

- **Cover:** a file named like `title`/`cover`, or a portrait image showing the title lettering. It goes in the `image:` front matter field and is shown at the top of the story and on the home-page card. Don't place it inside the body as well.
- **Scene images** go just **before** the paragraph whose events they show, in **both** language blocks, each with a caption in that language. Spread them through the story; don't stack two images next to each other.
- If there is no cover-like image, use the most striking scene as `image:` and still place the rest in the body.

## 5. Write `_stories/<slug>.md`

Use this exact shape. The `te`/`en` classes are what the language switch hides and shows, and `markdown="1"` lets kramdown render the Markdown inside the divs.

```markdown
---
title: తెలుగు శీర్షిక
title_en: English Title
author: సూర్య
author_en: Surya
date: YYYY-MM-DD            # today
category: జానపద కథ          # జానపద కథ, పంచతంత్రం, అనువాద కథ (retold foreign tale), పురాణ కథ, సొంత కథ …
category_en: Folk Tale      # Folk Tale, Panchatantra, Retold Classic, Mythology, Original Story …
original: The Legend of Sleepy Hollow   # only for retellings
image: /assets/images/<slug>/title.jpg  # optional cover
summary: ఒకటి రెండు వాక్యాల్లో కథ పరిచయం — ముగింపు చెప్పకుండా.
summary_en: A one- or two-sentence teaser that doesn't give away the ending.
moral: తెలుగు నీతి.
moral_en: The moral in English.
---

<div class="te" markdown="1">

మొదటి పేరా…

<figure>
  <img src="{{ site.baseurl }}/assets/images/<slug>/image-1.jpg" alt="చిత్ర వివరణ" width="1600" height="1195" loading="lazy">
  <figcaption>చిత్రానికి చిన్న శీర్షిక</figcaption>
</figure>

తర్వాతి పేరా…

</div>

<div class="en" markdown="1">

First paragraph…

<figure>
  <img src="{{ site.baseurl }}/assets/images/<slug>/image-1.jpg" alt="Image description" width="1600" height="1195" loading="lazy">
  <figcaption>A short caption</figcaption>
</figure>

Next paragraph…

</div>
```

Rules:
- Leave a blank line after every opening `<div …>` and before every `</div>`, and a blank line between paragraphs. Don't indent paragraphs, because four leading spaces turn them into code blocks.
- Take `width`/`height` from the optimizer output. They stop the page from jumping while images load.
- Always write image paths as `{{ site.baseurl }}/assets/...` inside the body. Front matter `image:` has no baseurl, because the layout adds it.
- Put a YAML value in quotes if it contains `:` or begins with a quote mark.
- Don't add the moral to the body. The layout shows it in the నీతి box.

## 6. Archive the originals

Move (don't copy) everything that belonged to the story out of `input-story/` into `archive/<date>-<slug>/`, at the repo root and **not** inside `input-story/`:

```bash
mkdir -p archive/<date>-<slug> && mv input-story/<files...> archive/<date>-<slug>/
```

`archive/` and `input-story/` are git-ignored and excluded from Jekyll, so the raw originals stay on this machine and are never published. Remove a subfolder of `input-story/` once it is empty. Leave anything you didn't convert where it is.

## 7. Check, publish, verify

1. Sanity-check the new file: the front matter parses (`python -c "import yaml,sys; yaml.safe_load(open(sys.argv[1],encoding='utf-8').read().split('---')[1])" _stories/<slug>.md`). Both `<div class="te"` and `<div class="en"` are present. Every image path in the file exists under `assets/images/<slug>/`.
2. Commit only the story file and its image folder:
   ```bash
   git add _stories/<slug>.md assets/images/<slug> && git commit -m "Add story: <English title>" && git push
   ```
   End the commit message with the co-author line from the current session's attribution instructions.
3. Wait for the Pages build: `gh run list -L 1` for the run id, then `gh run watch <id> --exit-status`. Next, confirm the page answers 200 with `curl -s -o /dev/null -w "%{http_code}" https://suryaraor.github.io/chandamama/stories/<slug>/`. If the build fails, read `gh run view <id> --log-failed`, fix the problem and push again.

## 8. Report

Tell the user:
- the live link to each story,
- which language you translated into,
- where each image went (cover, or before which scene),
- what you archived and where,
- any typos you noticed but left alone, and anything you skipped.
