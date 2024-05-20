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
    // Это необходимо при изменении посещенного места, чтобы поставить метку
    if (Boolean(longitudeForm) && Boolean(latitudeForm)){
        const coords = [longitudeForm.value, latitudeForm.value]
        map.geoObjects.add(new ymaps.Placemark(coords))
    }

    // Добавляем метку на карту при клике
    map.events.add('click', function(event){
        map.geoObjects.removeAll()
        const coords = event.get('coords')
        map.geoObjects.add(new ymaps.Placemark(coords));
        // Обновляем значения в форме
        longitudeForm.value = coords[0]
        latitudeForm.value = coords[1]
    })
});
