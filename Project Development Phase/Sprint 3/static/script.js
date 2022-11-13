window.onload = function () {
  document.getElementById("loader").style.display="none";
  document.getElementById("content").style.visibility="visible";
  input = document.getElementById("upload");
  submit = document.getElementById("submit");
  statustxt = document.getElementById("status");
  input.addEventListener("change", function () {
    if (input.value == "") statustxt.innerText = "No file selected";
    else statustxt.innerText = input.files[0].name;
    statustxt.style.visibility="visible";
  });
  submit.addEventListener('click',function(){
    if (input.value == "") statustxt.innerText = "No file selected";
    else statustxt.innerText = "Working on it...";
    statustxt.style.visibility="visible";
  });
};
