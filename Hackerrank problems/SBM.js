
(function matchSocks(n, ar){
    let pairs = 0;
    let socks = {};

    ar.forEach((sock) =>{
        if(!socks[sock]){
            socks[sock] = 0;
        }
        socks[sock] = socks[sock] + 1;

        if(!(socks[sock] % 2)){
            pairs = pairs + 1;
        }

        return pairs;
    })
    console.log(pairs);

})(9, [10,20,20,10,10,30,50,10,20]);

