# చందమామ

Telugu stories in the classic Chandamama style, published with GitHub Pages (Jekyll).

**Site:** https://suryaraor.github.io/chandamama/

## Writing a new story

1. Copy `story-template.md` into `_stories/` and give it a short English file name, e.g. `_stories/telivaina-kundelu.md`. The file name becomes the URL.
2. Fill in the front matter:

   | Field      | Required | Example                     |
   |------------|----------|-----------------------------|
   | `title`    | yes      | `తెలివైన కుందేలు`            |
   | `author`   | no       | `సూర్య`                      |
   | `date`     | yes      | `2026-10-22` (sorts the list, newest first) |
   | `category` | no       | `జానపద కథ`, `పంచతంత్రం`, `భేతాళ కథ` |
   | `image`    | no       | `/assets/images/kundelu.jpg` |
   | `moral`    | no       | shown in a నీతి box at the end |

3. Write the story below the `---` in plain Telugu. Leave a blank line between paragraphs.
4. Put pictures in `assets/images/`. Use `![వివరణ](/chandamama/assets/images/pic.jpg)` to place one inside the story.
5. Commit and push to `gh-pages`. The site rebuilds in about a minute.

You can also do all of this from the GitHub website: open `_stories/`, click **Add file → Create new file**, paste the template, and commit.
