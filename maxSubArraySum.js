// function maxSubArraySum(nums, size) {
//   if (size < 0 || size > nums.length) {
//     //for asserting
//     return null;
//   }

//   let currSum = 0;
//   let maxSumSeen = -Infinity; //should in case we have a negative sum

//   for (let i = 0; i < nums.length; i++) {
//     currSum += nums[i]; //adds next item in subarray after summing in each iteration
//     if (i >= size - 1) {
//       maxSumSeen = Math.max(currSum, maxSumSeen);
//       currSum -= nums[i - (size - 1)]; //subtracts the first item in subarray after summing in each iteration
//     }
//   }

//   return maxSumSeen;
// }

// const arr1 = [1, 2, 3, 5, 4, 8, 6, 2];

// console.log(maxSubArraySum(arr1, 3));

function maxSubArraySum(nums, size) {
  if (size < 0 || size > nums.length) {
    //for asserting
    return null;
  }

  let currSum = 0;
  let maxSumSeen = -Infinity; //should in case we have a negative sum.

  for (let i = 0; i < nums.length - 1; i++) {
    currSum += nums[i]; //adds next item in subarray after summing in each iteration
    if (i >= size - 1) {
      maxSumSeen = Math.max(currSum, maxSumSeen);
      currSum -= nums[i - (size - 1)]; //subtracts the first item in subarray after summing in each iteration
    }
  }

  return maxSumSeen;
}

const arr1 = [1, 2, 3, 5, 4, 8, 6, 2];

console.log(maxSubArraySum(arr1, 3));
