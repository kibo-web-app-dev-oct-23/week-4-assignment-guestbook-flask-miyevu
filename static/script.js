function filters() {
    var filterBy = document.getElementById("filter").value;
    var sortOrder = document.getElementById("order").value;
    var url = "/viewguestbook?filter=" + filterBy + "&order=" + sortOrder;
    window.location.href = url;
}