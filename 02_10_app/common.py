def user_directory_path(instance, filename):
    return 'RestAPI_/{0}_{1}_{2}'\
        .format(instance.id, instance.create_date, filename)