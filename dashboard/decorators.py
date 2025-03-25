from django.contrib.auth.decorators import user_passes_test

def group_required(*group_names):
    def check_group(user):
        if user.is_superuser:
            return True
        for group in group_names:
            if user.groups.filter(name=group).exists():
                return True
    return user_passes_test(check_group,login_url='home')

manager_required = group_required('Manager')
editor_required = group_required('Manager','Editor')
author_required = group_required('Manager','Editor','Author')
