//첫째 줄에 N(2 <= N <= 1000), M(1 <= M <= 10000), K(1 <= K <= 10000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
//둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10,000이하의 수로 주어진다.
//입력으로 주어지는 K는 항상 M보다 작거나 같다.
//첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다.

const [N, M, K] = prompt("세 개의 숫자를 입력해주세요.\n N:숫자 개수(2<=N<=1000), \n M:더하는 횟수(1<=M<=10000), \n K:연속으로 더할 수 있는 횟수(1<=K<=10000) \n K는 M보다 작거나 같음").split(" ").map(Number);

const Arr = prompt("숫자를 입력하세요(공백으로 구분)").split(" ").sort().reverse().map(Number);

function check(N, M, K, Arr){
    while(true){
        if(N<2 || N>1000 || M==0 || M>10000 || K==0 || K>10000){
            alert("범위 안의 숫자를 입력해주세요.");
            break;
        }
        else if(K>M){
            alert("K는 M보다 값이 작거나 같게 해주세요.");
            break;
        }
        else{
            for(let a of Arr){
                if(a==0 || a>10000){
                    alert("범위 안의 숫자를 입력해주세요.");
                    break;
                }
                else if(Arr.length!==N){
                    alert("N개의 숫자를 입력해주세요.");
                    break;
                }
                else{
                    return N, M, K, Arr;
                }
            }
        }
    }
}

check(N, M, K, Arr);

function cal(){
    const first = Arr[0];
    const second = Arr[1];
    const a = first * (Math.floor(M/(K+1))*K);
    const b = (M % (K+1) * first) + a
    const c = second * ((K+1)-K)*Math.floor(M/(K+1));
    const result = b + c;

    const num = document.querySelector(".num");
    num.innerText = result;
}

cal();
