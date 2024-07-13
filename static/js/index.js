function sign_in() {
    location.href = "sign_in";
}



$(document).ready(function () {
    user = $("#User").text();
    if(user == ''){

    }else{
        $.ajax({
            type: "POST",
            url: "/bank2",
            data: {"user":user},
            success: function(response){
                console.log(response['msg']); /* 자기 돈*/

            }
        })

    }
    $.ajax({
        type: "GET",
        url: "/review",
        data: {},
        success: function(response){
            var temp = response['all_reviews'];
            console.log(temp[0]['Title']) /* all_reviews : 모든 조의 설명(재품 이름, 설명)*/
            var temp2 = response['funded_money']
            console.log(temp2[0]['FundedMoney'])/*1조의 펀딩 금액*/
        }
    })
});

function FIRST(){
    user = $("#User").text();
    console.log(user)
    if(user == ''){
        alert("학번을 입력해 주세요!")
    }else{
        location.href = "page/"+user+"/first"
    }
}


    function SECOND(){
    user = $("#User").text();
    console.log(user)
    if(user == ''){
        alert("학번을 입력해 주세요!")
    }else{
        location.href = "page/"+user+"/second"
    }
}

function THIRD(){
    user = $("#User").text();
    console.log(user)
    if(user == ''){
        alert("학번을 입력해 주세요!")
    }else{
        location.href = "page/"+user+"/third"
    }
}

function FOURTH(){
    user = $("#User").text();
    console.log(user)
    if(user == ''){
        alert("학번을 입력해 주세요!")
    }else{
        location.href = "page/"+user+"/fourth"
    }
}

function FIFTH(){
    user = $("#User").text();
    console.log(user)
    if(user == ''){
        alert("학번을 입력해 주세요!")
    }else{
        location.href = "page/"+user+"/fifth"
    }
}

function SIXTH(){
    user = $("#User").text();
    console.log(user)
    if(user == ''){
        alert("학번을 입력해 주세요!")
    }else{
        location.href = "page/"+user+"/sixth"
    }
}

function SEVENTH(){
    user = $("#User").text();
    console.log(user)
    if(user == ''){
        alert("학번을 입력해 주세요!")
    }else{
        location.href = "page/"+user+"/seventh"
    }
}

function EIGHTH(){
    user = $("#User").text();
    console.log(user)
    if(user == ''){
        alert("학번을 입력해 주세요!")
    }else{
        location.href = "page/"+user+"/eighth"
    }
}


