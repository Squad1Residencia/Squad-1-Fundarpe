function filterProjects() {
  var input = document.getElementById('myInput');
  var filter = input.value.toUpperCase();
  var ul = document.getElementById("myUL");
  var li = ul.getElementsByTagName('li');

  for (var i = 0; i < li.length; i++) {
    var a = li[i].textContent || li[i].innerText;
    if (a.toUpperCase().indexOf(filter) > -1) {
      li[i].style.display = "";
    } else {
      li[i].style.display = "none";
    }
  }
}