const questions = {
  question: "運が良い方だ",

  yes: {
    question: "常識や伝統なんてゴミだ",
    yes: {
      question: "出世欲が強く仕事に熱中出来るが、あそびも大好きだ",
      yes: { guess: "hideyoshi" },
      no: { guess: "nobunaga" }
    },
    no: {
      question: "心配性である",
      yes: { guess: "ieyasu" },
      no: { guess: "tadakatu" }
    }
  },

  no: {
    question: "注意散漫になり、ミスをすることがある",
    yes: { guess: "yoshimoto" },
    no: {
      question: "たまに冷静さを失い無鉄砲になる",
      yes: { guess: "katsuyori" },
      no: {
        question: "忠誠心がある。  上司や組織に貢献する事が好きだ",
        yes: {
          question: "人から好かれるタイプだ",
          yes: { guess: "kanetsugu" },
          no: { guess: "mitsunari" }
        },
        no: { guess: "mitsuhide" }
      }
    }
  }

};

let currentNode = questions;

const questionText = document.getElementById('question-text');
const yesBtn = document.getElementById('yes-btn');
const noBtn = document.getElementById('no-btn');
const result = document.getElementById('result');

function updateUI() {
  if (currentNode.guess) {
    questionText.textContent = "診断完了";
    result.style.display = 'block';
    yesBtn.style.display = 'none';
    noBtn.style.display = 'none';
  } else {
    questionText.textContent = currentNode.question;
    result.style.display = 'none';
  }
}

yesBtn.addEventListener('click', () => {
  currentNode = currentNode.yes;
  updateUI();
});

noBtn.addEventListener('click', () => {
  currentNode = currentNode.no;
  updateUI();
});

result.onclick = function () {
  window.location.href = '/result?id=' + encodeURIComponent(currentNode.guess);
};

updateUI();

