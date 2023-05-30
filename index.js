const randomArr = (length) => {
  const arr = new Array(length);

  const randomNumber = () => {
    return Math.floor(Math.random() * 10);
  };

  for (let i = 0; i < length; i++) {
    arr[i] = randomNumber();
  }

  return arr;
};

const N = randomNumber();
const M = Math.floor(Math.random() * 10);

const findNumber = (N, M) => {
  const A = randomArr(N);
  const B = randomArr(M);

  B.forEach((i) => {
    if (!A[i] && !i) return;

    if (A.includes(i)) {
      i = 1;
    } else {
      i = 0;
    }

    console.log(i);
  });
};

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = null;

rl.on("line", function (line) {
  input = parseInt(line);

  rl.close();
}).on("close", function () {
  findNumber(input, input);

  process.exit();
});
