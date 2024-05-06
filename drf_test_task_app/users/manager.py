from django.contrib.auth import models as auth_models


class UserManager(auth_models.BaseUserManager):

    def create_user(self, email, password=None, is_staff=False, is_superuser=False):
        """
        Creates and saves a user with a specified email address and password.

        :param email:
        :param password:
        :param is_staff:
        :param is_superuser:
        :return:User
        """

        if not email:
            raise ValueError("User must have an email")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()

        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with a specified email address and password.

        :param email:
        :param password:
        :return: User
        """
        user = self.create_user(
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True
        )
        user.save()

        return user
