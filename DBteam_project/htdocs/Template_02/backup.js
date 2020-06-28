var ctgrRest = [];
var ctgrAct = [];
var ctgrPlace = [];
function attach(val) {
    if (val.checked == true) {
        if (val.name == "ctgrRest[]") {
            ctgrRest.push(val.value);
            ctgrRest.sort();
        }
        else if (val.name == "ctgrAct[]") {
            ctgrAct.push(val.value);
            ctgrAct.sort();
        }
        else {
            ctgrPlace.push(val.value);
            ctgrPlace.sort();
        }
    }
    else {
        if (val.name == "ctgrRest[]") {
            const i = ctgrRest.indexOf(val.value);
            if (i > -1) ctgrRest.splice(i, 1);
            ctgrRest.sort();
        }
        else if (val.name == "ctgrAct[]") {
            const i = ctgrAct.indexOf(val.value);
            if (i > -1) ctgrAct.splice(i, 1);
            ctgrAct.sort();
        }
        else {
            const i = ctgrPlace.indexOf(val.value);
            if (i > -1) ctgrPlace.splice(i, 1);
            ctgrPlace.sort();
        }
    }
    checkUpper(val);
    console.log(ctgrRest);
    console.log(ctgrAct);
    console.log(ctgrPlace);
}

//checkUnder: parameter > name 이 ctgr 인 체크박스
//Function: name이 ctgr인 체크박스를 체크 / 체크해제하면 하위 체크박스들도 체크 / 체크 해제된다.
function checkUnder(val) {
    console.log(val.id);
    console.log(ctgrRest);
    console.log(ctgrAct);
    console.log(ctgrPlace);
    switch (val.id) {
        case "restaurantCheck":
            var descendence = document.getElementsByName("ctgrRest[]");
            descendence.forEach(element => {
                element.checked = val.checked;
            });
            break;
        case "placeCheck":
            var descendence = document.getElementsByName("ctgrPlace[]");
            descendence.forEach(element => {
                element.checked = val.checked;
            });
            break;
        case "activityCheck":
            var descendence = document.getElementsByName("ctgrAct[]");
            descendence.forEach(element => {
                element.checked = val.checked;
            });
            break;
    }
    

}

//checkUpper: parameter > name 이 ctgrRest / ctgrAct / ctgrPlace 인 체크박스
//Function: name 이 ctgrRest / ctgrAct / ctgrPlace 인 체크박스들을 체크 / 체크해제하면 상위 체크박스도 체크 / 체크 해제된다.
function checkUpper(val) {
    var arr = document.getElementsByName(val.name);
    var allFalse = true;
    switch (val.name) {
        case "ctgrRest[]":
            arr.forEach(element => {
                if (element.checked == true) {
                    document.getElementById("restaurantCheck").checked = true;
                    allFalse = false;
                }
            });
            if (allFalse) {
                document.getElementById("restaurantCheck").checked = false;
            }
            break;
        case "ctgrAct[]":
            arr.forEach(element => {
                if (element.checked == true) {
                    document.getElementById("activityCheck").checked = true;
                    allFalse = false;
                }
            });
            if (allFalse) {
                document.getElementById("activityCheck").checked = false;
            }
            break;
        case "ctgrPlace[]":
            arr.forEach(element => {
                if (element.checked == true) {
                    document.getElementById("placeCheck").checked = true;
                    allFalse = false;
                }
            });
            if (allFalse) {
                document.getElementById("placeCheck").checked = false;
            }
            break;
    }

}

function showResult() {
    ctgrTop5Bar();
    
}
