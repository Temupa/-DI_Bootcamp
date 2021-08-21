let user = prompt("Which language do you speak?","") 
user = user.toLowerCase() 
switch(user)
{
    case 'french':
        console.log("Bonjour")
      break;
    case 'english':
        console.log("Hello")
      break;
      case 'hebrew': 
        console.log("Shalom")
        break;
    default: 
        console.log("01110011 01101111 01110010 01110010 01111001")
  }   