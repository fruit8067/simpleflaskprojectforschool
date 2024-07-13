



function Fund(){
    var Account = $("#Account").text()
    var urlString = window.location.href
    var input = $("#input").val()

    // URL에서 경로 부분 추출
    var path = new URL(urlString).pathname;

    // 경로를 '/'로 분할하여 배열로 변환
    var pathSegments = path.split('/');
    console.log(pathSegments)

    // 첫 번째 경로 요소 가져오기 (helloworld)
    var Student = pathSegments[2];
    var Group = pathSegments[3] + "Group";
    $.ajax({
        type: "POST",
        url: "/review",
        data: {"Account" : Account, "Group" : Group, "input": input, "student": Student},
        success: function (response) {
            alert(response['msg']);
            window.location.reload();
        }
    })
}

function maintitle(){
    var urlString = window.location.href
    // URL에서 경로 부분 추출
    var path = new URL(urlString).pathname;
    // 경로를 '/'로 분할하여 배열로 변환
    var pathSegments = path.split('/');
    console.log(pathSegments)
    // 첫 번째 경로 요소 가져오기 (helloworld)
    var Student = pathSegments[2];
    location.href = "http://58.234.239.62:5000/"+Student

}