/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 
 This one is a bit annoying because the hashmap solution is pretty easy to think of
 but you also have to consider the situation in which the two of the same values are added
 to the target

 you resolve this issue simply by having the hash map store the last time the value occured,
 meaning that when you are iterating, you have the future occurence of the value and the previous
 
 Time Complexity: O(n)
 */
 var twoSum = function(nums, target) {
    let object = {}

    for(const i in nums){
        const diff = target - nums[i];

        if(diff.toString() in object)
            return [Number(object[diff]), Number(i)]
        
        object[nums[i]] = i 

    };
    
    return [-1,-1]
};