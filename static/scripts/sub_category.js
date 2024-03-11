let add_buttons = document.getElementsByClassName('product-details')

const user_id = JSON.parse(document.getElementById('user_id').textContent);
console.log(add_buttons)

let added_product = document.createElement('div')

    let left = document.createElement('div')
        let button1 = document.createElement('button')
    left.appendChild(button1)
    left.className = 'left'

    let middle = document.createElement('div')
    middle.className = 'middle'

    let right = document.createElement('div')
        let button2 = document.createElement('button')
    right.appendChild(button2)
    right.className = 'right'

added_product.appendChild(left)
added_product.appendChild(middle)
added_product.appendChild(right)

for (let index = 0; index < add_buttons.length; index++) {
    const element = add_buttons[index].getElementsByClassName('add')[0].getElementsByTagName('button')[0];
    console.log(element)
    element.onclick = function () {
        shopSocket.send(JSON.stringify({
            "message": "add_cart",
            "product_id":element.id.split('_')[3],
        }));
        add_buttons[index].getElementsByClassName('add')[0].innerHTML =  added_product.innerHTML
        add_buttons[index].getElementsByClassName('add')[0].className = "button-cart edit"

        left_button = add_buttons[index].getElementsByClassName('left')[0].getElementsByTagName('button')[0]
        left_button.id='minus_count_'+element.id.split('_')[3]
        left_button.onclick = function () {
            shopSocket.send(JSON.stringify({
                "message": "minus_count",
                "product_id":left_button.id.split('_')[2],
            }));
        }
        
        right_button = add_buttons[index].getElementsByClassName('right')[0].getElementsByTagName('button')[0]
        right_button.id = 'plus_count_'+element.id.split('_')[3]
        right_button.onclick = function () {
            shopSocket.send(JSON.stringify({
                "message": "plus_count",
                "product_id":right_button.id.split('_')[2],
            }));
        }
    }
    
}

let shopSocket = null;

function connect() {
    shopSocket = new WebSocket("ws://" + window.location.host + "/ws/user/" + user_id + "/");

    shopSocket.onopen = function(e) {
        console.log("Successfully connected to the WebSocket.");
    }

    shopSocket.onclose = function(e) {
        console.log("WebSocket connection closed unexpectedly. Trying to reconnect in 2s...");
        setTimeout(function() {
            console.log("Reconnecting...");
            connect();
        }, 2000);
    };

    shopSocket.onerror = function(err) {
        console.log("WebSocket encountered an error: " + err.message);
        console.log("Closing the socket.");
        shopSocket.close();
    }
}

connect()