# Implementation Plan: Jun Goto's New Website

## Goal Description
Build a modern, responsive, and fast academic website hosted on GitHub Pages to replace the existing Google Site. The site will be built with **clean HTML5 and CSS3** to ensure long-term maintainability and ease of editing (no complex build steps required).

## User Review Required
> [!IMPORTANT]
> **Technology Choice**: I am proposing **Plain HTML/CSS** instead of a generator like Jekyll/Hugo for maximum simplicity. You can edit text directly in the HTML files.
> **PDF Strategy**: I will initially link to the existing external PDFs (Google Drive/Journal links) to keep the migration simple. We can move files to the repo later if desired.

## Proposed Changes

### Project Structure
We will create a simple multi-page structure:
```
jun-goto-website/
├── index.html          (Home)
├── research.html       (Publications & Working Papers)
├── teaching.html       (Lecture)
├── cv.html             (CV link/embed)
├── css/
│   └── style.css       (Global styles)
└── assets/
    └── images/         (Profile photo, etc.)
```

### [NEW] Core Files

#### [NEW] [index.html](file:///c:/Users/gotoj/git_project/jun-goto-website/index.html)
*   **Content**: Name, Affiliation, Research Fields, Contact Info.
*   **Design**: Clean hero section, simple typography.

#### [NEW] [research.html](file:///c:/Users/gotoj/git_project/jun-goto-website/research.html)
*   **Content**: List of Publications and Working Papers.
*   **Design**: Clean list layout with distinct styling for titles, authors, and abstracts.

#### [NEW] [teaching.html](file:///c:/Users/gotoj/git_project/jun-goto-website/teaching.html)
*   **Content**: List of courses.
*   **Design**: Simple card or list view.

#### [NEW] [cv.html](file:///c:/Users/gotoj/git_project/jun-goto-website/cv.html)
*   **Content**: Link to download CV PDF, potentially an embedded view or a summary HTML version.

#### [NEW] [style.css](file:///c:/Users/gotoj/git_project/jun-goto-website/css/style.css)
*   **Design System**:
    *   **Font**: Inter or Roboto (via Google Fonts) for a modern academic look.
    *   **Colors**: Neutral background (white/off-white), dark text, subtle accent color (e.g., a deep blue or slate).
    *   **Responsive**: Mobile-friendly navigation (hamburger menu on small screens).

## Verification Plan

### Automated Tests
*   None (Static site).

### Manual Verification
1.  **Local Preview**: Run a local server (e.g., `python -m http.server`) and use the Browser Agent to navigate all pages.
2.  **Responsiveness**: Check layout on mobile/desktop viewports.
3.  **Link Check**: Verify all external links (PDFs, Journals) work.
