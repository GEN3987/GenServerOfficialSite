var database = firebase.database();
let room = "check";
const send = document.getElementById("send");
const name = document.getElementById("name");
const message = document.getElementById("message");
const output = document.getElementById("output");
//受信処理
database.ref(room).on("child_added", function(data) {
   const v = data.val();
   const k = data.key;
   let str = "";
   str += '<h1>現在のサーバーの状況：' + v.message + '</h1>';
   output.innerHTML += str;
});
