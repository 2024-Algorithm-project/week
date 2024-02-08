//N, M
const form_1 = document.querySelector("#form-1");
const input_1 = document.querySelector("#input-1");
const input_2 = document.querySelector("#input-2");
const form1_btn1 = document.querySelector("#form-1 #button-1");
const form1_btn2 = document.querySelector("#form-1 #button-2");

//A_i
const form_2 = document.querySelector("#form-2");
const input_box = document.querySelector("#input-box");
const form2_btn1 = document.querySelector("#form-2 #button-1");
const form2_btn2 = document.querySelector("#form-2 #button-2");

//result
const result_box = document.querySelector("#result-box");

//event
form_1.addEventListener("submit", cal_1);
form_1.addEventListener("reset", reset);

//cal
function cal_1(event){
    event.preventDefault();
    const N = input_1.value;
    const M = input_2.value;
    for(let a=1; a<=N-1; a++){
        let input_A = document.createElement("input");
        input_A.setAttribute("id", "input-A");
        input_box.appendChild(input_A);
    }
    form1_btn1.disabled=true;
    form2_btn1.style.display="block";
    form2_btn2.style.display="block";

    form_2.addEventListener("submit", cal_2);
    function cal_2(event){
        event.preventDefault();
        let arr = [];
        let input = document.querySelectorAll("#input-A");

        for(let a of input){
            arr.push(parseInt(a.value));
        }

        let result = 0;

        for(let j of arr){
            if(j<=M){
                result += j;
            }
        }

        let p = document.createElement("p");
        p.setAttribute("id", "final");
        p.innerText = `정체 구간 총 거리 : ${result}`;
        result_box.appendChild(p);
    }

    form_2.addEventListener("reset", reset);
    function reset(){
        result_box.replaceChildren();
    }
}

//reset
function reset(){
    location.reload(true);
}