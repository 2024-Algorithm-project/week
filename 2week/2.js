const form = document.querySelector("#form");
const input_area = document.querySelector("#area");
const input_move = document.querySelector("#move");
const result = document.querySelector(".result");

form.addEventListener("submit", move);

function move(event){
    event.preventDefault();
    const moving = input_move.value.split(" ");
    const N = input_area.value;
    let x = 1;
    let y = 1;
    for(let i of moving){
        if(i=="L" && x>1){
            x -= 1;
        }
        else if(i=="R" && x<=N){
            x += 1;
        }
        else if(i=="U" && y>1){
            y -= 1;
        }
        else if(i=="D" && y<=N){
            y += 1;
        }
    }
    result.innerText= `${x},${y}`;
}


function reset(){
    check.remove();
}