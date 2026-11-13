---
name: Miles Song
description: A quiet academic reading system in warm white, charcoal, and restrained vermilion.
colors:
  page: "#f7f7f2"
  surface: "#eeeee7"
  ink: "#292923"
  muted: "#686860"
  line: "#ddddd4"
  accent: "#a74326"
  soft-ink: "#505049"
  strong-line: "#b8b8ad"
  button-hover: "#45453b"
  nav-hover: "#efefe8"
  nav-current: "#eaeae2"
  accent-deep: "#742a13"
typography:
  display:
    fontFamily: "Inter, 'Segoe UI', 'Microsoft YaHei', sans-serif"
    fontSize: "clamp(32px, 3vw, 42px)"
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: "-0.035em"
  headline:
    fontFamily: "Inter, 'Segoe UI', 'Microsoft YaHei', sans-serif"
    fontSize: "30px"
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: "-0.03em"
  title:
    fontFamily: "Inter, 'Segoe UI', 'Microsoft YaHei', sans-serif"
    fontSize: "22px"
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: "-0.025em"
  lead:
    fontFamily: "Inter, 'Segoe UI', 'Microsoft YaHei', sans-serif"
    fontSize: "25px"
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: "-0.025em"
  body:
    fontFamily: "Inter, 'Segoe UI', 'Microsoft YaHei', sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.7
  body-compact:
    fontFamily: "Inter, 'Segoe UI', 'Microsoft YaHei', sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.75
  label:
    fontFamily: "Inter, 'Segoe UI', 'Microsoft YaHei', sans-serif"
    fontSize: "13px"
    fontWeight: 400
    lineHeight: 1.7
  action:
    fontFamily: "Inter, 'Segoe UI', 'Microsoft YaHei', sans-serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.4
  action-compact:
    fontFamily: "Inter, 'Segoe UI', 'Microsoft YaHei', sans-serif"
    fontSize: "13px"
    fontWeight: 400
    lineHeight: 1.4
  code:
    fontFamily: "Consolas, 'Liberation Mono', monospace"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: 1.8
rounded:
  mobile-nav: "3px"
  sm: "4px"
  avatar: "6px"
  pill: "100px"
spacing:
  "4": "4px"
  "8": "8px"
  "12": "12px"
  "16": "16px"
  "20": "20px"
  "24": "24px"
  "28": "28px"
  "32": "32px"
  "40": "40px"
  "48": "48px"
  "56": "56px"
  "60": "60px"
components:
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.page}"
    typography: "{typography.action}"
    rounded: "{rounded.pill}"
    padding: "8px 22px"
  button-primary-hover:
    backgroundColor: "{colors.button-hover}"
  button-compact:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.page}"
    typography: "{typography.action-compact}"
    rounded: "{rounded.pill}"
    padding: "7px 18px"
  button-copy:
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    padding: "8px"
  text-link:
    textColor: "{colors.ink}"
  text-link-hover:
    textColor: "{colors.accent}"
  section-link:
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: "8px 14px"
  section-link-hover:
    backgroundColor: "{colors.nav-hover}"
    textColor: "{colors.ink}"
  section-link-current:
    backgroundColor: "{colors.nav-current}"
    textColor: "{colors.ink}"
  research-row:
    textColor: "{colors.soft-ink}"
    typography: "{typography.body-compact}"
  content-inset:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.soft-ink}"
    rounded: "{rounded.sm}"
    padding: "24px 28px"
  publication-row:
    textColor: "{colors.ink}"
    padding: "32px 0"
  citation-panel:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
---

# Design System: Miles Song

## Overview

**Creative North Star: "The Quiet Academic Page"**

A warm, light reading surface gives academic content room to be understood. Cursor-influenced restraint appears in the charcoal Inter typography, compact pill actions, fine dividers, and almost imperceptible surface changes. English is the principal language; the Chinese name 宋明远 remains part of the public identity.

The visual hierarchy follows the content: a clear personal name, readable paragraphs, distinct section headings, and paper titles that lead their records. The real GitHub avatar is the identity image. Persistent navigation provides orientation while the page remains a continuous document.

**Key Characteristics:**

- Warm white and charcoal with small vermilion accents.
- Regular and medium Inter typography with compact, readable metadata.
- Unboxed reading rows, fine dividers, and occasional tonal insets.
- Persistent section context and native links and disclosures.

## Colors

The palette is warm and nearly neutral, with a muted vermilion accent. The frontmatter defines the implementation colors; the sidecar's tonal ramps are preview metadata.

### Primary

- **Muted Vermilion** (`accent`): selected destinations, venue names, link hover states, keyboard focus, and brief copy feedback.
- **Deep Vermilion** (`accent-deep`): hover emphasis on paper-resource links.

### Neutral

- **Warm Paper** (`page`): the page, opaque sticky header, and mobile navigation background; also text on charcoal actions.
- **Quiet Inset** (`surface`): contextual research notes and expanded citations.
- **Charcoal Ink** (`ink`): headings, emphasized author names, primary controls, and default links.
- **Reading Ink** (`soft-ink`): longer research descriptions, biography, and paper summaries.
- **Muted Ink** (`muted`): dates, supporting metadata, secondary identity text, and inactive navigation.
- **Fine Rule** (`line`): section, row, toolbar, and container boundaries.
- **Strong Rule** (`strong-line`): inline-link underlines and the scrollbar.
- **Action Hover** (`button-hover`): the lighter charcoal state of pill actions.
- **Navigation Hover** (`nav-hover`) and **Navigation Current** (`nav-current`): subtle neutral fills that distinguish hover from the section being read.

### Named Rules

**The Quiet Accent Rule.** Keep primary actions charcoal and content surfaces neutral; reserve vermilion for links, venue metadata, small identity details, and interaction feedback.

## Typography

**Display and Body Font:** locally hosted Inter, with Segoe UI, Microsoft YaHei, and sans-serif fallbacks.

**Chinese Identity Font:** Microsoft YaHei, PingFang SC, and sans-serif fallbacks.

**Code Font:** Consolas, Liberation Mono, and monospace fallbacks.

The type is restrained, with normal-weight prose and medium-weight headings. Slightly tightened heading tracking supplies distinction without decorative display styling. The wordmark uses a semibold weight (600); this exception does not extend to the reading hierarchy.

### Hierarchy

- **Display:** the personal name. The frontmatter records the wide-screen fluid size; narrower layouts use the observed overrides in Layout.
- **Headline:** primary section headings.
- **Title:** publication titles. Research subheadings use a smaller size (17px), while subsection headings use an intermediate size (21px).
- **Lead:** the introductory research statement, limited to a comfortable width (720px).
- **Body:** biography and general prose. Biography and section introductions are limited to a reading measure (72ch).
- **Body compact:** research descriptions and paper summaries.
- **Label:** dates and supporting metadata. Dates and years use tabular numerals. Author lists use the label size with more generous leading (1.85), becoming slightly tighter on phones (1.8).
- **Action / Action compact:** pill labels in the main content and header.
- **Code:** wrapped, selectable citation text.

The Chinese name is secondary to the English name, with normal weight, muted color, and slightly open tracking (0.05em). Text remains in its natural case. Link labels and venue metadata are not decorative all-capital overlines.

### Named Rules

**The Title First Rule.** A publication begins with its title, followed by venue and year, the complete author list, the summary, and resource actions.

## Layout

The page uses an equal-margin centered wrapper. On a standard desktop it is capped at a width (1152px), with a navigation column (176px), a gap (80px), and a flexible reading column. At a viewport width of 1440px, the reading column is 896px wide. The header is sticky and shares the same wrapper.

| Viewport | Outer gutter | Reading structure | Navigation |
| --- | --- | --- | --- |
| 1600px and wider | 48px | Wrapper up to 1200px; 176px rail; 96px gap | Sticky left rail |
| 1200–1599px | 48px | Wrapper up to 1152px; 176px rail; 80px gap | Sticky left rail |
| 901–1199px | 40px | 148px rail; 48px gap | Sticky left rail |
| 601–900px | 36px | One reading column | Sticky horizontal row below the header |
| 360–600px | 24px | One reading column | Compact horizontal row |
| 359px and narrower | 18px | One reading column | Compact horizontal row |

The desktop header height (76px) becomes more compact (64px) at the horizontal-navigation breakpoint. The left rail sits below the header, with its sticky top offset (164px) reduced on narrower desktops (140px). Horizontal navigation sits directly below the header and keeps every destination visible.

Sections are separated by fine rules and generous vertical space. Standard content sections use top and bottom padding (56px / 60px), reduced on phones (40px / 44px). Smaller repeated spaces come from the frontmatter scale. Anchored sections reserve space for sticky chrome with a scroll margin (112px on desktop; 144px at 900px and below).

Research and repository rows align a short heading column (228px) with prose across a gap (32px). The heading column becomes narrower (180px) below 1200px, then expands slightly (200px) in the single-column tablet layout; phones stack each heading above its description. News pairs a narrow date column (92px) with text, becoming more compact on phones (72px).

The profile name uses the display token on wide screens, with fixed overrides at the existing breakpoints: 38px at 1199px and below, 44px at 900px and below, 32px at 600px and below, and 28px at 359px and below. Phone section headings reduce to 27px, publication titles to 20px, and body text to 15px. The lead reduces to 23px on phones, with a line height of 1.5, and to 21px below 360px.

## Elevation & Depth

The system has no box shadows. Depth comes from opaque sticky layers, quiet inset fills, fine neutral rules, and whitespace. The page background continues through the header and horizontal navigation, so orientation remains visible without introducing a floating-card treatment.

### Named Rules

**The Flat Reading Rule.** Group content with spacing, fine dividers, and tonal insets; keep reading rows on the page surface.

## Shapes

The dominant geometry is rectangular. Reading rows have no enclosing card shape. Navigation and inset panels have small corners; the avatar remains a square image with gently softened corners. Only the main actions use the full pill shape.

Icons are inline, thin-stroke SVGs with rounded line caps and joins. They sit beside readable text labels. They communicate direction, external access, disclosure, or copying rather than serving as decoration.

## Components

### Pill actions

Compact and direct. The primary and compact variants share charcoal fill, warm-paper text, a matching border (1px), and the pill shape. The main action has a minimum height (46px); the header action remains at least 44px tall.

Hover lightens the charcoal fill and moves the action upward slightly (1px); pressing moves it downward (1px). Both use a short transition (160ms, ease). Phone actions use the compact label size and horizontal padding (18px).

### Text and inline links

Text actions have a minimum height (44px) and a small adjacent SVG where appropriate. Hover uses vermilion; external arrows move slightly in the indicated direction. Paper-resource links begin in vermilion and deepen with an underline on hover.

Links inside prose have visible neutral underlines at rest, with an underline offset (4px). Hover changes both text and underline to vermilion. Every keyboard-focusable control receives an accent outline (2px) with an offset (5px).

### Section navigation

The desktop rail uses muted text, small corners, and a minimum row height (46px). Hover introduces a very light neutral fill. The current section uses the stronger neutral fill, charcoal text, medium weight, and a small arrow.

On narrower screens, links share one horizontal row and retain a minimum height (44px). The arrow is hidden while the current fill and text treatment remain. The active location follows reading position through `aria-current="location"`; at the end of the document, the final section remains current. The underlying links remain ordinary section anchors.

### Reading rows

Research descriptions are unboxed and use aligned heading and prose columns. Repository rows add a fine top rule, a text link, and muted supporting technology text. News and education use compact date or year columns. Responsive stacking preserves reading order and avoids a card grid.

### Quiet inset

A contextual note uses the quiet inset fill, small corners, and generous internal padding from the component token. Its title is medium weight (16px); its supporting text is smaller (14px) with relaxed leading (1.8). Phone padding is reduced evenly (20px).

### Publication entry

The title leads a flat record. Venue and year sit below it, followed by authors, a short summary, and wrapped resource actions. Titles have a maximum width (750px), while author lists have a generous measure (90ch). The author's own name uses medium charcoal text within the muted author list.

A fine rule separates successive records. The first entry omits that rule and uses only a small top inset (4px). Subsequent rows use the component padding, reduced vertically on phones (28px).

### Citation disclosure and copy control

BibTeX opens through a native disclosure. Its SVG plus turns slightly (45 degrees) while open. The citation fills the available row width in a quiet inset with a fine border, small corners, and a compact toolbar.

Citation text wraps at available space and remains selectable. The copy control is a text button with a minimum height (44px), a small SVG, and a vermilion hover state. While copying it uses muted text and a wait cursor; success is announced briefly, and copy failure selects the citation for manual copying. This utility does not introduce a new filled-button treatment.

### Identity image and motion

Use the real GitHub avatar as the square profile image. Its desktop size (124px) adapts to the existing narrower layouts, reaching 82px on phones and 64px below 360px. Hover gently scales the image (1.025 over 220ms) inside its clipped frame.

Motion is limited to short state feedback, smooth anchor scrolling, and a single subtle profile entrance (550ms). Reduced-motion preferences disable animation and transitions and return scrolling to its immediate behavior.

## Do's and Don'ts

### Do:

- **Do** use the warm neutral palette and small vermilion accents for the roles defined above.
- **Do** keep headings medium weight and prose regular, with readable supporting metadata.
- **Do** place each paper title before its venue, year, authors, and resource actions.
- **Do** maintain visible section context, keyboard focus, and ordinary anchor destinations.
- **Do** keep research text in reading rows and use tonal insets for contextual detail.
- **Do** preserve the real GitHub avatar, English identity, and Chinese name.

### Don't:

- **Don't** promote venue names, dates, or invented labels into decorative overlines above titles.
- **Don't** turn the reading sequence into a grid of raised promotional cards.
- **Don't** replace the restrained Inter hierarchy with oversized decorative display type.
- **Don't** introduce synthetic identity imagery, ornamental icons, or unsupported content claims.
- **Don't** make paper access, basic navigation, or citation disclosure depend on animation.
