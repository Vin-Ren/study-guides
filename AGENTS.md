# Agent instructions

## Purpose

This repository hosts static study guides on GitHub Pages. New material should be easy to find, work from its published URL, and keep all local resources with the guide.

## Repository conventions

- Use paths of the form `semester-<number>/<Course-or-subject>/<Guide-Name>/`.
- Use `index.html` as the entry point for every guide folder. Keep one guide (or a tightly related set) self-contained in its folder.
- Store local media in `assets/` within the guide folder. Preserve descriptive filenames and reference files with relative URLs (e.g. `assets/diagram.png`), never machine-specific absolute paths.
- Use UTF-8 text and portable, case-consistent names. Match the case of paths exactly; GitHub Pages runs on a case-sensitive filesystem.
- Prefer a standalone HTML page with embedded CSS/JS when practical. External libraries and fonts are allowed only when necessary; load them from reputable HTTPS CDNs and provide graceful fallbacks.
- Do not rename or remove existing guides or their assets unless explicitly requested. Avoid unrelated edits to existing guide content.
- Do not commit credentials, private course materials, or copyrighted source material unless the user confirms they have permission to publish it. GitHub Pages content is public.

## Adding a guide

1. Inspect the source material and establish what is safe and useful to publish.
2. Create the destination folder following the repository layout and add its `index.html` plus all required assets.
3. Update the root `index.html` guide directory and the `README.md` contents list.
4. Test every local asset reference. Check for missing files, broken links, and obvious browser-console/runtime errors when feasible.
5. Verify the page works under a project subpath (the repo URL includes `/study-guides/`); use relative asset links and avoid root-relative paths such as `/assets/...`.
6. Summarize the added path and any testing or deployment limitations.

## Git workflow

- Make focused changes and commit with a concise message.
- Publish by pushing to `main` only when authorized by the user.
- Never expose or print authentication tokens. Do not change repository visibility or GitHub Pages settings unless asked.
