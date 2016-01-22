var fs = require('fs');
var topojson = require('topojson');

var geojson = JSON.parse(fs.readFileSync('../data/joined_2014_essex-county.json', 'utf8'));

geojson.features = geojson.features.filter(item => item.properties.medcat);

// console.log(geojson.features);

var topology = topojson.topology({ 'collection': geojson }, {
	'property-transform': (feature) => feature.properties
});

// console.log(topology.objects.collection); // inspect TopoJSON

fs.writeFile('../web/new.json', JSON.stringify(topology), 'utf8', function(err) {
	console.log('done');
});
