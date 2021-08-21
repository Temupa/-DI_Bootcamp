
let sentence = ("The movie is not that bad, I like it");
let final;

let wordNot = sentence.search('not');

let wordBad = sentence.search('bad');

console.log(wordNot);


if (wordBad > wordNot && wordBad != -1 && wordNot != -1) {
    let subs = sentence.substring(wordNot, wordBad + 3);
    final = sentence.replace(subs, "good");
} else {
    final = sentence;
}
alert(final);