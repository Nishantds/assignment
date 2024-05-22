from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import (
    get_user_model,
)


User = get_user_model()


class CustomAuthenticationBackend(ModelBackend):
    """
    This Authentication Backend Authenticates a User Against the Mobile No.
    Possible Usage Can Be Facebook Login Where User Can Also Use Mobile No. to
    Create an Account.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            mobile_number = request.data.get('mobile_number')
            password = request.data.get('password')
        except:
             mobile_number=username
        """
        Authenticate Using the Mobile/password And Return a User
        """
        
        try:
            if mobile_number:
                user = User.objects.filter(phone=mobile_number,is_active=True).first()
            else:
                return None
        except User.DoesNotExist:
            return None
            
        else:
            try:
                if user.check_password(password):
                    return user   
            except:
                pass        
               
            
            return None

    def get_user(self, user_id):
        """
        Returns a User Against a Given User Id
        """

        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None