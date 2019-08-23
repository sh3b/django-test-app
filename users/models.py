from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        # Custom permissions
        permissions = (("can_view_view1", "Can view view1"),
                       ("can_view_view2", "Can view view2"))