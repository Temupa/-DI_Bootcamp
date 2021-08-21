let user = prompt("type a verb","") //1
    if(user.length >= 3 && user.slice(-3) != "ing") 
    {
        console.log(user + "ing")
    }
    else if(user.length >= 3 && user.slice(-3) == "ing") 
    {
        console.log(user + "ly")
    }
    else if(user.length < 3)
    {
        console.log(user)
  }
