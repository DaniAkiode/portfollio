function countingValleys(steps, path) {
    var valleys = 0;
    var level = 0 ;

    for (var i = 0; i <= path.length; i++) {
        if (path[i] === 'U') {
            level ++;   
     
        }
        else{
            level --;
           
        }

        if(level == 0 && path[i] === 'U'){
            valleys++;
        }   
        
    }
    console.log(valleys) 

}
countingValleys(8, ['U','D','D','D','U','D','U','U'])

function countingValleys(steps, path) {
    var valleys = 0;
    var level = 0 ;
    var i = 0;
    while ( i <= path.length ) {
        if (path[i] === 'U') {
            level ++;   
     
        }
        else{
            level --;
           
        }

        if(level == 0 && path[i] === 'U'){
            valleys++;
        }   
        i++;
    }
    console.log(valleys) 

}
countingValleys(8, ['U','D','D','D','U','D','U','U'])