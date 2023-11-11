function applyFilters() {
    var filterBy = document.getElementById("filter").value;
    var sortOrder = document.getElementById("order").value;
    var url = "/view_guestbook?filter=" + filterBy + "&order=" + sortOrder;
    window.location.href = url;
}