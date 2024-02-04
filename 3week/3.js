const form = document.querySelector("#form");
const input = document.querySelector("#input");
const result = document.querySelector(".result");
form.addEventListener("submit", cal)

function cal(event){
    event.preventDefault();
    const list = input.value.split(" ").map(Number);
    const N = list[0];
    let x = list[1];
    let y = list[2];
    const result_list = [];
    for(let i=1; i<=N; ++i){
        if(i%x==0 && i%y==0){
            result_list.push("AB");
        }
        else if(i%x==0){
            result_list.push("A");
        }
        else if(i%y==0){
            result_list.push("B");
        }
        else{
            result_list.push("N");
        }
    }
    for(let a of result_list){
        const p = document.createElement("p");
        p.innerText = a;
        result.appendChild(p);
    }
}
