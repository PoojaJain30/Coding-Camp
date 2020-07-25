// FizzBuzz game

function fizzBuzz(num) {
    var result = [num];
    console.log(result);
    for (i = 0 ; i <= num ; i++){
        if( i % 3 == 0 & i % 5 == 0){
            result[i] = 'FizzBuzz';
        } else if ( i % 3 == 0){
            result[i] = 'Fizz';
        } else if ( i % 5 == 0){
            result[i] = 'Buzz';
        } else {
            result[i] = String(i);
        }
    }
    return result.slice(1);
}

console.log(fizzBuzz(15))