let esl_symbolic = require("esl_symbolic");
let fs = require("fs");
let source = esl_symbolic.string("source");
fs.readFile(source, "utf8", (_, data) => {
  console.log(data);
});
