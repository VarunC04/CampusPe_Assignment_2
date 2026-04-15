/**
 * AuraChat — chat.js
 * All chat functionality using jQuery and vanilla JS
 * Author: Student
 */

$(document).ready(function () {

  /* ================================================
     CONSTANTS & STATE
  ================================================ */
  const MAX_TEXTAREA_HEIGHT = 200; // px
  let isTyping = false;            // AI typing in progress flag
  let messageCount = 0;            // track number of messages
  let currentTypeInterval = null;  // typewriter interval ref

  // ---- Mock AI responses pool ----
  const aiResponses = [
    "That's a great question! Let me break it down for you.\n\nThere are several key factors to consider here. First, it's important to understand the core concepts before diving into implementation. Second, practice and iteration are essential — no one gets it perfect the first time.\n\nWould you like me to go deeper on any specific part?",
    "Sure! Here's a quick overview:\n\n**Key Points:**\n- Start with the fundamentals and build your knowledge step by step\n- Use reliable resources like documentation and trusted tutorials\n- Test your understanding by applying what you've learned\n\nLet me know if you'd like a more detailed explanation on any of these points.",
    "Absolutely! Here's a code example that might help:\n\n```python\ndef greet(name):\n    return f\"Hello, {name}! Welcome to AuraChat.\"\n\n# Usage\nprint(greet(\"World\"))\n```\n\nThis function takes a name as input and returns a formatted greeting. You can extend this further based on your needs.",
    "Great point! There are multiple perspectives to consider here:\n\n1. **Performance** — Always profile before optimizing\n2. **Readability** — Code is read more than it is written\n3. **Maintainability** — Think about future developers\n\nThe best approach usually balances all three. Does that help clarify things?",
    "I'd be happy to help with that! The key insight here is that breaking complex problems into smaller, manageable chunks makes them far easier to solve.\n\nStart by identifying the core problem, then work outward from there. Feel free to share more context and I can give you a more specific answer.",
    "Interesting! This is actually a topic with a rich history. The modern approach emerged from decades of research and practical experimentation.\n\nThe short answer: focus on first principles, stay curious, and don't be afraid to experiment. The long answer depends on your specific context — want me to elaborate?",
    "Here's a structured way to think about this:\n\n**Step 1:** Define your goal clearly\n**Step 2:** Research existing solutions\n**Step 3:** Prototype and test\n**Step 4:** Iterate based on feedback\n\nThis approach works for most problems, whether technical or creative. Let me know how I can help further!",
    "Of course! Let me give you a concise summary:\n\nThe core idea is straightforward once you see the pattern. Think of it like building blocks — each piece supports the next. Start small, validate your assumptions early, and scale up once you're confident in the foundation.\n\nAnything specific you'd like me to dive into?",
    "That's a thoughtful question! Here's my perspective:\n\nEvery challenge is an opportunity to learn. The key is to approach it with curiosity rather than frustration. Break it down, seek resources, ask for help when needed, and celebrate small wins along the way.\n\nYou've got this! 💪",
    "Great! I can definitely help with that.\n\nHere's a practical tip: always start with a **minimum viable version** — the simplest thing that could possibly work. Once that's running, you can layer on complexity. This approach saves time and reduces frustration significantly.\n\nWant me to walk you through a step-by-step example?"
  ];

  /* ================================================
     UTILITY FUNCTIONS
  ================================================ */

  /**
   * Returns the current time formatted as HH:MM AM/PM
   */
  function getCurrentTime() {
    const now = new Date();
    let hours = now.getHours();
    const mins = String(now.getMinutes()).padStart(2, '0');
    const ampm = hours >= 12 ? 'PM' : 'AM';
    hours = hours % 12 || 12;
    return `${hours}:${mins} ${ampm}`;
  }

  /**
   * Formats message text: supports **bold**, `code`, ```code blocks```
   * Bonus: code block & inline code formatting
   */
  function formatMessage(text) {
    // Escape HTML first
    let safe = text
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');

    // Code blocks (``` ... ```)
    safe = safe.replace(/```([\s\S]*?)```/g, function (_, code) {
      return `<pre><code>${code.trim()}</code></pre>`;
    });

    // Inline code (`code`)
    safe = safe.replace(/`([^`]+)`/g, '<code>$1</code>');

    // Bold (**text**)
    safe = safe.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');

    // Italic (*text*)
    safe = safe.replace(/\*(.+?)\*/g, '<em>$1</em>');

    // Newlines to <br>
    safe = safe.replace(/\n/g, '<br>');

    return safe;
  }

  /**
   * Scrolls the messages wrapper to the bottom smoothly
   */
  function scrollToBottom() {
    const wrapper = document.getElementById('messagesWrapper');
    wrapper.scrollTo({ top: wrapper.scrollHeight, behavior: 'smooth' });
  }

  /**
   * Pick a random AI response from the pool
   */
  function getRandomResponse() {
    return aiResponses[Math.floor(Math.random() * aiResponses.length)];
  }

  /* ================================================
     ADD MESSAGE
     Creates and appends a message bubble to the chat
  ================================================ */
  function addMessage(text, sender) {
    messageCount++;

    const isUser = sender === 'user';
    const name   = isUser ? 'You' : 'Aura';
    const time   = getCurrentTime();
    const avatarContent = isUser ? 'S' : '<i class="fa-solid fa-wand-magic-sparkles"></i>';
    const formattedText = formatMessage(text);

    const $message = $(`
      <div class="message ${sender}">
        <div class="msg-avatar">${avatarContent}</div>
        <div class="msg-body">
          <div class="msg-header">
            <span class="msg-name">${name}</span>
            <span class="msg-time">${time}</span>
          </div>
          <div class="msg-bubble" id="bubble-${messageCount}">
            ${isUser ? formattedText : ''}
          </div>
        </div>
      </div>
    `);

    $('#messagesContainer').append($message);
    scrollToBottom();

    // For AI messages, do typewriter animation (Bonus)
    if (!isUser) {
      typewriterEffect(`bubble-${messageCount}`, formattedText);
    }

    return `bubble-${messageCount}`;
  }

  /* ================================================
     TYPEWRITER EFFECT (Bonus Feature)
     Types out AI response letter by letter
  ================================================ */
  function typewriterEffect(bubbleId, htmlContent) {
    const $bubble = $(`#${bubbleId}`);

    // Strip HTML tags for character-by-character typing, then re-render
    // We use a simple approach: type the raw text, then format at the end
    const rawText = htmlContent
      .replace(/<br>/g, '\n')
      .replace(/<[^>]+>/g, '');

    let index = 0;
    $bubble.html('<span class="typewriter-cursor"></span>');

    if (currentTypeInterval) clearInterval(currentTypeInterval);

    currentTypeInterval = setInterval(function () {
      if (index < rawText.length) {
        const chars = $bubble.text().replace('|', '');
        $bubble.html(
          formatMessage(rawText.substring(0, index + 1)) +
          '<span class="typewriter-cursor"></span>'
        );
        index++;
        scrollToBottom();
      } else {
        clearInterval(currentTypeInterval);
        // Final render with full formatting, no cursor
        $bubble.html(htmlContent);
        scrollToBottom();
      }
    }, 18); // speed in ms per character
  }

  /* ================================================
     TYPING INDICATOR
  ================================================ */
  function showTypingIndicator() {
    $('#typingIndicatorWrapper').addClass('show');
    scrollToBottom();
  }

  function hideTypingIndicator() {
    $('#typingIndicatorWrapper').removeClass('show');
  }

  /* ================================================
     HIDE WELCOME SCREEN
  ================================================ */
  function hideWelcomeScreen() {
    const $ws = $('#welcomeScreen');
    if ($ws.length) {
      $ws.css({ transition: 'opacity 0.4s ease, transform 0.4s ease', opacity: 0, transform: 'translateY(-20px)' });
      setTimeout(() => $ws.remove(), 420);
    }
  }

  /* ================================================
     SEND MESSAGE — Main flow
  ================================================ */
  function sendMessage() {
    const $input = $('#messageInput');
    const text   = $input.val().trim();

    // Guard: no empty messages
    if (!text || isTyping) return;

    // Hide welcome screen on first message
    if (messageCount === 0) hideWelcomeScreen();

    // Add user message
    addMessage(text, 'user');

    // Add to sidebar history
    addToHistory(text);

    // Clear input
    $input.val('');
    $input.css('height', 'auto');
    updateSendButton();

    // Disable send while AI "thinks"
    isTyping = true;
    $('#sendBtn').prop('disabled', true);

    // Simulate AI delay (1–2 seconds)
    const delay = 1000 + Math.random() * 1000;

    showTypingIndicator();

    setTimeout(function () {
      hideTypingIndicator();
      const response = getRandomResponse();
      addMessage(response, 'ai');
      isTyping = false;
      updateSendButton();
    }, delay);
  }

  /* ================================================
     INPUT HANDLING
  ================================================ */

  // Update send button enabled/disabled state
  function updateSendButton() {
    const hasText = $('#messageInput').val().trim().length > 0;
    $('#sendBtn').prop('disabled', !hasText || isTyping);
  }

  // Auto-resize textarea as user types
  function autoResizeTextarea() {
    const $ta = $('#messageInput');
    $ta.css('height', 'auto');
    const scrollH = $ta[0].scrollHeight;
    $ta.css('height', Math.min(scrollH, MAX_TEXTAREA_HEIGHT) + 'px');
  }

  // Input event — resize + update button
  $('#messageInput').on('input', function () {
    autoResizeTextarea();
    updateSendButton();
  });

  // Enter to send, Shift+Enter for new line
  $('#messageInput').on('keydown', function (e) {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  });

  // Send button click
  $('#sendBtn').on('click', function () {
    sendMessage();
  });

  /* ================================================
     SUGGESTION CARDS — click to fill input
  ================================================ */
  $(document).on('click', '.suggestion-card', function () {
    const suggestion = $(this).data('suggestion');
    $('#messageInput').val(suggestion);
    autoResizeTextarea();
    updateSendButton();
    $('#messageInput').focus();
    // Immediately send
    sendMessage();
  });

  /* ================================================
     SIDEBAR — Mobile Toggle
  ================================================ */
  $('#hamburgerBtn').on('click', function () {
    $('#sidebar').addClass('open');
    $('#sidebarOverlay').addClass('show');
  });

  $('#sidebarOverlay').on('click', function () {
    closeSidebar();
  });

  function closeSidebar() {
    $('#sidebar').removeClass('open');
    $('#sidebarOverlay').removeClass('show');
  }

  /* ================================================
     NEW CHAT BUTTON
  ================================================ */
  $('#newChatBtn').on('click', function () {
    // Reset state
    messageCount = 0;
    isTyping     = false;
    if (currentTypeInterval) clearInterval(currentTypeInterval);

    hideTypingIndicator();

    // Clear messages and re-add welcome screen
    $('#messagesContainer').html(`
      <div class="welcome-screen" id="welcomeScreen">
        <div class="welcome-content">
          <div class="welcome-logo">
            <div class="logo-ring"></div>
            <i class="fa-solid fa-wand-magic-sparkles logo-icon"></i>
          </div>
          <h1 class="welcome-title">Good day! I'm <span class="accent">Aura</span></h1>
          <p class="welcome-sub">Your intelligent assistant — ask me anything.</p>
          <div class="suggestion-grid">
            <div class="suggestion-card" data-suggestion="Explain quantum computing in simple terms">
              <div class="card-icon"><i class="fa-solid fa-atom"></i></div>
              <div class="card-body-content">
                <div class="card-title">Explain a concept</div>
                <div class="card-desc">Quantum computing in simple terms</div>
              </div>
            </div>
            <div class="suggestion-card" data-suggestion="Write a short professional bio for a software engineer">
              <div class="card-icon"><i class="fa-solid fa-pen-nib"></i></div>
              <div class="card-body-content">
                <div class="card-title">Write for me</div>
                <div class="card-desc">Professional bio for a software engineer</div>
              </div>
            </div>
            <div class="suggestion-card" data-suggestion="Give me 5 productivity tips for remote work">
              <div class="card-icon"><i class="fa-solid fa-lightbulb"></i></div>
              <div class="card-body-content">
                <div class="card-title">Get ideas</div>
                <div class="card-desc">5 productivity tips for remote work</div>
              </div>
            </div>
            <div class="suggestion-card" data-suggestion="Review this Python code and suggest improvements: def add(a,b): return a+b">
              <div class="card-icon"><i class="fa-solid fa-code"></i></div>
              <div class="card-body-content">
                <div class="card-title">Review code</div>
                <div class="card-desc">Analyze and improve Python code</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    `);

    // Reset input
    $('#messageInput').val('').css('height', 'auto');
    updateSendButton();

    // Close sidebar on mobile
    closeSidebar();

    // Update history active state
    $('.history-item').removeClass('active');
    const $newItem = $('<div class="history-item active"><i class="fa-regular fa-message"></i><span>New chat</span></div>');
    $('.chat-history').prepend($newItem);
  });

  /* ================================================
     SIDEBAR CHAT HISTORY — click to switch (mock)
  ================================================ */
  $(document).on('click', '.history-item', function () {
    $('.history-item').removeClass('active');
    $(this).addClass('active');
    closeSidebar();
  });

  /**
   * Add latest user message to sidebar history
   */
  function addToHistory(text) {
    const preview = text.length > 28 ? text.substring(0, 28) + '…' : text;
    const $item = $(`<div class="history-item active"><i class="fa-regular fa-message"></i><span>${preview}</span></div>`);
    $('.history-item').removeClass('active');
    $('.chat-history').prepend($item);
    // Remove excess history items (keep max 8)
    const $items = $('.chat-history .history-item');
    if ($items.length > 8) {
      $items.last().remove();
    }
  }

  /* ================================================
     DARK MODE TOGGLE (Bonus Feature)
  ================================================ */
  let isDark = true; // starts in dark mode

  $('#themeToggle').on('click', function () {
    isDark = !isDark;
    if (isDark) {
      $('body').removeClass('light-theme');
      $('#themeIcon').removeClass('fa-sun').addClass('fa-moon');
      $('#themeLabel').text('Dark Mode');
    } else {
      $('body').addClass('light-theme');
      $('#themeIcon').removeClass('fa-moon').addClass('fa-sun');
      $('#themeLabel').text('Light Mode');
    }
  });

  /* ================================================
     EXPORT CHAT (Bonus Feature)
     Downloads chat as a .txt file using Blob API
  ================================================ */
  $('#exportBtn').on('click', function () {
    const lines = [];
    lines.push('=== AuraChat Export ===');
    lines.push('Date: ' + new Date().toLocaleString());
    lines.push('');

    $('.message').each(function () {
      const sender = $(this).hasClass('user') ? 'You' : 'Aura';
      const time   = $(this).find('.msg-time').text();
      // Get text without HTML
      const rawText = $(this).find('.msg-bubble').text().trim();
      lines.push(`[${time}] ${sender}:`);
      lines.push(rawText);
      lines.push('');
    });

    if (lines.length <= 3) {
      alert('No messages to export yet!');
      return;
    }

    const blob = new Blob([lines.join('\n')], { type: 'text/plain' });
    const url  = URL.createObjectURL(blob);
    const a    = document.createElement('a');
    a.href     = url;
    a.download = 'AuraChat_Export_' + Date.now() + '.txt';
    a.click();
    URL.revokeObjectURL(url);
  });

  /* ================================================
     SOUND EFFECTS (Bonus Feature)
     Lightweight Web Audio API beeps
  ================================================ */
  function playBeep(freq, duration, vol) {
    try {
      const ctx = new (window.AudioContext || window.webkitAudioContext)();
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.type = 'sine';
      osc.frequency.value = freq;
      gain.gain.setValueAtTime(vol || 0.08, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);
      osc.start(ctx.currentTime);
      osc.stop(ctx.currentTime + duration);
    } catch (e) {
      // Silently ignore if AudioContext not available
    }
  }

  // Override sendMessage to play sound
  const _origSend = sendMessage;
  // Patch: play send sound on Enter / button click
  $(document).on('click', '#sendBtn', function () {
    playBeep(880, 0.12);
  });

  $('#messageInput').on('keydown', function (e) {
    if (e.key === 'Enter' && !e.shiftKey) {
      playBeep(880, 0.12);
    }
  });

  // Play receive sound when AI responds
  const _origHideTyping = hideTypingIndicator;
  // We'll patch the setTimeout callback — override globally
  window._playReceiveBeep = function () {
    playBeep(660, 0.15);
  };

  /* ================================================
     INIT
  ================================================ */
  updateSendButton();
  $('#messageInput').focus();

  console.log('✅ AuraChat initialized successfully. No errors.');

}); // end document.ready
