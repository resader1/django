
if('{{msg}}' == 1){
    alert("로그인됨");
    location.href = '/'
}
else if('{{msg}}' == 0){
    alert("아이디 또는 비번 일치하지 않음")
}