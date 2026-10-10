# Contributing a study guide

This repository is a public static site. Before adding content, confirm the material is appropriate to publish publicly and that you have the right to share it.

## Folder structure

```text
study-guides/
├── index.html                         # Published guide directory
├── semester-5/
│   └── RPL/
│       └── Midterm-Prep/
│           ├── index.html             # Guide entry point
│           └── assets/                # Images and other local files
└── semester-<n>/...
```

Use `semester-<n>/<Course-or-subject>/<Guide-Name>/index.html` for new entries. Keep assets beside the guide that uses them. Avoid spaces and case-only filename distinctions in new paths.

## Checklist

- [ ] `index.html` exists in the new guide directory.
- [ ] All required local files are included; references use relative paths.
- [ ] Links work from the GitHub Pages project URL, not only from a local file URL.
- [ ] Images have useful alternative text; headings and controls are usable on mobile.
- [ ] External dependencies use HTTPS and have sensible fallbacks where possible.
- [ ] Root `index.html` and `README.md` list the new guide.
- [ ] No secrets, personal data, or unauthorized source material are included.
- [ ] The guide was previewed and local asset paths checked.

## Preview

From the repository root:

```sh
python -m http.server 8000
```

Open `http://localhost:8000/` and navigate to the guide. A local server is preferable to opening files directly for pages that use fetch, modules, or browser storage.
