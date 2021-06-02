function repeatedString(s,n){
    let count = 0;
    let RA = 0;
    let manders = n % s.length;
    

    for (let i = s.length; i-- > 0;) {
        if(s.charAt(i) == 'a') {
            ++count;
            
            if(i < manders) {
                ++RA;
            }

        }
        
    }

    return ((n - manders) / s.length * count) + RA;
  
}


repeatedString('aba', 10)



