# AuraChat — AI Chat Interface
**CampusPe Gen AI Assignment | Student Submission**

## Overview
AuraChat is a modern, responsive AI chat interface inspired by Claude and ChatGPT. Built with HTML5, CSS3, JavaScript, jQuery, and Bootstrap 5.

## Features Implemented
### Core Tasks
- ✅ **Task 1** — Semantic HTML5 structure, welcome screen with 4 suggestion cards, input area
- ✅ **Task 2** — CSS variables, message bubbles, animations, full responsive design
- ✅ **Task 3** — Message display, input handling, mock AI responses with typing indicator
- ✅ **Task 4** — Sidebar (260px fixed), chat history, mobile hamburger menu + overlay

### Bonus Features
- ✅ **Dark/Light mode toggle** — smooth theme transition with CSS variables
- ✅ **Typewriter animation** — AI responses type out letter by letter
- ✅ **Code block formatting** — supports `inline code` and \`\`\`code blocks\`\`\`
- ✅ **Export chat** — downloads conversation as .txt using Blob API
- ✅ **Sound effects** — subtle beeps on send/receive using Web Audio API
- ✅ **Custom scrollbar** — styled with CSS

## File Structure
```
YourName_ChatUI/
├── index.html          ← Main HTML file
├── css/
│   └── style.css       ← All custom styles (well-organized, commented)
├── js/
│   └── chat.js         ← All JavaScript + jQuery functionality
├── screenshots/
│   ├── desktop.png
│   ├── tablet.png
│   └── mobile.png
└── README.md           ← This file
```

## How to Run
1. Unzip the project folder
2. Open `index.html` in any modern browser (Chrome, Firefox, Safari, Edge)
3. No server required — it's fully client-side
4. Test responsiveness using browser DevTools (F12 → Toggle device toolbar)

## Technologies Used
| Technology | Version | Purpose |
|---|---|---|
| HTML5 | — | Semantic markup |
| CSS3 | — | Custom styles, animations, variables |
| JavaScript (ES6+) | — | Core logic |
| jQuery | 3.7.1 | DOM manipulation |
| Bootstrap | 5.3.3 | Responsive grid |
| Font Awesome | 6.5.1 | Icons |
| Google Fonts | — | Syne + DM Sans |

## Design Choices
- **Fonts:** Syne (display/headings) + DM Sans (body) — distinctive and readable
- **Color scheme:** Deep navy/slate dark theme with violet accent (#7c6af7)
- **Light mode:** Clean off-white with matching violet accent
- **Animations:** Subtle fade-in for messages, bouncing typing dots, typewriter AI output

## Testing Checklist
- [x] Messages appear correctly when sent
- [x] User and AI messages are visually different
- [x] Send button disabled when input is empty
- [x] Send button enabled when there is text
- [x] Enter key sends message; Shift+Enter creates new line
- [x] Typing indicator shows and hides correctly
- [x] Auto-scroll works when new messages appear
- [x] Textarea auto-resizes as user types
- [x] Suggestion cards are clickable (auto-fill + send)
- [x] Welcome screen hides after first message
- [x] Sidebar appears and hides on mobile
- [x] Layout is responsive from 320px to 1920px
- [x] No console errors

---
*Submitted for CampusPe Gen AI Assignment — April 2026*
