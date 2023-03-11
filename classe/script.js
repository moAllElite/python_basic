//how to formatter date in java ?   
{ // example 1
   let f = new Intl.DateTimeFormat('en');
   let a = f.formatToParts();
   console.log(a);
}
{ // example 2
   let f = new Intl.DateTimeFormat('hi');
   let a = f.formatToParts();
   console.log(a);
}

function join(t, a, s) {
   function format(m) {
      let f = new Intl.DateTimeFormat('en', m);
      return f.format(t);
   }
   return a.map(format).join(s);
}

let a = [{day: 'numeric'}, {month: 'short'}, {year: 'numeric'}];
let s = join(new Date, a, '-');
console.log(s);

let d = new Date(2010, 7, 5);
let ye = new Intl.DateTimeFormat('en', { year: 'numeric' }).format(d);
let mo = new Intl.DateTimeFormat('en', { month: 'short' }).format(d);
let da = new Intl.DateTimeFormat('en', { day: '2-digit' }).format(d);
console.log(`${da}-${mo}-${ye}`);



//Source: https://stackoverflow.com/questions/3552461



