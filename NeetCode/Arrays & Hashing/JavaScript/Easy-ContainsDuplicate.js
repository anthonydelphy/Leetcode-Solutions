/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const object = {};

    for(let i = 0; i < nums.length; i++){
        if(nums[i] in object)
            return true;
        else
            object[nums[i]] = 0; 
    };

    return false;
};