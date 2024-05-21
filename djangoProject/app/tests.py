from django.test import TestCase

from .forms import PlaceForm

# Create your tests here.
positive_data = [
    {
        'name': 'Москва',
        'description': 'Москва — город, вдохновляющий своим многообразием культуры, архитектуры и возможностей.',
        'longitude': 55.75168691643619,
        'latitude': 37.62182129919391,
    },
    {
        'name': 'Остров Татышев',
        'description': 'Самый крупный остров на реке Енисей в черте Красноярска',
        'longitude': 56.02376877180873,
        'latitude': 92.93913879394529,
    },
    {
        'name': 'Balance Sport&Spa',
        'description': 'Фитнес-клуб Balance Sport&Spa — это место, где можно не только заниматься спортом,'
                       ' но и расслабиться в бассейне, сауне или джакузи.',
        'longitude': 92.854662,
        'latitude': 56.024512,
    }
]

negative_data = [
    {
        'name': "",
        'description': "Крутое место для программистов",
        'longitude': 55.751,
        'latitude': 37.621,
    },
    {
        'name': "ТРЦ Планета",
        'description': '',
        'longitude': 60.2,
        'latitude': 56.02,
    },
    {
        'name': 'Театр оперы и балета',
        'description': 'стационарный репертуарный театр в городе Красноярске. Основан в 1976 году.'
                       ' Первая постановка была представлена в 1978 году.',
        'longitude': '',
        'latitude': 56.03,
    },
    {
        'name': 'Лувр',
        'description': 'один из крупнейших и самый популярный художественный музей мира.'
                       ' Музей расположен в центре Парижа',
        'longitude': 56.03,
        'latitude': '',
    }
]


class TestForm(TestCase):
    """
    Тесты для проверки формы
    """

    def test_positive_valid_form(self):
        for review in positive_data:
            form = PlaceForm(data=review)
            self.assertTrue(form.is_valid())

    def test_negative_valid_form(self):
        for review in negative_data:
            form = PlaceForm(data=review)
            self.assertFalse(form.is_valid())
