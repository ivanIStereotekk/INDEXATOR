

var emPty = '';
console.log(emPty);

function getTextFrom(text){
    alert(text);
    let myData = emPty + text;
    console.log(myData);

}

function makePost(myData){
        axios.post("https://127.0.0.1:8000/path", {
        'path': myData,
    })
    .then((response) => {
      console.log(response);
    });

}




//function showMessage() {
//  let message = "Привет, я JavaScript!";
//
//  alert( message );
//}