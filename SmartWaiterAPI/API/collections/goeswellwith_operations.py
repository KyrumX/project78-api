from API.models import GoesWellWith, Menu


def get_goeswellwith_items(menuitem1):
    entries = GoesWellWith.objects.filter(menuitem1=menuitem1)
    result = []

    if entries.count() <= 0:
        result.append('None')
        return result
    else:
        for e in entries:
            result.append(Menu.objects.get(id=e.menuitem2_id).name)

    return result