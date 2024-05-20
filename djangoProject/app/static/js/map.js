//   ymaps.ready(function () {
//     var map = new ymaps.Map("map", {
//       center: [55.76, 37.64],
//       zoom: 10,
//       controls: ['SearchControl']
//     });
//
//     if (map) {
//       ymaps.modules.require(['Placemark', 'Circle'], function (Placemark, Circle) {
//         var placemark = new Placemark([55.37, 35.45]);
//       });
//     }
//     map.events.add('click', function(event){
//         const coordinates = event.get('coords');
//         console.log(coordinates)
//     })
//     var searchControl = new ymaps.control.SearchControl({
//     options: {
//     // Будет производиться поиск по топонимам и организациям.
//     provider: 'yandex#search'
//    }
//     });
// myMap.controls.add(searchControl);
//   });
//
const longitudeForm = document.getElementsByName('longitude')[0]
const latitudeForm = document.getElementsByName('latitude')[0]
ymaps.ready(function() {
    let centerCoords;
    if (Boolean(longitudeForm.value) && Boolean(latitudeForm.value)){
        centerCoords = [longitudeForm.value, latitudeForm.value]
    }
    else{
        centerCoords = [56.10, 92.9];
    }
    var map = new ymaps.Map('map', {
        center: centerCoords,
        zoom: 10,
        controls: []
    });
    // Проверяем, что в форме широты и долготы есть значения
    if (Boolean(longitudeForm) && Boolean(latitudeForm)){
        const coords = [longitudeForm.value, latitudeForm.value]
        // console.log(coords)
        map.geoObjects.add(new ymaps.Placemark(coords))
    }

    map.events.add('click', function(event){
        map.geoObjects.removeAll    ()
        map.geoObjects.add(new ymaps.Placemark(event.get('coords')));
        longitudeForm.value = event.get('coords')[0]
        latitudeForm.value = event.get('coords')[1]
    })
});
