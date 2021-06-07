function hourglassSum(arr) {
    // Write your code here
    let mxiX = 3;
    let mxiY = 3;
    let umax = -Infinity;
    
    for (let y = 0; y <= mxiY; y++) {
        for (let x = 0; x <=mxiX; x++) {
            let sum = arr[y][x] + arr[y][x+1] + arr[y][x+2] + arr[y+1][x+1] + arr[y+2][x]            + arr[y+2][x+1] + arr[y+2][x+2];
            
            if(umax < sum){
                umax = sum
            }
        }
    }
    
    return umax
}