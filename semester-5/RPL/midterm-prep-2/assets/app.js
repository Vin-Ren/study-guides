(() => {
  const questions = [...document.querySelectorAll('.question')];
  const progress = document.getElementById('progress-fill');
  const scoreResult = document.getElementById('score-result');
  const weakTopics = document.getElementById('weak-topics');

  function updateProgress() {
    const available = document.documentElement.scrollHeight - window.innerHeight;
    progress.style.width = `${available > 0 ? Math.min(100, scrollY / available * 100) : 0}%`;
  }
  addEventListener('scroll', updateProgress, { passive: true });
  addEventListener('resize', updateProgress);
  updateProgress();

  function selectedAnswer(card) {
    return card.querySelector('input[type="radio"]:checked');
  }
  function reveal(card) {
    const chosen = selectedAnswer(card);
    const feedback = card.querySelector('.feedback');
    if (!chosen) {
      feedback.hidden = false;
      feedback.classList.remove('is-correct', 'is-wrong');
      feedback.firstElementChild.textContent = 'Select an answer first.';
      return false;
    }
    const correct = Number(chosen.value) === Number(card.dataset.answer);
    feedback.hidden = false;
    feedback.classList.toggle('is-correct', correct);
    feedback.classList.toggle('is-wrong', !correct);
    feedback.firstElementChild.textContent = `${correct ? 'Correct' : 'Review this'} · Answer: ${'ABCD'[Number(card.dataset.answer)]}`;
    return correct;
  }
  questions.forEach(card => card.querySelector('.check-answer').addEventListener('click', () => reveal(card)));

  document.getElementById('score-quiz').addEventListener('click', () => {
    let answered = 0;
    let correct = 0;
    const missed = [];
    questions.forEach((card, index) => {
      const chosen = selectedAnswer(card);
      if (chosen) {
        answered += 1;
        if (reveal(card)) correct += 1;
        else missed.push(`Q${index + 1}: ${card.dataset.topic}`);
      }
    });
    scoreResult.textContent = `${correct} correct out of ${answered} answered (${questions.length} total).`;
    weakTopics.textContent = missed.length ? `Review ${missed.join('; ')}. Send me these question numbers for a focused drill.` : (answered === questions.length ? 'No missed questions. Ask me for harder scenarios on any topic you want to stretch.' : 'Answer more questions to identify weak topics.');
    document.getElementById('practice').scrollIntoView({ behavior: 'smooth' });
  });

  document.getElementById('reset-quiz').addEventListener('click', () => {
    questions.forEach(card => {
      card.querySelectorAll('input[type="radio"]').forEach(input => { input.checked = false; });
      const feedback = card.querySelector('.feedback');
      feedback.hidden = true;
      feedback.classList.remove('is-correct', 'is-wrong');
      feedback.firstElementChild.textContent = `Answer: ${'ABCD'[Number(card.dataset.answer)]}`;
    });
    scoreResult.textContent = '';
    weakTopics.textContent = 'Your missed topics will appear here after you score the quiz.';
  });

  document.getElementById('copy-weak').addEventListener('click', async event => {
    try {
      await navigator.clipboard.writeText(weakTopics.textContent);
      event.currentTarget.textContent = 'Copied';
      setTimeout(() => { event.currentTarget.textContent = 'Copy my weak topics'; }, 1800);
    } catch {
      event.currentTarget.textContent = 'Select and copy the text above';
    }
  });

  // Mermaid is optional: plain code blocks remain readable when the CDN is unavailable.
  const diagrams = [...document.querySelectorAll('pre code.language-mermaid')];
  if (diagrams.length) {
    diagrams.forEach(code => {
      const host = document.createElement('div');
      host.className = 'mermaid';
      host.textContent = code.textContent;
      code.parentElement.replaceWith(host);
    });
    const loader = document.createElement('script');
    loader.src = 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js';
    loader.onload = () => {
      try { window.mermaid.initialize({ startOnLoad: false, theme: 'neutral', securityLevel: 'strict' }); window.mermaid.run({ querySelector: '.mermaid' }); }
      catch { /* Diagram source remains visible. */ }
    };
    document.head.append(loader);
  }
})();
