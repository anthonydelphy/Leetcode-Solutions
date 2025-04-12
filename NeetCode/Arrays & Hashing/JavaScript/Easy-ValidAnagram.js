/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */

 // This could also be solved utilizing sorting, but using a hashtable idea only goes through each string once.
var isAnagram = function(s, t) {
    if(s.length !== t.length)
        return false
    
    let object = {}
    
    for(let i = 0; i < s.length; i++){
        if (s[i] in object){
            object[s[i]] += 1;
            continue;
        }
        else
            object[s[i]] = 1;
    }

    for(let i = 0; i < t.length; i++){
        if (t[i] in object){
            object[t[i]] -= 1
            continue;
        }
        else{
            return false;
        }
    }

    for(const key in object)
        if(object[key] !== 0)
            return false  

    return true;
            
};