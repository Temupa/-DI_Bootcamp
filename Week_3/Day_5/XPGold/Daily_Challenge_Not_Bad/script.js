let sentence = ["The","movie","is","not","that","bad","I","like","it"]
let wordNot = sentence.indexOf("not") 
let wordBad = sentence.indexOf("bad") 
let spacebetweenwords = Math.abs(wordBad - wordNot)

if(wordBad > wordNot)
{
    sentence.splice(wordNot,spacebetweenwords+1,"good")
    console.log(sentence)
}

else if(wordBad > wordNot)
{
    console.log(sentence)
}

