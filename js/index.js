/*global google, map, console, $, arson, auto_theft, homicide, sex_assault, theft*/
var map,

//Yellow circle
	ARSON_BUTTON = 'https://storage.googleapis.com/support-kms-prod/SNP_2752063_en_v0',
//Blue circle
	AUTO_THEFT_BUTTON = 'https://storage.googleapis.com/support-kms-prod/SNP_2752068_en_v0 ',
//Red circle
	HOMICIDE_BUTTON = 'https://storage.googleapis.com/support-kms-prod/SNP_2752125_en_v0',
//Pink circle
	SEXUAL_ASSAULT_BUTTON = 'https://storage.googleapis.com/support-kms-prod/SNP_2752264_en_v0',
//Blue circle
	THEFT_BUTTON = 'https://storage.googleapis.com/support-kms-prod/SNP_2752068_en_v0';

function addMarker(lat, lon, button) {
	"use strict";
	var marker = new google.maps.Marker({
			position: new google.maps.LatLng(lat, lon),
			icon: button.icon,
			map: map
		});
	return marker;
}

function Crime(lat_lngs, button) {
	"use strict";
	var i;
	
	this.toggled = false;
	this.markers = [];
	
	for (i = 0; i < lat_lngs.length; i += 1) {
		this.markers.push(addMarker(lat_lngs[i][0], lat_lngs[i][1], button));
	}
}

Crime.prototype.setAllMap = function (map) {
	"use strict";
	var i;
	
	for (i = 0; i < this.markers.length; i += 1) {
		this.markers[i].setMap(map);
	}
};

Crime.prototype.showMarkers = function () {
	"use strict";
	this.setAllMap(map);
};

Crime.prototype.clearMarkers = function () {
	"use strict";
	this.setAllMap(null);
};

var arsony = new Crime(arson, ARSON_BUTTON),
	gta = new Crime(auto_theft, AUTO_THEFT_BUTTON),
	murder = new Crime(homicide, HOMICIDE_BUTTON),
	rape = new Crime(sex_assault, SEXUAL_ASSAULT_BUTTON),
	robbery = new Crime(theft, THEFT_BUTTON);

function initialize() {
	"use strict";
	
	map = new google.maps.Map(document.getElementById('map-canvas'), {
		// 38º 89' N, 77º 03' W
		center: { lat: 38.89, lng: -77.03 },
		zoom: 8
	});
}

google.maps.event.addDomListener(window, 'load', initialize);

$("input[name='crime']").click(function () {
	"use strict";
	var type = $(this).attr('value'),
		i;
	
	switch (type) {
			
	case 'arson':
		if (!arsony.toggled) {
			arsony.showMarkers();
		} else {
			arsony.clearMarkers();
		}
			
		arsony.toggled = !arsony.toggled;

		break;
	case 'auto_theft':
		if (!gta.toggled) {
			gta.showMarkers();
		} else {
			gta.clearMarkers();
		}
			
		gta.toggled = !gta.toggled;

		break;
	case 'homicide':
		if (!murder.toggled) {
			murder.showMarkers();
		} else {
			murder.clearMarkers();
		}
			
		murder.toggled = !murder.toggled;

		break;
	case 'sex_assault':
		if (!rape.toggled) {
			rape.showMarkers();
		} else {
			rape.clearMarkers();
		}
			
		rape.toggled = !rape.toggled;

		break;
	default:
		if (!robbery.toggled) {
			robbery.showMarkers();
		} else {
			robbery.clearMarkers();
		}
			
		robbery.toggled = !robbery.toggled;

		break;
			
	}
	
});