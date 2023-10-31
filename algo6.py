/* 
Given a non-empty array of odd length containing ints where every int but one
has a matching pair (another int that is the same)
return the only int that has no matching pair.
*/

const nums1 = [1];
const expected1 = 1;

const nums2 = [5, 4, 5];
const expected2 = 4;

const nums3 = [5, 4, 3, 4, 3, 4, 5];
const expected3 = 4; // there is a pair of 4s but one 4 has no pair.

const nums4 = [5, 2, 6, 2, 3, 1, 6, 3, 2, 5, 2];
const expected4 = 1;

function oddOccurrencesInArray(nums = []) {
    const freqTable = {};
  
    for (const n of nums) {
      if (freqTable.hasOwnProperty(n)) {
        freqTable[n]++;
      } else {
        freqTable[n] = 1;
      }
    }
  

    for (const key in freqTable) {
      if (freqTable[key] % 2 !== 0) {
        return +key; // + converts the string key back to int.
      }
    }
  
  }

console.log(oddOccurrencesInArray(nums1), "should equal", expected1);
console.log(oddOccurrencesInArray(nums2), "should equal", expected2);
console.log(oddOccurrencesInArray(nums3), "should equal", expected3);
console.log(oddOccurrencesInArray(nums4), "should equal", expected4);

/*****************************************************************************/
function oddOccurrencesInArray(nums) {
  const freqs = {};

  for (let i=nums.length-1; i>=0; i--) {
    const n = nums[i];
    if (n in freqs) {
      freqs[n].freq += 1;
      freqs[n].idx = i;
    }
    else {
      freqs[n] = {
        num: n,
        freq: 1,
        idx: i,
      };
    }
  }

  return Object.values(freqs)
               .filter(v => v.freq % 2 === 1)
               .reduce((a, e) => e.idx < a.idx ? e : a)
               .num;
}
