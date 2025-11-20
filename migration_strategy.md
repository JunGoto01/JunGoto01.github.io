# Website Migration Strategy: Google Site to GitHub Pages

## 1. Project Goals
*   **Modernize**: Transition from Google Sites to a polished, professional static site hosted on GitHub Pages.
*   **Preserve SEO**: Maintain the high search ranking of the existing Google Site for "Jun Goto".
*   **Agentic Workflow**: Use Antigravity's Browser Agent for analysis, implementation, and verification.

## 2. Architecture & Design
*   **Platform**: GitHub Pages (Static Site).
*   **Technology**: Simple HTML/CSS or a lightweight static site generator (Jekyll/Hugo) as per preference for "simple text file editing".
*   **Key Sections**:
    *   Home / Bio
    *   Research (Papers, Abstracts)
    *   Teaching
    *   CV
    *   Contact
    *   (Optional) Datasets / Japanese content placeholder
*   **Design Aesthetic**: Clean, academic, responsive, typography-focused. References: Philipp M. Lutscher, Mark David Nieman.

## 3. Migration Workflow

### Phase 1: Analysis & Planning (Current)
1.  **Site Audit**: Use Browser Agent to crawl `https://sites.google.com/site/jungotoswebsite/home`.
2.  **Structure Mapping**: Document current content inventory and information architecture.
3.  **Design Proposal**: Create a specific implementation plan for the new site structure.

### Phase 2: Implementation
1.  **Scaffold**: Initialize project structure in `jun-goto-website`.
2.  **Develop**: Build core pages and styles.
3.  **Migrate Content**: Transfer text and links from the analysis artifact.
4.  **Verify**: Use Browser Agent to test layout and links locally (`localhost`).

### Phase 3: Deployment & SEO Transition
1.  **Deploy**: Push to GitHub and enable GitHub Pages.
2.  **Live Verification**: Browser Agent checks the live URL.
3.  **SEO "Front Door" Strategy**:
    *   **Do NOT delete** the old Google Site.
    *   Add a prominent banner/link to the top of the Google Site: *"This site is archived. Visit my new homepage at..."*
    *   Update external links (GRIPS, Scholar, ORCID) to point to the new GitHub URL.

## 4. Next Steps
*   [ ] Run Browser Agent to analyze the existing Google Site.
*   [ ] Draft the detailed Implementation Plan based on the audit.
