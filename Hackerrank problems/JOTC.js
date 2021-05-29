function jumpingOnClouds(c){
    var jump = 0; 
    var i = 0;
    while (i < c.length -1){
        jump++;
        i = c[i + 2 ] == 0 ? i + 2 : i + 1
    }
    return jump 
}

jumpingOnClouds([0,0,1,0,0,1,0])