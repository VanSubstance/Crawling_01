//checkUnder: parameter > name 이 ctgr 인 체크박스
//Function: name이 ctgr인 체크박스를 체크 / 체크해제하면 하위 체크박스들도 체크 / 체크 해제된다.
function checkUnder(val) {    
    switch (val.id) {
        case "restaurantCheck":
            var under = document.getElementsByName("ctgrRest[]");
            under.forEach(element => {
                element.checked = val.checked;
            });
            break;
        case "activityCheck":
            var under = document.getElementsByName("ctgrAct[]");
            under.forEach(element => {
                element.checked = val.checked;
            });
            break;
        case "placeCheck":
            var under = document.getElementsByName("ctgrPlace[]");
            under.forEach(element => {
                element.checked = val.checked;
            });
            break;
        default:
            alert("Error");
            break;
    }
}

//checkUpper: parameter > name 이 ctgrRest / ctgrAct / ctgrPlace 인 체크박스
//Function: name 이 ctgrRest / ctgrAct / ctgrPlace 인 체크박스들을 체크 / 체크해제하면 상위 체크박스도 체크 / 체크 해제된다.
function checkUpper(val) {
    switch (val.name) {
        case "ctgrRest[]":
            var upper = document.getElementById("restaurantCheck");
            upper.checked = val.checked;
            break;
        case "ctgrAct[]":
            var upper = document.getElementById("activityCheck");
            upper.checked = val.checked;
            break;
        case "ctgrPlace[]":
            var upper = document.getElementById("placeCheck");
            upper.checked = val.checked;
            break;
        default:
            alert("Error");
            break;
    }

}

function showResult() {
    ctgrTop5Bar();
    
}
