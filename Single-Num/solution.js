//single - num 

var singleNum = function(nums) {
    let result = nums[0];
    for (i=1; i < nums.length; i++) {
        result = result ^ nums[i];
    }
    return result;
};

console.log(singleNum([4,1,2,1,2]));
console.log(singleNum([2,1,2]));
