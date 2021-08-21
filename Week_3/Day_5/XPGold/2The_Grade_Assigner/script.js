let user = prompt("Which grade do you got?","")

if (user > 90)  {
    console.log("A");
}
else if(user > 80 && user <= 90) 
{
    console.log("B");
}

else if (user >= 70 && user <= 80) 
{
    console.log("C")
}
else if(user < 70) 
{
    console.log("D")
}
