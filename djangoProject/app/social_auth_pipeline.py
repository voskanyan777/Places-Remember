from .models import UserImage


def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'vk-oauth2':
        user.first_name = response.get('first_name')
        user.last_name = response.get('last_name')
        user.save()

        # Попытка получить существующую запись UserImage для пользователя
        try:
            image = UserImage.objects.get(user=user)
            image.image = response.get('user_photo')
            image.save()
        except UserImage.DoesNotExist:
            # Если запись не найдена, создаём новую
            image = UserImage(user=user, image=response.get('user_photo'))
            image.save()
