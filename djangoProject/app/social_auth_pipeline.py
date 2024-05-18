def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'vk-oauth2':
        print("save_profile called")
        user.first_name = response.get('first_name')
        user.last_name = response.get('last_name')
        print(response.get('first_name'))
        print(response.get('last_name'))
        user.save()
