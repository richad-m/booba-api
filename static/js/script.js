var speed = 1;

/* Call this function with a string containing the ID name to
 * the element containing the number you want to do a count animation on.*/
function incEltNbr(id) {
  number = document.getElementById(id);
  finalNumber = Number(document.getElementById(id).innerHTML);
  incNbrRec(0, finalNumber, number);
}

/*A recursive function to increase the number.*/
function incNbrRec(i, finalNumber, number) {
  if (i <= finalNumber) {
    number.innerHTML = i;
    setTimeout(function () {
      //Delay a bit before calling the function again.
      incNbrRec(i + 1, finalNumber, number);
    }, speed);
  }
}

/*Function called on button click*/
function incNbr() {
  incEltNbr("nbr");
}

incEltNbr(
  "nbr-quotes"
); /*Call this funtion with the ID-name for that element to increase the number within*/
