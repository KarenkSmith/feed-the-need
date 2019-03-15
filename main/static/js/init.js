// Materialize

// Initialize #nav-mobile sidenav
var sn = document.querySelectorAll('.sidenav');
M.Sidenav.init(sn[0], {
  edge: 'left',
  draggable: true,
  preventScrolling: true
});