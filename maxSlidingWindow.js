// let findMaxSlidingWindow = function (nums, windowSize) {
//   let result = [];
//   // ................................................................

//   //return expty list
//   if (nums.length == 0) {
//     return result;
//   }

//   //if window_size is greater than the array size,
//   //set the window_size to nums.length()
//   if (windowSize > nums.length) {
//     windowSize = nums.length;
//   }

//   // ................................................................

//   //Initializing doubly ended queue for storing indices using array
//   let window = [];

//   //find out max for first window
//   for (let i = 0; i < windowSize; i++) {
//     // For every element, remove the previous smaller elements from window
//     while (window.length > 0 )
//   }
// };

// let findMaxSlidingWindow = function (nums, windowSize) {
//   let result = [];

//   if (nums.length == 0) {
//     return result;
//   }

//   //If windowSize is greater than the array size,
//   //set the window_size to nums.length()
//   if (windowSize > nums.length) {
//     windowSize = nums.length;
//   }

//   // initializing doubly ended queue for storing indices using array
//   let window = [];

//   //find out max for first window
//   for (let i = 0; i < windowSize; i++) {
//     //for every elemnt, remove the previous smaller elements from window
//   }
// };

// [3, 4, 5, 6, 7, 8, 9, 10];

// 5, 6, 7, 8, 9, 10;

// //windowSize .........SIZE
// //window..............STORAGE....THE DOUBLY ENDED QUEUE FOR STORUNG INDICES USING ARRAY

// window.length - 1 .....INDEX OF LAST ITEM IN ARRAY window
// window[window.length - 1] ....LAST ITEM OF ARRAY window

console.log("first");

let findMaxSlidingWindow = function (nums, windowSize) {
  let result = [];

  if (nums.length == 0) {
    return result;
  }

  //If windowSize is greater than the array size,
  //set the window_size to nums.length()
  if (windowSize > nums.length) {
    windowSize = nums.length;
  }

  // initializing doubly ended queue for storing indices using array
  let window = [5, 3, 8, 4, 2];

  //find out max for first window
  for (let i = 0; i < windowSize; i++) {
    //for every elemnt, remove the previous smaller elements from window
    console.log(i);
    console.log(nums[i], "corresponding array Item");
  }
  console.log(window.length, "window Length");
  console.log(window.length - 1, "last Item Index");
  console.log(window[window.length - 1], "last Item"); //9

  console.log(nums[window[window.length - 1]]);
};

const testArray = [3, 4, 5, 6, 7, 8, 9, 10];

console.log(findMaxSlidingWindow(testArray, 3));
