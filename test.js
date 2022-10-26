// const gfg = new Array(5);

// console.log({ gfg });

// for (let i = 0; i < gfg.length; i++) {
//   gfg[i] = new Array(2);
//   console.log({ i });
// }

// for (var i = 0; i < 2; i++) {
//   for (var j = 0; j < 2; j++) {
//     document.write(gfg[i][j] + " ");
//   }
//   // document.write("<br>");
// }

// Create one dimensional array
var gfg = new Array(5);
console.log({ gfg });

// Loop to create 2D array using 1D array
for (var i = 0; i < gfg.length; i++) {
  gfg[i] = new Array(2);
}

var h = 0;

// Loop to initialize 2D array elements.
for (var i = 0; i < 2; i++) {
  for (var j = 0; j < 2; j++) {
    gfg[i][j] = h++;
  }
}

// Loop to display the elements of 2D array.
for (var i = 0; i < 2; i++) {
  for (var j = 0; j < 2; j++) {
    console.log(gfg[i][j] + " ");
  }
}
