// GOOGLE MAPS 

const KEY = "AIzaSyDyxRFvU2V2-X6wyUxzk-6y4jfIIaBqts0";
    
// Zoom levels
const WORLD = 1;
const CONTINENT = 5;
const CITY = 10;
const STREETS = 15;
const BUILDINGS = 20;

const mapStyle = [
	{
		"elementType": "geometry",
		"stylers": [
		{
			"color": "#f5f5f5"
		}
		]
	},
	{
		"elementType": "labels.icon",
		"stylers": [
		{
			"visibility": "off"
		}
		]
	},
	{
		"elementType": "labels.text.fill",
		"stylers": [
		{
			"color": "#616161"
		}
		]
	},
	{
		"elementType": "labels.text.stroke",
		"stylers": [
		{
			"color": "#f5f5f5"
		}
		]
	},
	{
		"featureType": "administrative.land_parcel",
		"elementType": "labels.text.fill",
		"stylers": [
		{
			"color": "#bdbdbd"
		}
		]
	},
	{
		"featureType": "poi",
		"elementType": "geometry",
		"stylers": [
		{
			"color": "#eeeeee"
		}
		]
	},
	{
		"featureType": "poi",
		"elementType": "labels.text.fill",
		"stylers": [
		{
			"color": "#757575"
		}
		]
	},
	{
		"featureType": "poi.park",
		"elementType": "geometry",
		"stylers": [
		{
			"color": "#e5e5e5"
		}
		]
	},
	{
		"featureType": "poi.park",
		"elementType": "labels.text.fill",
		"stylers": [
		{
			"color": "#9e9e9e"
		}
		]
	},
	{
		"featureType": "road",
		"elementType": "geometry",
		"stylers": [
		{
			"color": "#ffffff"
		}
		]
	},
	{
		"featureType": "road.arterial",
		"elementType": "labels.text.fill",
		"stylers": [
		{
			"color": "#757575"
		}
		]
	},
	{
		"featureType": "road.highway",
		"elementType": "geometry",
		"stylers": [
		{
			"color": "#dadada"
		}
		]
	},
	{
		"featureType": "road.highway",
		"elementType": "labels.text.fill",
		"stylers": [
		{
			"color": "#616161"
		}
		]
	},
	{
		"featureType": "road.local",
		"elementType": "labels.text.fill",
		"stylers": [
		{
			"color": "#9e9e9e"
		}
		]
	},
	{
		"featureType": "transit.line",
		"elementType": "geometry",
		"stylers": [
		{
			"color": "#e5e5e5"
		}
		]
	},
	{
		"featureType": "transit.station",
		"elementType": "geometry",
		"stylers": [
		{
			"color": "#eeeeee"
		}
		]
	},
	{
		"featureType": "water",
		"elementType": "geometry",
		"stylers": [
		{
			"color": "#e5efff"
		}
		]
	},
	{
		"featureType": "water",
		"elementType": "labels.text.fill",
		"stylers": [
		{
			"color": "#9e9e9e"
		}
		]
	}
];

var map, gc;
var mark = [], iW = [];
var lat = 34.013253, lng = -118.495211;

// Escapes HTML characters in a template literal string, to prevent XSS
function sanitizeHTML(strings) {
	const entities = {'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'};
	let result = strings[0];
	for (let i = 1; i < arguments.length; i++) {
		result += String(arguments[i]).replace(/[&<>'"]/g, (char) => {
		return entities[char];
		});
		result += strings[i];
	}
	return result;
}
	
function initMap() {
   map = new google.maps.Map(document.getElementById('map'), {
		zoom: STREETS,
		center: {lat: lat, lng: lng},
		mapTypeId: 'roadmap',
		styles: mapStyle,
		zoomControl: true,
		mapTypeControl: false,
		mapTypeControlOptions: {
			style: google.maps.MapTypeControlStyle.DEFAULT
		},
		scaleControl: true,
		streetViewControl: false,
		rotateControl: true,
		fullscreenControl: true,
	});

	gc = new google.maps.Geocoder();

	// Markers and info windows
	for (var i = 0; i < window.items.length; i++) {
		let item = window.items[i];
		let cs = `<strong>${item.quantity} ${item.item}</strong><br>${item.address}<br>${item.date}`;
		iW.push(new google.maps.InfoWindow({
			content: cs,
			maxWidth: 200
		 }));
		gc.geocode({'address': item.address}, function(results, status) {
			if (status === 'OK') {
				lat = results[0].geometry.location.lat();
				lng = results[0].geometry.location.lng();
				map.setCenter(results[0].geometry.location);
			}
		});
		mark.push(new google.maps.Marker({
			position: {lat: lat, lng: lng},
			map: map,
			title: item.item,
			zIndex: i
		}));
		mark[i].addListener('click', function() {
			i = this.zIndex;
			iW[i].open(map, mark[i]);
		 });
	 }

	// Geolocate
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(function(position) {
		  var pos = {
			 lat: position.coords.latitude,
			 lng: position.coords.longitude
		  };
		  map.setCenter(pos);
		}, 
		function() {
		  handleLocationError(true, iW, map.getCenter());
		});
	} 
	else {
		// Error
		handleLocationError(false, iW, map.getCenter());
	}

	// // keypress event listener
	// var search = document.getElementById("search");
	// search.addEventListener("keypress", function(e) {
	// 	if (e.code === "Enter") {
	// 		geocodeAddress(gc, map);
	// 	}
	// });

	// // keypress event listener
	// var where = document.getElementById("where");
	// where.addEventListener("keypress", function(e) {
	// 	if (e.code === "Enter") {
	// 		var attr = document.getElementById("attr");
	// 		var ps = new google.maps.places.PlacesService(attr);
	// 		var query = where.value;
	// 		ps.textSearch(
	// 			{
	// 				'query': query,
	// 				'location': {lat: window.lat, lng: window.lng},
	// 			}, 
	// 			function(results, status) {
	// 			if (status === 'OK') {
	// 				results.forEach(function(r, i) {
	// 					attr.innerHTML += `
	// 						<div class="orange" style="padding: 10px; margin: 10px">
	// 							<div class="name" style="font-size: 14px; line-height: 20px">${r.name}</div>
	// 							<div class="address" style="font-size: 14px; line-height: 20px">${r.formatted_address}</div>
	// 							<form id="form-${i}" action="/pieholes" method="POST" style="line-height: 20px">
	// 								<input type="hidden" name="lat" value="${r.geometry.location.lat()}">
	// 								<input type="hidden" name="lng" value="${r.geometry.location.lng()}">
	// 								<input type="hidden" name="name" value="${r.name}">
	// 								<input type="hidden" name="address" value="${r.formatted_address}">
	// 								<input type="hidden" name="url" value="${r.url}">
	// 								<button type="submit" class="btn black" form="form-${i}" style="color: white; height: 20px; line-height: 0; padding: 5px; margin: 5px 0;" value="Add" name="submit">+</button>
	// 							</form>
	// 						</div>
	// 				`;
	// 				});
	// 			}
	// 		})
	// 	}
	// });
}

// Set map location
function geocodeAddress(gc, map) {
	var address = document.getElementById("icon_prefix").value;
	gc.geocode({'address': address}, function(results, status) {
		if (status === 'OK') {
			lat = results[0].geometry.location.lat();
			lng = results[0].geometry.location.lng();
			map.setCenter(results[0].geometry.location);
		}
	});
}

function handleLocationError(browserHasGeolocation, iW, pos) {
	iW.setPosition(pos);
	iW.setContent(browserHasGeolocation ?
		'Error: Geolocation service failed' :
		'Error: Your browser doesn\'t support geolocation');
	iW.open(map);
 }