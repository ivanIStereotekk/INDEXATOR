

var emPty = '';
console.log(emPty);

function getTextFrom(text){
    alert(text);
    let secondURLpart = text;
    let myURL = "http://127.0.0.1:8000/path?path="+secondURLpart.trim();
    console.log(myURL.trim());
    let xhr = new XMLHttpRequest();
	  xhr.open("POST", myURL);
	  xhr.send(JSON.stringify(text));
	  xhr.onreadystatechange = function() {
  if (xhr.readyState != 4) {
    return
  }

  if (xhr.status === 200) {
    console.log('result', xhr.responseText)
    document.getElementById("result").innerHTML = "Files in directory :"+ xhr.responseText;
  } else {
    console.log('err', xhr.responseText)
    document.getElementById("result").innerHTML = "Empty directory: "+ xhr.responseText;
  }
}
}

//	  console.log(xhr.responseText+ " ------- Result");
//	  document.getElementById("result").innerHTML = xhr.responseText + "++++";
//
//	  }
//      let resText = JSON.stringify(xhr.responseJSON)