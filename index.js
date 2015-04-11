/*global google, map*/

function initialize() {
	"use strict";
	var mapOptions = {
		// 38º 89' N, 77º 03' W
		center: { lat: 38.89, lng: -77.03 },
		zoom: 8
	},
		map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions),

		marker = new google.maps.Marker({
			position: new google.maps.LatLng(38.9001286, -77.0163752),
			icon: {
				path: google.maps.SymbolPath.CIRCLE,
				scale: 4
			},
			map: map,
			title: 'what what'
		});

}

google.maps.event.addDomListener(window, 'load', initialize);