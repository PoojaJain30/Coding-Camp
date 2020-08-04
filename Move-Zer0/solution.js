// Move Zero

var moveZero = function(nums) {
    for(i = 0; i <nums.length ; i++){
        if (nums[i] == 0) {
            nums.splice(i,1);
            nums.push(0);
        };
    return nums;
    };
};

console.log(moveZero([0,1,0,3,12]));