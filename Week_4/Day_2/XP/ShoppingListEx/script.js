let stock = {  
    "banana": 6,
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry": 1
}

let prices = {
    "banana": 4,
    "apple": 2,
    "pear": 1,
    "orange": 1.5,
    "blueberry": 10
}

let shoppinglist = ["banana", "orange", "apple"]; 

function myBill() 
{
    let totalprice = 0;
    if (stock.banana > 0) {
        totalprice = totalprice + prices.banana;
        stock.banana--; 
    }
    if (stock.orange > 0) {
        totalprice = totalprice + prices.orange;
        stock.orange--; 
    }
    if (stock.apple > 0) {
        totalprice = totalprice + prices.apple;
        stock.apple--; 
    }
    console.log("The total price of your bill is: " + totalprice); 
    return totalprice;
}

myBill();