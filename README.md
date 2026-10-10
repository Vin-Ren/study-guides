# Study Guides

A collection of browser-friendly study guides, revision notes, and practice materials. The repository is published with GitHub Pages at <https://vin-ren.github.io/study-guides/>.

## Contents

- [Semester 5 — RPL — Midterm Prep](semester-5/RPL/Midterm-Prep/)

## Add a new guide

1. Choose a descriptive location following `semester-<n>/<Course-or-subject>/<Guide-Name>/`.
2. Put the page entry point in that folder as `index.html`.
3. Keep local images, stylesheets, scripts, and other resources alongside it (for example, in an `assets/` subfolder). Use relative paths so the guide works under GitHub Pages' project-site URL prefix.
4. Follow the detailed checklist in [AGENTS.md](AGENTS.md) and [CONTRIBUTING.md](CONTRIBUTING.md).
5. Commit and push to `main`. Pages deploys from the repository root; each guide is available at `https://vin-ren.github.io/study-guides/<path>/`.

## Local preview

Open a guide's `index.html` directly for simple self-contained pages. For pages using local fetches or browser modules, run a local static server from the repository root, for example:

```sh
python -m http.server 8000
```

Then open `http://localhost:8000/semester-5/RPL/Midterm-Prep/`.

## Publishing

GitHub Pages is configured to publish the `main` branch from `/`.
